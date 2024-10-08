from supabase import create_client, Client
import asyncio
import os
import re
import requests
import json
import random
import traceback
import ast
from openai import OpenAI
from telegram import CallbackQuery, Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove,Poll
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from telegram.error import BadRequest, NetworkError, TimedOut
from telegram.error import Forbidden, TelegramError
from datetime import datetime, timedelta
from flask import Flask, app
from telegram.request import HTTPXRequest
from deepgram import DeepgramClient, PrerecordedOptions, SpeakOptions
from dotenv import load_dotenv
from functools import partial
load_dotenv()
from openai import AsyncOpenAI
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from word_lists import get_all_pronunciation_sentences, get_random_word, get_all_words, get_random_pronunciation_sentence
import re
import google.generativeai as genai
from PIL import Image
import io
from collections import deque
from grammar_exercises import EXERCISES
from lessons import LESSONS
from vocab import get_words
import json
import ast
import random
url: str = "https://ruzcfhezadjscqipzhiw.supabase.co"

supabase_key = os.getenv('SUPABASE_KEY')

key: str= supabase_key

supabase: Client = create_client(url, key)
# Telegram bot token
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_IDS = [1115038445]
app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200


try:
    num_cores = os.cpu_count()

    # Create the thread pool
    executor = ThreadPoolExecutor(max_workers=num_cores)  # Adjust the number of workers as needed
except Exception as e:
    print("🚨 executor = ThreadPoolExecutor(max_workers=8)",e)
    executor = ThreadPoolExecutor(max_workers=8)

# Main menu keyboard
main_menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("📚 Dictionary"), KeyboardButton("🔍 Grammar Checker")],
    [KeyboardButton("✏️ Spelling Checker")]
], resize_keyboard=True)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username
    user_data = await supabase_select("users", "*", "user_id", user_id)
    
    if not user_data.data:
        # Insert basic user info into the database
        await supabase_insert("users", {"user_id": user_id, "username": username})
        # await ask_preferred_accent(update, context)
        await send_main_menu(update, context)
    else:
        context.user_data.clear()
        await remove_keyboard(update,context)
        await send_main_menu(update, context)
async def remove_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_id = update.effective_chat.id
        message_id = update.message.message_id - 1
        await context.bot.edit_message_reply_markup(
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=None
        )
    except Exception as e:
        
        # print(f"Error removing keyboard: {e}")
        try:
                await update.effective_message.edit_reply_markup(reply_markup=None)
        except Exception as e:
                pass
                # await update.effective_message.delete()
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if not query:
        await error_handler(update, context, "Invalid callback query")
        return

    await query.answer()
    
    user_id = update.effective_user.id
    data = query.data
    
    try:
        if data.startswith('language_'):
            await remove_keyboard(update,context)
            language = data.split('_')[1]
            await supabase_update("users", {"language": language}, "user_id", user_id)
            await ask_english_level(update, context)
        
        elif data.startswith('level_'):
            await remove_keyboard(update,context)
            level = data.split('_')[1]
            await supabase_update("users", {"level": level}, "user_id", user_id)
            await ask_preferred_accent(update, context)
        
        elif data.startswith('accent_'):
            await remove_keyboard(update,context)
            accent = data.split('_')[1]
            await supabase_update("users", {"preferred_accent": accent}, "user_id", user_id)
            await send_main_menu(update, context)
        elif query.data.startswith('spelling_'):
            await remove_keyboard(update,context)
            difficulty = query.data.split('_')[1]
            print(difficulty)
            if difficulty == 'continue':
                await spelling_practice_start(update, context, "Let's try another word. Choose the difficulty:")
            elif difficulty == 'stop':
                await stop_spelling(update, context)
            else:
                await spelling_practice_process(update, context, difficulty)
        # You can add more elif blocks here for other button types
        elif query.data.startswith('learn_'):
            await handle_learn_word(update, context)
        elif query.data == 'pronunciation_next':
            await remove_keyboard(update,context)
            await pronunciation_next(update, context)
        elif query.data == 'pronunciation_get':
            await remove_keyboard(update,context)
            await pronunciation_get(update, context)
        elif query.data == 'pronunciation_try_again':
            await remove_keyboard(update,context)
            await pronunciation_try_again(update, context)
        elif query.data == 'pronunciation_stop':
            await remove_keyboard(update,context)
            await stop_pronunciation_practice(update, context)
        elif query.data == 'grammar_check_another':
            await remove_keyboard(update, context)
            if context.user_data['grammar_check_queue']:
                await process_grammar_check_queue(update, context)
            else:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="يمكنك إرسال المزيد من النصوص أو الصور لتصحيحها. أو إذا انتهيت، يمكنك العودة إلى القائمة الرئيسية."
                )
            context.user_data['mode'] = 'grammar_check'
        elif query.data == 'return_main_menu':
            await remove_keyboard(update, context)
            context.user_data.clear()
            await send_main_menu(update, context)
        elif query.data.startswith('exercise_'):
            await handle_exercise_response(update, context)
        elif query.data == 'grammar_continue':
            await grammar_lessons_start(update, context)
        elif query.data == 'return_main_menu':
            context.user_data.clear()
            await send_main_menu(update, context)
        elif query.data in ['more_exercises', 'continue_exercises']:
            await remove_keyboard(update,context)
            if context.user_data['exercise_index'] >= len(context.user_data['current_exercises']):
                # If we've used all current exercises, get new ones
                topic = context.user_data.get('grammar_topic')
                subtopic = context.user_data.get('grammar_subtopic')
                sub_subtopic = context.user_data.get('grammar_sub_subtopic')
                await send_exercise(query, context, topic, subtopic, sub_subtopic)
            else:
                # If we still have exercises, send the next batch
                await send_next_exercise_batch(query, context)
        elif query.data == 'return_topics':
            await remove_keyboard(update,context)
            await grammar_lessons_start(query, context)
        # Vocabulary flashcard handling
        
        elif data.startswith('vocab_'):
            action = data.split('_')[1]
            print("action",action)
            # if action in ['know', 'dont']:
            # word = data.split('_')[2]
            # print("word",word)
            if action == 'know':
                await remove_keyboard(update,context)
                # Add word to known words
                word = data.split('_')[2]
                print("word_know",word)
                
                
                await context.bot.send_message(chat_id=update.effective_chat.id, text=f"رائع! أنت تعرف الكلمة '{word}'. دعنا ننتقل إلى الكلمة التالية.")
                user_data = await supabase_select("users", "vocab_know", "user_id", user_id)
                vocab_know = set(user_data.data[0]['vocab_know']) if user_data.data and user_data.data[0]['vocab_know'] else set()
                vocab_know.add(word)
                await supabase_update("users", {"vocab_know": list(vocab_know)}, "user_id", user_id)
                # await query.edit_message_text(f"Great! You know the word '{word}'. Let's move to the next word.")
                await vocabulary_flashcards(update, context)
            elif action == 'dont':
                await remove_keyboard(update,context)
                word = data.split('_')[3]
                print("word_dont",word)
                # Add word to unknown words
                user_data = await supabase_select("users", "vocab_dont_know", "user_id", user_id)
                vocab_dont_know = set(user_data.data[0]['vocab_dont_know']) if user_data.data and user_data.data[0]['vocab_dont_know'] else set()
                vocab_dont_know.add(word)
                await supabase_update("users", {"vocab_dont_know": list(vocab_dont_know)}, "user_id", user_id)
                # Get word definition using LLM
                prompt = f"You are English teacher and your task is to provide a simple definition including the meaning and an example sentence in English for the word '{word}': follow this template the word:\n its most common meaning/s in Arabic 4 maximum \n\n (Definition: write it in English and translate it to Arabic. do not forget to translate it to arabic) \n\n 1 or 2 Examples: in English \n only this do not write anything else, you should organize the text and make it readable in telegram and do not forget include the Arabic text without the way of pronounce it in english just the arabic text  and you should provide accurate result"
                prompt += f"to make it looks better and more organized you can use HTML style format <strong>bold</strong> for bold text this for the definition  , <ins>underline</ins> for underline text this for the meaning in Arabic and <blockquote> </blockquote> for examples also make it bold the examples\n\n please make sure to use them properly "
                await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
                definition = await unify(prompt)
                keyboard = [
                    [InlineKeyboardButton("الكلمة التالية ⬅️", callback_data="vocab_next"),InlineKeyboardButton("إلغاء ❌", callback_data="vocab_stop")],
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{definition}", reply_markup=reply_markup,parse_mode="HTML")
            elif action == 'next':
                await remove_keyboard(update,context)
                await vocabulary_flashcards(update, context)
            elif action == 'stop':
                await remove_keyboard(update,context)
                # await send_main_menu(update, context)
                # await context.bot.send_message(chat_id=update.effective_chat.id, text="Vocabulary practice stopped. You can start again anytime!")
                # await query.edit_message_text("Vocabulary practice stopped. You can start again anytime!")
                await send_main_menu(update, context)
            elif action == 'change':
                await remove_keyboard(update,context)
                keyboard = [
                    [InlineKeyboardButton("سهلة (A1 - A2)", callback_data="change_level_simple")],
                    [InlineKeyboardButton("متوسطة (B1 - B2)", callback_data="change_level_medium")],
                    [InlineKeyboardButton("صعبة (B2 - C1)", callback_data="change_level_hard")]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await context.bot.send_message(chat_id=update.effective_chat.id, text="اختر مستوى صعوبة المفردات:", reply_markup=reply_markup) 
                # await query.edit_message_text(
                #     "Choose your preferred vocabulary level:",
                    #     reply_markup=reply_markup
                    # )
        elif data.startswith('change_level_'):
            await remove_keyboard(update,context)
            level = data.split('_')[2]
            await supabase_update("users", {"vocab_level": level}, "user_id", user_id)
            await vocabulary_flashcards(update, context)
        elif data.startswith('word_recap_'):
            action = data.split('_')[2]
            if action == 'next':
                await remove_keyboard(update,context)
                await vocabulary_recap(update, context)
            elif action == 'stop':
                await remove_keyboard(update,context)
                context.user_data.pop('word_recap_session', None)
                # await context.bot.send_message(chat_id=update.effective_chat.id, text="Vocabulary recap stopped. You can start again anytime!")
                await send_main_menu(update, context)
        elif data == "try_again":
            await remove_keyboard(update,context)
            await send_main_menu(update,context)
        # else:
        #     await edit_message_with_fallback(update, context, "I'm sorry, I didn't understand that command.")
    
    except Exception as e:
        error_message = f"An error occurred in button_handler: {str(e)}"
        print(error_message)
        error_traceback = traceback.format_exc()
        print(error_traceback)
        await error_handler(update, context, error_message)
async def pronunciation_next(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await pronunciation_practice_start(update, context)

async def pronunciation_get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_sentence = context.user_data.get('current_sentence')
    if not current_sentence:
        await update.callback_query.edit_message_text("آسف ليس لدي جملة للتدرب عليها حالياً، دعنا نبدأ من جديد")
        await pronunciation_practice_start(update, context)
        return

    user_id = update.effective_user.id
    user_data = await supabase_select("users", "preferred_accent", "user_id", user_id)
    preferred_accent = user_data.data[0]['preferred_accent'] if user_data.data else "American"

    # if preferred_accent == "American":
    #     preferred_accent = "Dan"
    #     await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="RECORD_VOICE")
    #     audio_file = await convert_text_to_audio(current_sentence, preferred_accent)
    # elif preferred_accent == "British":
    #     preferred_accent = "aura-athena-en"
    #     audio_file = await deepgram_tts(current_sentence, preferred_accent)
    preferred_accent = "Dan"
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="RECORD_VOICE")
    audio_file = await convert_text_to_audio(current_sentence, preferred_accent)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("حاول مرة أخرى 🔁", callback_data='pronunciation_try_again'),
         InlineKeyboardButton("التالي ⬅️", callback_data='pronunciation_next')],
        [InlineKeyboardButton("إلغاء ❌", callback_data='pronunciation_stop')]
    ])
    try:
        with open(audio_file, 'rb') as audio:
            await update.callback_query.message.reply_voice(audio)
    except Exception as e:
        print(e)
        with open(audio_file, 'rb') as audio:
            await context.bot.send_voice(chat_id=update.effective_chat.id, voice=audio)
        # await update.callback_query.message.reply_text(current_sentence)
    finally:
        if os.path.exists(audio_file):
                os.remove(audio_file) 
    await update.callback_query.message.reply_text(
        "هذا هو النطق الصحيح ✅، هل تريد المحاولة مرة أخرى أو الإنتقال إلى الكلمة/الجملة التالية؟",
        reply_markup=keyboard
    )

async def pronunciation_try_again(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_sentence = context.user_data.get('current_sentence')
    await update.callback_query.edit_message_text(
        f"حسنًا، لنحاول مرة أخرى. يُرجى تسجيل صوتك وأنت تقول هذه الجملة:\nn{current_sentence}\nn\أرسل رسالتك الصوتية عندما تكون مستعدًا."
    )
async def dictionary_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup([
        # [KeyboardButton("📚 Dictionary")],
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    await update.message.reply_text(
        "أكتب الكلمة التي تريد البحث عنها في القاموس باللغة الإنجليزية (كلمتين حد أقصى)",
        reply_markup=keyboard
    )
    context.user_data['mode'] = 'dictionary'
    context.user_data['awaiting_word'] = True

async def dictionary_process(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    word = update.message.text.strip().lower()
    # print("word",word)
    
    
    
    if len(word.split()) > 2:
        await update.message.reply_text("الرجاء كتابة كلمتين كحد أقصى", reply_markup=keyboard)
        context.user_data['awaiting_word'] = True
        return
    # Check if all characters are English letters or spaces
    if not re.match(r'^[a-z\s]+$', word):
        await update.message.reply_text("الرجاء إدخال الكلمة باللغة الإنجليزية فقط", reply_markup=keyboard)
        context.user_data['awaiting_word'] = True
        return
    # await update.message.reply_text("الرجاء الإنتظار لحظات")

    prompt = f"""Task: you are experienced English teacher and your task is to provide a detailed explanation of the word or phrase '{word}' in both English and Arabic, simulating the depth and precision of a professional translator or a high-quality dictionary. Ensure the explanation is comprehensive and clear for language learners.

Instructions:

- <ins> Meaning (المعنى) : </ins> provide the most common meaning of the word or phrase in Arabic 4 maximum and 1 minimum only the meaning nothing else and should be the true meaning of the word.

- <ins> Definition in English: </ins> Offer a precise, clear, and easy-to-understand definition of the word or phrase.

- <ins> (التعريف باللغة العربية): </ins> Translate the definition into fluent, accurate Arabic, ensuring that it conveys the same meaning and nuances as in English.

- <ins> Word Family: </ins> List all relevant forms of the word, including:
  • Verb: e.g., imagine
  • Noun: e.g., imagination
  • Adjective: e.g., imaginative
  • Adverb: e.g., imaginatively
  Include any additional derivatives or inflections if applicable (e.g., plural forms, comparative/superlative forms for adjectives, participles for verbs).
  
- <ins> Part of Speech (أجزاء الكلام): </ins> Identify all relevant parts of speech (e.g., noun, verb,adjective, adverb). For each part of speech, provide:


- <ins> Definition in English: </ins> A specific definition related to that part of speech.

- <ins> (التعريف باللغة العربية): </ins> A natural Arabic translation of the specific definition.

- <ins> Example (مثال): </ins> Show how the word is used in a sentence only in english.
- <ins> Usage Examples: </ins> Offer 5 contextual examples that illustrate the word/phrase being used in various sentences. Each sentence should be followed by its Arabic translation.
for verbs include the other format of the word past, present(ing), and past participle and for Nouns include it in single and plural

- <ins> phrasal verbs (الأفعال المركبة) if possible and their meaning and defination in Arabic with 1 example

- <ins> Synonyms (المرادفات): </ins> List at least 3 synonyms of the word/phrase .

- <ins> Antonyms (المتضادات): </ins> List at least 3 antonyms (Note if the word does not have any antonyms do not write it).

Ensure that both the English and Arabic explanations are easy to follow, accurate, and reflect the nuances of each language.
Focus on clarity and readability, making it suitable for language learners at various levels.

do not include * or # in the text 

"""
    prompt += f"\n\nto make it looks better and more organized you can use HTML style format <strong>bold</strong> for bold text this for the definition  , <ins>underline</ins> for underline text this for the meaning in Arabic and titles ,<blockquote> </blockquote> for examples and make sure you accurtlly do that for the examples in English\n\n please make sure to use them properly "
    try:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
        dictionary_content = await unify(prompt)
        await update.message.reply_text(dictionary_content,parse_mode="HTML")
        
        user_id = update.effective_user.id
        user_data = await supabase_select("users", "preferred_accent", "user_id", user_id)
        preferred_accent = user_data.data[0]['preferred_accent'] if user_data.data else "American"
        # if preferred_accent == "American":
        #     preferred_accent = "Dan"
        #     await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="RECORD_VOICE")
        #     audio_file = await convert_text_to_audio(word, "Dan")
        # elif preferred_accent == "British":
        #     preferred_accent = "aura-athena-en"
        #     audio_file = await deepgram_tts(word, preferred_accent)
        preferred_accent = "Dan"
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="RECORD_VOICE")
        audio_file = await convert_text_to_audio(word, preferred_accent)
        try:
            with open(audio_file, 'rb') as audio:
                await update.message.reply_voice(audio)
        except Exception as e:
            print(e)
        finally:
            # Delete the file after sending
            if os.path.exists(audio_file):
                os.remove(audio_file)

        await update.message.reply_text("أبحث عن كلمة أخرى أو أضغط (/stop) للعودة للقائمة الرئيسية", reply_markup=keyboard)
        context.user_data['awaiting_word'] = True
        # user_id = update.effective_user.id
        user_data = await supabase_select("users", "vocab_know", "user_id", user_id)
        vocab_know = set(user_data.data[0]['vocab_know']) if user_data.data and user_data.data[0]['vocab_know'] else set()
        vocab_know.add(word)
        await supabase_update("users", {"vocab_know": list(vocab_know)}, "user_id", user_id)
    except Exception as e:
        await error_handler(update, context, f"An error occurred: {str(e)}")
        context.user_data['awaiting_word'] = True


def setup_handlers(application):
    application.add_handler(CommandHandler('stop', stop_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, error_message: str):
    print(f"ID: {update.effective_user.id} Username: {update.effective_user.username} | {error_message}")
    issue_message = "آسف هناك مشكلة في البوت حاليا الرجاء المحاولة مرة أخرى"
    userID = update.effective_user.id
    keyboard = [[InlineKeyboardButton("المحاولة مرة أخرى 🔁", callback_data=f"try_again")]]
                # [InlineKeyboardButton("Contact me ↗️", url=f"https://t.me/ielts_pathway")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        if update.effective_message:
            await update.effective_message.reply_text(issue_message, reply_markup=reply_markup)
            
        # elif update.callback_query:
        #     await edit_message_with_fallback(update, context, issue_message)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=issue_message, reply_markup=reply_markup)
    except Exception as e:
        print(f"Failed to send error message: {e}")

async def audio_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await remove_keyboard(update,context)
    
    if context.user_data.get('mode') == 'pronunciation_practice':
        current_sentence = context.user_data.get('current_sentence')
        if not current_sentence:
            await update.message.reply_text("آسف ليس هناك جمل للتدرب عليها حاليا، دعنا نبدأ من جديد")
            await pronunciation_practice_start(update, context)
            return

        file_id = update.message.voice.file_id
        try:
            
            transcript = await convert_audio_to_text(file_id, update, context)
            if not transcript:
                await update.message.reply_text("آسف لم أستطع فهم رسالتك الصوتية، حاول مرة أخرى بشكل أوضح")
                return
            transcript_clean = re.sub(r'[^\w\s]', '', transcript.lower().strip())
            current_sentence_clean = re.sub(r'[^\w\s]', '', current_sentence.lower().strip())
            
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("التالي ⬅️", callback_data='pronunciation_next'),
                 InlineKeyboardButton("النطق الصحيح 🔊", callback_data='pronunciation_get')],
                [InlineKeyboardButton("إلغاء ❌", callback_data='pronunciation_stop')]
            ])

            keyboard2 = InlineKeyboardMarkup([
                [InlineKeyboardButton("التالي ⬅️", callback_data='pronunciation_next'),
                 InlineKeyboardButton("إلغاء ❌", callback_data='pronunciation_stop')]
            ])
            
            if transcript_clean == current_sentence_clean:
                await update.message.reply_text("أحسنت ✅، النطق صحيح", reply_markup=keyboard2)
            else:
                await update.message.reply_text(
                    f"محاولة جيدة، لكن ليس صحيح تماماً، يمكنك المحاولة مرة أخرى أو اختيار أحد الخيارات التالية\n\n"
                    f"أنت قلت: {transcript}\n\n"
                    f"الجملة الصحيحة هي: {current_sentence}",
                    reply_markup=keyboard
                )
        except Exception as e:
            await error_handler(update, context, f"An error occurred while processing your audio: {str(e)}")

    elif context.user_data.get('mode') == 'ai_tutor':
        file_id = update.message.voice.file_id
        try:
            await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="RECORD_VOICE")
            transcript = await convert_audio_to_text(file_id, update, context)
            # transcript = await wisperSTT(file_id,update,context)
            if not transcript:
                text = "آسف لم أستطع فهم رسالتك الصوتية، يرجى المحاولة مرة أخرى، يرجى تسجيل صوتك فقط باللغة الإنجليزية إذا أردت استخدام اللغة العربية، يرجى إرسالها كرسالة"
                await update.message.reply_text(text)
                return
            context.user_data['ai_tutor_mode'] = 'voice'
            # Instead of processing here, call the ai_tutor function
            await ai_tutor(update, context,transcript)
        except Exception as e:
            await error_handler(update, context, f"An error occurred while processing your audio: {str(e)}")

    # else:
    #     await update.message.reply_text("آسف لم أستطع فهم رسالتك الصوتية؟")
        

async def register_user(update: Update, context: ContextTypes.DEFAULT_TYPE, language):
    user_id = update.effective_user.id
    await supabase_update("users", {"language": language}, "user_id", user_id)
    del context.user_data['awaiting_language']
    await send_welcome_message(update, context)

async def send_welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "Thank you for providing your information! 🎉\n\n"
        "Welcome to the English Learning Bot. Here's what I can help you with:\n"
        "📚 Dictionary: Look up words and their meanings\n"
        "🔍 Grammar Checker: Check your sentences for grammatical errors\n"
        "✏️ Spelling Checker: Verify the spelling of words\n\n"
        "Please select an option from the menu below to get started!"
    )
    await edit_message_with_fallback(update, context, welcome_message)
    await send_main_menu(update, context)

async def handle_dictionary_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE, word):
    prompt = f"Provide a comprehensive explanation for the word '{word}', including its definition, part of speech, example sentences, synonyms, and antonyms if applicable. Format the response in an easy-to-read manner."
    
    try:
        result = await unify(prompt)
        await update.message.reply_text(result)
    except Exception as e:
        print(e)
        pass
        # await update.message.reply_text(f"An error occurred while looking up the word: {str(e)}")
    
    context.user_data['awaiting_word'] = False


async def ask_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"{update.effective_user.id} ask language")
    try:
        user_id = update.effective_user.id
        keyboard = [
            [InlineKeyboardButton("Arabic 🇸🇦", callback_data=f'language_Arabic'),
            InlineKeyboardButton("Urdu 🇵🇰", callback_data=f'language_Urdu')],
            [InlineKeyboardButton("Persian 🇮🇷", callback_data=f'language_Persian'),
            InlineKeyboardButton("Uzbek 🇺🇿", callback_data=f'language_Uzbek')],
            [InlineKeyboardButton("English 🇬🇧", callback_data=f'language_English')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.effective_message.reply_text("Welcome to the English Learning Bot! \nPlease select your native language:", reply_markup=reply_markup)
    except Exception as e:
        text = ("🚨 ask language function", e)
        error_traceback = traceback.format_exc()
        print(error_traceback)
        await error_handler(update, context, text)

async def stop_pronunciation_practice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()  # Clear user data
    # await update.callback_query.edit_message_text("Pronunciation practice has been stopped. Returning to the main menu.")
    await send_main_menu(update, context)  
async def spelling_practice_start(update: Update, context: ContextTypes.DEFAULT_TYPE,text):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("سهلة", callback_data='spelling_simple'),
         InlineKeyboardButton("متوسطة", callback_data='spelling_medium')],
        [InlineKeyboardButton("صعبة", callback_data='spelling_hard'),
         InlineKeyboardButton("التدرب على جمل", callback_data='spelling_sentence')],
        [InlineKeyboardButton("إلغاء ❌", callback_data='spelling_stop')]
    ])
    keyboard2 = ReplyKeyboardMarkup([
        # [KeyboardButton("📚 Dictionary")],
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    if update.callback_query:
        await update.callback_query.edit_message_text(text)
        await update.callback_query.edit_message_reply_markup(reply_markup=keyboard)
    else:
        await update.message.reply_text(text, reply_markup=keyboard2)
        await update.message.reply_text("اختر مستوى الصعوبة:", reply_markup=keyboard)
    context.user_data['mode'] = 'spelling_practice'
    # context.user_data['correct_count'] = 0
    # context.user_data['wrong_count'] = 0
    context.user_data['awaiting_difficulty'] = True
    # if 'used_words' not in context.user_data:
    #     context.user_data['used_words'] = set()

async def spelling_practice_process(update: Update, context: ContextTypes.DEFAULT_TYPE, difficulty: str):
    if "used_words" not in context.user_data:
        context.user_data["used_words"] = []

    all_words = get_all_words(difficulty)
    max_attempts = len(all_words)  # To prevent infinite loop if all words are used
    attempts = 0

    while attempts < max_attempts:
        word = get_random_word(difficulty)
        # print(context.user_data["used_words"])
        if word not in context.user_data["used_words"]:
            context.user_data["used_words"].append(word)
            break
        attempts += 1

    if attempts == max_attempts:
        await update.effective_message.reply_text("لقد تدربت على جميع الكلمات المتاحة لهذا المستوى، يرجى اختيار مستوى جديد أو إلغاء التدريب")
        await spelling_practice_start(update, context, "اختر مستوى جديد:")
        return

    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    context.user_data['current_word'] = word
    context.user_data['attempts'] = 0
    context.user_data['awaiting_difficulty'] = False
    context.user_data['current_difficulty'] = difficulty

    if 'session_words' not in context.user_data:
        context.user_data['session_words'] = {'correct': [], 'incorrect': []}

    user_id = update.effective_user.id
    user_data = await supabase_select("users", "preferred_accent", "user_id", user_id)
    preferred_accent = user_data.data[0]['preferred_accent'] if user_data.data else "American"
    # if preferred_accent == "American":
    #     preferred_accent = "Dan"
    #     await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="RECORD_VOICE")
    #     audio_file = await convert_text_to_audio(word, preferred_accent)
    # elif preferred_accent == "British":
    #     preferred_accent = "aura-athena-en"
    #     audio_file = await deepgram_tts(word, preferred_accent)
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="RECORD_VOICE")
    audio_file = await convert_text_to_audio(word, "Dan")
    # print(audio_file)
    try:
        with open(audio_file, 'rb') as audio:
            await update.effective_message.reply_voice(audio)
    except Exception as e:
        print(e)
        with open(audio_file, 'rb') as audio:
            await context.bot.send_voice(chat_id=update.effective_chat.id, voice=audio)
    finally:
            # Delete the file after sending
            try:
                if os.path.exists(audio_file):
                    os.remove(audio_file)
            except Exception as e:
                print(e)
    await update.effective_message.reply_text("يرجى كتابة الكلمة/الجملة التي قمت بالإستماع إليها:", reply_markup=keyboard)


async def send_long_message(update, context, message, reply_markup=None, parse_mode='HTML'):
    max_length = 4096  # Maximum message length allowed by Telegram
    message_chunks = [message[i:i+max_length] for i in range(0, len(message), max_length)]
    
    for i, chunk in enumerate(message_chunks):
        await asyncio.sleep(1)  # 1-second delay between messages
        if i == len(message_chunks) - 1 and reply_markup:
            # Add reply markup to the last chunk
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=chunk,
                parse_mode=parse_mode,
                reply_markup=reply_markup
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=chunk,
                parse_mode=parse_mode
            )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # print(text)
    
    if text == "✏️ التهجئة" or text == "✏️ Spelling Checker":
        await spelling_practice_start(update, context,"أهلا بك في التدرب على الاسبلينغ")
    elif text == "📚 القاموس":
        await dictionary_start(update, context)
    elif text == "/stop":
        
        await stop_command(update, context)
    elif context.user_data.get('mode') == 'spelling_practice' and not context.user_data.get('awaiting_difficulty'):
        await check_spelling(update, context)
    elif context.user_data.get('mode') == 'dictionary' and context.user_data.get('awaiting_word'):
        context.user_data['awaiting_word'] = False
        await dictionary_process(update, context)
    elif text == "🗣️ تمارين النطق":
        context.user_data['mode'] = 'pronunciation_practice'
        await pronunciation_practice_start(update, context)
    elif text == "🔍 القواعد":
        main_menu_keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("📚 دروس القواعد"), KeyboardButton("🔍 مصحح القواعد")],
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
        await update.message.reply_text("أختر أحد هذه الخيارات للبدء",reply_markup=main_menu_keyboard)
    
    elif context.user_data.get('mode') == 'grammar_check':
        if 'grammar_check_queue' not in context.user_data:
            context.user_data['grammar_check_queue'] = deque()

        if update.message.text and update.message.text not in ["📚 القاموس", "🔍 مصحح القواعد", "✏️ التهجئة", "🗣️ تمارين النطق"]:
            context.user_data['grammar_check_queue'].append(('text', update.message.text))
        elif update.message.photo:
            context.user_data['grammar_check_queue'].append(('photo', update.message.photo[-1].file_id))
        elif update.message.document:
            keyboard = ReplyKeyboardMarkup([
                [KeyboardButton("/stop")]
            ], resize_keyboard=True)
            await update.message.reply_text("آسف يمكنك فقط إرسال صورة أو كتابة",reply_markup=keyboard)
            return
        else:
            keyboard = ReplyKeyboardMarkup([
                [KeyboardButton("/stop")]
            ], resize_keyboard=True)
            await update.message.reply_text("الرجاء إرسال الجملة التي تريد تصحيحها (يمكنك إرسال صورة لكتابتك)",reply_markup=keyboard)
            return

        if len(context.user_data['grammar_check_queue']) == 1:
            await process_grammar_check_queue(update, context)
        else:
            print("queued")
            # await update.message.reply_text(f"Queued for grammar checking. {len(context.user_data['grammar_check_queue'])} items in queue.")
        return
    
    elif text == "🔍 مصحح القواعد":
        keyboard = ReplyKeyboardMarkup([
                [KeyboardButton("/stop")]
            ], resize_keyboard=True)
        await update.message.reply_text("الرجاء إرسال الجملة التي تريد تصحيحها (يمكنك إرسال صورة لكتابتك)",reply_markup=keyboard)
        context.user_data['mode'] = 'grammar_check'
        context.user_data['grammar_check_queue'] = deque()
    elif text == "📚 دروس القواعد":
            await grammar_lessons_start(update, context)
    elif context.user_data.get('grammar_state') == 'topic':
        await grammar_subtopic(update, context)
    elif context.user_data.get('grammar_state') == 'subtopic':
        await grammar_lesson(update, context)
    elif context.user_data.get('grammar_state') == 'sub_subtopic':
        await grammar_sub_subtopic(update, context)
    elif text in ['More Exercises', 'Return to Topics'] and context.user_data.get('grammar_state') == 'more_exercises':
        await handle_more_exercises(update, context)
    
    
    elif text == "🔤 المفردات":
        keyboard = ReplyKeyboardMarkup([
            [KeyboardButton("🔄 مراجعة المفردات"), KeyboardButton("🔤 تعلم مفردات جديدة")],
            [KeyboardButton("/stop")]
        ], resize_keyboard=True)
        await update.message.reply_text("أختر أحد هذه الخيارات للبدء:",reply_markup=keyboard)
    
    elif text == "🔄 مراجعة المفردات":
        await remove_keyboard(update,context)
        context.user_data['word_recap_session'] = []
        await vocabulary_recap(update, context)
    
    elif text == "🔤 تعلم مفردات جديدة":
        await remove_keyboard(update,context)
        await vocabulary_flashcards(update, context)
    elif text == "🧑‍🏫 معلم اللغة الانجليزية (AI)":
        context.user_data['mode'] = 'ai_tutor'
        await ai_tutor(update, context,"")
    elif context.user_data.get('mode') == 'ai_tutor':
        try:
            if text.lower() in ['exit', '/stop']:
                context.user_data.clear()
                await send_main_menu(update, context)
            else:
                await ai_tutor(update, context,"")
        except Exception as e:
            await ai_tutor(update, context,"")
    
    elif text == "🔍 مصادر اللغة الانجليزية":
        markup = ReplyKeyboardMarkup([
        [KeyboardButton("Reading"), KeyboardButton("Listening")],
        [KeyboardButton("Speaking"), KeyboardButton("Writing")],
        [KeyboardButton("English learning Plan")],
        [KeyboardButton("/stop")]])
        await context.bot.send_message(chat_id=update.effective_chat.id, text="الرجاء اختيار أحد الخيارات من القائمة أدناه للبدء!",reply_markup=markup)
    elif text == "Reading":
        await reading_sources(update, context)
    elif text == "Listening":
        await listening_sources(update, context)
    elif text == "Speaking":
        await speaking_sources(update, context)
    elif text == "Writing":
        await writing_sources(update, context)
    elif text == "English learning Plan":
        await english_learning_plan(update, context)
    # else:
    #     await update.message.reply_text("I'm sorry, I didn't understand that command. Please use the menu options.")


async def process_grammar_check_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    while context.user_data['grammar_check_queue']:
        item_type, item_content = context.user_data['grammar_check_queue'].popleft()
        if item_type == 'text':
            await grammar_check_text(update, context, item_content)
        elif item_type == 'photo':
            await grammar_check_image(update, context, item_content)

    # await context.bot.send_message(
    #     chat_id=update.effective_chat.id,
    #     text="All items have been processed. You can send more text or images for checking, or return to the main menu.",
    #     # reply_markup=get_grammar_check_keyboard()
    # )

async def check_spelling(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_spelling = re.sub(r'[^\w\s]', '', update.message.text.strip().lower())
    correct_spelling = re.sub(r'[^\w\s]', '', context.user_data['current_word'].lower())
    
    if user_spelling == correct_spelling:
        context.user_data['correct_count'] = context.user_data.get('correct_count', 0) + 1
        context.user_data['session_words']['correct'].append(context.user_data['current_word'])
        await spelling_practice_start(update, context, "Correct ✅! Well done!")
    else:
        context.user_data['attempts'] += 1
        if context.user_data['attempts'] < 4:
            text = f"آسف، هذا غير صحيح. لديك {4 - context.user_data['attempts']} محاولات أخرى. حاول مرة أخرى:"
            await update.message.reply_text(text)
        else:
            context.user_data['wrong_count'] = context.user_data.get('wrong_count', 0) + 1
            context.user_data['session_words']['incorrect'].append(context.user_data['current_word'])
            if context.user_data['current_difficulty'] != 'sentence':
                keyboard = InlineKeyboardMarkup([
                    [InlineKeyboardButton(f"أعرف أكثر عن '{context.user_data['current_word']}'", callback_data=f'learn_{context.user_data["current_word"]}')],
                    [InlineKeyboardButton("التالي ⬅️", callback_data='spelling_continue')]
                ])
                await update.message.reply_text(
                    f"آسف، التهجئة الصحيحة هي: <strong><ins> {context.user_data['current_word']}</ins></strong>",
                    reply_markup=keyboard,
                    parse_mode="HTML"
                )
            else:
                await spelling_practice_start(update, context, f"Sorry, the correct spelling is: {context.user_data['current_word']}")


def setup_handlers(application):
    application.add_handler(CommandHandler('stop', stop_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    application.add_handler(CallbackQueryHandler(button_handler))

async def ask_english_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"{update.effective_user.id} ask english level")
    try:
        user_id = update.effective_user.id
        keyboard = [
            [InlineKeyboardButton("Beginner", callback_data=f'level_Beginner')],
            [InlineKeyboardButton("Elementary", callback_data=f'level_Elementary')],
            [InlineKeyboardButton("Intermediate", callback_data=f'level_Intermediate')],
            [InlineKeyboardButton("Upper Intermediate", callback_data=f'level_UpperIntermediate')],
            [InlineKeyboardButton("Advanced", callback_data=f'level_Advanced')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.effective_message.reply_text("What is your current level of English?", reply_markup=reply_markup)
    except Exception as e:
        text = ("🚨 ask english level function", e)
        error_traceback = traceback.format_exc()
        print(error_traceback)
        await error_handler(update, context, text)

async def ask_preferred_accent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"{update.effective_user.id} ask preferred accent")
    try:
        user_id = update.effective_user.id
        keyboard = [
            [InlineKeyboardButton("لهجة أمريكية 🇺🇸", callback_data=f'accent_American')],
            [InlineKeyboardButton("لهجة بريطانية 🇬🇧", callback_data=f'accent_British')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.effective_message.reply_text("ماهي اللهجة التي تفضلها؟", reply_markup=reply_markup)
    except Exception as e:
        text = ("🚨 ask preferred accent function", e)
        error_traceback = traceback.format_exc()
        print(error_traceback)
        await error_handler(update, context, text)
        
async def send_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    main_menu_keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("📚 القاموس"), KeyboardButton("🔍 القواعد")],
        [KeyboardButton("✏️ التهجئة"), KeyboardButton("🗣️ تمارين النطق")],
        [KeyboardButton("🔤 المفردات"),KeyboardButton("🧑‍🏫 معلم اللغة الانجليزية (AI)")],
        # [KeyboardButton("🔍 مصادر اللغة الانجليزية")]
    ], resize_keyboard=True)
    
    welcome_message = (
        "مرحبًا بك في بوت تعلم اللغة الإنجليزية! 🎉\n\n"
        "ماذا تود أن تفعل اليوم؟\n\n"
        "📚 <strong><u>القاموس:</u></strong> ابحث عن الكلمات ومعانيها\n"
        "🔍 <strong><u>القواعد:</u></strong> تصحيح الكتابة ودروس للقواعد مع التمارين\n"
        "✏️ <strong><u>التهجئة:</u></strong> التدرب على تهجئة الكلمات\n"
        "🗣️ <strong><u>تمارين النطق:</u></strong> التدرب على النطق\n"
        "🔤 <strong><u>المفردات:</u></strong> راجع الكلمات أو تعلم مفردات جديدة\n"
        "🧑‍🏫 <strong><u>معلم الذكاء الاصطناعي:</u></strong> احصل على دروس مخصصة بناءً على مستواك وتفضيلاتك\n"
        "يرجى تحديد خيار من القائمة أدناه للبدء!"
        # "🔍 موارد تعلم اللغة الإنجليزية: استكشف موارد القراءة والاستماع والتحدث والكتابة\n\n"

    )
    await update.effective_message.reply_text(welcome_message, reply_markup=main_menu_keyboard,parse_mode="HTML")
    await supabase_update("users", {"last_use": datetime.now().isoformat()}, "user_id", update.effective_user.id)
async def edit_message_with_fallback(update: Update, context: ContextTypes.DEFAULT_TYPE, new_text: str):
    query = update.callback_query
    try:
        if query and query.message:
            await query.edit_message_text(new_text)
        else:
            raise AttributeError("No valid callback query message")
    except BadRequest as e:
        if str(e) == "Message is not modified: specified new message content and reply markup are exactly the same as a current content and reply markup of the message":
            # Message is already up to date, no need to do anything
            return
        else:
            print(f"Error editing message via query: {e}")
            try:
                await context.bot.edit_message_text(
                    chat_id=update.effective_chat.id,
                    message_id=update.effective_message.message_id,
                    text=new_text
                )
            except Exception as e:
                print(f"Error editing message via bot: {e}")
                await update.effective_chat.send_message(new_text)
    except Exception as e:
        print(f"Unexpected error: {e}")
        await update.effective_chat.send_message(new_text)
async def handle_learn_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    word = query.data.split('_')[1]
    prompt = f"""Task: Provide a brief yet clear explanation for the word '{word}' that is easy to understand and useful for language learners.

        Instructions:

        Meaning: Provide the most common meaning of the word or phrase in Arabic 4 maximum and 1 minimum only the meaning nothing else and should be the true meaning of the word.
        
        Definition: Give a concise and clear definition of the word/phrase in English and translate it to arabic.

        Part of Speech: Identify the part of speech (e.g., noun, verb, adjective).

        Example Sentence: Provide one example sentence using the word/phrase in context.

        Synonym (if applicable): List one synonym for the word and translate it into Arabic (if needed).

        Antonym (if applicable): List one antonym for the word and translate it into Arabic (if needed).

        Formatting Guidelines:

        Make sure the explanation is easy to follow and simple for language learners to grasp."""
    prompt += f"\n\nto make it looks better and more organized you can use HTML style format <strong>bold</strong> for bold text this for the definition  , <ins>underline</ins> for underline text this for the meaning in Arabic and <blockquote> </blockquote> for examples also make it bold the examples\n\n please make sure to use them properly "
    try:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
        result = await unify(prompt)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("أستمر ⬅️", callback_data='spelling_continue')]])
        await query.edit_message_text(text=result, reply_markup=keyboard,parse_mode="HTML")
    except Exception as e:
        print(e)
        await error_handler(update, context, f"An error occurred while looking up the word: {str(e)}")
async def pronunciation_practice_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "pronunciation_sentence" in context.user_data:
        context.user_data["pronunciation_sentence"] = []
    
    all_sentences = get_all_pronunciation_sentences()
    max_attempts = len(all_sentences)  # To prevent infinite loop if all sentences are used
    attempts = 0

    while attempts < max_attempts:
        sentence = get_random_pronunciation_sentence()
        if sentence not in context.user_data.setdefault("pronunciation_sentence",[]):
            context.user_data["pronunciation_sentence"].append(sentence)
            break
        attempts += 1

    if attempts == max_attempts:
        await update.effective_message.reply_text("لقد تدربت على كل الجمل المتاحة لهذا المستوى. يُرجى اختيار مستوى آخر أو إيقاف التدريب.")
        await pronunciation_practice_start(update, context, "اختر مستوى جديد أو إيقاف التدريب:")
        return
    context.user_data['current_sentence'] = sentence
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 جرب جملة أخرى", callback_data='pronunciation_next')]])
    keyboard2 = ReplyKeyboardMarkup([
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    text = f"من فضلك سجل نفسك وأنت تقول هذه الجملة:\n<blockquote> {sentence} </blockquote>"
    text2 = "أرسل رسالتك الصوتية عندما تكون مستعدًا."
    if update.callback_query:
        try:
            await update.callback_query.edit_message_text(text, reply_markup=keyboard2,parse_mode="HTML")
            await update.callback_query.edit_message_text(text2, reply_markup=keyboard)
        except Exception as e:
            await update.effective_chat.send_message(text, reply_markup=keyboard2,parse_mode="HTML")
            await update.effective_chat.send_message(text2, reply_markup=keyboard)
    else:
        await update.message.reply_text(text, reply_markup=keyboard2,parse_mode="HTML")
        await update.message.reply_text(text2,reply_markup=keyboard,parse_mode="HTML")
     
async def pronunciation_next(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await pronunciation_practice_start(update, context)


async def grammar_check_text(update: Update, context: ContextTypes.DEFAULT_TYPE,text=None):
    user_text = text or update.message.text
    
    prompt = f"""
    You are an expert English teacher. Analyze the following text for grammatical errors, 
    spelling mistakes, and suggestions for improvement. Provide a detailed report including:
    1. Overall assessment
    2. Grammatical errors (if any)
    3. Spelling mistakes (if any)
    4. Suggestions for improvement
    5. Corrected version of the text
    you should Explain in mixed Arabic and English and make it clear and easy to understand and make it orgnaized
    Text to analyze: {user_text}
    """
    prompt += f"\n\nto make it looks better and more organized you can use HTML style format <strong>bold</strong> for bold text  , <ins>underline</ins> for underline text  and <blockquote> </blockquote> for examples also make it bold the examples\n\n please make sure to use them properly "

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("تصحيح جملة أخرى", callback_data='grammar_check_another'),
         InlineKeyboardButton("العودة إلى القائمة", callback_data='return_main_menu')]
    ])
    keyboard2 = ReplyKeyboardMarkup([
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    
    try:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
        llm_response = await unify(prompt)
        
        await update.message.reply_text("تصحيح النص:",reply_markup=keyboard2,parse_mode="HTML")
        await send_long_message(update, context, llm_response, keyboard)
    except Exception as e:
        await error_handler(update, context, f"An error occurred while analyzing the text: {str(e)}")

async def grammar_check_image(update: Update, context: ContextTypes.DEFAULT_TYPE,file_id=None):
    if not update.message.photo:
        await update.message.reply_text("رجاءاً أرسل صورة لكتابتك لتصحيحها .")
        return

    # file = await context.bot.get_file(update.message.photo[-1].file_id)
    if file_id:
        file = await context.bot.get_file(file_id)
    else:
        file = await context.bot.get_file(update.message.photo[-1].file_id)
    image_bytes = await file.download_as_bytearray()
    image = Image.open(io.BytesIO(image_bytes))
    caption = update.message.caption if update.message.caption else "No caption provided"
    # print(caption)
    image_prompt = f"""
    Analyze the text in this image for grammatical errors, spelling mistakes, and suggestions 
    for improvement. Provide a detailed report including:
    1. Extracted text from the image
    2. Overall assessment
    3. Grammatical errors (if any)
    4. Spelling mistakes (if any)
    5. Suggestions for improvement
    6. Corrected version of the text
    you should Explain in mixed Arabic and English and make it clear and easy to understand and make it orgnaized

    Additionally, the user provided the following caption for this image:
    "{caption}"
    Please consider this caption in your analysis if it's relevant to the text in the image."""
    
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("تصحيح جملة أخرى", callback_data='grammar_check_another'),
         InlineKeyboardButton("العودة إلى القائمة", callback_data='return_main_menu')]
    ])
    keyboard2 = ReplyKeyboardMarkup([
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
    try:
        extracted_text = await gemini_ocr(image_prompt, image)
        
        prompt = f"""
        you will be given report of grammar check rewrite the report in mixed Arabic and English and make it clear and easy to understand and make it orgnaized
        the report: \n\n{extracted_text}
        """
        prompt += f"\n\nto make it looks better and more organized you can use HTML style format <strong>bold</strong> for bold text  , <ins>underline</ins> for underline text  and <blockquote> </blockquote> for examples also make it bold the examples\n\n please make sure to use them properly and only use these  tags and make sure you do it accurtally and perfectly this will be for telegram bot"
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
        llm_response = await unify(prompt)
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
        await update.message.reply_text("هذا هو تصحيح كتابتك:",reply_markup=keyboard2,parse_mode="HTML")
        await send_long_message(update, context, llm_response, keyboard)
    except Exception as e:
        await error_handler(update, context, f"An error occurred while analyzing the image: {str(e)}")


GRAMMAR_TOPICS = {
    "الأزمنة": {
        "زمن المضارع": ["المضارع البسيط", "المضارع المستمر", "المضارع التام", "المضارع التام المستمر"],
        "زمن الماضي": ["الماضي البسيط", "الماضي المستمر", "الماضي التام", "الماضي التام المستمر"],
        "زمن المستقبل": ["المستقبل البسيط", "المستقبل المستمر", "المستقبل التام", "المستقبل التام المستمر"]
    },
    "أجزاء الكلام": ["الأسماء", "الأفعال", "الصفات", "الظرف-الحال", "الضمائر", "حروف الجر", "حروف العطف", "أدوات التعريف","الأفعال الناقصة","الجمل الشرطية"],
    "تركيب الجملة": ["الجمل البسيطة", "الجمل المركبة", "الجمل المعقدة", "الجمل المركبة المعقدة"],
    "علامات الترقيم": ["(,) الفاصلة", "(.) نقطة نهاية الجملة", "(؟) علامة الإستفهام", "(!) علامة التعجب", "(;) فاصلة منقوطة", "(:) نقطتان", '("") علامة الاقتباس', "(-) الشرطة", ],
    # "Other Topics": []
}

async def grammar_lessons_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topics = list(GRAMMAR_TOPICS.keys())
    keyboard = []
    for i in range(0, len(topics), 2):
        row = [KeyboardButton(topics[i])]
        if i + 1 < len(topics):
            row.append(KeyboardButton(topics[i + 1]))
        keyboard.append(row)
    
    keyboard.append([KeyboardButton("/stop")])
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("أختر موضوع القواعد:", reply_markup=reply_markup)
    context.user_data['grammar_state'] = 'topic'
async def grammar_subtopic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text
    if topic in GRAMMAR_TOPICS:
        subtopics = GRAMMAR_TOPICS[topic]
        keyboard = []
        
        if isinstance(subtopics, dict):
            subtopics_list = list(subtopics.keys())
        else:
            subtopics_list = subtopics
        
        for i in range(0, len(subtopics_list), 2):
            row = [KeyboardButton(subtopics_list[i])]
            if i + 1 < len(subtopics_list):
                row.append(KeyboardButton(subtopics_list[i + 1]))
            keyboard.append(row)
        keyboard.append([KeyboardButton("/stop")])
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(f"أختر الدرس:", reply_markup=reply_markup)
        context.user_data['grammar_state'] = 'subtopic'
        context.user_data['grammar_topic'] = topic
    else:
        await update.message.reply_text("رجاءاً أختر الدرس من القائمة.")
async def grammar_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE, topic=None, subtopic=None):
    if not topic:
        topic = context.user_data.get('grammar_topic')
        subtopic = update.message.text
    
    if topic in GRAMMAR_TOPICS:
        if isinstance(GRAMMAR_TOPICS[topic], dict):
            if subtopic in GRAMMAR_TOPICS[topic]:
                if isinstance(GRAMMAR_TOPICS[topic][subtopic], list):
                    # This is a sub-subtopic
                    # This is a sub-subtopic
                    sub_subtopics = GRAMMAR_TOPICS[topic][subtopic]
                    keyboard = []
                    
                    for i in range(0, len(sub_subtopics), 2):
                        row = [KeyboardButton(sub_subtopics[i])]
                        if i + 1 < len(sub_subtopics):
                            row.append(KeyboardButton(sub_subtopics[i + 1]))
                        keyboard.append(row)
                    keyboard.append([KeyboardButton("/stop")])
                    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                    await update.message.reply_text(f"أختر الدرس:", reply_markup=reply_markup)
                    context.user_data['grammar_state'] = 'sub_subtopic'
                    context.user_data['grammar_subtopic'] = subtopic
                else:
                    # This is the final subtopic
                    keyboard = ReplyKeyboardMarkup([[KeyboardButton("/stop")]], resize_keyboard=True)
                    await send_lesson_content(update, context, topic, subtopic)
                    await update.message.reply_text("هذه بعض التمارين المخصصة للتدرب على الدرس:", reply_markup=keyboard)
                    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
                    await send_exercise(update, context, topic, subtopic)
            else:
                await update.message.reply_text("رجاءاً، أختر الدرس من القائمة.")
        elif isinstance(GRAMMAR_TOPICS[topic], list):
            if subtopic in GRAMMAR_TOPICS[topic]:
                keyboard = ReplyKeyboardMarkup([[KeyboardButton("/stop")]], resize_keyboard=True)
                await send_lesson_content(update, context, topic, subtopic)
                await update.message.reply_text("هذه بعض التمارين المخصصة للتدرب على الدرس:", reply_markup=keyboard)
                await send_exercise(update, context, topic, subtopic)
            else:
                await update.message.reply_text("رجاءاً، أختر الدرس من القائمة.")
    else:
        await update.message.reply_text("رجاءاً، أختر الدرس من القائمة.")

async def grammar_sub_subtopic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = context.user_data.get('grammar_topic')
    subtopic = context.user_data.get('grammar_subtopic')
    sub_subtopic = update.message.text
    
    if sub_subtopic in GRAMMAR_TOPICS[topic][subtopic]:
        keyboard = ReplyKeyboardMarkup([[KeyboardButton("/stop")]], resize_keyboard=True)
        await send_lesson_content(update, context, topic, subtopic, sub_subtopic)
        await update.message.reply_text("هذه بعض التمارين المخصصة للتدرب على الدرس:", reply_markup=keyboard)
        await send_exercise(update, context, topic, subtopic, sub_subtopic)
    else:
        await update.message.reply_text("رجاءاً، أختر الدرس من القائمة.")
def get_lesson_content(topic, subtopic, sub_subtopic=None):
    try:
        if sub_subtopic:
            lesson = LESSONS[topic][subtopic][sub_subtopic]
        else:
            lesson = LESSONS[topic][subtopic]
        
        return lesson["content"], lesson["youtube_link"], lesson["file_path"]
    except KeyError:
        return "Lesson content not found.", None, None

async def send_exercise(update: Update, context: ContextTypes.DEFAULT_TYPE, topic, subtopic, sub_subtopic=None):
    exercises = get_exercises(context, topic, subtopic, sub_subtopic)
    if not exercises:
        message = update.message if isinstance(update, Update) else update.message
        await message.reply_text("لا توجد تمارين متاحة لهذا الدرس. دعنا نعود إلى قائمة الدروس.")
        await grammar_lessons_start(update, context)
        return

    context.user_data['current_exercises'] = exercises
    context.user_data['exercise_index'] = 0
    await send_next_exercise_batch(update, context)

def shuffle_options(exercise):
    options = exercise['options']
    correct_answer = options[exercise['correct_option_id']]
    random.shuffle(options)
    new_correct_id = options.index(correct_answer)
    exercise['options'] = options
    exercise['correct_option_id'] = new_correct_id
    return exercise

async def send_next_exercise_batch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'current_exercises' not in context.user_data:
        # If we're starting a new lesson, get all exercises (they're already shuffled)
        context.user_data['current_exercises'] = get_exercises(context, context.user_data['topic'], context.user_data['subtopic'], context.user_data.get('sub_subtopic'))
        context.user_data['exercise_index'] = 0

    exercises = context.user_data['current_exercises']
    index = context.user_data['exercise_index']
    
    if isinstance(update, CallbackQuery):
        message = update.message
    else:
        message = update.effective_message

    batch_size = min(5, len(exercises) - index)
    for i in range(batch_size):
        exercise = exercises[index + i]
        exercise = shuffle_options(exercise)  # We still shuffle options for each exercise
        try:
            await message.reply_poll(
                question=exercise['question'],
                options=exercise['options'],
                type=Poll.QUIZ,
                correct_option_id=exercise['correct_option_id'],
                is_anonymous=True,
                explanation=exercise.get('explanation', '')
            )
        except BadRequest as e:
            if "Message is too long" in str(e):
                try:
                    await message.reply_poll(
                        question=exercise['question'],
                        options=exercise['options'],
                        type=Poll.QUIZ,
                        correct_option_id=exercise['correct_option_id'],
                        is_anonymous=True
                    )
                except BadRequest:
                    continue
            else:
                raise

    context.user_data['exercise_index'] += batch_size

    if context.user_data['exercise_index'] >= len(exercises):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("العودة إلى قائمة الدروس", callback_data='return_topics')]
        ])
        await message.reply_text(
            "تهانيناً! لقد أكملت كل التمارين لهذا الدرس.",
            reply_markup=keyboard
        )
    else:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("المزيد من التمارين ⬅️", callback_data='continue_exercises')],
            [InlineKeyboardButton("العودة إلى قائمة الدروس", callback_data='return_topics')]
        ])
        await message.reply_text(
            f"لقد أكملت {context.user_data['exercise_index']} تمارين. هل تريد المزيد من التمارين أو العودة الى قائمة الدروس",
            reply_markup=keyboard
        )

async def send_lesson_content(update: Update, context: ContextTypes.DEFAULT_TYPE, topic, subtopic, sub_subtopic=None):
    content, youtube_link, file_path = get_lesson_content(topic, subtopic, sub_subtopic)
    
    # Send lesson content
    # await update.message.reply_text(content)
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
    prompt= f"You will be given Grammar lesson on this topic {topic}, {subtopic}, {sub_subtopic} \n\nthis is the content of the lesson {content} \n\n i want you to orgnize the lesson and make is look better by applying HTML style format to make it looks better <strong>bold</strong> for bold text, <ins>underline</ins> for underline text and <blockquote> </blockquote> this for examples. you can use this when it is aprpriate to use it and when it is not important don't you use it you should make it perfectly Note: do not make any changes on the content just apply the new format style and only use these  tags <strong> <ins> <blockquote> and make sure you do it accurtally and perfectly this will be for telegram bot"
    # prompt += f"\n\nyou can use HTML style format to make it looks better <strong>bold</strong> for bold text, <ins>underline</ins> for underline text and <blockquote> </blockquote> this for examples. you can use this when it is aprpriate to use it and when it is not important don't you use it you should make it perfectly"
    lesson = await unify(prompt)
    await send_long_message(update, context, lesson,reply_markup=None)
    # Send YouTube link
    if youtube_link:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
        await update.message.reply_text(f"{youtube_link}")
    
    # Send file
    if file_path:
        try:
            with open(file_path, 'rb') as file:
                await update.message.reply_document(file)
        except FileNotFoundError:
            # await update.message.reply_text("Sorry, the lesson file is not available at the moment.")
            pass



def get_exercises(context: ContextTypes.DEFAULT_TYPE, topic, subtopic, sub_subtopic=None):
    try:
        if topic == "الأزمنة":
            if sub_subtopic:
                all_exercises = EXERCISES[topic][subtopic][sub_subtopic]
            else:
                return []
        else:
            all_exercises = EXERCISES[topic][subtopic]
        
        exercises_list = list(all_exercises.values()) if isinstance(all_exercises, dict) else all_exercises
        
        # Remove the used_exercise_indices check to always get all exercises
        available_exercises = [
            ex for ex in exercises_list 
            if len(ex['question']) <= 300 and all(len(option) <= 100 for option in ex['options'])
        ]
        # Shuffle the available exercises
        random.shuffle(available_exercises)
        
        return available_exercises
    except KeyError:
        print(f"KeyError in get_exercises: topic={topic}, subtopic={subtopic}, sub_subtopic={sub_subtopic}")
        return []



async def send_next_exercise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    exercises = context.user_data['current_exercises']
    index = context.user_data['exercise_index']

    if index < len(exercises):
        exercise = exercises[index]
        await update.effective_message.reply_poll(
            question=exercise['question'],
            options=exercise['options'],
            type=Poll.QUIZ,
            correct_option_id=exercise['correct_option_id'],
            is_anonymous=True
        )
        context.user_data['exercise_index'] += 1
    else:
        keyboard = ReplyKeyboardMarkup([['More Exercises', 'Return to Topics']], one_time_keyboard=True)
        await update.effective_message.reply_text(
            "تهانيناً! لقد أكملت كل التمارين لهذا الدرس.",
            reply_markup=keyboard
        )
        context.user_data['grammar_state'] = 'more_exercises'

async def handle_more_exercises(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'More Exercises':
        topic = context.user_data.get('grammar_topic')
        subtopic = context.user_data.get('grammar_subtopic')
        sub_subtopic = context.user_data.get('grammar_sub_subtopic')
        await send_exercise(update, context, topic, subtopic, sub_subtopic)
    else:
        await grammar_lessons_start(update, context)

async def handle_more_exercises(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text in ['More Exercises', 'Continue']:
        if context.user_data['exercise_index'] >= len(context.user_data['current_exercises']):
            # If we've used all current exercises, get new ones
            topic = context.user_data.get('grammar_topic')
            subtopic = context.user_data.get('grammar_subtopic')
            sub_subtopic = context.user_data.get('grammar_sub_subtopic')
            await send_exercise(update, context, topic, subtopic, sub_subtopic)
        else:
            # If we still have exercises, send the next batch
            await send_next_exercise_batch(update, context)
    else:
        await grammar_lessons_start(update, context)


async def handle_exercise_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    exercise = context.user_data.get('current_exercise')
    if not exercise:
        await query.edit_message_text("اسف هناك مشكلة لم استطع ارسال التمارين لهذا الدرس حاول مرة اخرى")
        return

    choice = int(query.data.split('_')[1])
    if choice == exercise['correct']:
        response = "Correct! Well done."
    else:
        response = f"Sorry, that's not correct. The right answer is: {exercise['choices'][exercise['correct']]}"

    await query.edit_message_text(f"{query.message.text}\n\n{response}")
    
    # Offer to continue or return to main menu
    keyboard = [
        [InlineKeyboardButton("الإستمرار", callback_data="grammar_continue")],
        [InlineKeyboardButton("العودة الى القائمة الرئيسية", callback_data="return_main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="ماذا تريد أن تفعل؟", reply_markup=reply_markup)

async def handle_more_exercises(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        await query.answer()

    if update.callback_query and update.callback_query.data == 'continue_exercises':
        await send_next_exercise_batch(update, context)
    elif update.callback_query and update.callback_query.data == 'return_topics':
        await grammar_lessons_start(update, context)

async def vocabulary_flashcards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Get user's current vocabulary level
    user_data = await supabase_select("users", "vocab_level, vocab_know, vocab_dont_know", "user_id", user_id)
    vocab_level = user_data.data[0]['vocab_level'] if user_data.data else "simple"
    vocab_know = set(user_data.data[0]['vocab_know']) if user_data.data and user_data.data[0]['vocab_know'] else set()
    vocab_dont_know = set(user_data.data[0]['vocab_dont_know']) if user_data.data and user_data.data[0]['vocab_dont_know'] else set()

    # Get words for the current level
    words = get_words(vocab_level)
    
    # Find a word that the user doesn't know
    unknown_words = set(words) - vocab_know - vocab_dont_know
    if not unknown_words:
        # If all words are known, move to the next level
        if vocab_level == "simple":
            vocab_level = "medium"
        elif vocab_level == "medium":
            vocab_level = "hard"
        else:
            await update.message.reply_text("ألف مبروك! لقد أنتهيت من تعلم كل الكلمات المتاحة")
            return
        
        # Update user's vocabulary level in the database
        await supabase_update("users", {"vocab_level": vocab_level}, "user_id", user_id)
        
        # Get words for the new level
        words = get_words(vocab_level)
        unknown_words = set(words) - vocab_know - vocab_dont_know

    # Choose a random unknown word
    word = random.choice(list(unknown_words))

    # Create inline keyboard
    keyboard = [
        [InlineKeyboardButton("أعرفها ✅", callback_data=f"vocab_know_{word}"),InlineKeyboardButton("لا أعرفها ❌", callback_data=f"vocab_dont_know_{word}")],
        [InlineKeyboardButton("تغيير مستوى المفردات 🔁", callback_data="vocab_change_level")],
        [InlineKeyboardButton("إلغاء ❌", callback_data="vocab_stop")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        await context.bot.send_message(chat_id=update.effective_chat.id , text=f"هل تعرف معنى الكلمة <strong><u>({word})</u></strong> ؟", reply_markup=reply_markup,parse_mode="HTML")
        # await update.callback_query.edit_message_text(f"Do you know the word: {word}?", reply_markup=reply_markup)
    else:
        await update.message.reply_text(f"هل تعرف معنى الكلمة <strong><u>({word})</u></strong> ؟", reply_markup=reply_markup,parse_mode="HTML")

async def vocabulary_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    action, word = query.data.split('_', 2)[1:]

    if action == "know":
        # Add word to known words
        user_data = await supabase_select("users", "vocab_know", "user_id", user_id)
        vocab_know = set(user_data.data[0]['vocab_know']) if user_data.data and user_data.data[0]['vocab_know'] else set()
        vocab_know.add(word)
        await supabase_update("users", {"vocab_know": list(vocab_know)}, "user_id", user_id)
        await query.edit_message_text(f"رائع! أنت تعرف الكلمة '{word}'. دعنا ننتقل إلى الكلمة التالية.")
        await vocabulary_flashcards(update, context)
    elif action == "dont":
        # Add word to unknown words
        user_data = await supabase_select("users", "vocab_dont_know", "user_id", user_id)
        vocab_dont_know = set(user_data.data[0]['vocab_dont_know']) if user_data.data and user_data.data[0]['vocab_dont_know'] else set()
        vocab_dont_know.add(word)
        await supabase_update("users", {"vocab_dont_know": list(vocab_dont_know)}, "user_id", user_id)

        # Get word definition using LLM
        prompt = f"Provide a simple definition and an example sentence for the word '{word}':"
        prompt += f"\n\nto make it looks better and more organized you can use HTML style format <strong>bold</strong> for bold text this for the definition  , <ins>underline</ins> for underline text this for the meaning in Arabic and <blockquote> </blockquote> for examples also make it bold the examples\n\n please make sure to use them properly "
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
        definition = await unify(prompt)

        keyboard = [
            [InlineKeyboardButton("الكلمة التالية ⬅️", callback_data="vocab_next")],
            [InlineKeyboardButton("إلغاء ❌", callback_data="vocab_stop")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(f"الكلمة: {word}\n\n{definition}", reply_markup=reply_markup,parse_mode="HTML")
    elif action == "next":
        await vocabulary_flashcards(update, context)
    elif action == "stop":
        # await query.edit_message_text("Vocabulary practice stopped. You can start again anytime!")
        await send_main_menu(update, context)


async def vocabulary_recap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Get user's known and unknown vocabularies
    user_data = await supabase_select("users", "vocab_know, vocab_dont_know", "user_id", user_id)
    vocab_know = set(user_data.data[0]['vocab_know']) if user_data.data and user_data.data[0]['vocab_know'] else set()
    vocab_dont_know = set(user_data.data[0]['vocab_dont_know']) if user_data.data and user_data.data[0]['vocab_dont_know'] else set()
    if not vocab_know and not vocab_dont_know:
        await update.message.reply_text("ليس لديك أي كلمات للمراجعة حاليا")
        await vocabulary_flashcards(update, context)
        return 
    # Combine known and unknown vocabularies
    all_vocab = list(vocab_know.union(vocab_dont_know))
    
    # Initialize or get the list of recapped words for this session
    if 'word_recap_session' not in context.user_data:
        context.user_data['word_recap_session'] = []

    # Remove words that have already been recapped in this session
    available_vocab = [word for word in all_vocab if word not in context.user_data['word_recap_session']]

    if not available_vocab:
        if update.callback_query:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="ممتاز! لقد انتهيت من مراجعة كل المفردات لهذا اليوم")
        else:
            await update.message.reply_text("ممتاز! لقد انتهيت من مراجعة كل المفردات لهذا اليوم")
        # Clear the recap session data
        context.user_data.pop('word_recap_session', None)
        await send_main_menu(update, context)
        return

    # Choose a random word
    word = random.choice(available_vocab)

    # Get meanings using LLM
    prompt = f"""Generate a Python list of four potential Arabic meanings for the English word '{word}'. The first meaning must be the correct meaning, while the other three should be incorrect but plausible. Ensure that the incorrect meanings are distinct, unrelated, and not synonyms of each other and the correct meaning in Arabic. Each meaning should be a single word. Output only the list in the following format:
    ["صحيح", "خاطئ1", "خاطئ2", "خاطئ3"]
    No additional text or explanation, just the list.
    """
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
    llm_response1 = await unify(prompt)
    prompt = f"""
    you will be given a list of four potential Arabic meanings for the English word '{word}'. The first meaning must be the correct meaning, while the other three should be incorrect 
    your task is to check these options and they shoud be different in the meaning of the correct answer in Arabic if you find any option that be potentially have similar meaning to the correct answer please change it to another one and make sure that the correct answer is in the first place ["صحيح", "خاطئ1", "خاطئ2", "خاطئ3"] make sure the correct answer is the true meaning of the word {word} and other options are not the correct answers 
    and you must return it as python list 
    the list is {llm_response1}
    """
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
    llm_response = await unify(prompt)
    # print(llm_response)
    try:
        # Use regex to find the list in the response
        list_match = re.search(r'\[.*?\]', llm_response, re.DOTALL)
        if list_match:
            list_string = list_match.group()
            meanings = ast.literal_eval(list_string)
        else:
            raise ValueError("No list found in LLM response")

        # Ensure we have exactly 4 meanings
        if len(meanings) != 4:
            raise ValueError("LLM did not return exactly 4 meanings")

    except Exception as e:
        print(f"Error processing LLM response: {e}")
        print(f"LLM response was: {llm_response}")
        meanings = ["معنى1", "معنى2", "معنى3", "معنى4"]  # 
    # Shuffle the meanings
    correct_meaning = meanings[0]
    random.shuffle(meanings)
    correct_option_id = meanings.index(correct_meaning)
    if update.callback_query:
        message = update.callback_query.message
    else:
        message = update.message
    # Create and send the poll
    word = f"<u>({word})</u>"
    keyboard = [
        [InlineKeyboardButton("الكلمة التالية ⬅️", callback_data="word_recap_next")],
        [InlineKeyboardButton("إلغاء ❌", callback_data="word_recap_stop")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_poll(
        question=f"مامعنى الكلمة {word}؟",
        question_parse_mode="HTML",
        options=meanings,
        type=Poll.QUIZ,
        correct_option_id=correct_option_id,
        explanation=f"معنى الكلمة <strong><u>{word}</u></strong> هو <strong><u>{correct_meaning}</u></strong>.",
        explanation_parse_mode="HTML",
        is_anonymous=False,
        reply_markup=reply_markup
    )

    # Add the word to the session's recap list
    context.user_data['word_recap_session'].append(word)

    # Provide option to continue or stop
    # keyboard = [
    #     [InlineKeyboardButton("الكلمة التالية ⬅️", callback_data="word_recap_next")],
    #     [InlineKeyboardButton("إلغاء ❌", callback_data="word_recap_stop")]
    # ]
    # reply_markup = InlineKeyboardMarkup(keyboard)
    
    # if update.callback_query:
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text="هل تريد الإستمرار أو التوقف", reply_markup=reply_markup)
    # else:
    #     await update.message.reply_text("هل تريد الإستمرار أو التوقف", reply_markup=reply_markup)


async def ai_tutor(update: Update, context: ContextTypes.DEFAULT_TYPE,transcription):
    user_id = update.effective_user.id
    if 'ai_tutor_history' not in context.user_data:
        context.user_data['ai_tutor_history'] = []
        context.user_data['ai_tutor_mode'] = 'text'  # Default to text mode
        
        # Add initial system message to history
        # system_message = {
        #     "role": "system",
        #     "content": "You are an AI English tutor. Your goal is to help the user improve their English skills. Be patient, encouraging, and provide clear explanations. If the user makes mistakes, gently correct them and explain why. Adapt your language to the user's proficiency level."
        # }
        # context.user_data['ai_tutor_history'].append(system_message)
        keyboard = ReplyKeyboardMarkup([
        # [KeyboardButton("📚 Dictionary")],
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
        await update.message.reply_text(
            "مرحبًا بك مع مدرس اللغة الانجليزية بالذكاء الاصطناعي! يمكنك أن تسألني عن أي شيء يتعلق باللغة الإنجليزية، وسأبذل قصارى جهدي لمساعدتك."
            "تستطيع ان تتواصل معي عبر الكتابة أو الرسائل الصوتية🔥",
            reply_markup=keyboard
        )
        return

    # Determine if the input is text or voice
    if update.message.text:
        user_message = update.message.text
        input_mode = 'text'
        voice_mode = False
    elif update.message.voice:
        # file_id = update.message.voice.file_id
        # user_message = await convert_audio_to_text(file_id, update, context)
        user_message = transcription
        # print("transcription ",transcription)
        input_mode = 'voice'
        voice_mode = True
    elif update.message.photo:
        file = await context.bot.get_file(update.message.photo[-1].file_id)
        image_bytes = await file.download_as_bytearray()
        image = Image.open(io.BytesIO(image_bytes))
        caption = update.message.caption if update.message.caption else "No caption provided"
        input_mode = 'photo'
        voice_mode = False
        user_message = caption
    else:
        await update.message.reply_text("عفوا يمكنك فقط التواصل معي عبر الرسائل النصية والصوتية")
        return

    if input_mode == 'voice':
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="RECORD_VOICE")
    elif input_mode == 'text':
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
    if input_mode == 'photo':
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
        history = context.user_data.get('ai_tutor_history',[])
        describe = await gemini_ocr2(f"describe the image for me in details and what the user wants from it {caption} and if it contains text extract all the text from it ",image)
        print("caption ",caption)
        prompt = f"""
        this is the caption provided by the user for the image:\n\n{caption}\n\n
        to help you more you will be provided with the image description and image content:\n\n {describe}

        """
        # response = await gemini_ocr2(prompt,image)
        response = await get_ai_tutor_response(context.user_data['ai_tutor_history'], prompt, voice_mode,True)
        # print("describe ",describe)
    else:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="TYPING")
        response = await get_ai_tutor_response(context.user_data['ai_tutor_history'], user_message, voice_mode,False)
    try:
        if input_mode == 'photo':
            context.user_data['ai_tutor_history'].append({"image_caption": caption})
            context.user_data['ai_tutor_history'].append({f"tutor_answer to the image caption {caption}": response })
            # context.user_data['ai_tutor_history'].append({f"image description of the image: {caption}": describe })
        else:
            context.user_data['ai_tutor_history'].append({"user_question": user_message})
            context.user_data['ai_tutor_history'].append({f"tutor_answer to the user question {user_message}": response })
    except Exception as e:
        print(e)
    
    if input_mode == 'voice':
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="RECORD_VOICE")
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="RECORD_VOICE")
        audio_file = await convert_text_to_audio(response, "Dan")
        try:
            with open(audio_file, 'rb') as audio:
                await update.message.reply_voice(audio)
        except Exception as e:
            print(e)
            # await update.message.reply_text(response)
            with open(audio_file, 'rb') as audio:
                await context.bot.send_voice(chat_id=update.effective_chat.id, voice=audio)
        finally:
            # Delete the file after sending
            if os.path.exists(audio_file):
                os.remove(audio_file)
        
    else:
        await update.message.reply_text(response,parse_mode="HTML")

    # Update the AI tutor mode for the next interaction
    context.user_data['ai_tutor_mode'] = input_mode
async def get_ai_tutor_response(history,user_message, voice_mode=False,photo=False):
    # print("history ",history)
    # print("user_message ",user_message)
    unify_API = await api_key_supabase("unify")
    client = AsyncOpenAI(
        base_url="https://api.unify.ai/v0/",
        api_key=unify_API
    )
    if voice_mode:
        
        system_prompt = f"You are an AI English tutor. Your goal is to help the user improve their English skills. Be patient, encouraging, and provide clear explanations. If the user makes mistakes, gently correct them and explain why. Adapt your language to the user's proficiency level. you will be asked questions from the student and you should answer them as if you are a real teacher. you should not add anything else just the answer to the question. to help you to be aware of the context of the question you will be provided with the chat history and the last message from the student this is the history of the char it contains student previous questions with your previous responses\n\n {history} \n\nyou can use the history as memory for you to remember previous chats, make your responses seem like a spoken conversation with the student, rather than a text-based interaction. your response should not be long make it short and concise"
        
    else:
        if photo:
            system_prompt = f"You are an AI English tutor. Your goal is to help the user improve their English skills. Be patient, encouraging, and provide clear explanations. If the user makes mistakes, gently correct them and explain why. Adapt your language to the user's proficiency level. you will be asked questions from the student and you should answer them as if you are a real teacher. you should not add anything else just the answer to the question. to help you to be aware of the context of the question you will be provided with the chat history and the last message from the student this is the history of the char it contains student previous questions with your previous responses\n\n {history} \n\nyou can use the history as memory for you to remember previous chats, Note if the user sent you his question in Arabic or any other language you should consider that and your response should be mixed in english and user language if sent it in only English respond in English \n\n another thing when the user asks you to explain something in English like grammar etc.. you should explain it in mixec Arabic and English the level of the user is beginner and needs the explanation in Arabic and english and you must explain them in detials and should be clear and simple to understand"
            system_prompt += f"\n\nyou can use HTML style format <strong>bold</strong> for bold text, <ins>underline</ins> for underline text and <blockquote> </blockquote> this for examples. you can use this when it is aprpriate to use it and when it is not important don't you use it"
        else:
            system_prompt = f"""You are an AI English tutor. Your goal is to help the user improve their English skills. 
        Be patient, encouraging, and provide clear explanations. If the user makes mistakes, 
        gently correct them and explain why. Adapt your language to the user's proficiency level.
        you will be asked questions from the student and you should answer them as if you are a real teacher. 
        you should not add anything else just the answer to the question. 
        to help you to be aware of the context of the question you will be provided with the chat history 
        and the last message from the student this is the history of the char it contains student previous 
        questions with your previous responses\n\n {history} \n\nyou can use the history as memory for you 
        to remember previous chats, 
        Here you will be given an image sent by the user and your task is to respond about what he wants from this image 
        you can find what he wants from the caption of the image if the user requested anythig in the caption you must answer him in details and if there was no caption please ask him what he wants you to do in Arabic and english , and you should be smart enough to understand what he wants from the image and you should be able to do it
        and if it is a question please answer it or if the user requested anything do it for him
        and you should be aware of the context of the question and the image and you should be able to do it
        your answer should be in the same language of the caption or the question or the request and be clear and simple to understand
        """
            system_prompt += f"\n\nyou can use HTML style format <strong>bold</strong> for bold text, <ins>underline</ins> for underline text and <blockquote> </blockquote> this for examples. you can use this when it is aprpriate to use it and when it is not important don't you use it"
    if photo:
        content = user_message
    else:
        
        content = f"this is the last message from the student {user_message}"
    # print("history \n\n",history)
    response = await client.chat.completions.create(
        model="gemini-1.5-flash-002@vertex-ai",
        messages=[{
            "role": "system",
            "content": system_prompt
        },
                  {"role": "user", "content": content }],
        max_tokens=4096,
        temperature=0.0,
        stream=False
    )
    result = response.choices[0].message.content
    result = re.sub(r'\*', '', result)
    result = re.sub(r'#', '', result)
    
    return result


async def reading_sources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "أفضل المصادر لتحسين مهارةالقراءة"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    text = "أفضل تطبيقات الجوال لتطوير مهارة القراءة"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    ph_list =["https://play.google.com/store/apps/details?id=com.ewa.ewaapp&pcampaignid=web_share","https://apps.apple.com/us/app/ewa-english-language-learning/id1200778841","https://play.google.com/store/apps/details?id=com.palmdev.expressenglish&pcampaignid=web_share","https://play.google.com/store/apps/details?id=com.google.android.apps.seekh&pcampaignid=web_share",]
    for i in ph_list:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=i)
    
    text = "أفضل المواقع لتحسين مهارة القراءة"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    ph_list =["https://learnenglish.britishcouncil.org/skills/reading","https://medium.com","https://BBC.com",]
    for i in ph_list:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=i)
    
    text = "أفضل الكتب لتحسين مهارة القراءة"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    ph_list =["https://t.me/Oxford_Bookwormss"]
    for i in ph_list:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=i)
    ph_list =["https://www.youtube.com/watch?v=Zo0WdtXNgv0","https://www.youtube.com/watch?v=7IvzjiomYks","https://www.youtube.com/watch?v=EFBGKdxFbNo"]
    for i in ph_list:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=i)
    
    
    
    
    
    
async def listening_sources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "أفضل المصادر لحسين مهارة الاستماع في اللغة الإنجليزية"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    text ="أبرز البرامج الصوتيه (البودكاست) لتطوير مهارة الاستماع في اللغة الإنجليزية"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    ph_list =["https://learnenglish.britishcouncil.org/skills/listening","https://open.spotify.com/show/2kzXWXMAAPZYfwtan7F2R5","https://open.spotify.com/show/6qXldSz1Ulq1Nvj2JK5kSR","https://open.spotify.com/show/4X48gpjrctXNJWtOnUgwq8"]
    for i in ph_list:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=i)
    
    # text = "أفضل المواقع لتحسين مهارة القراءة"
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    # ph_list =["https://learnenglish.britishcouncil.org/skills/reading","https://medium.com","https://BBC.com",]
    # for i in ph_list:
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text=i)
    
    text = "فيديوهات مميزة لكيفية تحسين مهارة الاستماع "
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    ph_list =["https://www.youtube.com/watch?v=B4ellCG4u84", "https://www.youtube.com/watch?v=xf8737RwwbU","https://www.youtube.com/watch?v=nMC16FZhsUM"]
    for i in ph_list:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=i)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="لاتنسى أيضا متابعة القنوات الأجنبية على اليوتيوب لتطوير مهارة الاستماع لديك")
    
async def writing_sources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
async def speaking_sources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
async def english_learning_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
async def api_key_supabase(provider):
    import random
    import time
    from typing import List
    
    async def execute_query():
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None,
            partial(supabase.table('api_keys').select('key').eq('provider', provider).eq('valid', True).execute)
        )
    
    try:
        start_time = time.time()
        
        result = await execute_query()
        
        if not result.data:
            raise ValueError(f"No API keys found for provider: {provider}")
        
        api_keys: List[str] = [item['key'] for item in result.data]
        
        end_time = time.time()
        execution_time = end_time - start_time
        # print(f"API key retrieval for {provider} took {execution_time:.4f} seconds")
        
        if len(api_keys) == 1:
            return api_keys[0]
        else:
            return random.choice(api_keys)
    
    except Exception as e:
        print(f"Error retrieving API key for {provider}: {str(e)}. Executing normal Supabase call...")
        try:
            # Execute normal Supabase call
            result = supabase.table('api_keys').select('key').eq('provider', provider).eq('valid', True).execute()
            
            if not result.data:
                raise ValueError(f"No API keys found for provider: {provider}")
            
            api_keys: List[str] = [item['key'] for item in result.data]
            
            if len(api_keys) == 1:
                return api_keys[0]
            else:
                return random.choice(api_keys)
        except Exception as final_e:
            print(f"Failed to execute Supabase query: {final_e}")
            raise Exception(f"Error retrieving API key for {provider}: {final_e}")



async def gemini_ocr(image_prompt, image_pil):
    max_retries = 3
    retries = 0
    
    try:
        while retries < max_retries:
            try:
                # keys = [gemini_api,gemini_api2]
                # api_key = random.choice(keys)
                api_key = await api_key_supabase("gemini")
                genai.configure(api_key=api_key)
                model_vision = genai.GenerativeModel('gemini-1.5-flash')
                response = model_vision.generate_content([image_prompt, image_pil])
                response.resolve()
                # extracted_text = response.text
                
                # Access the text parts
                extracted_text = ''.join(part.text for part in response.parts)
                extracted_text = re.sub(r'\*', '', extracted_text)
                extracted_text = re.sub(r'#', '', extracted_text)
                if len(extracted_text.split()) < 10:
                    raise Exception("Gemini Error it could not transcribe the text from the image")
                return extracted_text
            except Exception as e:
                print(e)
                retries += 1
                continue
        try:
            await Qwen2_ocr(image_prompt, image_pil,"Qwen/Qwen2-VL-72B-Instruct")
        except Exception as e:
            print(e)
            await Qwen2_ocr(image_prompt, image_pil,"mistralai/Pixtral-12B-2409")
        
    except Exception as e:

        print(e)
        raise Exception("Gemini and hyperbolic model Error it could not transcribe the text from the image")


async def gemini_ocr2(image_prompt, image_pil):
    max_retries = 5
    retries = 0
    
    try:
        while retries < max_retries:
            try:
                # keys = [gemini_api,gemini_api2]
                # api_key = random.choice(keys)
                api_key = await api_key_supabase("gemini")
                genai.configure(api_key=api_key)
                model_vision = genai.GenerativeModel('gemini-1.5-flash')
                response = model_vision.generate_content([image_prompt, image_pil])
                response.resolve()
                # extracted_text = response.text
                
                # Access the text parts
                extracted_text = ''.join(part.text for part in response.parts)
                extracted_text = re.sub(r'\*', '', extracted_text)
                extracted_text = re.sub(r'#', '', extracted_text)
                if len(extracted_text.split()) < 10:
                    raise Exception("Gemini Error it could not transcribe the text from the image")
                return extracted_text
            except Exception as e:
                print(e)
                retries += 1
                continue
        try:
            await Qwen2_ocr(image_prompt, image_pil,"Qwen/Qwen2-VL-72B-Instruct")
        except Exception as e:
            print(e)
            await Qwen2_ocr(image_prompt, image_pil,"mistralai/Pixtral-12B-2409")
        
    except Exception as e:

        print(e)
        raise Exception("Gemini and hyperbolic model Error it could not transcribe the text from the image")



async def Qwen2_ocr(image_prompt, image_pil,model):
    print(f"using {model} to extract essay")
    max_retries = 3
    retries = 0
    # print("image_pil",image_pil)
    import base64
    from io import BytesIO
    def encode_image(img):
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        encoded_string = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return encoded_string
    base64_img = encode_image(image_pil)
    api = "https://api.hyperbolic.xyz/v1/chat/completions"
    api_key = await api_key_supabase("hyperbolic")
    try:
        while retries < max_retries:
            try:
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                }


                payload = {
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text":f"{image_prompt}"},
                                {
                                    "type": "image_url",

                                    "image_url": {"url": f"data:image/jpeg;base64,{base64_img}"},
                                },
                            ],
                        }
                    ],
                    "model": model,
                    "max_tokens": 2048,
                    "temperature": 0.7,
                    "top_p": 0.9,
                }

                response = requests.post(api, headers=headers, json=payload)
                response_json = response.json()
                content = response_json['choices'][0]['message']['content']
                # print(content)
                return content
            except Exception as e:
                print(e)
                retries += 1
                continue
        raise Exception(f"{model} Error it could not transcribe the text from the image")
    except Exception as e:
        print(e)
        raise Exception(f"{model} Error it could not transcribe the text from the image")




async def supabase_select(table, column, equal,value ):
    async def execute_query():
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None,
            partial(supabase.table(table).select(column).eq(equal,value).execute)
        )

    delay = 1
    max_retries=2
    for attempt in range(max_retries):
        try:
            result = await execute_query()
            return result
        except Exception as e:
            import logging
            if attempt == max_retries - 1:
                # logging.warning(f"Attempt {attempt + 1} failed: {e}. Executing normal Supabase call...")
                try:
                    # Execute normal Supabase call
                    result = supabase.table(table).select(column).eq(equal, value).execute()
                    return result
                except Exception as final_e:
                    # logging.error(f"Failed to execute Supabase query after {max_retries} attempts and normal call: {final_e}")
                    raise Exception("🚨 Failed to execute Supabase query after {max_retries} attempts and normal call")
            # logging.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
            await asyncio.sleep(delay)
            delay *= 2  # Exponential backoff
        # except Exception as e:
        #     logging.error(f"Unexpected error in supabase_select: {e}")
        #     raise

    # logging.error(f"Max retries reached for Supabase query")
    # raise Exception("Max retries reached for Supabase query")


async def supabase_update(table, column, equal,value ):
    async def execute_query():
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(
            None,
            partial(supabase.table(table).update(column).eq(equal,value).execute)
        )
        
    delay = 1
    max_retries=2
    for attempt in range(max_retries):
        try:
            await execute_query()
            
        except Exception as e:
            import logging
            if attempt == max_retries - 1:
                # logging.error(f"Failed to execute Supabase query after {max_retries} attempts: {e}")
                try:
                    supabase.table(table).update(column).eq(equal,value).execute()
                except Exception as e:
                    raise Exception("🚨 Failed to execute Supabase query after {max_retries} attempts")
            # logging.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
            await asyncio.sleep(delay)
            delay *= 2  # Exponential backoff
        # except Exception as e:
        #     logging.error(f"Unexpected error in supabase_select: {e}")
        #     raise

    # logging.error(f"Max retries reached for Supabase query")
    # raise Exception("Max retries reached for Supabase query")

async def supabase_insert(table: str, data: dict):
    async def execute_insert():
        loop = asyncio.get_running_loop()
        # Add time_created field with current UTC timestamp
        data['time_created'] = datetime.now(timezone.utc).isoformat()
        return await loop.run_in_executor(
            None,
            partial(supabase.table(table).insert(data).execute)
        )

    try:
        result = await execute_insert()
        return result
    except Exception as e:
        print(f"Error inserting data into {table}: {str(e)}")
        raise



async def deepgram_tts(text, examiner_voice2):
    try:
        # deppgarm_api = random.choice(deepgram_api_keys)
        # if examiner_voice == "" or examiner_voice == None:
        #     examiner_voice2 = "aura-asteria-en"
        
        # else:
        #     print(f"🚨 No voice found for {examiner_voice}, using default voice")
        #     examiner_voice2 = "aura-asteria-en"
        
        deepgram_api = await api_key_supabase("deepgram")
        deepgram = DeepgramClient(deepgram_api)
        SPEAK_OPTIONS = {"text": text}
        filename = "output_deepgram.wav"
        options = SpeakOptions(
            model=examiner_voice2,
            encoding="linear16",
            container="wav",
        )
        response = deepgram.speak.rest.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename
    except Exception as e:
        print(f"🚨 deepgram error {e}")
        raise Exception("🚨 deepgram error")
async def make_request(text, examiner_voice,api):
      if not text.strip():
          raise ValueError("🚨 Input text contains no characters.")
      
      if examiner_voice == "" or examiner_voice == None:
          print("a problem in examiner voice: it is:",examiner_voice )
          examiner_voice = "Dan"
      
    #   unreal_speech_api = random.choice(unreal_speech_API_keys)
      response = requests.post(
          'https://api.v7.unrealspeech.com/stream',
          headers={
              'Authorization': f"Bearer {api}"
            #   'Authorization' : 'Bearer O1NloOK2SySJS72tnQ9ZaeRDYQPWecclkKgK6v1UmOsvfpsuSLDBTb'
          },
          json={
              'Text': text,
              'VoiceId': examiner_voice,
              'Bitrate': '64k',
              'Speed': '0',
              'Pitch': '1',
              'Codec': 'libmp3lame',
          }
      )
      
      if response.status_code == 200:
          # Save the audio content to a file
          import time
          audio_filename = f"user_audio_{int(time.time())}.mp3"
          with open(audio_filename, 'wb') as f:
              f.write(response.content)
          return audio_filename
      elif response.status_code == 402:
          supabase.table('api_keys').update({
              'valid': False
          }).eq('key', api).execute()
          raise Exception(f"🚨 Failed to convert text to audio. Status code: {response.status_code} API key: {api}")
      elif response.status_code == 400:
            try:
              print(f"response.status_code == 400 use deepgram directly {response.status_code}")
              
              return await deepgram_tts(text, examiner_voice)
            except Exception as e:
                print(f"🚨 deepgram error {e}")
                raise Exception("🚨 deepgram error")  
      else:
          try:
              print(f"unknown error from unreal speech: {response.status_code}")
              
              return await deepgram_tts(text, examiner_voice)
          except Exception as e:
                print(f"🚨 deepgram error {e}")
                raise Exception("🚨 deepgram error") 
        #   raise Exception(f"🚨 Failed to convert text to audio. Status code: {response.status_code} API key: {api}")

async def convert_text_to_audio(text, examiner_voice):
    try:
        print("convert text to audio")
        attempts = 0
        while attempts < 3:
            try:
                #   unreal_speech_api = random.choice(unreal_speech_API_keys)
                unreal_speech_api = await api_key_supabase("unrealspeech")
                #   print(unreal_speech_api)
                # return make_request(text, examiner_voice, unreal_speech_api)
                # loop = asyncio.get_running_loop()
                # task = await loop.run_in_executor(None, make_request, text, examiner_voice, unreal_speech_api)
                # return task
                result = await make_request(text, examiner_voice, unreal_speech_api)
                return result
            except Exception as e:
                print(f"Attempt {attempts + 1} failed: {e}")
                attempts += 1
                continue
        else:
            print("🚨 using deepgram instead of unreal speech")
            return await deepgram_tts(text, examiner_voice)
        
    except Exception as e:
        print(f"🚨 convert text to audio error {e}")
        raise Exception("🚨 convert text to audio error")




async def convert_audio_to_text(file_id, update, context):
    # print("DeepGram version: ",deepgram.__version__)
    try:
        try:
            # deppgarm_api = random.choice(deepgram_api_keys)
            deepgram_api = await api_key_supabase("deepgram")
            deepgram_client = DeepgramClient(deepgram_api)
            print(f"{update.effective_user.id} convert audio to text")
            file = await context.bot.get_file(file_id)
            
            file_path = file.file_path
            AUDIO_URL = {
                "url": file_path
            }
            
            options = PrerecordedOptions(
                model="nova-2",
                smart_format=True,
                filler_words=False,
                numerals=False,
            )
            # print(f"File path: {file_path}")
            response = deepgram_client.listen.rest.v("1").transcribe_url(AUDIO_URL, options)
            transcript = response.to_json(indent=4)
            response_data = json.loads(transcript)
            transcript_text = response_data['results']['channels'][0]['alternatives'][0]['transcript']
            return transcript_text
        except Exception as e:
            # deppgarm_api = random.choice(deepgram_api_keys)
            deepgram_api = await api_key_supabase("deepgram")
            deepgram_client = DeepgramClient(deepgram_api)
            print(f"{update.effective_user.id} convert audio to text second option")
            file = await context.bot.get_file(file_id)
            
            file_path = file.file_path
            AUDIO_URL = {
                "url": file_path
            }
            
            options = PrerecordedOptions(
                model="nova-2",
                smart_format=True,
                filler_words=True,
                numerals=False,
            )
            # print(f"File path: {file_path}")
            response = deepgram_client.listen.rest.v("1").transcribe_url(AUDIO_URL, options)
            transcript = response.to_json(indent=4)
            response_data = json.loads(transcript)
            transcript_text = response_data['results']['channels'][0]['alternatives'][0]['transcript']
            return transcript_text
    except Exception as e:
        text = ("🚨 convert audio to text function",e)
        # await update.message.reply_text(issue_message)
        error_traceback = traceback.format_exc()
        print(error_traceback)
        await error_handler(update, context,text)


# async def wisperSTT(filename,update,context):
#     try:
#         # groq_api = await api_key_supabase("groq")
#         groq_api = "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"
#         client = Groq(api_key=groq_api)
#         # filename = os.path.dirname(__file__) + "/audio.m4a"
#         print(filename)
#         file = await context.bot.get_file(filename)
            
#         file_path = file.file_path
#         print(file_path)
#         with open(file_path, "rb") as file:
#             transcription = client.audio.transcriptions.create(
#             file=(file_path, file.read()),
#             model="whisper-large-v3",
#             prompt="Transcribe the audio according to the language spoken. If the audio includes multiple languages, transcribe each part in its respective language. For instance, if a speaker uses both Arabic and English, write the Arabic parts in Arabic and the English parts in English within the same message.",
#             temperature=0.0,
#             response_format="verbose_json",
#             )
#             print(transcription.text)
#             return transcription.text
#     except Exception as e:
#         print(e)
#         return await convert_audio_to_text(filename,update,context)
async def gemini_model(prompt):
            try:
                # keys = [gemini_api,gemini_api2]
                # api_key = random.choice(keys)
                api_key = await api_key_supabase("gemini")
                genai.configure(api_key=api_key)
                model_vision = genai.GenerativeModel('gemini-1.5-flash')
                response = model_vision.generate_content(prompt)
                response.resolve()
                # extracted_text = response.text
                
                # Access the text parts
                extracted_text = ''.join(part.text for part in response.parts)
                # if len(extracted_text.split()) < 10:
                #     raise Exception("Gemini Error it could not transcribe the text from the image")
                return extracted_text
            except Exception as e:
                    print(e)


async def unify(prompt):
    try:
        result = await gemini_model(prompt)
        # result = re.sub(r'\*', '', result)
        # result = re.sub(r'#', '', result)
        result = result.replace('*', '').replace('#', '')
        return result
    except Exception as e:
        unify_API = await api_key_supabase("unify")
        client = AsyncOpenAI(
                    base_url="https://api.unify.ai/v0/",
                    api_key=unify_API
                )
        response = await client.chat.completions.create(
                            model="gemini-1.5-flash-002@vertex-ai",
                            messages=[
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=4096,
                            temperature=0.0,
                            stream=False
                        )
                        
        result = response.choices[0].message.content
        # result = re.sub(r'\*', '', result)
        # result = re.sub(r'#', '', result)
        result = result.replace('*', '').replace('#', '')
        return result


async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Clear the user data
    await remove_keyboard(update,context)
    context.user_data.clear()
    
    # Send a message about stopping the current operation
    stop_message = (
        "العودة الى القائمة الرئيسية"
    )
    if update.callback_query:
        await update.callback_query.edit_message_text(stop_message)
    else:
        await update.message.reply_text(stop_message)
    
    # Return to the main menu
    await send_main_menu(update, context)


async def stop_spelling(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Generate the report
    correct_count = context.user_data.get('correct_count', 0)
    wrong_count = context.user_data.get('wrong_count', 0)
    print(correct_count,wrong_count)
    
    total_count = correct_count + wrong_count
    
    if total_count > 0:
        accuracy = (correct_count / total_count) * 100
        correct_words = ", ".join(context.user_data['session_words']['correct'])
        incorrect_words = ", ".join(context.user_data['session_words']['incorrect'])
        
        report = "📊 Spelling Practice Report:\n\n"
        report += f"Total words attempted: {total_count}\n"
        report += f"Correct spellings: {correct_count}\n"
        report += f"Incorrect spellings: {wrong_count}\n"
        report += f"Accuracy: {accuracy:.2f}%\n\n"
        report += f"🟢 Correctly spelled words:\n{correct_words}\n\n"
        report += f"🔴 Incorrectly spelled words:\n{incorrect_words}\n\n"
        report += "Keep practicing to improve your spelling skills!"
    else:
        report = "You haven't attempted any words in this session."

    # Clear the user data
    context.user_data.clear()
    
    # Send the report
    if update.callback_query:
        await update.callback_query.edit_message_text(report)
    else:
        await update.message.reply_text(report)
    
    # Return to the main menu
    await send_main_menu(update, context)



BOT_TOKEN = "7844510473:AAGaz-6R3nLUZJCtCIb68LfoTLrBULSshvE"
# BOT_TOKEN = "7515607864:AAHhFH6C82sgNDWjQOr7RwYZBBLJpCYS20k"
async def main():
    print("main")
    request = HTTPXRequest(
    connection_pool_size=50,
    connect_timeout=10.0,
    read_timeout=300,
    pool_timeout=20.0
)
    # application = Application.builder().token(TOKEN).build()
    # application = Application.builder().token(BOT_TOKEN).read_timeout(200).connection_pool_size(50).build()
    application = (
    Application.builder()
    .token(BOT_TOKEN)
    .request(request)
    .build()
)
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    stop_handler = CommandHandler('stop', stop_command)
    application.add_handler(stop_handler)
    message_handler_instance = MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    application.add_handler(message_handler_instance)
    photo_handler = MessageHandler(filters.PHOTO, message_handler)
    application.add_handler(photo_handler)
    application.add_handler(CommandHandler('grammar', grammar_lessons_start))
    
    
    
    voice_handler_instance = MessageHandler(filters.VOICE, audio_handler)
    application.add_handler(voice_handler_instance)
    button_handler_instance = CallbackQueryHandler(button_handler,block=False)
    application.add_handler(button_handler_instance)
    application.add_handler(CommandHandler("vocabulary", vocabulary_flashcards))
    application.add_handler(CallbackQueryHandler(vocabulary_callback, pattern="^vocab_"))
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    while True:
        await asyncio.sleep(1)
def run_flask():
    app.run(host='0.0.0.0', port=8080) 

if __name__ == '__main__':
    # Start the Flask app in a separate thread
    from threading import Thread
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Run the bot in the main thread
    asyncio.run(main())
    
    
    
    
    

# In your main() function, add:
# setup_handlers(application)
