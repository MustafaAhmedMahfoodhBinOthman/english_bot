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
from groq import Groq
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
url: str = "https://ruzcfhezadjscqipzhiw.supabase.co"
key: str=  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1emNmaGV6YWRqc2NxaXB6aGl3Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNzYxNzAwMSwiZXhwIjoyMDQzMTkzMDAxfQ.zf536bzlbHZiLm-DcFBmjmZW52_QrVK8gT1uixfskKA"
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
        await ask_preferred_accent(update, context)
    else:
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
                    text="You can send more text or images for grammar checking. Or, if you're done, you can return to the main menu."
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
        
        else:
            await edit_message_with_fallback(update, context, "I'm sorry, I didn't understand that command.")
    
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
        await update.callback_query.edit_message_text("I'm sorry, I don't have a sentence for you to practice. Let's start over.")
        await pronunciation_practice_start(update, context)
        return

    user_id = update.effective_user.id
    user_data = await supabase_select("users", "preferred_accent", "user_id", user_id)
    preferred_accent = user_data.data[0]['preferred_accent'] if user_data.data else "American"

    if preferred_accent == "American":
        preferred_accent = "Scarlett"
        audio_file = await convert_text_to_audio(current_sentence, preferred_accent)
    elif preferred_accent == "British":
        preferred_accent = "aura-athena-en"
        audio_file = await deepgram_tts(current_sentence, preferred_accent)

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Try Again", callback_data='pronunciation_try_again'),
         InlineKeyboardButton("Next", callback_data='pronunciation_next')],
        [InlineKeyboardButton("stop", callback_data='pronunciation_stop')]
    ])

    await update.callback_query.message.reply_voice(audio_file)
    await update.callback_query.message.reply_text(
        "Here's the correct pronunciation. Would you like to try again or move to the next sentence?",
        reply_markup=keyboard
    )

async def pronunciation_try_again(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_sentence = context.user_data.get('current_sentence')
    await update.callback_query.edit_message_text(
        f"Okay, let's try again. Please record yourself saying this sentence:\n\n{current_sentence}\n\nSend your voice message when you're ready."
    )
async def dictionary_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup([
        # [KeyboardButton("📚 Dictionary")],
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    await update.message.reply_text(
        "Please enter a word or phrase (maximum 2 words) you'd like to look up:",
        reply_markup=keyboard
    )
    context.user_data['mode'] = 'dictionary'
    context.user_data['awaiting_word'] = True

async def dictionary_process(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    word = update.message.text.strip().lower()
    if len(word.split()) > 2:
        await update.message.reply_text("Please enter a maximum of 2 words.", reply_markup=keyboard)
        context.user_data['awaiting_word'] = True
        return

    await update.message.reply_text("Processing your request...")

    prompt = f"""Provide a comprehensive explanation for the word or phrase '{word}' in English, followed by an Arabic translation. Include the following:

1. English Definition: Provide a clear and concise definition.
2. Arabic Translation: Translate the definition into fluent, natural Arabic as a native speaker would.
3. Part of Speech: Specify all applicable parts of speech for this word/phrase.
4. Usage Examples: Provide 5 diverse, contextual examples of how to use this word/phrase in sentences.
5. Synonyms: List at least 3 synonyms (if applicable).
6. Antonyms: List at least 3 antonyms (if applicable).

For each part of speech:
- Provide a specific definition.
- Give an example sentence.

Format the response in an easy-to-read manner, suitable for language learners. Use clear headings and bullet points where appropriate.

Ensure that the Arabic translation is accurate, natural, and reflects the nuances of the English explanation."""

    try:
        dictionary_content = await unify(prompt)
        await update.message.reply_text(dictionary_content)

        user_id = update.effective_user.id
        user_data = await supabase_select("users", "preferred_accent", "user_id", user_id)
        preferred_accent = user_data.data[0]['preferred_accent'] if user_data.data else "American"
        if preferred_accent == "American":
            preferred_accent = "Scarlett"
            audio_file = await convert_text_to_audio(word, preferred_accent)
        elif preferred_accent == "British":
            preferred_accent = "aura-athena-en"
            audio_file = await deepgram_tts(word, preferred_accent)
        await update.message.reply_voice(audio_file)

        await update.message.reply_text("Enter another word or /stop to exit Dictionary mode.", reply_markup=keyboard)
        context.user_data['awaiting_word'] = True
    except Exception as e:
        await error_handler(update, context, f"An error occurred: {str(e)}")
        context.user_data['awaiting_word'] = True


def setup_handlers(application):
    application.add_handler(CommandHandler('stop', stop_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, error_message: str):
    print(f"ID: {update.effective_user.id} Username: {update.effective_user.username} | {error_message}")
    issue_message = "🚨 I'm sorry; there's an issue with the bot. Please try again, and if the problem persists, send me a message at @ielts_pathway."
    userID = update.effective_user.id
    keyboard = [[InlineKeyboardButton("Try Again 🔁", callback_data=f"{userID}try_again")],
                [InlineKeyboardButton("Contact me ↗️", url=f"https://t.me/ielts_pathway")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        if update.effective_message:
            await update.effective_message.reply_text(issue_message, reply_markup=reply_markup)
        elif update.callback_query:
            await edit_message_with_fallback(update, context, issue_message)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=issue_message, reply_markup=reply_markup)
    except Exception as e:
        print(f"Failed to send error message: {e}")

async def audio_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await remove_keyboard(update,context)
    if context.user_data.get('mode') != 'pronunciation_practice':
        await update.message.reply_text("I'm not sure what to do with this audio. Are you in pronunciation practice mode?")
        return

    current_sentence = context.user_data.get('current_sentence')
    if not current_sentence:
        await update.message.reply_text("I'm sorry, I don't have a sentence for you to practice. Let's start over.")
        await pronunciation_practice_start(update, context)
        return

    file_id = update.message.voice.file_id
    try:
        transcript = await convert_audio_to_text(file_id, update, context)
        # transcript = transcript.lower().strip()
        # current_sentence = current_sentence.lower().strip()
        transcript_clean = re.sub(r'[^\w\s]', '', transcript.lower().strip())
        current_sentence_clean = re.sub(r'[^\w\s]', '', current_sentence.lower().strip())
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Next", callback_data='pronunciation_next'),
             InlineKeyboardButton("Get Pronunciation", callback_data='pronunciation_get')],
            [InlineKeyboardButton("stop", callback_data='pronunciation_stop')]
        ])

        keyboard2 = InlineKeyboardMarkup([
            [InlineKeyboardButton("Next", callback_data='pronunciation_next'),
             InlineKeyboardButton("stop", callback_data='pronunciation_stop')]
        ])
        
        if transcript_clean == current_sentence_clean:
            await update.message.reply_text("Great job! Your pronunciation was correct.", reply_markup=keyboard2)
        else:
            await update.message.reply_text(
                f"Good attempt, but not quite right. Try again or choose an option below.\n\n"
                f"You said: {transcript}\n\n"
                f"The correct sentence is: {current_sentence}",
                reply_markup=keyboard
            )
    except Exception as e:
        await error_handler(update, context, f"An error occurred while processing your audio: {str(e)}")

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
        await update.message.reply_text(f"An error occurred while looking up the word: {str(e)}")
    
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
    await update.callback_query.edit_message_text("Pronunciation practice has been stopped. Returning to the main menu.")
    await send_main_menu(update, context)  
async def spelling_practice_start(update: Update, context: ContextTypes.DEFAULT_TYPE,text):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Simple", callback_data='spelling_simple'),
         InlineKeyboardButton("Medium", callback_data='spelling_medium')],
        [InlineKeyboardButton("Hard", callback_data='spelling_hard'),
         InlineKeyboardButton("Sentence", callback_data='spelling_sentence')],
        [InlineKeyboardButton("Stop", callback_data='spelling_stop')]
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
        await update.message.reply_text("Choose the difficulty level:", reply_markup=keyboard)
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
        await update.effective_message.reply_text("You've practiced all available words for this difficulty level. Please choose another difficulty or stop the practice.")
        await spelling_practice_start(update, context, "Choose a new difficulty level:")
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
    if preferred_accent == "American":
        preferred_accent = "Scarlett"
        audio_file = await convert_text_to_audio(word, preferred_accent)
    elif preferred_accent == "British":
        preferred_accent = "aura-athena-en"
        audio_file = await deepgram_tts(word, preferred_accent)
    
    await update.effective_message.reply_voice(audio_file)
    await update.effective_message.reply_text("Please spell the word/sentence you just heard:", reply_markup=keyboard)


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
    print(text)
    
    if text == "📝 Spelling Practice" or text == "✏️ Spelling Checker":
        await spelling_practice_start(update, context,"Welcome to Spelling Practice!")
    elif text == "📚 Dictionary":
        await dictionary_start(update, context)
    elif text == "/stop":
        
        await stop_command(update, context)
    elif context.user_data.get('mode') == 'spelling_practice' and not context.user_data.get('awaiting_difficulty'):
        await check_spelling(update, context)
    elif context.user_data.get('mode') == 'dictionary' and context.user_data.get('awaiting_word'):
        context.user_data['awaiting_word'] = False
        await dictionary_process(update, context)
    elif text == "🗣️ Pronunciation Practice":
        context.user_data['mode'] = 'pronunciation_practice'
        await pronunciation_practice_start(update, context)
    elif text == "🔍 Grammar":
        main_menu_keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("📚 Grammar lessons"), KeyboardButton("🔍 Grammar Checker")],
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
        await update.message.reply_text("Please select an option from the menu below to get started!",reply_markup=main_menu_keyboard)
    # elif text == "🔍 Grammar Checker":
    #     keyboard2 = ReplyKeyboardMarkup([
    #     [KeyboardButton("/stop")]
    # ], resize_keyboard=True)
    #     await update.message.reply_text("Please send your text or an image of text for grammar checking.",reply_markup=keyboard2)
    #     context.user_data['mode'] = 'grammar_check'
    # elif context.user_data.get('mode') == 'grammar_check':
    #     if update.message.text:
    #         await grammar_check_text(update, context)
    #     elif update.message.photo:
    #         await grammar_check_image(update, context)
    #     context.user_data['mode'] = None
    elif context.user_data.get('mode') == 'grammar_check':
        if 'grammar_check_queue' not in context.user_data:
            context.user_data['grammar_check_queue'] = deque()

        if update.message.text and update.message.text not in ["📚 Dictionary", "🔍 Grammar Checker", "✏️ Spelling Checker", "🗣️ Pronunciation Practice"]:
            context.user_data['grammar_check_queue'].append(('text', update.message.text))
        elif update.message.photo:
            context.user_data['grammar_check_queue'].append(('photo', update.message.photo[-1].file_id))
        elif update.message.document:
            await update.message.reply_text("Please send your text directly or as an image. I can't process document files.")
            return
        else:
            await update.message.reply_text("Please send a text message or an image for grammar checking.")
            return

        if len(context.user_data['grammar_check_queue']) == 1:
            await process_grammar_check_queue(update, context)
        else:
            await update.message.reply_text(f"Queued for grammar checking. {len(context.user_data['grammar_check_queue'])} items in queue.")
        return
    
    elif text == "🔍 Grammar Checker":
        await update.message.reply_text("Please send your text or images for grammar checking. You can send multiple messages or images, and I'll check them one by one.")
        context.user_data['mode'] = 'grammar_check'
        context.user_data['grammar_check_queue'] = deque()
    elif text == "📚 Grammar lessons":
            await grammar_lessons_start(update, context)
    elif context.user_data.get('grammar_state') == 'topic':
        await grammar_subtopic(update, context)
    elif context.user_data.get('grammar_state') == 'subtopic':
        await grammar_lesson(update, context)
    elif context.user_data.get('grammar_state') == 'sub_subtopic':
        await grammar_sub_subtopic(update, context)
    elif text in ['More Exercises', 'Return to Topics'] and context.user_data.get('grammar_state') == 'more_exercises':
        await handle_more_exercises(update, context)
    
    
    else:
        await update.message.reply_text("I'm sorry, I didn't understand that command. Please use the menu options.")


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
            await update.message.reply_text(f"Sorry, that's not correct. You have {4 - context.user_data['attempts']} attempts left. Try again:")
        else:
            context.user_data['wrong_count'] = context.user_data.get('wrong_count', 0) + 1
            context.user_data['session_words']['incorrect'].append(context.user_data['current_word'])
            if context.user_data['current_difficulty'] != 'sentence':
                keyboard = InlineKeyboardMarkup([
                    [InlineKeyboardButton(f"Learn about '{context.user_data['current_word']}'", callback_data=f'learn_{context.user_data["current_word"]}')],
                    [InlineKeyboardButton("Continue", callback_data='spelling_continue')]
                ])
                await update.message.reply_text(
                    f"Sorry, the correct spelling is: {context.user_data['current_word']}",
                    reply_markup=keyboard
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
            [InlineKeyboardButton("American 🇺🇸", callback_data=f'accent_American')],
            [InlineKeyboardButton("British 🇬🇧", callback_data=f'accent_British')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.effective_message.reply_text("Which accent do you prefer?", reply_markup=reply_markup)
    except Exception as e:
        text = ("🚨 ask preferred accent function", e)
        error_traceback = traceback.format_exc()
        print(error_traceback)
        await error_handler(update, context, text)
        
async def send_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    main_menu_keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("📚 Dictionary"), KeyboardButton("🔍 Grammar")],
        [KeyboardButton("✏️ Spelling Checker"), KeyboardButton("🗣️ Pronunciation Practice")]
    ], resize_keyboard=True)
    
    welcome_message = (
        "Welcome to the English Learning Bot! 🎉\n\n"
        "What would you like to do today?\n\n"
        "📚 Dictionary: Look up words and their meanings\n"
        "🔍 Grammar Checker: Check your text or images for grammatical errors\n"
        "✏️ Spelling Checker: Verify the spelling of words\n"
        "🗣️ Pronunciation Practice: Practice your pronunciation\n\n"
        "Please select an option from the menu below to get started!"
    )
    await update.effective_message.reply_text(welcome_message, reply_markup=main_menu_keyboard)

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
    prompt = f"""Provide a concise explanation for the word '{word}', including:
    1. Definition
    2. Part of speech
    3. One example sentence
    4. One synonym (if applicable)
    5. One antonym (if applicable)
    Format the response in an easy-to-read manner, suitable for language learners."""

    try:
        result = await unify(prompt)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Continue", callback_data='spelling_continue')]])
        await query.edit_message_text(text=result, reply_markup=keyboard)
    except Exception as e:
        await query.edit_message_text(f"An error occurred while looking up the word: {str(e)}")
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
        await update.effective_message.reply_text("You've practiced all available sentences for this difficulty level. Please choose another difficulty or stop the practice.")
        await pronunciation_practice_start(update, context, "Choose a new difficulty level:")
        return
    context.user_data['current_sentence'] = sentence
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Try another sentence", callback_data='pronunciation_next')]])
    keyboard2 = ReplyKeyboardMarkup([
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    text = f"Please record yourself saying this sentence:\n\n{sentence}"
    text2 = "Send your voice message when you're ready."
    if update.callback_query:
        try:
            await update.callback_query.edit_message_text(text, reply_markup=keyboard2)
            await update.callback_query.edit_message_text(text2, reply_markup=keyboard)
        except Exception as e:
            await update.effective_chat.send_message(text, reply_markup=keyboard2)
            await update.effective_chat.send_message(text2, reply_markup=keyboard)
    else:
        await update.message.reply_text(text, reply_markup=keyboard2)
        await update.message.reply_text(text2,reply_markup=keyboard)
     
async def pronunciation_next(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await pronunciation_practice_start(update, context)


async def grammar_check_text(update: Update, context: ContextTypes.DEFAULT_TYPE,text=None):
    user_text = text or update.message.text
    
    prompt = """
    You are an expert English teacher. Analyze the following text for grammatical errors, 
    spelling mistakes, and suggestions for improvement. Provide a detailed report including:
    1. Overall assessment
    2. Grammatical errors (if any)
    3. Spelling mistakes (if any)
    4. Suggestions for improvement
    5. Corrected version of the text

    Text to analyze:
    """
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Check Another", callback_data='grammar_check_another'),
         InlineKeyboardButton("Return to Main Menu", callback_data='return_main_menu')]
    ])
    keyboard2 = ReplyKeyboardMarkup([
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    
    try:
        llm_response = await unify(prompt + user_text)
        
        await update.message.reply_text("Here's the analysis of your text:",reply_markup=keyboard2)
        await send_long_message(update, context, llm_response, keyboard)
    except Exception as e:
        await error_handler(update, context, f"An error occurred while analyzing the text: {str(e)}")

async def grammar_check_image(update: Update, context: ContextTypes.DEFAULT_TYPE,file_id=None):
    if not update.message.photo:
        await update.message.reply_text("Please send an image containing text to analyze.")
        return

    # file = await context.bot.get_file(update.message.photo[-1].file_id)
    if file_id:
        file = await context.bot.get_file(file_id)
    else:
        file = await context.bot.get_file(update.message.photo[-1].file_id)
    image_bytes = await file.download_as_bytearray()
    image = Image.open(io.BytesIO(image_bytes))

    image_prompt = """
    Analyze the text in this image for grammatical errors, spelling mistakes, and suggestions 
    for improvement. Provide a detailed report including:
    1. Extracted text from the image
    2. Overall assessment
    3. Grammatical errors (if any)
    4. Spelling mistakes (if any)
    5. Suggestions for improvement
    6. Corrected version of the text
    """
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Check Another", callback_data='grammar_check_another'),
         InlineKeyboardButton("Return to Main Menu", callback_data='return_main_menu')]
    ])
    keyboard2 = ReplyKeyboardMarkup([
        [KeyboardButton("/stop")]
    ], resize_keyboard=True)
    
    try:
        extracted_text = await gemini_ocr(image_prompt, image)
        await update.message.reply_text("Here's the analysis of the text in your image:",reply_markup=keyboard2)
        await send_long_message(update, context, extracted_text, keyboard)
    except Exception as e:
        await error_handler(update, context, f"An error occurred while analyzing the image: {str(e)}")


GRAMMAR_TOPICS = {
    "Tenses": {
        "Present Tense": ["Present Simple", "Present Continuous", "Present Perfect", "Present Perfect Continuous"],
        "Past Tense": ["Past Simple", "Past Continuous", "Past Perfect", "Past Perfect Continuous"],
        "Future Tense": ["Future Simple", "Future Continuous", "Future Perfect", "Future Perfect Continuous"]
    },
    "Parts of Speech": ["Nouns", "Verbs", "Adjectives", "Adverbs", "Pronouns", "Prepositions", "Conjunctions", "Articles","Modal Verbs","If-Clauses"],
    "Sentence Structure": ["Simple Sentences", "Compound Sentences", "Complex Sentences", "Compound-Complex Sentences"],
    "Punctuation": ["Commas", "Periods", "Question Marks", "Exclamation Points", "Semicolons", "Colons", "Quotation Marks", "Dash", ],
    # "Other Topics": []
}

async def grammar_lessons_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton(topic)] for topic in GRAMMAR_TOPICS.keys()]
    keyboard.append([KeyboardButton("/stop")])
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Choose a grammar topic:", reply_markup=reply_markup)
    context.user_data['grammar_state'] = 'topic'

async def grammar_subtopic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text
    if topic in GRAMMAR_TOPICS:
        subtopics = GRAMMAR_TOPICS[topic]
        if isinstance(subtopics, dict):
            keyboard = [[KeyboardButton(subtopic)] for subtopic in subtopics.keys()]
            keyboard.append([KeyboardButton("/stop")])
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await update.message.reply_text(f"Choose a subtopic for {topic}:", reply_markup=reply_markup)
            context.user_data['grammar_state'] = 'subtopic'
            context.user_data['grammar_topic'] = topic
        else:
            await grammar_lesson(update, context, topic, subtopics[0])
    else:
        await update.message.reply_text("Invalid topic. Please choose from the options provided.")

async def grammar_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE, topic=None, subtopic=None):
    if not topic:
        topic = context.user_data.get('grammar_topic')
        subtopic = update.message.text
    
    if topic and subtopic in GRAMMAR_TOPICS[topic]:
        if isinstance(GRAMMAR_TOPICS[topic], dict) and isinstance(GRAMMAR_TOPICS[topic][subtopic], list):
            # This is a sub-subtopic
            keyboard = [[KeyboardButton(sub_subtopic)] for sub_subtopic in GRAMMAR_TOPICS[topic][subtopic]]
            keyboard.append([KeyboardButton("/stop")])
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await update.message.reply_text(f"Choose a specific topic for {subtopic}:", reply_markup=reply_markup)
            context.user_data['grammar_state'] = 'sub_subtopic'
            context.user_data['grammar_subtopic'] = subtopic
        else:
            keyboard = ReplyKeyboardMarkup([
            # [KeyboardButton("📚 Dictionary")],
            [KeyboardButton("/stop")]
        ], resize_keyboard=True) 
            # This is the final subtopic
            lesson_content = get_lesson_content(topic, subtopic)
            await update.message.reply_text(lesson_content,reply_markup=keyboard)
            await send_exercise(update, context, topic, subtopic)
    else:
        await update.message.reply_text("Invalid subtopic. Please choose from the options provided.")
async def grammar_sub_subtopic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = context.user_data.get('grammar_topic')
    subtopic = context.user_data.get('grammar_subtopic')
    sub_subtopic = update.message.text
    
    if sub_subtopic in GRAMMAR_TOPICS[topic][subtopic]:
        keyboard = ReplyKeyboardMarkup([
            # [KeyboardButton("📚 Dictionary")],
            [KeyboardButton("/stop")]
        ], resize_keyboard=True) 
        lesson_content = get_lesson_content(topic, subtopic, sub_subtopic)
        await update.message.reply_text(lesson_content,reply_markup=keyboard)
        await send_exercise(update, context, topic, subtopic, sub_subtopic)
    else:
        await update.message.reply_text("Invalid topic. Please choose from the options provided.")

def get_lesson_content(topic, subtopic, sub_subtopic=None):
    # This function would return the lesson content for a given topic and subtopic
    # For now, we'll return a placeholder text
    lesson_text = f"Here's a lesson on {subtopic}"
    if sub_subtopic:
        lesson_text += f" - {sub_subtopic}"
    lesson_text += f" (part of {topic}):\n\n"
    lesson_text += "[Lesson content would go here]\n\n"
    lesson_text += "For more information, check out these resources:\n"
    lesson_text += "- [Link to a relevant video]\n"
    lesson_text += "- [Link to a grammar website]"
    return lesson_text

# async def send_exercise(update: Update, context: ContextTypes.DEFAULT_TYPE, topic, subtopic, sub_subtopic=None):
#     exercises = get_exercises(topic, subtopic, sub_subtopic)
#     if not exercises:
#         await update.message.reply_text("No exercises available for this topic.")
#         return

#     context.user_data['current_exercises'] = exercises
#     context.user_data['exercise_index'] = 0
#     await send_next_exercise_batch(update, context)

async def send_exercise(update: Update, context: ContextTypes.DEFAULT_TYPE, topic, subtopic, sub_subtopic=None):
    exercises = get_exercises(context, topic, subtopic, sub_subtopic)
    if not exercises:
        message = update.message if isinstance(update, Update) else update.message
        await message.reply_text("You've completed all available exercises for this topic. Great job! Let's return to the topics menu.")
        await grammar_lessons_start(update, context)
        return

    context.user_data['current_exercises'] = exercises
    context.user_data['exercise_index'] = 0
    await send_next_exercise_batch(update, context)

async def send_next_exercise_batch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    exercises = context.user_data['current_exercises']
    index = context.user_data['exercise_index']
    
    if isinstance(update, CallbackQuery):
        message = update.message
    else:
        message = update.effective_message

    batch_size = min(10, len(exercises) - index)
    for i in range(batch_size):
        exercise = exercises[index + i]
        await message.reply_poll(
            question=exercise['question'],
            options=exercise['options'],
            type=Poll.QUIZ,
            correct_option_id=exercise['correct_option_id'],
            is_anonymous=True,
            explanation=exercise['explanation']
        )
#     await message.reply_poll(
#        question="اختر الإجابة الصحيحة:\nShe ____ (go) to school every day.",
#        options=["54", "56", "58", "62"],
#        type="quiz",
#        correct_option_id=1,
#        explanation="Remember: 7 x 8 = 56. A helpful trick is to know that 7 x 8 is the same as 8 x 7, which is 8 more than 7 x 7 (49)."
#    )
    context.user_data['exercise_index'] += batch_size

    if context.user_data['exercise_index'] >= len(exercises):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Return to Topics", callback_data='return_topics')]
        ])
        await message.reply_text(
            "You've completed all exercises for this topic! Would you like to return to the topics menu?",
            reply_markup=keyboard
        )
    else:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Continue", callback_data='continue_exercises')],
            [InlineKeyboardButton("Return to Topics", callback_data='return_topics')]
        ])
        await message.reply_text(
            "Would you like to continue with more exercises or return to the topics menu?",
            reply_markup=keyboard
        )
# def get_exercises(topic, subtopic, sub_subtopic=None):
#     if sub_subtopic:
#         all_exercises = EXERCISES[topic][subtopic][sub_subtopic]
#     else:
#         all_exercises = EXERCISES[topic][subtopic]
    
#     return random.sample(all_exercises, min(20, len(all_exercises)))  # Get 20 exercises if available

def get_exercises(context: ContextTypes.DEFAULT_TYPE, topic, subtopic, sub_subtopic=None):
    if sub_subtopic:
        all_exercises = EXERCISES[topic][subtopic][sub_subtopic]
    else:
        all_exercises = EXERCISES[topic][subtopic]
    
    # Convert the exercises to a list if it's not already
    exercises_list = list(all_exercises.values()) if isinstance(all_exercises, dict) else all_exercises
    
    # Get the set of used exercise indices
    used_indices = set(context.user_data.get('used_exercise_indices', []))
    
    # Filter out used exercises
    available_exercises = [ex for i, ex in enumerate(exercises_list) if i not in used_indices]
    
    # If no exercises are available, return an empty list
    if not available_exercises:
        return []
    
    # Update the used exercise indices
    new_used_indices = [exercises_list.index(ex) for ex in available_exercises]
    context.user_data['used_exercise_indices'] = list(used_indices.union(new_used_indices))
    
    return available_exercises


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
            "You've completed all exercises! Would you like more exercises or return to the topics menu?",
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
        await query.edit_message_text("Sorry, there was an error with the exercise. Please try again.")
        return

    choice = int(query.data.split('_')[1])
    if choice == exercise['correct']:
        response = "Correct! Well done."
    else:
        response = f"Sorry, that's not correct. The right answer is: {exercise['choices'][exercise['correct']]}"

    await query.edit_message_text(f"{query.message.text}\n\n{response}")
    
    # Offer to continue or return to main menu
    keyboard = [
        [InlineKeyboardButton("Continue Learning", callback_data="grammar_continue")],
        [InlineKeyboardButton("Return to Main Menu", callback_data="return_main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="What would you like to do next?", reply_markup=reply_markup)



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
          examiner_voice = "Liv"
      
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



async def unify(prompt):
    
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
    result = re.sub(r'\*', '', result)
    result = re.sub(r'#', '', result)
    
    return result



async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Clear the user data
    await remove_keyboard(update,context)
    context.user_data.clear()
    
    # Send a message about stopping the current operation
    stop_message = (
        "🛑 All current operations have been stopped.\n"
        "Your session data has been cleared.\n"
        "Returning to the main menu..."
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



BOT_TOKEN = "7515607864:AAHhFH6C82sgNDWjQOr7RwYZBBLJpCYS20k"

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