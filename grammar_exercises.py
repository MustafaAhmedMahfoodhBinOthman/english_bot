# grammar_exercises.py

# grammar_exercises.py

EXERCISES = {
    "الأزمنة": {
        "زمن المضارع": {
            "المضارع البسيط": [
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (go) to school every day.",
        "options": ["go", "goes", "going", "went"],
        "correct_option_id": 1,
        "explanation": "لأن الفاعل (She) مفرد، نضيف حرف (s) للفعل (go) في المضارع البسيط، ليصبح goes.  نستخدم المضارع البسيط للتعبير عن عادة يومية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (play) football on weekends.",
        "options": ["play", "plays", "played", "playing"],
        "correct_option_id": 0,
        "explanation": "بما أن الفاعل (We) جمع، يبقى الفعل (play) بدون تغيير في المضارع البسيط. ويعبر عن عادة متكررة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/like) coffee.",
        "options": ["does not like", "do not like", "does not likes", "doesn't liking"],
        "correct_option_id": 0,
        "explanation": "مع الفاعل المفرد (He) في النفي، نستخدم 'does not' + الفعل في المصدر (like) بدون أي تغيير."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThe sun ____ (rise) in the east.",
        "options": ["rise", "rises", "rising", "rose"],
        "correct_option_id": 1,
        "explanation": "(The sun) مفرد، لذا نضيف s للفعل (rise)  فيصبح rises، لأن الجملة تتحدث عن حقيقة علمية ثابتة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (visit) their grandmother every summer.",
        "options": ["visit", "visits", "visited", "visiting"],
        "correct_option_id": 0,
        "explanation": "الفاعل (They) جمع، لذا يبقى الفعل (visit) بدون تغيير في المضارع البسيط، للدلالة على حدث متكرر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/go) to the gym on Mondays.",
        "options": ["does not go", "do not goes", "not goes", "does not going"],
        "correct_option_id": 0,
        "explanation": "يستخدم 'does not' مع الفاعل المفرد (He)  للنفي في المضارع البسيط، يليه الفعل في المصدر (go)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere ____ (you/live)?",
        "options": ["you live", "do you lives", "do you live", "are you live"],
        "correct_option_id": 2,
        "explanation": "في السؤال، نستخدم 'Do' قبل الفاعل (you)  مع الفعل في المصدر (live)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (work) as a teacher.",
        "options": ["work", "works", "worked", "working"],
        "correct_option_id": 1,
        "explanation": "بما أن (She) مفرد، يُضاف 's'  إلى الفعل (work) فيصبح 'works' في المضارع البسيط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/eat) meat.",
        "options": ["do not eat", "don't eats", "does not eat", "not eating"],
        "correct_option_id": 0,
        "explanation": "مع الفاعل الجمع (We)  نستخدم 'do not' + الفعل في المصدر (eat)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow often ____ (he/visit) his parents?",
        "options": ["does he visits", "he visits", "does he visit", "do he visit"],
        "correct_option_id": 2,
        "explanation": "في السؤال الذي يبدأ بـ 'How often'، نستخدم 'does' مع الفاعل المفرد (he) والفعل في المصدر (visit)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIt ____ (seem) like a good idea.",
        "options": ["seem", "seems", "seeming", "seemed"],
        "correct_option_id": 1,
        "explanation": "الفاعل (It) يُعامل معاملة المفرد، لذلك نضيف 's' للفعل (seem) ليصبح 'seems'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/play) tennis every day.",
        "options": ["do not play", "does not plays", "doesn't play", "does not play"],
        "correct_option_id": 0,
        "explanation": "مع الفاعل الجمع (They) في النفي، نستخدم 'do not' + الفعل في المصدر (play)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nMy brother ____ (not/eat) vegetables.",
        "options": ["does not eat", "do not eats", "eats not", "does eats"],
        "correct_option_id": 0,
        "explanation": "لأن الفاعل (My brother) مفرد، نستخدم 'does not' + الفعل في المصدر (eat)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (like) to read books in her free time.",
        "options": ["like", "likes", "liking", "liked"],
        "correct_option_id": 1,
        "explanation": "(She) مفرد، لذا نضيف 's'  إلى الفعل (like) في المضارع البسيط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhen ____ (they/come) to visit?",
        "options": ["they come", "do they comes", "are they come", "do they come"],
        "correct_option_id": 3,
        "explanation": "في السؤال مع (they)، نستخدم  'do' + الفاعل + الفعل في المصدر (come)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nMy friends and I ____ (meet) every Saturday.",
        "options": ["meet", "meets", "meeting", "met"],
        "correct_option_id": 0,
        "explanation": "الفاعل جمع (My friends and I) لذلك نستخدم الفعل في المصدر (meet) بدون أي إضافات."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nJohn always ____ (help) his neighbors.",
        "options": ["help", "helps", "helped", "helping"],
        "correct_option_id": 1,
        "explanation": "بما أن الفاعل (John) مفرد، نضيف 's' للفعل (help) في المضارع البسيط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/buy) clothes online.",
        "options": ["does not buy", "does not buys", "don't buy", "does not buying"],
        "correct_option_id": 0,
        "explanation": "مع الفاعل المفرد (She) في النفي، نستخدم 'does not' + الفعل في المصدر (buy)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThe class ____ (start) at 9 AM every day.",
        "options": ["start", "starts", "starting", "started"],
        "correct_option_id": 1,
        "explanation": "الفاعل (The class) مفرد، لذا نضيف 's' للفعل (start)."
    },
    
    {
        "question": "اختر الإجابة الصحيحة:\nWhy ____ (you/not/speak) to her?",
        "options": ["you not speak", "do you not speak", "you not speaks", "are you not speaking"],
        "correct_option_id": 1,
        "explanation": "في السؤال المنفي مع (you)، نستخدم 'do you not' + الفعل في المصدر (speak)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (watch) TV every night.",
        "options": ["watch", "watches", "watching", "watched"],
        "correct_option_id": 1,
        "explanation": "بما أن (He) مفرد، نضيف 'es' للفعل (watch) في المضارع البسيط، فنقول: watches."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/go) to the park on weekends.",
        "options": ["don't go", "doesn't goes", "do not go", "are not go"],
        "correct_option_id": 0,
      "explanation": "يستخدم 'don't'  أو 'do not' مع الفاعل الجمع (they)  للنفي في المضارع البسيط، يليه الفعل في المصدر (go)."

    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (he/play) football?",
        "options": ["Does he plays", "Do he plays", "Does he play", "Is he playing"],
        "correct_option_id": 2,
        "explanation": "في السؤال مع الفاعل المفرد (He)، نستخدم 'Does' + الفاعل + الفعل في المصدر (play)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe always ____ (wake) up early.",
        "options": ["wake", "wakes", "waked", "waking"],
        "correct_option_id": 1,
        "explanation": "بما أن الفاعل (She) مفرد، نضيف 's' للفعل (wake) في المضارع البسيط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (live) in London.",
        "options": ["live", "lives", "living", "lived"],
        "correct_option_id": 0,
        "explanation": "مع الفاعل (I) نستخدم الفعل في المصدر (live) بدون أي تغيير في المضارع البسيط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (they/study) English?",
        "options": ["Do they study", "Does they study", "Do they studies", "Are they study"],
        "correct_option_id": 0,
        "explanation": "في السؤال مع الفاعل الجمع (They) نستخدم  'Do' + الفاعل + الفعل في المصدر (study)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/understand) French.",
        "options": ["do not understand", "don't understands", "doesn't understand", "does not understands"],
        "correct_option_id": 0,
        "explanation": "في النفي مع الفاعل الجمع (We)، نستخدم 'do not' + الفعل في المصدر (understand)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (go) to the gym every evening.",
        "options": ["go", "goes", "going", "went"],
        "correct_option_id": 1,
        "explanation": "(She) مفرد، لذا نضيف 's' للفعل (go) في المضارع البسيط، ليصبح goes."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/want) to eat dinner right now.",
        "options": ["don't want", "doesn't want", "do not wants", "do not want"],
        "correct_option_id": 0,
        "explanation": "في النفي مع (I)، نستخدم 'don't' أو 'do not' + الفعل في المصدر (want)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (come) home late every day.",
        "options": ["come", "comes", "came", "coming"],
        "correct_option_id": 1,
        "explanation": "لأن (He) مفرد، نضيف 's' للفعل (come) ليصبح comes في المضارع البسيط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/visit) us often.",
        "options": ["do not visit", "does not visits", "don't visits", "are not visit"],
        "correct_option_id": 0,
        "explanation": "مع الفاعل الجمع (They) في النفي، نستخدم  'do not' + الفعل في المصدر (visit)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (she/like) chocolate?",
        "options": ["Does she like", "Does she likes", "Do she likes", "Do she like"],
        "correct_option_id": 0,
        "explanation": "في السؤال مع الفاعل المفرد (She)، نستخدم 'Does' + الفاعل + الفعل في المصدر (like)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) on weekends.",
        "options": ["doesn't works", "did not work", "don't work", "doesn't work"],
        "correct_option_id": 3, # Corrected index
        "explanation": "في النفي مع الفاعل المفرد (He) نستخدم 'doesn't' أو 'does not' + الفعل في المصدر (work)."

    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (visit) my family every summer.",
        "options": ["visits", "visited", "visiting", "visit"],
        "correct_option_id": 3,
        "explanation": "مع الفاعل (I) نستخدم الفعل في المصدر (visit) بدون أي تغيير في المضارع البسيط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/know) the answer.",
        "options": ["do not know", "don't knows", "does not know", "not knowing"],
        "correct_option_id": 0,
        "explanation": "مع الفاعل الجمع (they) في النفي، نستخدم  'do not' + الفعل في المصدر (know)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (work) in a hospital.",
        "options": ["works", "work", "worked", "working"],
        "correct_option_id": 0,
        "explanation": "بما أن الفاعل (She) مفرد، نضيف 's' للفعل (work) في المضارع البسيط."
    }
],
            "المضارع المستمر": [
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (read) a book right now.",
        "options": ["reads", "is reading", "read", "is read"],
        "correct_option_id": 1,
        "explanation": "نستخدم المضارع المستمر للتعبير عن حدث يحدث الآن.  الصيغة هي: is/am/are + verb-ing،  لذا تكون الإجابة الصحيحة هي is reading."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (play) football at the moment.",
        "options": ["are playing", "play", "is playing", "playing"],
        "correct_option_id": 0,
        "explanation": "بما أن الفاعل جمع (They)، نستخدم are مع الفعل-ing،  فتكون الإجابة are playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/sleep) now.",
        "options": ["is not sleep", "isn't sleeping", "doesn't sleep", "is not sleeping"],
        "correct_option_id": 3,
        "explanation": "في النفي، نضع not بعد is/am/are.  لذا تكون الإجابة is not sleeping أو isn't sleeping."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThe sun ____ (shine) right now.",
        "options": ["is shining", "shines", "shine", "is shine"],
        "correct_option_id": 0,
        "explanation": "لأن الفاعل مفرد (The sun)، نستخدم is مع الفعل-ing: is shining."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (watch) a movie this evening.",
        "options": ["are watching", "is watching", "watch", "watching"],
        "correct_option_id": 0,
        "explanation": "بما أن الفاعل جمع (We)، نستخدم are + watching: are watching."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) on his project at the moment.",
        "options": ["is not working", "doesn't working", "isn't work", "is working not"],
        "correct_option_id": 0,
        "explanation": "في النفي مع الفاعل المفرد (He)، نستخدم 'is not' + verb+ing، أي is not working."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere ____ (you/go) right now?",
        "options": ["do you going", "are you going", "you go", "you are going"],
        "correct_option_id": 1,
        "explanation": "في السؤال، نضع is/am/are قبل الفاعل: Are you going."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (cook) dinner at this moment.",
        "options": ["cooking", "is cooking", "cooks", "cook"],
        "correct_option_id": 1,
        "explanation": "لأن الفاعل (She) مفرد، نستخدم is + cooking: is cooking."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/watch) TV right now.",
        "options": ["are not watching", "isn't watching", "aren't watching", "does not watch"],
        "correct_option_id": 2,
        "explanation": "نستخدم aren't أو are not + watching في النفي مع الفاعل (We): aren't watching."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow ____ (they/do) on their exam now?",
        "options": ["are they doing", "is they doing", "do they doing", "are they do"],
        "correct_option_id": 0,
        "explanation": "في السؤال مع (They)، نستخدم Are they doing؟"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (seem) to be enjoying his new job.",
        "options": ["seeming", "is seem", "is seeming", "seems"],
        "correct_option_id": 2,
        "explanation": "الأفعال التي تصف حالة مثل (seem) تأخذ ing في المضارع المستمر أحيانًا لوصف حالة مؤقتة: is seeming."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/play) tennis now.",
        "options": ["does not playing", "are not play", "are not playing", "isn't playing"],
        "correct_option_id": 2,
        "explanation": "مع (We) في النفي، نستخدم are not playing أو aren't playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nMy brother ____ (write) an email at the moment.",
        "options": ["is writing", "writes", "writing", "is writes"],
        "correct_option_id": 0,
        "explanation": "بما أن الفاعل مفرد (My brother)، نستخدم is writing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (have) a great time at the party right now.",
        "options": ["having", "is having", "has", "is have"],
        "correct_option_id": 1,
        "explanation": "نستخدم is having للتعبير عن حدث يحدث الآن."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhen ____ (they/arrive) at the airport?",
        "options": ["are they arriving", "they are arriving", "is they arriving", "do they arriving"],
        "correct_option_id": 0,
        "explanation": "في السؤال مع (They)، نستخدم are they arriving؟"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nMy friends and I ____ (meet) for coffee now.",
        "options": ["is meeting", "are meeting", "meets", "meet"],
        "correct_option_id": 1,
        "explanation": "بما أن الفاعل جمع، نستخدم are meeting."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nJohn ____ (help) his friend move right now.",
        "options": ["is helping", "helps", "is help", "helping"],
        "correct_option_id": 0,
        "explanation": "John مفرد، لذا الإجابة هي is helping."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/wear) her favorite dress today.",
        "options": ["doesn't wearing", "isn't wearing", "not wear", "is not wear"],
        "correct_option_id": 1,
        "explanation": "في النفي مع (She)، نستخدم isn't wearing أو is not wearing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThe class ____ (begin) at this moment.",
        "options": ["is beginning", "beginning", "is begin", "begins"],
        "correct_option_id": 0,
        "explanation": "The class مفرد، لذا الإجابة is beginning."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhy ____ (you/not/listen) to me right now?",
        "options": ["are you not listening", "is you not listening", "do you not listen", "aren't you listen"],
        "correct_option_id": 0,
        "explanation": "في السؤال المنفي مع (you)، نستخدم are you not listening أو aren't you listening?"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (watch) TV at the moment.",
        "options": ["is watching", "watching", "watches", "watched"],
        "correct_option_id": 0,
        "explanation": "يستخدم المضارع المستمر للتعبير عن حدث يحدث الآن، ولأن الفاعل (He) مفرد، تكون الإجابة is watching."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/go) to the park right now.",
        "options": ["aren't going", "isn't going", "don't go", "doesn't goes"],
        "correct_option_id": 0,
        "explanation": "في النفي مع الفاعل الجمع (They) في المضارع المستمر، نستخدم aren't going أو are not going."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (he/play) football now?",
        "options": ["Does he play", "Is he playing", "He plays", "Does he plays"],
        "correct_option_id": 1,
        "explanation": "في السؤال بالمضارع المستمر مع الفاعل المفرد (He)، نستخدم Is he playing?"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (wake) up early this week.",
        "options": ["is waking", "wakes", "waking", "wake"],
        "correct_option_id": 0,
        "explanation": "بما أن الفاعل (She) مفرد، نستخدم is waking في المضارع المستمر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (live) with my parents for now.",
        "options": ["living", "am living", "lives", "is living"],
        "correct_option_id": 1,
        "explanation": "مع الفاعل (I) في المضارع المستمر، نستخدم am living."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (they/study) for their exams?",
        "options": ["Do they studying", "Are they study", "Are they studying", "Do they study"],
        "correct_option_id": 2,
        "explanation": "في السؤال مع (They) في المضارع المستمر، نستخدم Are they studying?"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/travel) anywhere this summer.",
        "options": ["is not travelling", "are not traveling", "aren't travel", "doesn't traveling"],
        "correct_option_id": 1,
        "explanation": "في النفي مع (We) في المضارع المستمر، نستخدم are not traveling أو aren't traveling."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (go) to the gym at this moment.",
        "options": ["going", "is going", "goes", "went"],
        "correct_option_id": 1,
        "explanation": "بما أن الفاعل (She) مفرد، نستخدم is going في المضارع المستمر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/eat) dinner right now.",
        "options": ["am not eating", "isn't eating", "don't eat", "am not eat"],
        "correct_option_id": 0,
        "explanation": "في النفي مع (I) في المضارع المستمر، نستخدم am not eating."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (come) over to my house this evening.",
        "options": ["is coming", "comes", "coming", "is comes"],
        "correct_option_id": 0,
        "explanation": "لأن الفاعل (He) مفرد، نستخدم is coming في المضارع المستمر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/work) on the project currently.",
        "options": ["doesn't working", "are not working", "aren't work", "do not working"],
        "correct_option_id": 1,
        "explanation": "في النفي مع (They) في المضارع المستمر، نستخدم are not working أو aren't working."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (she/like) what we are doing right now?",
        "options": ["Does she like", "Is she liking", "Is she like", "Does she liking"],
        "correct_option_id": 1,
        "explanation": "في السؤال مع (She) في المضارع المستمر، نستخدم Is she liking?" #"like" can be used in the continuous tense when it expresses a changing opinion.
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/take) the bus today.",
        "options": ["isn't taking", "is not take", "doesn't taking", "don't take"],
        "correct_option_id": 0,
        "explanation": "في النفي مع (He) في المضارع المستمر، نستخدم isn't taking أو is not taking."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (write) a letter right now.",
        "options": ["is writing", "am writing", "writes", "wrote"],
        "correct_option_id": 1,
        "explanation": "مع (I) في المضارع المستمر، نستخدم am writing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/plan) the trip right now.",
        "options": ["are not planning", "isn't planning", "aren't plan", "do not planning"],
        "correct_option_id": 0,
        "explanation": "في النفي مع (They) في المضارع المستمر، نستخدم are not planning أو aren't planning."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (work) from home today.",
        "options": ["is working", "working", "works", "work"],
        "correct_option_id": 0,
        "explanation": "بما أن الفاعل (She) مفرد، نستخدم is working في المضارع المستمر."
    },
     {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (have) a meeting right now.",
        "options": ["are having", "have", "is having", "has"],
        "correct_option_id": 0,
        "explanation": "بما أن الفاعل جمع (They)، نستخدم are having في المضارع المستمر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/drive) to work this week.",
        "options": ["isn't driving", "is not drive", "doesn't drive", "don't drive"],
        "correct_option_id": 0,
        "explanation": "في النفي مع (She) في المضارع المستمر، نستخدم isn't driving أو is not driving."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (you/cook) dinner tonight?",
        "options": ["Are you cooking", "Do you cook", "You are cooking", "You cooking"],
        "correct_option_id": 0,
        "explanation": "في السؤال مع (You) في المضارع المستمر، نستخدم Are you cooking?"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (build) a house for his family.",
        "options": ["is building", "builds", "building", "is build"],
        "correct_option_id": 0,
        "explanation": "لأن الفاعل (He) مفرد، نستخدم is building في المضارع المستمر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/swim) in the pool today.",
        "options": ["are not swimming", "isn't swimming", "aren't swim", "don't swimming"],
        "correct_option_id": 0,
        "explanation": "في النفي مع (We) في المضارع المستمر، نستخدم are not swimming أو aren't swimming."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (it/rain) outside now?",
        "options": ["Is it raining", "Does it rain", "It is raining", "Is it rain"],
        "correct_option_id": 0,
        "explanation": "في السؤال مع (It) في المضارع المستمر، نستخدم Is it raining?"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (prepare) for the party.",
        "options": ["are preparing", "prepare", "preparing", "prepares"],
        "correct_option_id": 0,
        "explanation": "بما أن الفاعل جمع (They)، نستخدم are preparing في المضارع المستمر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/sleep) well these days.",
        "options": ["isn't sleeping", "is not sleep", "doesn't sleep", "is not sleeps"],
        "correct_option_id": 0,
        "explanation": "في النفي مع (She) في المضارع المستمر، نستخدم isn't sleeping أو is not sleeping."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (he/work) on a new project?",
        "options": ["Is he working", "Does he work", "Is he work", "Does he works"],
        "correct_option_id": 0,
        "explanation": "في السؤال مع (He) في المضارع المستمر، نستخدم Is he working?"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (learn) how to play the guitar.",
        "options": ["am learning", "learn", "learning", "learns"],
        "correct_option_id": 0,
        "explanation": "مع (I) في المضارع المستمر، نستخدم am learning."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/travel) by train.",
        "options": ["are not traveling", "not travelling", "isn't traveling", "doesn't travel"],
        "correct_option_id": 0, #Or 1 - Both spellings are acceptable
        "explanation": "في النفي مع (They) في المضارع المستمر، نستخدم are not traveling/travelling أو aren't traveling/travelling."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (she/sing) in the shower?",
        "options": ["Is she singing", "Does she sing", "She is singing", "Does she sings"],
        "correct_option_id": 0,
        "explanation": "في السؤال مع (She) في المضارع المستمر، نستخدم Is she singing?"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (fix) his car right now.",
        "options": ["is fixing", "fixes", "fixing", "is fix"],
        "correct_option_id": 0,
        "explanation": "لأن الفاعل (He) مفرد، نستخدم is fixing في المضارع المستمر."
    }
],

            "المضارع التام": [
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (finish) my homework.",
        "options": ["has finished", "finishing", "have finished", "finished"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'have' مع الفاعل 'I' في المضارع التام لنشير إلى حدث انتهى مؤخرًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (visit) the museum recently.",
        "options": ["is visiting", "have visited", "has visited", "visited"],
        "correct_option_id": 2,
        "explanation": "بما أن الفاعل 'She' مفرد، نستخدم 'has' في المضارع التام مع الفعل 'visited'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/see) this movie yet.",
        "options": ["hasn't seen", "haven't saw", "has seen", "haven't seen"],
        "correct_option_id": 3,
        "explanation": "في النفي مع 'We'، نستخدم haven't + past participle (seen)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (live) here for five years.",
        "options": ["have lived", "lived", "has lived", "is living"],
        "correct_option_id": 2,
        "explanation": "يستخدم المضارع التام مع for + duration, ولأن (He) مفرد، نستخدم has lived."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/finish) their lunch.",
        "options": ["hasn't finished", "haven't finished", "didn't finish", "haven't finish"],
        "correct_option_id": 1,
        "explanation": "مع (They) في النفي، نستخدم haven't finished."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (just/buy) a new car.",
        "options": ["has bought", "has just bought", "have bought just", "just bought"],
        "correct_option_id": 1,
        "explanation": "نستخدم has just bought في المضارع التام مع just."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow long ____ (you/know) him?",
        "options": ["have you known", "did you know", "do you know", "have you know"],
        "correct_option_id": 0,
        "explanation": "في السؤال مع How long، نستخدم have you known."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/decide) what to do yet.",
        "options": ["hasn't decided", "are not deciding", "haven't decided", "didn't decide"],
        "correct_option_id": 2,
        "explanation": "مع yet في النفي، نستخدم haven't decided."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (never/eat) sushi before.",
        "options": ["have eaten never", "didn't eat", "haven't eaten", "have never eaten"],
        "correct_option_id": 3,
        "explanation": "مع never، نستخدم have never eaten.  'never' يقع بين have/has والتصريف الثالث للفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (see) this movie three times.",
        "options": ["saw", "have seen", "has seen", "has saw"],
        "correct_option_id": 2,
        "explanation": "لأن الفاعل (He) مفرد، نستخدم has seen."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (already/finish) their homework when you called.",
        "options": ["already finished", "has already finished", "have already finished", "have finished already"],
        "correct_option_id": 2,
        "explanation": "نستخدم have already finished في المضارع التام مع already."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (read) all the books in the series so far.",
        "options": ["has read", "read", "have read", "has readed"],
        "correct_option_id": 0,
        "explanation": "مع so far، نستخدم has read."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (you/ever/be) to Japan?",
        "options": ["Have you been ever", "Did you ever been", "Did you ever be", "Have you ever been"],
        "correct_option_id": 3,
        "explanation": "في السؤال مع ever، نستخدم Have you ever been."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (just/receive) the email.",
        "options": ["have just received", "just received", "has just received", "have received just"],
        "correct_option_id": 0,
        "explanation": "نستخدم have just received في المضارع التام مع just."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow many times ____ (she/call) today?",
        "options": ["has she called", "is she calling", "has she call", "did she call"],
        "correct_option_id": 0,
        "explanation": "في السؤال مع How many times، نستخدم has she called."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (already/finish) his work.",
        "options": ["already finished", "has already finished", "is already finished", "have already finished"],
        "correct_option_id": 1,
        "explanation": "نستخدم has already finished مع already."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/meet) him before.",
        "options": ["haven't met", "hasn't met", "didn't met", "have not meet"],
        "correct_option_id": 0,
        "explanation": "مع before في النفي، نستخدم haven't met."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (just/arrive) at the airport.",
        "options": ["arrived just", "has just arrived", "just arrived", "have just arrived"],
        "correct_option_id": 3,
        "explanation": "نستخدم have just arrived مع just."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (be) to France twice this year.",
        "options": ["been", "have been", "has been", "was"],
        "correct_option_id": 2,
        "explanation": "لأن الفاعل (He) مفرد، نستخدم has been."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (she/ever/try) Indian food?",
        "options": ["Has she tried ever", "Has she ever tried", "Did she ever tried", "Did she try ever"],
        "correct_option_id": 1,
        "explanation": "في السؤال مع ever، نستخدم Has she ever tried."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/see) him this week.",
        "options": ["haven't saw", "hasn't seen", "haven't seen", "haven't see"],
        "correct_option_id": 2,
        "explanation": "مع this week في النفي، نستخدم haven't seen."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (already/buy) their tickets.",
        "options": ["has already bought", "already bought", "have already bought", "have bought already"],
        "correct_option_id": 2,
        "explanation": "نستخدم have already bought مع already."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (you/ever/hear) this song?",
        "options": ["Have you heard ever", "Have you ever hear", "Did you ever heard", "Have you ever heard"],
        "correct_option_id": 3,
        "explanation": "في السؤال مع ever، نستخدم Have you ever heard."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (be) to Paris several times.",
        "options": ["has been", "have been", "is been", "has be"],
        "correct_option_id": 0,
        "explanation": "لأن الفاعل (She) مفرد، نستخدم has been."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/decide) where to go yet.",
        "options": ["hasn't decided", "haven't decide", "haven't decided", "didn't decided"],
        "correct_option_id": 2,
        "explanation": "مع yet في النفي، نستخدم haven't decided."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (never/see) such a beautiful sunset.",
        "options": ["never seen", "have never seen", "have never saw", "haven't seen never"],
        "correct_option_id": 1,
        "explanation": "مع never، نستخدم have never seen."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (just/arrive) at the party.",
        "options": ["just arrived", "have just arrived", "has just arrived", "arrived just"],
        "correct_option_id": 1,
        "explanation": "نستخدم have just arrived مع just."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (she/ever/talk) to you about it?",
        "options": ["Has she talked ever", "Have she ever talked", "Has she ever talked", "Did she ever talked"],
        "correct_option_id": 2,
        "explanation": "في السؤال مع ever، نستخدم Has she ever talked."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (visit) that place before.",
        "options": ["did visit", "have visit", "has visited", "have visited"],
        "correct_option_id": 2,
        "explanation": "لأن الفاعل (He) مفرد، نستخدم has visited."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (already/make) their decision.",
        "options": ["already made", "have already made", "has already made", "made already"],
        "correct_option_id": 1,
        "explanation": "نستخدم have already made مع already."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/see) her friends in a long time.",
        "options": ["hasn't saw", "haven't seen", "has not seen", "have not seen"],
        "correct_option_id": 2,
        "explanation": "مع in a long time في النفي، نستخدم hasn't seen."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (you/ever/meet) a celebrity?",
        "options": ["Has you ever met", "Have you meet ever", "Have you ever met", "Did you ever met"],
        "correct_option_id": 2,
        "explanation": "في السؤال مع ever، نستخدم Have you ever met."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (never/eat) sushi before.",
        "options": ["haven't eat", "has never eaten", "never ate", "have never eaten"],
        "correct_option_id": 3,
        "explanation": "مع never، نستخدم have never eaten."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (already/leave) for their trip.",
        "options": ["are already left", "has already left", "already left", "have already left"],
        "correct_option_id": 3,
        "explanation": "نستخدم have already left مع already."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/decide) on a date yet.",
        "options": ["didn't decide", "haven't decide", "hasn't decided", "haven't decided"],
        "correct_option_id": 3,
        "explanation": "مع yet في النفي، نستخدم haven't decided."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (travel) to many countries.",
        "options": ["is traveling", "traveled", "have traveled", "has traveled"],
        "correct_option_id": 3,
        "explanation": "(He) مفرد، لذا نستخدم has + past participle (traveled/travelled)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/eat) dinner yet.",
        "options": ["don't eat", "didn't eat", "haven't eaten", "hasn't eaten"],
        "correct_option_id": 2,
        "explanation": "في النفي مع (They)، نستخدم haven't + eaten."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (you/ever/see) the Eiffel Tower?",
        "options": ["Do you ever see", "Have you seen ever", "Did you ever see", "Have you ever seen"],
        "correct_option_id": 3,
        "explanation": "في السؤال مع ever، نستخدم Have + subject + ever + past participle."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (write) a book about her travels.",
        "options": ["wrote", "written", "has written", "have written"],
        "correct_option_id": 2,
        "explanation": "لأن الفاعل (She) مفرد، نستخدم has written."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/speak) to him today.",
        "options": ["hasn't spoken", "didn't speak", "haven't spoken", "haven't spoke"],
        "correct_option_id": 2,
        "explanation": "مع (I) في النفي، نستخدم haven't spoken."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this city for ten years.",
        "options": ["lived", "are living", "have lived", "has lived"],
        "correct_option_id": 2,
        "explanation": "مع (We) نستخدم have lived في المضارع التام."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/visit) her family this year.",
        "options": ["doesn't visit", "didn't visit", "haven't visited", "hasn't visited"],
        "correct_option_id": 3,
        "explanation": "مع (She) في النفي، نستخدم hasn't visited."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (they/ever/try) Thai food?",
        "options": ["Do they ever try", "Have they tried ever", "Did they ever try", "Have they ever tried"],
        "correct_option_id": 3,
        "explanation": "في السؤال مع ever و(They)، نستخدم Have they ever tried?"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (read) that book twice.",
        "options": ["read", "have read", "readed", "has read"],
        "correct_option_id": 3,
        "explanation": "لأن الفاعل (He) مفرد، نستخدم has read."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/finish) my work yet.",
        "options": ["don't finish", "hasn't finished", "didn't finish", "haven't finished"],
        "correct_option_id": 3,
        "explanation": "مع (I) في النفي، نستخدم haven't finished."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (visit) us several times.",
        "options": ["visited", "are visiting", "have visited", "has visited"],
        "correct_option_id": 2,
        "explanation": "مع (They) نستخدم have visited في المضارع التام."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/see) the movie yet.",
        "options": ["doesn't see", "didn't see", "haven't seen", "hasn't seen"],
        "correct_option_id": 3,
        "explanation": "مع (She) في النفي، نستخدم hasn't seen."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n____ (you/ever/be) to London?",
        "options": ["Do you ever be", "Have you been ever", "Did you ever be", "Have you ever been"],
        "correct_option_id": 3,
        "explanation": "في السؤال مع ever و(you)، نستخدم Have you ever been?"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (play) the piano since he was a child.",
        "options": ["played", "is playing", "have played", "has played"],
        "correct_option_id": 3,
        "explanation": "(He) مفرد، لذا نستخدم has + past participle (played)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (know) her for a long time.",
        "options": ["knew", "am knowing", "has known", "have known"],
        "correct_option_id": 3,
        "explanation": "مع (I) نستخدم have known في المضارع التام."
    }
],
            "المضارع التام المستمر": [
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (study) for three hours.",
        "options": ["study", "have been studying", "am studying", "studied"],
        "correct_option_id": 1,
        "explanation": "يستخدم المضارع التام المستمر للتعبير عن فعل مستمر لفترة زمنية محددة.  لأن الفعل مستمر منذ ثلاث ساعات، نستخدم have been studying."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (wait) for you for an hour.",
        "options": ["has waited", "is waiting", "waited", "has been waiting"],
        "correct_option_id": 3,
        "explanation": "لأن الفعل مستمر منذ ساعة، نستخدم has been waiting."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (play) soccer since morning.",
        "options": ["have played", "played", "have been playing", "are playing"],
        "correct_option_id": 2,
        "explanation": "since morning يدل على استمرار الفعل منذ الصباح، نستخدم have been playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (work) here for two years.",
        "options": ["has worked", "worked", "has been working", "is working"],
        "correct_option_id": 2,
        "explanation": "for two years يدل على استمرار العمل لفترتين، نستخدم has been working."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/eat) yet.",
        "options": ["have not eaten", "haven't been eating", "aren't eating", "haven't eaten"],
        "correct_option_id": 1,
        "explanation": "في النفي، نستخدم haven't been eating لوصف فعل مستمر حتى الآن."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/sleep) well lately.",
        "options": ["hasn't slept", "hasn't been sleeping", "is not sleeping", "didn't sleep"],
        "correct_option_id": 1,
        "explanation": "lately يدل على استمرار الحالة السيئة للنوم، نستخدم hasn't been sleeping."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow long ____ (you/learn) English?",
        "options": ["are you learning", "did you learn", "have you learned", "have you been learning"],
        "correct_option_id": 3,
        "explanation": "How long يستخدم مع المضارع التام المستمر: have you been learning."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (study) for their exams this week.",
        "options": ["have studied", "studied", "have been studying", "are studying"],
        "correct_option_id": 2,
        "explanation": "this week يدل على استمرار الدراسة طوال هذا الأسبوع، نستخدم have been studying."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (play) the guitar since he was a child.",
        "options": ["has played", "is playing", "played", "has been playing"],
        "correct_option_id": 3,
        "explanation": "since he was a child يدل على استمرار العزف منذ الطفولة، نستخدم has been playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/see) each other for a long time.",
        "options": ["haven't seen", "have not been seeing", "have not seen", "didn't see"],
        "correct_option_id": 1,
        "explanation": "for a long time يستخدم مع المضارع التام المستمر، في النفي نستخدم haven't been seeing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (exercise) regularly since last year.",
        "options": ["have exercised", "exercised", "are exercising", "have been exercising"],
        "correct_option_id": 3,
        "explanation": "since last year يدل على استمرار التمرين منذ العام الماضي، نستخدم have been exercising."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (work) on this project since last month.",
        "options": ["is working", "worked", "has worked", "has been working"],
        "correct_option_id": 3,
        "explanation": "since last month يدل على استمرار العمل منذ الشهر الماضي، نستخدم has been working."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow long ____ (they/wait) for the bus?",
        "options": ["did they wait", "have they waited", "are they waiting", "have they been waiting"],
        "correct_option_id": 3,
        "explanation": "How long يستخدم مع المضارع التام المستمر: have they been waiting."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/understand) this concept for weeks.",
        "options": ["have not understood", "didn't understand", "haven't been understanding", "haven't understood"],
        "correct_option_id": 2,
        "explanation": "for weeks يدل على استمرار عدم الفهم لأسابيع، نستخدم haven't been understanding."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (read) that book for a month.",
        "options": ["read", "is reading", "has read", "has been reading"],
        "correct_option_id": 3,
        "explanation": "for a month يدل على استمرار القراءة لمدة شهر، نستخدم has been reading."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (clean) the house all day.",
        "options": ["have cleaned", "are cleaning", "cleaned", "have been cleaning"],
        "correct_option_id": 3,
        "explanation": "all day يدل على استمرار التنظيف طوال اليوم، نستخدم have been cleaning."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (discuss) this topic for hours.",
        "options": ["are discussing", "have discussed", "discussed", "have been discussing"],
        "correct_option_id": 3,
        "explanation": "for hours يدل على استمرار النقاش لساعات، نستخدم have been discussing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/finish) her homework yet.",
        "options": ["hasn't finished", "has finished not", "haven't finished", "isn't finishing"],
        "correct_option_id": 0,
        "explanation": "yet يستخدم مع المضارع التام، في النفي نستخدم hasn't finished."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (study) for his exams since last week.",
        "options": ["has studied", "is studying", "studied", "has been studying"],
        "correct_option_id": 3,
        "explanation": "since last week يدل على استمرار الدراسة منذ الأسبوع الماضي، نستخدم has been studying."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (travel) a lot this year.",
        "options": ["traveled", "have traveled", "are traveling", "have been traveling"],
        "correct_option_id": 3,
        "explanation": "this year يدل على استمرار السفر طوال هذا العام، نستخدم have been traveling."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (look) for my keys for an hour.",
        "options": ["am looking", "have looked", "have been looking", "looked"],
        "correct_option_id": 2,
        "explanation": "for an hour يدل على استمرار البحث لساعة، نستخدم have been looking."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (watch) that series since it came out.",
        "options": ["is watching", "has watched", "watched", "has been watching"],
        "correct_option_id": 3,
        "explanation": "since it came out يدل على استمرار المشاهدة منذ صدور المسلسل، نستخدم has been watching."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/play) since last summer.",
        "options": ["hasn't played", "didn't play", "haven't played", "have not been playing"],
        "correct_option_id": 2,
        "explanation": "since last summer يستخدم مع المضارع التام المستمر، في النفي نستخدم haven't been playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (wait) for the doctor for over an hour.",
        "options": ["waited", "is waiting", "has waited", "has been waiting"],
        "correct_option_id": 3,
        "explanation": "for over an hour يدل على استمرار الانتظار لأكثر من ساعة، نستخدم has been waiting."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/speak) to her since the party.",
        "options": ["hasn't spoken", "didn't speak", "haven't spoken", "have not been speaking"],
        "correct_option_id": 3,
        "explanation": "since the party يستخدم مع المضارع التام المستمر، في النفي نستخدم haven't been speaking."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (run) every morning for health.",
        "options": ["am running", "have run", "run", "have been running"],
        "correct_option_id": 3,
        "explanation": "every morning يدل على استمرار الجري كل صباح، نستخدم have been running."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (work) on their presentation for weeks.",
        "options": ["have worked", "are working", "worked", "have been working"],
        "correct_option_id": 3,
        "explanation": "for weeks يدل على استمرار العمل لأسابيع، نستخدم have been working."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/finish) her report yet.",
        "options": ["has finished not", "haven't finished", "isn't finishing", "hasn't finished"],
        "correct_option_id": 3,
        "explanation": "yet يستخدم مع المضارع التام، في النفي نستخدم hasn't finished."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (learn) guitar for two years.",
        "options": ["learned", "is learning", "has learned", "has been learning"],
        "correct_option_id": 3,
        "explanation": "for two years يدل على استمرار التعلم لمدة سنتين، نستخدم has been learning."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (exercise) every day this month.",
        "options": ["exercised", "have exercised", "are exercising", "have been exercising"],
        "correct_option_id": 3,
        "explanation": "every day this month يدل على استمرار التمرين كل يوم هذا الشهر، نستخدم have been exercising."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/clean) their room for weeks.",
        "options": ["didn't clean", "hasn't cleaned", "haven't cleaned", "have not been cleaning"],
        "correct_option_id": 3,
        "explanation": "for weeks يستخدم مع المضارع التام المستمر، في النفي نستخدم haven't been cleaning."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (study) English for a long time.",
        "options": ["studied", "is studying", "has studied", "has been studying"],
        "correct_option_id": 3,
        "explanation": "for a long time يستخدم مع المضارع التام المستمر: has been studying."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (wait) for his friend for hours.",
        "options": ["has been waiting", "is waiting", "has waited", "waited"],
        "correct_option_id": 0,
        "explanation": "for hours يدل على استمرار الانتظار لساعات، نستخدم has been waiting."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/see) that movie yet.",
        "options": ["haven't seen", "didn't see", "hasn't seen", "haven't been seeing"],
        "correct_option_id": 3,
        "explanation": "yet يستخدم مع المضارع التام المستمر، في النفي نستخدم haven't been seeing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (read) this book since last week.",
        "options": ["have been reading", "am reading", "read", "have read"],
        "correct_option_id": 0,
        "explanation": "since last week يدل على استمرار القراءة منذ الأسبوع الماضي، نستخدم have been reading."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (live) in this city for five years.",
        "options": ["has lived", "has been living", "lived", "is living"],
        "correct_option_id": 1,
        "explanation": "for five years يدل على استمرار العيش لخمس سنوات، نستخدم has been living."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/play) video games lately.",
        "options": ["haven't been playing", "didn't play", "haven't played", "aren't playing"],
        "correct_option_id": 0,
        "explanation": "lately يدل على استمرار عدم اللعب مؤخرًا، نستخدم haven't been playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (work) overtime all week.",
        "options": ["has been working", "has worked", "worked", "is working"],
        "correct_option_id": 0,
        "explanation": "all week يدل على استمرار العمل الإضافي طوال الأسبوع، نستخدم has been working."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (travel) around the world for a year.",
        "options": ["have been traveling", "are traveling", "traveled", "have traveled"],
        "correct_option_id": 0,
        "explanation": "for a year يدل على استمرار السفر لمدة عام، نستخدم have been traveling."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/study) hard recently.",
        "options": ["haven't been studying", "didn't study", "haven't studied", "am not studying"],
        "correct_option_id": 0,
        "explanation": "recently يدل على استمرار عدم الجد في الدراسة مؤخرًا، نستخدم haven't been studying."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (wait) at the airport since morning.",
        "options": ["is waiting", "has been waiting", "waited", "has waited"],
        "correct_option_id": 1,
        "explanation": "since morning يدل على استمرار الانتظار منذ الصباح، نستخدم has been waiting."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (learn) a new language for six months.",
        "options": ["have been learning", "have learned", "learned", "are learning"],
        "correct_option_id": 0,
        "explanation": "for six months يدل على استمرار التعلم لمدة ستة أشهر، نستخدم have been learning."
    }
]
        },
        "زمن الماضي": {
            "الماضي البسيط": [
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (visit) my grandparents last week.",
        "options": ["visit", "have visited", "was visiting", "visited"],
        "correct_option_id": 3,
        "explanation": "يستخدم الماضي البسيط للتعبير عن حدث انتهى في الماضي.  لأن الزيارة كانت الأسبوع الماضي، نستخدم visited."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (play) tennis yesterday.",
        "options": ["plays", "has played", "played", "was playing"],
        "correct_option_id": 2,
        "explanation": "الحدث (لعب التنس) حدث وانتهى بالأمس، لذا نستخدم الماضي البسيط played."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (go) to the beach last summer.",
        "options": ["have gone", "go", "went", "going"],
        "correct_option_id": 2,
        "explanation": "الحدث (الذهاب إلى الشاطئ) حدث وانتهى في الصيف الماضي، لذا نستخدم went."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/finish) his homework.",
        "options": ["doesn't finish", "hasn't finished", "not finished", "didn't finish"],
        "correct_option_id": 3,
        "explanation": "في جملة الماضي البسيط المنفية، نستخدم didn't + المصدر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (see) that movie last night.",
        "options": ["see", "have seen", "was seeing", "saw"],
        "correct_option_id": 3,
        "explanation": "لأن مشاهدة الفيلم حدث وانتهى الليلة الماضية، نستخدم saw."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/like) the food at the restaurant.",
        "options": ["doesn't like", "hasn't liked", "not liked", "didn't like"],
        "correct_option_id": 3,
        "explanation": "للتعبير عن عدم الإعجاب في الماضي، نستخدم didn't like."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow long ____ (you/live) in this city?",
        "options": ["do you live", "are you living", "have you lived", "did you live"],
        "correct_option_id": 3,
        "explanation": "How long في سياق الماضي البسيط يستخدم مع did you live."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (travel) to Spain last year.",
        "options": ["travel", "have traveled", "was traveling", "traveled"],
        "correct_option_id": 3,
        "explanation": "السفر حدث وانتهى العام الماضي، لذا نستخدم traveled."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (eat) breakfast at 8 AM.",
        "options": ["eats", "was eating", "has eaten", "ate"],
        "correct_option_id": 3,
        "explanation": "أكل الإفطار حدث وانتهى في الساعة الثامنة صباحًا، نستخدم ate."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/go) to the concert last night.",
        "options": ["don't go", "have not gone", "not gone", "didn't go"],
        "correct_option_id": 3,
        "explanation": "في جملة الماضي البسيط المنفية، نستخدم didn't go."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (see) her at the party.",
        "options": ["was seeing", "see", "seen", "saw"],
        "correct_option_id": 3,
        "explanation": "رؤية الشخص في الحفل حدث وانتهى، لذا نستخدم saw."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (work) at the cafe for two years.",
        "options": ["is working", "has worked", "was working", "worked"],
        "correct_option_id": 3,
        "explanation": "العمل في المقهى حدث وانتهى، لذا نستخدم worked."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow many books ____ (you/read) last month?",
        "options": ["read", "do you read", "have you read", "did you read"],
        "correct_option_id": 3,
        "explanation": "How many books مع الماضي البسيط نستخدم did you read."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/see) him yesterday.",
        "options": ["not saw", "haven't seen", "don't see", "didn't see"],
        "correct_option_id": 3,
        "explanation": "في جملة الماضي البسيط المنفية، نستخدم didn't see."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (visit) the museum last week.",
        "options": ["have visited", "visit", "was visiting", "visited"],
        "correct_option_id": 3,
        "explanation": "الزيارة حدث وانتهى الأسبوع الماضي، لذا نستخدم visited."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (play) soccer in college.",
        "options": ["was playing", "plays", "has played", "played"],
        "correct_option_id": 3,
        "explanation": "لعب كرة القدم حدث وانتهى في الكلية، لذا نستخدم played."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/attend) the meeting.",
        "options": ["don't attend", "have not attended", "not attended", "didn't attend"],
        "correct_option_id": 3,
        "explanation": "في جملة الماضي البسيط المنفية، نستخدم didn't attend."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (dance) beautifully at the party.",
        "options": ["dances", "was dancing", "has danced", "danced"],
        "correct_option_id": 3,
        "explanation": "الرقص في الحفل حدث وانتهى، لذا نستخدم danced."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (finish) my project on time.",
        "options": ["was finishing", "have finished", "finish", "finished"],
        "correct_option_id": 3,
        "explanation": "إنهاء المشروع حدث وانتهى في الوقت المحدد، لذا نستخدم finished."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/come) to the event.",
        "options": ["doesn't come", "haven't come", "not come", "didn't come"],
        "correct_option_id": 3,
        "explanation": "في جملة الماضي البسيط المنفية، نستخدم didn't come."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (break) my leg last year.",
        "options": ["break", "broken", "was breaking", "broke"],
        "correct_option_id": 3,
        "explanation": "كسر الساق حدث وانتهى العام الماضي، لذا نستخدم broke."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (find) her keys last night.",
        "options": ["find", "has found", "was finding", "found"],
        "correct_option_id": 3,
        "explanation": "إيجاد المفاتيح حدث وانتهى الليلة الماضية، لذا نستخدم found."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/finish) the work on time.",
        "options": ["not finished", "haven't finished", "don't finish", "didn't finish"],
        "correct_option_id": 3,
        "explanation": "في جملة الماضي البسيط المنفية، نستخدم didn't finish."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (go) to the gym every day last year.",
        "options": ["go", "have gone", "was going", "went"],
        "correct_option_id": 3,
        "explanation": "الذهاب إلى الصالة الرياضية كان حدثًا متكررًا في الماضي، لذا نستخدم went."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (take) a trip to Italy last summer.",
        "options": ["take", "have taken", "was taking", "took"],
        "correct_option_id": 3,
        "explanation": "الرحلة إلى إيطاليا حدث وانتهى في الصيف الماضي، لذا نستخدم took."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (write) a letter to her friend.",
        "options": ["writes", "has written", "was writing", "wrote"],
        "correct_option_id": 3,
        "explanation": "كتابة الرسالة حدث وانتهى، لذا نستخدم wrote."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/know) about the changes.",
        "options": ["not knew", "haven't known", "don't know", "didn't know"],
        "correct_option_id": 3,
        "explanation": "في جملة الماضي البسيط المنفية، نستخدم didn't know."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (start) their own business last year.",
        "options": ["start", "were starting", "have started", "started"],
        "correct_option_id": 3,
        "explanation": "بدء العمل حدث وانتهى العام الماضي، لذا نستخدم started."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (see) a doctor last week.",
        "options": ["see", "was seeing", "has seen", "saw"],
        "correct_option_id": 3,
        "explanation": "زيارة الطبيب حدث وانتهى الأسبوع الماضي، لذا نستخدم saw."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (celebrate) our anniversary last month.",
        "options": ["celebrate", "were celebrating", "have celebrated", "celebrated"],
        "correct_option_id": 3,
        "explanation": "الاحتفال حدث وانتهى الشهر الماضي، لذا نستخدم celebrated."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (call) me yesterday.",
        "options": ["calls", "was calling", "has called", "called"],
        "correct_option_id": 3,
        "explanation": "الاتصال حدث وانتهى بالأمس، لذا نستخدم called."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (forget) my password.",
        "options": ["forget", "was forgetting", "has forgotten", "forgot"],
        "correct_option_id": 3,
        "explanation": "نسيان كلمة المرور حدث وانتهى، لذا نستخدم forgot."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (go) to the cinema last night.",
        "options": ["went", "go", "have gone", "are going"],
        "correct_option_id": 0,
        "explanation": "الذهاب إلى السينما حدث وانتهى الليلة الماضية، نستخدم went."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (buy) a new dress last week.",
        "options": ["buy", "has bought", "buys", "bought"],
        "correct_option_id": 3,
        "explanation": "شراء الفستان حدث وانتهى الأسبوع الماضي، نستخدم bought."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/see) our friends last weekend.",
        "options": ["don't see", "didn't see", "haven't seen", "weren't seeing"],
        "correct_option_id": 1,
        "explanation": "في جملة الماضي البسيط المنفية، نستخدم didn't see."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (study) for the exam yesterday.",
        "options": ["studies", "was studying", "studied", "has studied"],
        "correct_option_id": 2,
        "explanation": "الدراسة حدث وانتهى بالأمس، نستخدم studied."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (cook) dinner last night.",
        "options": ["cook", "cooked", "have cooked", "were cooking"],
        "correct_option_id": 1,
        "explanation": "طبخ العشاء حدث وانتهى الليلة الماضية، نستخدم cooked."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/play) football yesterday.",
        "options": ["don't play", "didn't play", "wasn't playing", "haven't played"],
        "correct_option_id": 1,
        "explanation": "في جملة الماضي البسيط المنفية، نستخدم didn't play."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (drink) a glass of water.",
        "options": ["drinks", "was drinking", "drank", "has drunk"],
        "correct_option_id": 2,
        "explanation": "شرب الماء حدث وانتهى، نستخدم drank."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (walk) to school this morning.",
        "options": ["walked", "walk", "have walked", "were walking"],
        "correct_option_id": 0,
        "explanation": "المشي إلى المدرسة حدث وانتهى هذا الصباح، نستخدم walked."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/go) to the party last Saturday.",
        "options": ["doesn't go", "didn't go", "wasn't going", "haven't gone"],
        "correct_option_id": 1,
        "explanation": "في جملة الماضي البسيط المنفية، نستخدم didn't go."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (arrive) late to the meeting.",
        "options": ["arrived", "arrive", "have arrived", "were arriving"],
        "correct_option_id": 0,
        "explanation": "الوصول حدث وانتهى، نستخدم arrived."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (sing) a beautiful song.",
        "options": ["sings", "was singing", "has sung", "sang"],
        "correct_option_id": 3,
        "explanation": "الغناء حدث وانتهى، نستخدم sang."
    }
],
            "الماضي المستمر": [
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (watch) TV when she called.",
        "options": ["watch", "was watched", "watched", "was watching"],
        "correct_option_id": 3,
        "explanation": "نستخدم Past Continuous (was/were + ing) لوصف فعل مستمر في الماضي عندما حدث فعل آخر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/play) football when it started to rain.",
        "options": ["wasn't playing", "not played", "weren't playing", "didn't play"],
        "correct_option_id": 2,
        "explanation": "Past Continuous منفي يستخدم مع weren't + ing  لوصف فعل مستمر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (read) a book while waiting.",
        "options": ["read", "has read", "was reading", "reading"],
        "correct_option_id": 2,
        "explanation": "while يدل على فعل مستمر في الماضي، نستخدم was reading."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/finish) his work at that time.",
        "options": ["not finished", "wasn't finishing", "wasn't finish", "didn't finish"],
        "correct_option_id": 1,
        "explanation": "Past Continuous منفي يستخدم مع wasn't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (talk) about the movie when the lights went out.",
        "options": ["talked", "talk", "was talking", "were talking"],
        "correct_option_id": 3,
        "explanation": "Past Continuous يستخدم لوصف فعل مستمر في الماضي، نستخدم were talking."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (cook) dinner when the phone rang.",
        "options": ["cooking", "has cooked", "cooked", "was cooking"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was cooking."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow long ____ (they/study) in the library?",
        "options": ["did they study", "are they studying", "have they studied", "were they studying"],
        "correct_option_id": 3,
        "explanation": "How long يستخدم مع Past Continuous: were they studying."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (work) on her project all night.",
        "options": ["worked", "was work", "has worked", "was working"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was working."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/sleep) during the lecture.",
        "options": ["didn't sleep", "not slept", "hasn't slept", "wasn't sleeping"],
        "correct_option_id": 3,
        "explanation": "Past Continuous منفي يستخدم مع wasn't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (play) games when the power went out.",
        "options": ["played", "play", "have played", "were playing"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/listen) to music when she arrived.",
        "options": ["didn't listen", "not listened", "haven't listened", "wasn't listening"],
        "correct_option_id": 3,
        "explanation": "Past Continuous منفي يستخدم مع wasn't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (study) while he was watching TV.",
        "options": ["studied", "has studied", "studies", "was studying"],
        "correct_option_id": 3,
        "explanation": "while يدل على فعل مستمر في الماضي، نستخدم was studying."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow many hours ____ (you/sleep) last night?",
        "options": ["did you sleep", "have you slept", "are you sleeping", "were you sleeping"],
        "correct_option_id": 3,
        "explanation": "How many hours يستخدم مع Past Continuous: were you sleeping."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (have) dinner at 7 PM.",
        "options": ["have", "are having", "had", "were having"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were having."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (wait) for the bus when it started to rain.",
        "options": ["waited", "was waiting", "have waited", "were waiting"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were waiting."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (listen) to music while studying.",
        "options": ["listened", "has listened", "listens", "was listening"],
        "correct_option_id": 3,
        "explanation": "while يدل على فعل مستمر في الماضي، نستخدم was listening."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/see) you at the party.",
        "options": ["didn't see", "not saw", "haven't seen", "wasn't seeing"],
        "correct_option_id": 3,
        "explanation": "Past Continuous منفي يستخدم مع wasn't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (play) outside when it got dark.",
        "options": ["played", "play", "have played", "were playing"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (dance) at the event.",
        "options": ["danced", "dances", "has danced", "was dancing"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was dancing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (discuss) the project when the manager interrupted.",
        "options": ["discussed", "discuss", "have discussed", "were discussing"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were discussing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/eat) anything when he arrived.",
        "options": ["not eaten", "haven't eaten", "wasn't eating", "didn't eat"],
        "correct_option_id": 2,
        "explanation": "Past Continuous منفي يستخدم مع wasn't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (wait) for her friend.",
        "options": ["wait", "has waited", "waited", "was waiting"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was waiting."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (play) video games when the power went out.",
        "options": ["have played", "play", "played", "were playing"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (study) for my exam at that time.",
        "options": ["study", "have studied", "studied", "was studying"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was studying."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (call) me while I was sleeping.",
        "options": ["calls", "has called", "called", "was calling"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was calling."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (travel) when the car broke down.",
        "options": ["travel", "have traveled", "traveled", "were traveling"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were traveling."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/come) to the meeting yesterday.",
        "options": ["not came", "hasn't come", "wasn't coming", "didn't come"],
        "correct_option_id": 2,
        "explanation": "Past Continuous منفي يستخدم مع wasn't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (talk) about the event when it happened.",
        "options": ["talk", "have talked", "talked", "were talking"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were talking."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/remember) his name at that moment.",
        "options": ["not remembered", "haven't remembered", "wasn't remembering", "didn't remember"],
        "correct_option_id": 2,
        "explanation": "Past Continuous منفي يستخدم مع wasn't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (play) the piano when I entered.",
        "options": ["plays", "has played", "played", "was playing"],
        "correct_option_id": 3,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (read) a book when the phone rang.",
        "options": ["was reading", "read", "has read", "reading"],
        "correct_option_id": 0,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was reading."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/work) when I visited.",
        "options": ["weren't working", "didn't work", "not working", "wasn't working"],
        "correct_option_id": 0,
        "explanation": "Past Continuous منفي يستخدم مع weren't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (listen) to music while driving.",
        "options": ["was listening", "listened", "have listened", "listening"],
        "correct_option_id": 0,
        "explanation": "while يدل على فعل مستمر في الماضي، نستخدم was listening."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (cook) dinner when the fire alarm went off.",
        "options": ["cooked", "was cooking", "has cooked", "cooking"],
        "correct_option_id": 1,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was cooking."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/sleep) when the earthquake hit.",
        "options": ["weren't sleeping", "didn't sleep", "not sleeping", "wasn't sleeping"],
        "correct_option_id": 0,
        "explanation": "Past Continuous منفي يستخدم مع weren't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (play) the guitar when his friend called.",
        "options": ["played", "has played", "was playing", "playing"],
        "correct_option_id": 2,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was playing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (walk) in the park when it started to rain.",
        "options": ["were walking", "walked", "have walked", "walking"],
        "correct_option_id": 0,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were walking."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/watch) TV at that time.",
        "options": ["wasn't watching", "didn't watch", "not watched", "haven't watched"],
        "correct_option_id": 0,
        "explanation": "Past Continuous منفي يستخدم مع wasn't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (dance) when the music started.",
        "options": ["danced", "has danced", "was dancing", "dancing"],
        "correct_option_id": 2,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم was dancing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (study) for the exam when the power went out.",
        "options": ["were studying", "studied", "have studied", "studying"],
        "correct_option_id": 0,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were studying."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/drive) when the accident happened.",
        "options": ["wasn't driving", "didn't drive", "not driving", "hasn't driven"],
        "correct_option_id": 0,
        "explanation": "Past Continuous منفي يستخدم مع wasn't + ing."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (eat) dinner when the phone rang.",
        "options": ["ate", "were eating", "have eaten", "eating"],
        "correct_option_id": 1,
        "explanation": "Past Continuous لوصف فعل مستمر في الماضي، نستخدم were eating."
    }
],
            "الماضي التام": [
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (finish) my homework before dinner.",
        "options": ["finished", "have finished", "was finishing", "had finished"],
        "correct_option_id": 3,
        "explanation": "استخدمنا هنا Past Perfect (had finished) لأنّ فعل إتمام الواجب المنزلي (finish) حدث *قبل* حدث آخر في الماضي وهو وقت العشاء.  Past Perfect يُستخدم لوصف حدث سابق لحدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/see) him before the party.",
        "options": ["didn't see", "hasn't seen", "not saw", "hadn't seen"],
        "correct_option_id": 3,
        "explanation": "هنا،  'before the party' يشير إلى أن عدم رؤيتها له (not see) حدث *قبل* وقت محدد في الماضي (الحفلة).  لذا،  نستخدم Past Perfect منفي (hadn't seen) للدلالة على هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (leave) before we arrived.",
        "options": ["left", "have left", "was leaving", "had left"],
        "correct_option_id": 3,
        "explanation": "مغادرتهم (leave) حدثت *قبل* وصولنا (arrived).  للتعبير عن هذا التسلسل، نحتاج إلى Past Perfect (had left)؛ لأنّ كلا الفعلين حدثا في الماضي، لكن أحدهما سبق الآخر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/finish) his project by the deadline.",
        "options": ["didn't finish", "not finished", "hasn't finished", "hadn't finished"],
        "correct_option_id": 3,
        "explanation": "عدم إكمال المشروع (not finish) حدث *قبل* الموعد النهائي (deadline)، وهو نقطة زمنية محددة في الماضي.  لذا، نستخدم Past Perfect منفي (hadn't finished) للإشارة إلى هذا الحدث السابق."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (arrive) at the airport before the flight.",
        "options": ["arrived", "have arrived", "was arriving", "had arrived"],
        "correct_option_id": 3,
        "explanation": "الوصول إلى المطار (arrive) حدث *قبل* موعد الرحلة (flight).  Past Perfect (had arrived) يُظهر هذا الترتيب الزمني للأحداث في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/read) the book before the exam.",
        "options": ["didn't read", "not read", "haven't read", "hadn't read"],
        "correct_option_id": 3,
        "explanation": "عدم قراءة الكتاب (not read) حدث *قبل* الامتحان (exam).  للتأكيد على هذا التسلسل الزمني في الماضي، نستخدم Past Perfect منفي (hadn't read)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow long ____ (you/live) in London before moving?",
        "options": ["did you live", "have you lived", "are you living", "had you lived"],
        "correct_option_id": 3,
        "explanation": "السؤال هنا عن مدة إقامة سابقة (before moving) في لندن.  لأنّها مدة زمنية في الماضي،  نستخدم Past Perfect (had you lived)  لسؤال عن مدة زمنية مضت قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (graduate) before she got her job.",
        "options": ["graduated", "has graduated", "was graduating", "had graduated"],
        "correct_option_id": 3,
        "explanation": "التخرج (graduate) حدث *قبل* الحصول على وظيفة (got her job).  Past Perfect (had graduated) يُبرز أنّ التخرج سبق الحصول على الوظيفة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/meet) her before the event.",
        "options": ["didn't meet", "not met", "hasn't met", "hadn't met"],
        "correct_option_id": 3,
        "explanation": "عدم لقائه بها (not meet) حدث *قبل* الحدث (event).  للتسلسل الزمني الصحيح، نستخدم Past Perfect منفي (hadn't met)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (take) the bus before the train.",
        "options": ["took", "have taken", "was taking", "had taken"],
        "correct_option_id": 3,
        "explanation": "ركوب الحافلة (take) حدث *قبل* ركوب القطار.  Past Perfect (had taken) يُوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/visit) that museum before.",
        "options": ["didn't visit", "not visited", "haven't visited", "hadn't visited"],
        "correct_option_id": 3,
        "explanation": "عدم زيارة المتحف (not visit) حدث في الماضي *قبل* نقطة زمنية أخرى في الماضي (الآن).  Past Perfect منفي (hadn't visited) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/complete) her assignment before the deadline.",
        "options": ["didn't complete", "not completed", "hasn't completed", "hadn't completed"],
        "correct_option_id": 3,
        "explanation": "عدم إكمال الواجب (not complete) حدث *قبل* الموعد النهائي (deadline).  Past Perfect منفي (hadn't completed) يُوضح هذا الترتيب الزمني للأحداث في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow many times ____ (you/see) that movie before?",
        "options": ["did you see", "have you seen", "are you seeing", "had you seen"],
        "correct_option_id": 3,
        "explanation": "هنا، نسأل عن عدد مرات مشاهدة فيلم *قبل* وقت معين في الماضي.  لذلك نستخدم Past Perfect (had you seen)  لأنّ الفعل حدث مرارًا وتكرارًا في الماضي *قبل* حدث آخر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (arrive) at the hotel before the wedding.",
        "options": ["arrived", "have arrived", "was arriving", "had arrived"],
        "correct_option_id": 3,
        "explanation": "الوصول إلى الفندق (arrive) حدث *قبل* حفل الزفاف (wedding).  Past Perfect (had arrived) يُبرز هذا التسلسل الزمني للأحداث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (call) me before I got home.",
        "options": ["called", "calls", "has called", "had called"],
        "correct_option_id": 3,
        "explanation": "اتصاله (call) حدث *قبل* وصولي إلى المنزل (got home).  لذا، نستخدم Past Perfect (had called) للدلالة على هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/finish) the project before the presentation.",
        "options": ["didn't finish", "not finished", "hasn't finished", "hadn't finished"],
        "correct_option_id": 3,
        "explanation": "عدم الانتهاء من المشروع (not finish) حدث *قبل* العرض التقديمي (presentation).  لذا، نستخدم Past Perfect منفي (hadn't finished)  للتعبير عن هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (learn) English before moving to the UK.",
        "options": ["learned", "learn", "has learned", "had learned"],
        "correct_option_id": 3,
        "explanation": "تعلم اللغة الإنجليزية (learn) حدث *قبل* الانتقال إلى المملكة المتحدة (moving to the UK).  Past Perfect (had learned) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (forget) to bring my notes.",
        "options": ["had forgotten", "forgot", "have forgotten", "was forgetting"],
        "correct_option_id": 3,
        "explanation": "نسيان إحضار الملاحظات (forget) حدث *قبل* نقطة زمنية أخرى في الماضي (الآن). نستخدم Past Perfect (had forgotten)  للتعبير عن هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (see) that play before it ended.",
        "options": ["saw", "have seen", "were seeing", "had seen"],
        "correct_option_id": 3,
        "explanation": "مشاهدتهم للمسرحية (see) حدث *قبل* انتهائها (ended).  Past Perfect (had seen)  يُبين هذا الترتيب الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/eat) at that restaurant before.",
        "options": ["didn't eat", "not eaten", "hasn't eaten", "hadn't eaten"],
        "correct_option_id": 3,
        "explanation": "عدم تناول الطعام في هذا المطعم (not eat) حدث *قبل* نقطة زمنية أخرى في الماضي.  Past Perfect منفي (hadn't eaten) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (write) the report before the meeting.",
        "options": ["wrote", "write", "was writing", "had written"],
        "correct_option_id": 3,
        "explanation": "كتابة التقرير (write) حدث *قبل* الاجتماع (meeting).  Past Perfect (had written) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/see) the news before.",
        "options": ["didn't see", "not saw", "hasn't seen", "hadn't seen"],
        "correct_option_id": 3,
        "explanation": "عدم مشاهدة الأخبار (not see) حدث *قبل* نقطة زمنية أخرى في الماضي.  Past Perfect منفي (hadn't seen) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (finish) their work before the deadline.",
        "options": ["finished", "have finished", "was finishing", "had finished"],
        "correct_option_id": 3,
        "explanation": "إنهاء العمل (finish) حدث *قبل* الموعد النهائي (deadline).  Past Perfect (had finished) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (read) the book before the class started.",
        "options": ["read", "has read", "was reading", "had read"],
        "correct_option_id": 3,
        "explanation": "قراءة الكتاب (read) حدث *قبل* بداية الدرس (class started).  Past Perfect (had read) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (discuss) the project before the meeting.",
        "options": ["discussed", "have discussed", "was discussing", "had discussed"],
        "correct_option_id": 3,
        "explanation": "مناقشة المشروع (discuss) حدث *قبل* الاجتماع (meeting).  Past Perfect (had discussed) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (visit) Paris before his trip to Rome.",
        "options": ["visited", "visits", "has visited", "had visited"],
        "correct_option_id": 3,
        "explanation": "زيارة باريس (visit) حدث *قبل* رحلته إلى روما (trip to Rome).  Past Perfect (had visited) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/take) that course before.",
        "options": ["didn't take", "not taken", "hasn't taken", "hadn't taken"],
        "correct_option_id": 3,
        "explanation": "عدم أخذ هذه الدورة (not take) حدث *قبل* نقطة زمنية أخرى في الماضي.  Past Perfect منفي (hadn't taken) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (know) each other for years before they got married.",
        "options": ["knew", "have known", "were knowing", "had known"],
        "correct_option_id": 3,
        "explanation": "معرفتهم ببعضهم البعض (know) حدث *قبل* زواجهم (got married).  Past Perfect (had known) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/finish) her homework before dinner.",
        "options": ["didn't finish", "not finished", "hasn't finished", "hadn't finished"],
        "correct_option_id": 3,
        "explanation": "عدم إتمام الواجب المنزلي (not finish) حدث *قبل* وقت العشاء (dinner).  Past Perfect منفي (hadn't finished) يوضح هذا الترتيب الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (break) my leg before the race.",
        "options": ["broke", "break", "have broken", "had broken"],
        "correct_option_id": 3,
        "explanation": "كسر رجلي (break) حدث *قبل* السباق (race).  Past Perfect (had broken) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (eat) all the cake before the party started.",
        "options": ["had eaten", "ate", "have eaten", "were eating"],
        "correct_option_id": 0,
        "explanation": "أكل الكيك (eat) حدث *قبل* بداية الحفلة (party started).  Past Perfect (had eaten) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/see) that movie before.",
        "options": ["hasn't seen", "didn't see", "hadn't seen", "not seen"],
        "correct_option_id": 2,
        "explanation": "عدم مشاهدة الفيلم (not see) حدث *قبل* نقطة زمنية أخرى في الماضي.  Past Perfect منفي (hadn't seen) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (finish) our work before we went home.",
        "options": ["had finished", "finished", "have finished", "were finishing"],
        "correct_option_id": 0,
        "explanation": "إنهاء العمل (finish) حدث *قبل* الذهاب إلى المنزل (went home).  Past Perfect (had finished) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (study) English before he moved to London.",
        "options": ["studied", "has studied", "was studying", "had studied"],
        "correct_option_id": 3,
        "explanation": "دراسة اللغة الإنجليزية (study) حدث *قبل* الانتقال إلى لندن (moved to London).  Past Perfect (had studied) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/go) to the concert before.",
        "options": ["didn't go", "haven't gone", "hadn't gone", "not gone"],
        "correct_option_id": 2,
        "explanation": "عدم الذهاب إلى الحفل (not go) حدث *قبل* نقطة زمنية أخرى في الماضي.  Past Perfect منفي (hadn't gone) يوضح هذا التسلسل الزمني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (already/eat) dinner when he arrived.",
        "options": ["already ate", "had already eaten", "have already eaten", "was already eating"],
        "correct_option_id": 1,
        "explanation": "أكل العشاء (eat) حدث *قبل* وصوله (arrived).  Past Perfect (had already eaten) يوضح هذا التسلسل الزمني، مع already لتأكيد أن الفعل حدث قبل الوقت المحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (never/visit) that country before.",
        "options": ["never visited", "had never visited", "has never visited", "wasn't visiting"],
        "correct_option_id": 1,
        "explanation": "عدم زيارة هذا البلد (never visit) حدث *قبل* نقطة زمنية أخرى في الماضي.  Past Perfect منفي (had never visited) يوضح هذا التسلسل الزمني، مع never للدلالة على عدم حدوث الفعل من قبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in that house for five years before moving.",
        "options": ["had lived", "lived", "have lived", "were living"],
        "correct_option_id": 0,
        "explanation": "العيش في ذلك المنزل (live) حدث *قبل* الانتقال (moving).  Past Perfect (had lived) يوضح هذا التسلسل الزمني، مع for five years للدلالة على مدة زمنية سابقة."
    }
],
            "الماضي التام المستمر": [
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (study) for three hours before the exam started.",
        "options": ["have studied", "studied", "had been studying", "was studying"],
        "correct_option_id": 2,
        "explanation": "استخدمنا Past Perfect Continuous (had been studying) لأن الدراسة (study) استمرت لثلاث ساعات *قبل* حدث آخر في الماضي (بدء الامتحان).  Past Perfect Continuous يُستخدم لوصف فعل مستمرّ  كان مستمرًا *قبل* حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (wait) for an hour when he finally arrived.",
        "options": ["waited", "has been waiting", "was waiting", "had been waiting"],
        "correct_option_id": 3,
        "explanation": "الانتظار (wait) استمرّ لساعة *قبل* وصوله (arrived).  Past Perfect Continuous (had been waiting) يوضح استمرار الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (play) football for two hours before it started to rain.",
        "options": ["played", "have played", "were playing", "had been playing"],
        "correct_option_id": 3,
        "explanation": "لعب كرة القدم (play) استمرّ لساعتين *قبل* بدء المطر (started to rain).  Past Perfect Continuous (had been playing) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (work) on the project for weeks before the deadline.",
        "options": ["was working", "worked", "has been working", "had been working"],
        "correct_option_id": 3,
        "explanation": "العمل على المشروع (work) استمرّ لأسابيع *قبل* الموعد النهائي (deadline).  Past Perfect Continuous (had been working) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (travel) for hours when we finally reached our destination.",
        "options": ["were traveling", "travelled", "have traveled", "had been traveling"],
        "correct_option_id": 3,
        "explanation": "السفر (travel) استمرّ لساعات *قبل* الوصول إلى الوجهة (reached our destination).  Past Perfect Continuous (had been traveling) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/eat) anything before the meeting.",
        "options": ["didn't eat", "wasn't eating", "not eaten", "hadn't been eating"],
        "correct_option_id": 3,
        "explanation": "عدم تناول الطعام (not eat) استمرّ *قبل* الاجتماع (meeting).  Past Perfect Continuous منفي (hadn't been eating) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow long ____ (you/work) here before you decided to leave?",
        "options": ["were you working", "have you worked", "did you work", "had you been working"],
        "correct_option_id": 3,
        "explanation": "السؤال عن مدة العمل (work) *قبل* اتخاذ قرار المغادرة (decided to leave).  Past Perfect Continuous (had you been working) مناسب هنا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (practice) for a month before the concert.",
        "options": ["practiced", "has practiced", "was practicing", "had been practicing"],
        "correct_option_id": 3,
        "explanation": "التمرين (practice) استمرّ لمدة شهر *قبل* الحفل (concert).  Past Perfect Continuous (had been practicing) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/see) the movie before last night.",
        "options": ["didn't see", "wasn't seeing", "hasn't seen", "hadn't been seeing"],
        "correct_option_id": 3,
        "explanation": "عدم مشاهدة الفيلم (not see) استمرّ *قبل* الليلة الماضية (last night).  Past Perfect Continuous منفي (hadn't been seeing) يُناسب هذا السياق."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (live) in that house for ten years before moving.",
        "options": ["lived", "have lived", "were living", "had been living"],
        "correct_option_id": 3,
        "explanation": "العيش في ذلك المنزل (live) استمرّ لعشر سنوات *قبل* الانتقال (moving).  Past Perfect Continuous (had been living) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/visit) my grandparents for a long time before last week.",
        "options": ["didn't visit", "not visited", "haven't visited", "hadn't been visiting"],
        "correct_option_id": 3,
        "explanation": "عدم زيارة الأجداد (not visit) استمرّ لفترة طويلة *قبل* الأسبوع الماضي (last week).  Past Perfect Continuous منفي (hadn't been visiting) يُناسب هذا السياق."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/complete) her assignments before the final exam.",
        "options": ["didn't complete", "not completed", "hasn't completed", "hadn't been completing"],
        "correct_option_id": 3,
        "explanation": "عدم إكمال الواجبات (not complete) استمرّ *قبل* الامتحان النهائي (final exam).  Past Perfect Continuous منفي (hadn't been completing) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow many hours ____ (you/learn) before the test?",
        "options": ["did you learn", "have you learned", "were you learning", "had you been learning"],
        "correct_option_id": 3,
        "explanation": "السؤال عن مدة التعلم (learn) *قبل* الاختبار (test).  Past Perfect Continuous (had you been learning) يُناسب هذا السياق."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (watch) TV for hours when the power went out.",
        "options": ["watched", "have watched", "were watching", "had been watching"],
        "correct_option_id": 3,
        "explanation": "مشاهدة التلفزيون (watch) استمرّ لساعات *قبل* انقطاع الكهرباء (power went out).  Past Perfect Continuous (had been watching) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (run) for an hour before he stopped to rest.",
        "options": ["ran", "have run", "was running", "had been running"],
        "correct_option_id": 3,
        "explanation": "الركض (run) استمرّ لساعة *قبل* التوقف للراحة (stopped to rest).  Past Perfect Continuous (had been running) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/exercise) regularly before we joined the gym.",
        "options": ["didn't exercise", "not exercised", "hasn't exercised", "hadn't been exercising"],
        "correct_option_id": 3,
        "explanation": "عدم ممارسة الرياضة بانتظام (not exercise) استمرّ *قبل* الانضمام إلى الصالة الرياضية (joined the gym).  Past Perfect Continuous منفي (hadn't been exercising) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (teach) for five years before she took a break.",
        "options": ["taught", "has taught", "was teaching", "had been teaching"],
        "correct_option_id": 3,
        "explanation": "التدريس (teach) استمرّ لخمس سنوات *قبل* أخذ استراحة (took a break).  Past Perfect Continuous (had been teaching) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (study) for the exam all week.",
        "options": ["studied", "have studied", "was studying", "had been studying"],
        "correct_option_id": 3,
        "explanation": "الدراسة (study) استمرت طوال الأسبوع (all week) *قبل* نقطة زمنية أخرى في الماضي.  Past Perfect Continuous (had been studying) يوضح مدة الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (wait) for the bus when it started to rain.",
        "options": ["waited", "were waiting", "have waited", "had been waiting"],
        "correct_option_id": 3,
        "explanation": "الانتظار (wait) استمرّ *قبل* بدء المطر (started to rain).  Past Perfect Continuous (had been waiting) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/see) her for ages before we met last week.",
        "options": ["didn't see", "not seen", "hasn't seen", "hadn't been seeing"],
        "correct_option_id": 3,
        "explanation": "عدم رؤية (not see) استمرّ لفترة طويلة (for ages) *قبل* اللقاء الأسبوع الماضي (met last week). Past Perfect Continuous منفي (hadn't been seeing) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (work) on that project for months.",
        "options": ["worked", "was working", "has worked", "had been working"],
        "correct_option_id": 3,
        "explanation": "العمل على المشروع (work) استمرّ لشهور *قبل* نقطة زمنية أخرى في الماضي. Past Perfect Continuous (had been working) يوضح مدة الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/finish) her homework before dinner.",
        "options": ["hadn't been finishing", "didn't finish", "not finished", "hasn't finished"],
        "correct_option_id": 0,
        "explanation": "عدم إتمام الواجب المنزلي (not finish) استمرّ *قبل* وقت العشاء (dinner). Past Perfect Continuous منفي (hadn't been finishing) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in that city for years before moving.",
        "options": ["lived", "have lived", "were living", "had been living"],
        "correct_option_id": 3,
        "explanation": "العيش في تلك المدينة (live) استمرّ لسنوات *قبل* الانتقال (moving). Past Perfect Continuous (had been living) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow long ____ (you/study) before the test?",
        "options": ["did you study", "have you studied", "were you studying", "had you been studying"],
        "correct_option_id": 3,
        "explanation": "السؤال عن مدة الدراسة (study) *قبل* الاختبار (test). Past Perfect Continuous (had you been studying) يُناسب هذا السياق."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (play) the game for hours before it ended.",
        "options": ["played", "have played", "were playing", "had been playing"],
        "correct_option_id": 3,
        "explanation": "لعب اللعبة (play) استمرّ لساعات *قبل* انتهائها (ended). Past Perfect Continuous (had been playing) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/travel) before my trip last year.",
        "options": ["didn't travel", "not traveled", "hasn't traveled", "hadn't been traveling"],
        "correct_option_id": 3,
        "explanation": "عدم السفر (not travel) استمرّ *قبل* رحلتي العام الماضي (trip last year). Past Perfect Continuous منفي (hadn't been traveling) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (dance) for hours before she took a break.",
        "options": ["danced", "has danced", "was dancing", "had been dancing"],
        "correct_option_id": 3,
        "explanation": "الرقص (dance) استمرّ لساعات *قبل* أخذ استراحة (took a break). Past Perfect Continuous (had been dancing) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (exercise) regularly before joining the class.",
        "options": ["had been exercising", "didn't exercise", "not exercised", "hasn't exercised"],
        "correct_option_id": 0,
        "explanation": "ممارسة الرياضة بانتظام (exercise) استمرت *قبل* الانضمام إلى الصف (joining the class). Past Perfect Continuous (had been exercising) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/see) the news before.",
        "options": ["hadn't been seeing", "didn't see", "not saw", "hasn't seen"],
        "correct_option_id": 0,
        "explanation": "عدم مشاهدة الأخبار (not see) استمرّ *قبل* نقطة زمنية أخرى في الماضي. Past Perfect Continuous منفي (hadn't been seeing) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/meet) before last year.",
        "options": ["hadn't been meeting", "didn't meet", "not met", "hasn't met"],
        "correct_option_id": 0,
        "explanation": "عدم اللقاء (not meet) استمرّ *قبل* العام الماضي (last year). Past Perfect Continuous منفي (hadn't been meeting) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (wait) for his friend for hours.",
        "options": ["had been waiting", "was waiting", "has waited", "waited"],
        "correct_option_id": 0,
        "explanation": "الانتظار (wait) استمرّ لساعات *قبل* نقطة زمنية أخرى في الماضي. Past Perfect Continuous (had been waiting) يوضح مدة الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/study) before the exam.",
        "options": ["hadn't been studying", "didn't study", "not studied", "haven't studied"],
        "correct_option_id": 0,
        "explanation": "عدم الدراسة (not study) استمرّ *قبل* الامتحان (exam). Past Perfect Continuous منفي (hadn't been studying) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (read) this book for a week before finishing it.",
        "options": ["had been reading", "was reading", "read", "have read"],
        "correct_option_id": 0,
        "explanation": "قراءة الكتاب (read) استمرت لأسبوع *قبل* الانتهاء منه (finishing it). Past Perfect Continuous (had been reading) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (live) in that house for ten years before selling it.",
        "options": ["had been living", "lived", "has been living", "was living"],
        "correct_option_id": 0,
        "explanation": "العيش في ذلك المنزل (live) استمرّ لعشر سنوات *قبل* بيعه (selling it). Past Perfect Continuous (had been living) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/play) video games for a long time before last night.",
        "options": ["hadn't been playing", "didn't play", "not played", "haven't played"],
        "correct_option_id": 0,
        "explanation": "عدم لعب ألعاب الفيديو (not play) استمرّ لفترة طويلة *قبل* الليلة الماضية (last night). Past Perfect Continuous منفي (hadn't been playing) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (work) overtime for months before taking a vacation.",
        "options": ["had been working", "worked", "has been working", "was working"],
        "correct_option_id": 0,
        "explanation": "العمل الإضافي (work) استمرّ لشهور *قبل* أخذ إجازة (taking a vacation). Past Perfect Continuous (had been working) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (travel) around the world for two years before settling down.",
        "options": ["have been traveling", "were traveling", "had been traveling", "traveled"],
        "correct_option_id": 2,
        "explanation": "السفر حول العالم (travel) استمرّ لمدة عامين *قبل* الاستقرار (settling down). Past Perfect Continuous (had been traveling) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/exercise) for a long time before I started feeling unwell.",
        "options": ["hadn't been exercising", "didn't exercise", "not exercised", "haven't exercised"],
        "correct_option_id": 0,
        "explanation": "عدم ممارسة الرياضة (not exercise) استمرّ لفترة طويلة *قبل* الشعور بالتوعك (started feeling unwell). Past Perfect Continuous منفي (hadn't been exercising) يوضح هذا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (wait) for the bus for half an hour when it finally arrived.",
        "options": ["had been waiting", "was waiting", "waited", "has been waiting"],
        "correct_option_id": 0,
        "explanation": "الانتظار (wait) استمرّ لنصف ساعة *قبل* وصول الحافلة (finally arrived). Past Perfect Continuous (had been waiting) يوضح مدة الفعل قبل حدث آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (study) English for six months before taking the exam.",
        "options": ["have been studying", "were studying", "had been studying", "studied"],
        "correct_option_id": 2,
        "explanation": "دراسة اللغة الإنجليزية (study) استمرت لمدة ستة أشهر *قبل* اجتياز الامتحان (taking the exam). Past Perfect Continuous (had been studying) يوضح مدة الفعل قبل حدث آخر في الماضي."
    }
]
        },
        "زمن المستقبل": {
            "المستقبل البسيط": [
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (go) to the store tomorrow.",
        "options": ["go", "am going", "was going", "will go"],
        "correct_option_id": 3,
        "explanation": "نستخدم  'will go'  لأنّ الجملة تصفُّ فعلاً سيحدث في المستقبل (غدًا).  'Will'  هو المساعد المستخدم في زمن المضارع البسيط للمستقبل للتعبير عن قرارات مفاجئة أو توقعات أو تنبؤات."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (visit) her grandmother next week.",
        "options": ["visits", "is visiting", "visited", "will visit"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'will visit'  لأنّ الجملة تتحدث عن زيارة ستحدث في المستقبل (الأسبوع القادم).  'Will' يُستخدم هنا للتعبير عن حدث مُخطط له في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (play) soccer this weekend.",
        "options": ["play", "are playing", "played", "will play"],
        "correct_option_id": 3,
        "explanation": "التعبير 'this weekend' يشير إلى حدث مستقبلي، و'will play'  هو الصياغة الصحيحة في زمن المضارع البسيط للمستقبل للتعبير عن توقعات أو خطط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (have) a party next Saturday.",
        "options": ["have", "are having", "had", "will have"],
        "correct_option_id": 3,
        "explanation": "زمن المضارع البسيط للمستقبل (will have) يُستخدم للتعبير عن حدث مُرتقب في المستقبل (السبت القادم).  يُفضل استخدام 'will' على 'going to'  في هذه الحالة لوصف تخطيط مستقبلي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (study) for his exams next month.",
        "options": ["studies", "is studying", "studied", "will study"],
        "correct_option_id": 3,
        "explanation": "التعبير 'next month'  يشير إلى المستقبل، و'will study'  يُستخدم للتعبير عن نية أو توقع للدراسة في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/forget) to call you.",
        "options": ["don't forget", "didn't forget", "am not forgetting", "will not forget"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not forget'  يُعبر عن نية عدم نسيان الاتصال في المستقبل.  'Will not'  (أو won't)  هو الشكل المُختصر والمثالي في هذه الحالة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow long ____ (you/stay) in London?",
        "options": ["are you staying", "did you stay", "have you stayed", "will you stay"],
        "correct_option_id": 3,
        "explanation": "في سؤال عن مدة الإقامة في لندن،  'will you stay'  هو الصيغة الصحيحة لزمن المضارع البسيط للمستقبل.  يُستخدم  'will'  لسؤال عن توقع أو خطط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/go) to the meeting tomorrow.",
        "options": ["doesn't go", "didn't go", "is not going", "will not go"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not go' (أو won't go) يُعبر عن عدم الذهاب إلى الاجتماع في المستقبل.  هذا هو الشكل الأنسب لوصف نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (move) to a new house next month.",
        "options": ["move", "are moving", "moved", "will move"],
        "correct_option_id": 3,
        "explanation": "التعبير 'next month'  يشير إلى المستقبل، و'will move'  يُستخدم للتعبير عن نية أو توقع للانتقال إلى منزل جديد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/play) football this weekend.",
        "options": ["doesn't play", "didn't play", "is not playing", "will not play"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not play' (أو won't play) يُعبر عن عدم لعب كرة القدم في المستقبل.  'will not'  أفضل من الأزمنة الأخرى للتعبير عن نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (travel) to Italy next summer.",
        "options": ["travel", "am traveling", "traveled", "will travel"],
        "correct_option_id": 3,
        "explanation": "التعبير 'next summer'  يشير إلى المستقبل، و'will travel'  يُستخدم للتعبير عن خطط السفر إلى إيطاليا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/see) the new movie this weekend.",
        "options": ["don't see", "didn't see", "are not seeing", "will not see"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not see' (أو won't see) يُعبر عن عدم مشاهدة الفيلم الجديد في المستقبل.  يُفضل  'will not'  لتوضيح نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow many languages ____ (you/learn)?",
        "options": ["are you learning", "did you learn", "have you learned", "will you learn"],
        "correct_option_id": 3,
        "explanation": "في سؤال عن عدد اللغات التي سيتعلمها الشخص،  'will you learn'  هو الصيغة الصحيحة لزمن المضارع البسيط للمستقبل.  'will'  يُستخدم هنا للاستفسار عن نية مستقبلية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (finish) her homework later.",
        "options": ["finishes", "is finishing", "finished", "will finish"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will finish'  يُعبر عن نية إنهاء الواجب المنزلي في المستقبل.  'will'  هنا يُناسب التعبير عن توقع أو نية مستقبلية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/attend) the conference next week.",
        "options": ["don't attend", "didn't attend", "are not attending", "will not attend"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not attend' (أو won't attend)  يُعبر عن عدم حضور المؤتمر في المستقبل.  'will not'  أفضل من الأزمنة الأخرى للتعبير عن نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (work) on that project next month.",
        "options": ["works", "is working", "worked", "will work"],
        "correct_option_id": 3,
        "explanation": "التعبير 'next month'  يشير إلى المستقبل، و'will work'  يُستخدم للتعبير عن نية أو توقع للعمل على المشروع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/meet) you tomorrow.",
        "options": ["don't meet", "didn't meet", "am not meeting", "will not meet"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not meet' (أو won't meet) يُعبر عن عدم اللقاء غداً.  'will not'  يُناسب التعبير عن نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (join) us for dinner tonight.",
        "options": ["joins", "is joining", "joined", "will join"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will join'  يُعبر عن نية الانضمام إلى العشاء الليلة.  'will'  هنا يُناسب التعبير عن توقع أو نية مستقبلية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/go) to the party next week.",
        "options": ["don't go", "didn't go", "are not going", "will not go"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not go' (أو won't go) يُعبر عن عدم الذهاب إلى الحفلة في المستقبل.  يُفضل  'will not'  لتوضيح نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (read) that book next week.",
        "options": ["read", "am reading", "have read", "will read"],
        "correct_option_id": 3,
        "explanation": "التعبير 'next week'  يشير إلى المستقبل، و'will read'  يُستخدم للتعبير عن نية أو توقع لقراءة الكتاب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (call) you later.",
        "options": ["calls", "is calling", "called", "will call"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will call'  يُعبر عن نية الاتصال في المستقبل.  'will'  هنا يُناسب التعبير عن توقع أو نية مستقبلية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/visit) us this weekend.",
        "options": ["don't visit", "didn't visit", "are not visiting", "will not visit"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not visit' (أو won't visit)  يُعبر عن عدم الزيارة هذا الأسبوع.  'will not'  يُناسب التعبير عن نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (buy) a new phone next month.",
        "options": ["buy", "am buying", "bought", "will buy"],
        "correct_option_id": 3,
        "explanation": "التعبير 'next month'  يشير إلى المستقبل، و'will buy'  يُستخدم للتعبير عن نية أو توقع لشراء هاتف جديد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHow many times ____ (you/call) me?",
        "options": ["are you calling", "did you call", "have you called", "will you call"],
        "correct_option_id": 3,
        "explanation": "في سؤال عن عدد المرات التي سيتصل بها الشخص،  'will you call'  هو الصيغة الصحيحة لزمن المضارع البسيط للمستقبل.  يُستخدم  'will'  للاستفسار عن نية مستقبلية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/go) to the beach this summer.",
        "options": ["doesn't go", "didn't go", "is not going", "will not go"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not go' (أو won't go)  يُعبر عن عدم الذهاب إلى الشاطئ هذا الصيف.  يُفضل  'will not'  لتوضيح نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (meet) him at the party tomorrow.",
        "options": ["meet", "am meeting", "met", "will meet"],
        "correct_option_id": 3,
        "explanation": "التعبير 'tomorrow'  يشير إلى المستقبل، و'will meet'  يُستخدم للتعبير عن نية أو توقع للقاء."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (take) a vacation next month.",
        "options": ["take", "are taking", "took", "will take"],
        "correct_option_id": 3,
        "explanation": "التعبير 'next month'  يشير إلى المستقبل، و'will take'  يُستخدم للتعبير عن نية أو توقع لأخذ إجازة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/like) the movie.",
        "options": ["doesn't like", "didn't like", "is not liking", "will not like"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not like' (أو won't like)  يُعبر عن عدم الإعجاب بالفيلم في المستقبل.  يُفضل  'will not'  لتوضيح توقع مستقبلي منفي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/see) her tomorrow.",
        "options": ["don't see", "didn't see", "am not seeing", "will not see"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not see' (أو won't see)  يُعبر عن عدم رؤية الشخص غداً.  يُناسب  'will not'  التعبير عن نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/go) to the concert next week.",
        "options": ["don't go", "didn't go", "are not going", "will not go"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not go' (أو won't go) يُعبر عن عدم الذهاب إلى الحفل الموسيقي في الأسبوع القادم.  يُفضل استخدام 'will not' للتعبير عن نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (study) hard for the exam.",
        "options": ["studies", "is studying", "studied", "will study"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will study' يُعبر عن نية الدراسة بجدّ.  'will' يُناسب التعبير عن توقع أو نية مستقبلية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (travel) to Paris next year.",
        "options": ["travel", "are traveling", "traveled", "will travel"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will travel' يُعبر عن خطط السفر إلى باريس.  'will' يُناسب التعبير عن نية أو توقع مستقبلي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/eat) dinner tonight.",
        "options": ["don't eat", "didn't eat", "am not eating", "will not eat"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will not eat' (أو won't eat) يُعبر عن عدم تناول العشاء الليلة.  'will not' يُناسب التعبير عن نية مستقبلية منفية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (meet) his friend tomorrow.",
        "options": ["meets", "is meeting", "met", "will meet"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will meet' يُعبر عن نية اللقاء بصديقه غداً.  'will' يُناسب التعبير عن نية أو توقع مستقبلي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (not/work) tomorrow.",
        "options": ["don't work", "didn't work", "aren't working", "won't work"],
        "correct_option_id": 3,
        "explanation": "استخدام 'won't work' يُعبر عن عدم العمل غداً.  'won't' هو الشكل المُختصر والمُناسب لنفي نية مستقبلية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (buy) a new car next year.",
        "options": ["buys", "is buying", "bought", "will buy"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will buy' يُعبر عن نية شراء سيارة جديدة.  'will' يُناسب التعبير عن نية أو توقع مستقبلي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI ____ (not/go) to the party tonight.",
        "options": ["don't go", "didn't go", "am not going", "won't go"],
        "correct_option_id": 3,
        "explanation": "استخدام 'won't go' يُعبر عن عدم الذهاب إلى الحفلة الليلة.  'won't' هو الشكل المُختصر والمُناسب لنفي نية مستقبلية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (visit) their family next month.",
        "options": ["visit", "are visiting", "visited", "will visit"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will visit' يُعبر عن نية زيارة العائلة.  'will' يُناسب التعبير عن نية أو توقع مستقبلي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (finish) his homework soon.",
        "options": ["finishes", "is finishing", "finished", "will finish"],
        "correct_option_id": 3,
        "explanation": "استخدام 'will finish' يُعبر عن نية إنهاء الواجب المنزلي قريباً.  'will' يُناسب التعبير عن توقع أو نية مستقبلية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (not/see) them tomorrow.",
        "options": ["don't see", "didn't see", "aren't seeing", "won't see"],
        "correct_option_id": 3,
        "explanation": "استخدام 'won't see' يُعبر عن عدم رؤية هؤلاء الأشخاص غداً.  'won't' هو الشكل المُختصر والمُناسب لنفي نية مستقبلية."
    }
],
            "المستقبل المستمر": [
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will I be ____ (do) at this time tomorrow?",
        "options": ["do", "done", "doing", "did"],
        "correct_option_id": 2,
        "explanation": "يستخدم Future Continuous (will be + فعل + ing) لوصف فعل مستمر في لحظة محددة في المستقبل.  السؤال يستفسر عن نشاطي المستمر في وقت محدد غداً،  لذلك نستخدم 'doing'  لأنها تشير إلى فعل مستمر في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe will be ____ (study) for her exams next week.",
        "options": ["studied", "studying", "studies", "study"],
        "correct_option_id": 1,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم للتعبير عن فعل مستمرّ خلال فترة زمنية في المستقبل.  'next week'  تحدد فترة زمنية، و'studying' تصفُّ فعلًا مستمرًا خلالها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey will be ____ (play) soccer in the park.",
        "options": ["play", "played", "playing", "plays"],
        "correct_option_id": 2,
        "explanation": "يستخدم Future Continuous (will be + فعل + ing) لوصف فعل مستمرّ في المستقبل.  'playing'  تصفُّ فعلًا مستمرًا في زمن محدد (في الحديقة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe will be ____ (have) dinner at 7 PM.",
        "options": ["had", "has", "having", "have"],
        "correct_option_id": 2,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في وقت محدد في المستقبل.  'having'  تصفُّ فعلًا مستمرًا (تناول العشاء)  في وقت محدد (الساعة 7 مساءً)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe will be ____ (work) on his project during the weekend.",
        "options": ["worked", "works", "working", "work"],
        "correct_option_id": 2,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ خلال فترة زمنية في المستقبل.  'during the weekend'  تحدد فترة زمنية، و'working' تصفُّ فعلًا مستمرًا خلالها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will she ____ (do) when you arrive?",
        "options": ["be doing", "did", "do", "does"],
        "correct_option_id": 0,
        "explanation": "يستخدم Future Continuous (will be + فعل + ing)  لسؤال عن فعل مستمرّ في المستقبل.  'be doing'  تصفُّ فعلًا مستمرًا في زمن مُحدد (عندما تصل)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey will be ____ (not/play) in the tournament.",
        "options": ["don't play", "not playing", "not play", "didn't play"],
        "correct_option_id": 1,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لوصف فعل مستمرّ منفي في المستقبل.  'not playing'  تُعبر عن فعل مستمرّ منفي في زمن مُحدد (في البطولة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will I be ____ (not/see) on TV?",
        "options": ["not see", "not seeing", "didn't see", "doesn't see"],
        "correct_option_id": 1,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لسؤال عن فعل مستمرّ منفي في المستقبل.  'not seeing' تُعبر عن فعل مستمرّ منفي (عدم المشاهدة) في زمن مُحدد (على التلفزيون)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI will be ____ (watch) a movie tonight.",
        "options": ["watched", "watches", "watching", "watch"],
        "correct_option_id": 2,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في المستقبل.  'watching'  تصفُّ فعلًا مستمرًا في زمن مُحدد (الليلة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe will be ____ (not/attend) the meeting next week.",
        "options": ["not attend", "don't attend", "not attending", "didn't attend"],
        "correct_option_id": 2,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لوصف فعل مستمرّ منفي في المستقبل.  'not attending'  تُعبر عن فعل مستمرّ منفي (عدم الحضور) في زمن مُحدد (الأسبوع القادم)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI will be ____ (not/meet) you tomorrow.",
        "options": ["not meet", "not be meeting", "didn't meet", "don't meet"],
        "correct_option_id": 1,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لوصف فعل مستمرّ منفي في المستقبل.  'not be meeting' تُعبر عن فعل مستمرّ منفي (عدم اللقاء) في زمن مُحدد (غداً)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will you be ____ (do) when I call?",
        "options": ["doing", "do", "did", "does"],
        "correct_option_id": 0,
        "explanation": "يستخدم Future Continuous (will be + فعل + ing)  لسؤال عن فعل مستمرّ في المستقبل.  'doing'  تصفُّ فعلًا مستمرًا في زمن مُحدد (عندما أتصل)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe will be ____ (travel) to France next month.",
        "options": ["travelling", "travel", "travels", "traveled"],
        "correct_option_id": 0,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في المستقبل.  'travelling'  تصفُّ فعلًا مستمرًا (السفر)  في زمن مُحدد (الأسبوع القادم)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe will be ____ (enjoy) the concert tomorrow.",
        "options": ["enjoying", "enjoy", "enjoyed", "enjoys"],
        "correct_option_id": 0,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في المستقبل.  'enjoying'  تصفُّ فعلًا مستمرًا (الاستمتاع)  في زمن مُحدد (غداً)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe will be ____ (cook) dinner when they arrive.",
        "options": ["cooked", "cooking", "cooks", "cook"],
        "correct_option_id": 1,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في المستقبل.  'cooking'  تصفُّ فعلًا مستمرًا (الطبخ)  في زمن مُحدد (عندما يصلون)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will he be ____ (work) on next week?",
        "options": ["working", "work", "worked", "works"],
        "correct_option_id": 0,
        "explanation": "يستخدم Future Continuous (will be + فعل + ing)  لسؤال عن فعل مستمرّ في المستقبل.  'working'  تصفُّ فعلًا مستمرًا (العمل) في زمن مُحدد (الأسبوع القادم)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey will be ____ (visit) their grandparents this weekend.",
        "options": ["visit", "visiting", "visited", "visits"],
        "correct_option_id": 1,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في المستقبل.  'visiting'  تصفُّ فعلًا مستمرًا (الزيارة)  في زمن مُحدد (هذا الأسبوع)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nYou will be ____ (study) for your exams at this time next week.",
        "options": ["studying", "studies", "study", "studied"],
        "correct_option_id": 0,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في وقت محدد في المستقبل.  'studying'  تصفُّ فعلًا مستمرًا (الدراسة) في زمن مُحدد (هذا الوقت من الأسبوع القادم)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nAt this time tomorrow, I will be ____ (fly) to New York.",
        "options": ["flew", "flown", "flying", "fly"],
        "correct_option_id": 2,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في وقت محدد في المستقبل.  'flying'  تصفُّ فعلًا مستمرًا (الطيران) في زمن مُحدد (هذا الوقت غداً)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will she ____ (not/study) for her test?",
        "options": ["not study", "not be studying", "doesn't study", "didn't study"],
        "correct_option_id": 1,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لسؤال عن فعل مستمرّ منفي في المستقبل.  'not be studying' تُعبر عن فعل مستمرّ منفي (عدم الدراسة) في زمن مُحدد (قبل الاختبار)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe will be ____ (not/attend) the concert this weekend.",
        "options": ["not attending", "not attend", "didn't attend", "don't attend"],
        "correct_option_id": 0,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لوصف فعل مستمرّ منفي في المستقبل.  'not attending'  تُعبر عن فعل مستمرّ منفي (عدم الحضور) في زمن مُحدد (هذا الأسبوع)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nAt this moment next year, they will be ____ (travel) around Europe.",
        "options": ["travel", "travelling", "travels", "traveled"],
        "correct_option_id": 1,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في وقت محدد في المستقبل.  'travelling'  تصفُّ فعلًا مستمرًا (السفر) في زمن مُحدد (هذا الوقت من العام القادم)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe will be ____ (drive) to work during rush hour.",
        "options": ["driving", "drive", "drove", "drives"],
        "correct_option_id": 0,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في وقت محدد في المستقبل.  'driving'  تصفُّ فعلًا مستمرًا (القيادة)  في زمن مُحدد (خلال ساعة الذروة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will I be ____ (eat) for lunch?",
        "options": ["eating", "eat", "eats", "ate"],
        "correct_option_id": 0,
        "explanation": "يستخدم Future Continuous (will be + فعل + ing)  لسؤال عن فعل مستمرّ في المستقبل.  'eating'  تصفُّ فعلًا مستمرًا (الأكل) في زمن مُحدد (وقت الغداء)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey will be ____ (watch) the game on TV.",
        "options": ["watched", "watches", "watching", "watch"],
        "correct_option_id": 2,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في المستقبل.  'watching'  تصفُّ فعلًا مستمرًا (المشاهدة) في زمن مُحدد (على التلفزيون)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will he be ____ (not/cook) for dinner?",
        "options": ["not cooking", "doesn't cook", "not cook", "didn't cook"],
        "correct_option_id": 0,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لسؤال عن فعل مستمرّ منفي في المستقبل.  'not cooking' تُعبر عن فعل مستمرّ منفي (عدم الطبخ) في زمن مُحدد (وقت العشاء)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nAt this time next month, I will be ____ (prepare) for my presentation.",
        "options": ["preparing", "prepares", "prepare", "prepared"],
        "correct_option_id": 0,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في وقت محدد في المستقبل.  'preparing'  تصفُّ فعلًا مستمرًا (الإعداد)  في زمن مُحدد (هذا الوقت من الشهر القادم)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe will be ____ (not/sleep) when we arrive.",
        "options": ["not sleeping", "not sleep", "didn't sleep", "doesn't sleep"],
        "correct_option_id": 0,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لوصف فعل مستمرّ منفي في المستقبل.  'not sleeping' تُعبر عن فعل مستمرّ منفي (عدم النوم) في زمن مُحدد (عندما نصل)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will they be ____ (discuss) in the meeting?",
        "options": ["discussed", "discussing", "discuss", "discusses"],
        "correct_option_id": 1,
        "explanation": "يستخدم Future Continuous (will be + فعل + ing)  لسؤال عن فعل مستمرّ في المستقبل.  'discussing'  تصفُّ فعلًا مستمرًا (المناقشة) في زمن مُحدد (خلال الاجتماع)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI will be ____ (not/play) video games this weekend.",
        "options": ["not playing", "not play", "don't play", "didn't play"],
        "correct_option_id": 0,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لوصف فعل مستمرّ منفي في المستقبل.  'not playing'  تُعبر عن فعل مستمرّ منفي (عدم اللعب) في زمن مُحدد (هذا الأسبوع)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey will be ____ (go) to the beach tomorrow.",
        "options": ["going", "go", "went", "goes"],
        "correct_option_id": 0,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في المستقبل.  'going'  تصفُّ فعلًا مستمرًا (الذهاب) في زمن مُحدد (غداً)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will she be ____ (work) on at this time next year?",
        "options": ["worked", "working", "works", "work"],
        "correct_option_id": 1,
        "explanation": "يستخدم Future Continuous (will be + فعل + ing)  لسؤال عن فعل مستمرّ في المستقبل.  'working'  تصفُّ فعلًا مستمرًا (العمل) في زمن مُحدد (هذا الوقت من العام القادم)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe will be ____ (not/visit) our friends this weekend.",
        "options": ["not visiting", "not visit", "didn't visit", "don't visit"],
        "correct_option_id": 0,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لوصف فعل مستمرّ منفي في المستقبل.  'not visiting'  تُعبر عن فعل مستمرّ منفي (عدم الزيارة) في زمن مُحدد (هذا الأسبوع)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe will be ____ (not/go) to the party.",
        "options": ["not going", "not go", "didn't go", "doesn't go"],
        "correct_option_id": 0,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لوصف فعل مستمرّ منفي في المستقبل.  'not going'  تُعبر عن فعل مستمرّ منفي (عدم الذهاب) في زمن مُحدد (إلى الحفلة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nAt this time next week, I will be ____ (present) my project.",
        "options": ["presenting", "presents", "presented", "present"],
        "correct_option_id": 0,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في وقت محدد في المستقبل.  'presenting'  تصفُّ فعلًا مستمرًا (العرض) في زمن مُحدد (هذا الوقت من الأسبوع القادم)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will they be ____ (plan) for the future?",
        "options": ["planned", "planning", "plans", "plan"],
        "correct_option_id": 1,
        "explanation": "يستخدم Future Continuous (will be + فعل + ing)  لسؤال عن فعل مستمرّ في المستقبل.  'planning'  تصفُّ فعلًا مستمرًا (التخطيط) في زمن مُحدد (للمستقبل)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nI will be ____ (talk) to my friends later.",
        "options": ["talking", "talk", "talked", "talks"],
        "correct_option_id": 0,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في المستقبل.  'talking'  تصفُّ فعلًا مستمرًا (التحدث) في زمن مُحدد (لاحقاً)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe will be ____ (clean) the house when I arrive.",
        "options": ["cleaned", "cleans", "cleaning", "clean"],
        "correct_option_id": 2,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في المستقبل.  'cleaning'  تصفُّ فعلًا مستمرًا (التنظيف) في زمن مُحدد (عندما أصل)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat will he be ____ (not/work) on?",
        "options": ["not working", "not work", "didn't work", "doesn't work"],
        "correct_option_id": 0,
        "explanation": "Future Continuous منفي (will not be + فعل + ing) يُستخدم لسؤال عن فعل مستمرّ منفي في المستقبل.  'not working' تُعبر عن فعل مستمرّ منفي (عدم العمل) في زمن مُحدد (على شيء ما)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey will be ____ (enjoy) their vacation next week.",
        "options": ["enjoyed", "enjoys", "enjoying", "enjoy"],
        "correct_option_id": 2,
        "explanation": "Future Continuous (will be + فعل + ing) يُستخدم لوصف فعل مستمرّ في المستقبل.  'enjoying'  تصفُّ فعلًا مستمرًا (الاستمتاع)  في زمن مُحدد (الأسبوع القادم)."
    }
],
            "المستقبل التام": [
    {
        "question": "اختر الإجابة الصحيحة:\nBy next week, I ____ (finish) this project.",
        "options": ["will finish", "will have finished", "finish", "am finishing"],
        "correct_option_id": 1,
        "explanation": "نستخدم Future Perfect (will have + past participle) للتعبير عن فعل سيكتمل قبل وقت محدد في المستقبل.  'By next week'  يشير إلى وقت مُحدد في المستقبل،  و'will have finished'  يُعبر عن اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/complete) her studies by the end of the year.",
        "options": ["won't complete", "will not have completed", "isn't completing", "didn't complete"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي (will not have + past participle) يُستخدم للتعبير عن فعل لن يكتمل قبل وقت محدد في المستقبل.  'By the end of the year'  يُحدد وقتًا مستقبليًا، و'will not have completed'  يُعبر عن عدم اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (leave) before you arrive.",
        "options": ["will leave", "will have left", "leave", "are leaving"],
        "correct_option_id": 1,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعل منتهي قبل حدث آخر في المستقبل. 'Before you arrive'  يُحدد وقتًا مستقبليًا، و'will have left'  يُعبر عن اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/eat) dinner by the time we get there.",
        "options": ["won't eat", "will not have eaten", "isn't eating", "didn't eat"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي (will not have + past participle) يُستخدم للتعبير عن فعل لن يكتمل قبل وقت محدد في المستقبل.  'By the time we get there'  يُحدد وقتًا مستقبليًا، و'will not have eaten'  يُعبر عن عدم اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (finish) the project by Friday.",
        "options": ["will finish", "will have finished", "are finishing", "finished"],
        "correct_option_id": 1,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعل سيكتمل قبل وقت محدد في المستقبل.  'By Friday'  يُحدد وقتًا مستقبليًا، و'will have finished'  يُعبر عن اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/travel) to Europe by next summer.",
        "options": ["won't travel", "will not have traveled", "isn't traveling", "didn't travel"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي (will not have + past participle) يُستخدم للتعبير عن فعل لن يكتمل قبل وقت محدد في المستقبل.  'By next summer'  يُحدد وقتًا مستقبليًا، و'will not have traveled'  يُعبر عن عدم اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (complete) their work by the end of the week.",
        "options": ["will complete", "will have completed", "are completing", "completed"],
        "correct_option_id": 1,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعل سيكتمل قبل وقت محدد في المستقبل.  'By the end of the week'  يُحدد وقتًا مستقبليًا، و'will have completed'  يُعبر عن اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/read) the book by tomorrow.",
        "options": ["won't read", "will not have read", "isn't reading", "didn't read"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي (will not have + past participle) يُستخدم للتعبير عن فعل لن يكتمل قبل وقت محدد في المستقبل.  'By tomorrow'  يُحدد وقتًا مستقبليًا، و'will not have read'  يُعبر عن عدم اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (graduate) by next June.",
        "options": ["will graduate", "will have graduated", "are graduating", "graduated"],
        "correct_option_id": 1,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعل سيكتمل قبل وقت محدد في المستقبل.  'By next June'  يُحدد وقتًا مستقبليًا، و'will have graduated'  يُعبر عن اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/arrive) by 8 o'clock.",
        "options": ["won't arrive", "will not have arrived", "isn't arriving", "didn't arrive"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي (will not have + past participle) يُستخدم للتعبير عن فعل لن يكتمل قبل وقت محدد في المستقبل.  'By 8 o'clock'  يُحدد وقتًا مستقبليًا، و'will not have arrived'  يُعبر عن عدم اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nBy next year, they ____ (travel) around the world.",
        "options": ["will travel", "will have traveled", "are traveling", "traveled"],
        "correct_option_id": 1,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعل سيكتمل قبل وقت محدد في المستقبل.  'By next year'  يُحدد وقتًا مستقبليًا، و'will have traveled'  يُعبر عن اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/finish) his homework by tonight.",
        "options": ["won't finish", "will not have finished", "isn't finishing", "didn't finish"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي (will not have + past participle) يُستخدم للتعبير عن فعل لن يكتمل قبل وقت محدد في المستقبل.  'By tonight'  يُحدد وقتًا مستقبليًا، و'will not have finished'  يُعبر عن عدم اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (learn) a lot by the end of the course.",
        "options": ["will learn", "will have learned", "are learning", "learned"],
        "correct_option_id": 1,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعل سيكتمل قبل وقت محدد في المستقبل.  'By the end of the course'  يُحدد وقتًا مستقبليًا، و'will have learned'  يُعبر عن اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/see) him before he returns.",
        "options": ["won't see", "will not have seen", "isn't seeing", "didn't see"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي (will not have + past participle) يُستخدم للتعبير عن فعل لن يكتمل قبل وقت محدد في المستقبل.  'Before he returns'  يُحدد وقتًا مستقبليًا، و'will not have seen'  يُعبر عن عدم اكتمال الفعل قبل ذلك الوقت."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nBy tomorrow, I ____ (finish) reading this book.",
        "options": ["will finish", "will have finished", "am finishing", "finish"],
        "correct_option_id": 1,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By tomorrow' يُحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/send) the email by noon.",
        "options": ["won't send", "will not have sent", "isn't sending", "didn't send"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل. 'By noon'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (leave) before the party starts.",
        "options": ["will leave", "will have left", "leave", "are leaving"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل حدث آخر في المستقبل.  'Before the party starts'  يُحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/arrive) by the time the meeting begins.",
        "options": ["won't arrive", "will not have arrived", "isn't arriving", "didn't arrive"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By the time the meeting begins'  يُحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (complete) the report by Monday.",
        "options": ["will complete", "will have completed", "are completing", "completed"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By Monday'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/finish) her work by tomorrow evening.",
        "options": ["won't finish", "will not have finished", "isn't finishing", "didn't finish"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By tomorrow evening'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (go) home before it gets dark.",
        "options": ["will go", "will have gone", "go", "are going"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل حدث آخر في المستقبل.  'Before it gets dark'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/eat) lunch by 2 PM.",
        "options": ["won't eat", "will not have eaten", "isn't eating", "didn't eat"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By 2 PM'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (receive) the results by Friday.",
        "options": ["will receive", "will have received", "are receiving", "received"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By Friday'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/send) the package by tomorrow.",
        "options": ["won't send", "will not have sent", "isn't sending", "didn't send"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By tomorrow'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (complete) their training by next month.",
        "options": ["will complete", "will have completed", "are completing", "completed"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By next month'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/write) the essay by the deadline.",
        "options": ["won't write", "will not have written", "isn't writing", "didn't write"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By the deadline'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (solve) the problem by tomorrow morning.",
        "options": ["will solve", "will have solved", "are solving", "solved"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By tomorrow morning'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/call) him before he leaves.",
        "options": ["won't call", "will not have called", "isn't calling", "didn't call"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'Before he leaves'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (arrive) in London by next week.",
        "options": ["will arrive", "will have arrived", "are arriving", "arrived"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By next week'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/read) the entire book by the weekend.",
        "options": ["won't read", "will not have read", "isn't reading", "didn't read"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By the weekend'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (prepare) for the exam by next month.",
        "options": ["will prepare", "will have prepared", "are preparing", "prepared"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By next month'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/finish) her project by Friday.",
        "options": ["won't finish", "will not have finished", "isn't finishing", "didn't finish"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By Friday'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (sell) their car by next year.",
        "options": ["will sell", "will have sold", "are selling", "sold"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By next year'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/meet) his friend before the party.",
        "options": ["won't meet", "will not have met", "isn't meeting", "didn't meet"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'Before the party'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (complete) our studies by next summer.",
        "options": ["will complete", "will have completed", "are completing", "completed"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By next summer'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/write) the letter by tomorrow.",
        "options": ["won't write", "will not have written", "isn't writing", "didn't write"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By tomorrow'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (find) a solution by the end of the week.",
        "options": ["will find", "will have found", "are finding", "found"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By the end of the week'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/call) her before she leaves.",
        "options": ["won't call", "will not have called", "isn't calling", "didn't call"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'Before she leaves'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (travel) to Italy by next year.",
        "options": ["will travel", "will have traveled", "are traveling", "traveled"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By next year'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/buy) a new house by next spring.",
        "options": ["won't buy", "will not have bought", "isn't buying", "didn't buy"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By next spring'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (finish) their project by the deadline.",
        "options": ["will finish", "will have finished", "are finishing", "finished"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By the deadline'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/see) that movie before next month.",
        "options": ["won't see", "will not have seen", "isn't seeing", "didn't see"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'Before next month'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (learn) to drive by next summer.",
        "options": ["will learn", "will have learned", "are learning", "learned"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By next summer'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/complete) the course by December.",
        "options": ["won't complete", "will not have completed", "isn't completing", "didn't complete"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By December'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (build) the house by next year.",
        "options": ["will build", "will have built", "are building", "built"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By next year'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/meet) his idol before the concert.",
        "options": ["won't meet", "will not have met", "isn't meeting", "didn't meet"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'Before the concert'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (travel) to Japan by next spring.",
        "options": ["will travel", "will have traveled", "are traveling", "traveled"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By next spring'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/write) the report by tomorrow afternoon.",
        "options": ["won't write", "will not have written", "isn't writing", "didn't write"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'By tomorrow afternoon'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (finish) their studies by the end of the year.",
        "options": ["will finish", "will have finished", "are finishing", "finished"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By the end of the year'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/call) me before the meeting.",
        "options": ["won't call", "will not have called", "isn't calling", "didn't call"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'Before the meeting'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (learn) everything by the end of the course.",
        "options": ["will learn", "will have learned", "are learning", "learned"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By the end of the course'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/go) to the party before she finishes her work.",
        "options": ["won't go", "will not have gone", "isn't going", "didn't go"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'Before she finishes her work'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (complete) their homework before the deadline.",
        "options": ["will complete", "will have completed", "are completing", "completed"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'Before the deadline'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/visit) his grandparents before next week.",
        "options": ["won't visit", "will not have visited", "isn't visiting", "didn't visit"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'Before next week'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWe ____ (receive) the results by the end of the week.",
        "options": ["will receive", "will have received", "are receiving", "received"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By the end of the week'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe ____ (not/buy) that dress before the party.",
        "options": ["won't buy", "will not have bought", "isn't buying", "didn't buy"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'Before the party'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey ____ (finish) the game by 10 PM.",
        "options": ["will finish", "will have finished", "are finishing", "finished"],
        "correct_option_id": 1,
        "explanation": "Future Perfect يُستخدم للتعبير عن اكتمال الفعل قبل وقت محدد في المستقبل.  'By 10 PM'  يحدد وقتًا مستقبليًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe ____ (not/call) me before he leaves for work.",
        "options": ["won't call", "will not have called", "isn't calling", "didn't call"],
        "correct_option_id": 1,
        "explanation": "Future Perfect منفي يُستخدم للتعبير عن عدم اكتمال الفعل قبل وقت محدد في المستقبل.  'Before he leaves for work'  يحدد وقتًا مستقبليًا."
    }
],
            "المستقبل التام المستمر": [
  {
    "question": "اختر الإجابة الصحيحة:\nBy next week, I ____ (study) for two months.",
    "options": ["will study", "will be studying", "will have been studying", "have been studying"],
    "correct_option_id": 2,
    "explanation": "نستخدم Future Perfect Continuous (will have been + present participle) للتعبير عن فعل مستمرّ سيستمرّ لفترة زمنية محددة قبل وقت في المستقبل.  'By next week'  يحدد نقطة زمنية في المستقبل.  'will have been studying'  تشير إلى أنَّ الدراسة ستكون مستمرة لفترة شهرين قبل ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/wait) for him for more than an hour by the time he arrives.",
    "options": ["won't wait", "won't be waiting", "will not have been waiting", "didn't wait"],
    "correct_option_id": 2,
    "explanation": "يستخدم Future Perfect Continuous منفي (will not have been + present participle) للتعبير عن فعل مستمرّ لن يستمرّ لفترة زمنية محددة قبل وقت في المستقبل.  'By the time he arrives'  يحدد نقطة زمنية في المستقبل.  'will not have been waiting'  تشير إلى أنَّ انتظارها لن يستمرّ لأكثر من ساعة قبل وصوله."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nThey ____ (live) in that house for ten years by next year.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next year'  يُشير إلى وقت مُحدد، و'will have been living'  يُعبر عن استمرار السكن في المنزل لمدة عشر سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) on that project for a year by the deadline.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل. 'By the deadline'  يُشير إلى وقت مُحدد، و'will not have been working'  يُعبر عن عدم استمرار العمل على المشروع لمدة عام كامل حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (learn) English for six months by the end of the course.",
    "options": ["will learn", "will be learning", "will have been learning", "have been learning"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the end of the course'  يُشير إلى وقت مُحدد، و'will have been learning'  يُعبر عن استمرار تعلم اللغة الإنجليزية لمدة ستة أشهر حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/wait) for him for long by the time he arrives.",
    "options": ["won't wait", "won't be waiting", "will not have been waiting", "didn't wait"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he arrives'  يُشير إلى وقت مُحدد، و'will not have been waiting'  يُعبر عن عدم استمرار الانتظار لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nThey ____ (play) video games for hours by the time their parents come home.",
    "options": ["will play", "will be playing", "will have been playing", "have been playing"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the time their parents come home'  يُشير إلى وقت مُحدد، و'will have been playing'  يُعبر عن استمرار اللعب لساعات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/study) for long by the time the exam starts.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time the exam starts'  يُشير إلى وقت مُحدد، و'will not have been studying'  يُعبر عن عدم استمرار الدراسة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (work) on this project for a month by the deadline.",
    "options": ["will work", "will be working", "will have been working", "have been working"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the deadline'  يُشير إلى وقت مُحدد، و'will have been working'  يُعبر عن استمرار العمل على المشروع لمدة شهر حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/live) in that apartment for a year by the time they move.",
    "options": ["won't live", "won't be living", "will not have been living", "didn't live"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time they move'  يُشير إلى وقت مُحدد، و'will not have been living'  يُعبر عن عدم استمرار السكن في الشقة لمدة عام كامل حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next summer, they ____ (travel) for a year.",
    "options": ["will travel", "will be traveling", "will have been traveling", "have been traveling"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next summer'  يُشير إلى وقت مُحدد، و'will have been traveling'  يُعبر عن استمرار السفر لمدة عام حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/wait) for her for long by the time she arrives.",
    "options": ["won't wait", "won't be waiting", "will not have been waiting", "didn't wait"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time she arrives'  يُشير إلى وقت مُحدد، و'will not have been waiting'  يُعبر عن عدم استمرار الانتظار لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (learn) this subject for three months by the end of the semester.",
    "options": ["will learn", "will be learning", "will have been learning", "have been learning"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the end of the semester'  يُشير إلى وقت مُحدد، و'will have been learning'  يُعبر عن استمرار التعلم لمدة ثلاثة أشهر حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) for very long by the time the exam begins.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time the exam begins'  يُشير إلى وقت مُحدد، و'will not have been studying'  يُعبر عن عدم استمرار الدراسة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next year, they ____ (live) in that city for five years.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next year'  يُشير إلى وقت مُحدد، و'will have been living'  يُعبر عن استمرار العيش في تلك المدينة لمدة خمس سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) at that company for long by the time he quits.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he quits'  يُشير إلى وقت مُحدد، و'will not have been working'  يُعبر عن عدم استمرار العمل في تلك الشركة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (wait) for the bus for half an hour by the time it arrives.",
    "options": ["will wait", "will be waiting", "will have been waiting", "have been waiting"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the time it arrives'  يُشير إلى وقت مُحدد، و'will have been waiting'  يُعبر عن استمرار الانتظار لمدة نصف ساعة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) for very long by the time the exam begins.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time the exam begins'  يُشير إلى وقت مُحدد، و'will not have been studying'  يُعبر عن عدم استمرار الدراسة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next month, they ____ (play) in the league for two years.",
    "options": ["will play", "will be playing", "will have been playing", "have been playing"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next month'  يُشير إلى وقت مُحدد، و'will have been playing'  يُعبر عن استمرار اللعب في الدوري لمدة عامين حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/study) English for a year by the time he graduates.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he graduates'  يُشير إلى وقت مُحدد، و'will not have been studying'  يُعبر عن عدم استمرار دراسة اللغة الإنجليزية لمدة عام كامل حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (wait) in line for an hour by the time we get our tickets.",
    "options": ["will wait", "will be waiting", "will have been waiting", "have been waiting"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the time we get our tickets'  يُشير إلى وقت مُحدد، و'will have been waiting'  يُعبر عن استمرار الانتظار في الطابور لمدة ساعة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/work) at this company for very long by the time she finds a new job.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time she finds a new job'  يُشير إلى وقت مُحدد، و'will not have been working'  يُعبر عن عدم استمرار العمل في هذه الشركة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next Friday, they ____ (play) in the league for two years.",
    "options": ["will play", "will be playing", "will have been playing", "have been playing"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next Friday'  يُشير إلى وقت مُحدد، و'will have been playing'  يُعبر عن استمرار اللعب في الدوري لمدة عامين حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/study) for the test for very long by the time it starts.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time it starts'  يُشير إلى وقت مُحدد، و'will not have been studying'  يُعبر عن عدم استمرار الدراسة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this apartment for five years by next year.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next year'  يُشير إلى وقت مُحدد، و'will have been living'  يُعبر عن استمرار العيش في هذه الشقة لمدة خمس سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/wait) at the airport for long by the time her flight is called.",
    "options": ["won't wait", "won't be waiting", "will not have been waiting", "didn't wait"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time her flight is called'  يُشير إلى وقت مُحدد، و'will not have been waiting'  يُعبر عن عدم استمرار الانتظار في المطار لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next spring, they ____ (work) at this company for three years.",
    "options": ["will work", "will be working", "will have been working", "have been working"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next spring'  يُشير إلى وقت مُحدد، و'will have been working'  يُعبر عن استمرار العمل في هذه الشركة لمدة ثلاث سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/teach) at this school for long by the time he moves to a new city.",
    "options": ["won't teach", "won't be teaching", "will not have been teaching", "didn't teach"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he moves to a new city'  يُشير إلى وقت مُحدد، و'will not have been teaching'  يُعبر عن عدم استمرار التدريس في هذه المدرسة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this apartment for a year by the time our lease ends.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the time our lease ends'  يُشير إلى وقت مُحدد، و'will have been living'  يُعبر عن استمرار العيش في هذه الشقة لمدة عام حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) at this university for long by the time she graduates.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time she graduates'  يُشير إلى وقت مُحدد، و'will not have been studying'  يُعبر عن عدم استمرار الدراسة في هذه الجامعة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next summer, they ____ (play) in the orchestra for ten years.",
    "options": ["will play", "will be playing", "will have been playing", "have been playing"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next summer'  يُشير إلى وقت مُحدد، و'will have been playing'  يُعبر عن استمرار العزف في الأوركسترا لمدة عشر سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) at this job for very long by the time he finds a new one.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل. 'By the time he finds a new one'  يُشير إلى وقت مُحدد، و'will not have been working'  يُعبر عن عدم استمرار العمل في هذه الوظيفة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next December, they ____ (study) at this university for four years.",
    "options": ["will study", "will be studying", "will have been studying", "have been studying"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next December'  يُشير إلى وقت مُحدد، و'will have been studying'  يُعبر عن استمرار الدراسة في هذه الجامعة لمدة أربع سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/play) in the band for long by the time they disband.",
    "options": ["won't play", "won't be playing", "will not have been playing", "didn't play"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time they disband'  يُشير إلى وقت مُحدد، و'will not have been playing'  يُعبر عن عدم استمرار العزف في الفرقة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this town for twenty years by our golden anniversary.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل. 'By our golden anniversary'  يُشير إلى وقت مُحدد، و'will have been living'  يُعبر عن استمرار العيش في هذه المدينة لمدة عشرين سنة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/teach) this course for long by the time the semester ends.",
    "options": ["won't teach", "won't be teaching", "will not have been teaching", "didn't teach"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time the semester ends'  يُشير إلى وقت مُحدد، و'will not have been teaching'  يُعبر عن عدم استمرار تدريس هذه الدورة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next month, they ____ (learn) to play the guitar for a year.",
    "options": ["will learn", "will be learning", "will have been learning", "have been learning"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next month'  يُشير إلى وقت مُحدد، و'will have been learning'  يُعبر عن استمرار تعلم العزف على الجيتار لمدة عام حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) at that company for long by the time he gets a promotion.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he gets a promotion'  يُشير إلى وقت مُحدد، و'will not have been working'  يُعبر عن عدم استمرار العمل في تلك الشركة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this city for fifteen years by our next anniversary.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By our next anniversary'  يُشير إلى وقت مُحدد، و'will have been living'  يُعبر عن استمرار العيش في هذه المدينة لمدة خمسة عشر عامًا حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) for long by the time the semester ends.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time the semester ends'  يُشير إلى وقت مُحدد، و'will not have been studying'  يُعبر عن عدم استمرار الدراسة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next year, they ____ (travel) to many countries.",
    "options": ["will travel", "will be traveling", "will have been traveling", "have been traveling"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next year'  يُشير إلى وقت مُحدد، و'will have been traveling'  يُعبر عن استمرار السفر حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/wait) for his friend for long by the time he arrives.",
    "options": ["won't wait", "won't be waiting", "will not have been waiting", "didn't wait"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he arrives'  يُشير إلى وقت مُحدد، و'will not have been waiting'  يُعبر عن عدم استمرار الانتظار لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (work) at this company for ten years by our next anniversary.",
    "options": ["will work", "will be working", "will have been working", "have been working"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By our next anniversary'  يُشير إلى وقت مُحدد، و'will have been working'  يُعبر عن استمرار العمل في هذه الشركة لمدة عشر سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) this subject for a whole year by the time she finishes her degree.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time she finishes her degree'  يُشير إلى وقت مُحدد، و'will not have been studying'  يُعبر عن عدم استمرار دراسة هذا الموضوع لمدة عام كامل حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next year, they ____ (live) in this building for five years.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next year'  يُشير إلى وقت مُحدد، و'will have been living'  يُعبر عن استمرار العيش في هذا المبنى لمدة خمس سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/play) video games for very long by the time his parents come home.",
    "options": ["won't play", "won't be playing", "will not have been playing", "didn't play"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time his parents come home'  يُشير إلى وقت مُحدد، و'will not have been playing'  يُعبر عن عدم استمرار لعب ألعاب الفيديو لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (learn) this language for three years by the end of the year.",
    "options": ["will learn", "will be learning", "will have been learning", "have been learning"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل. 'By the end of the year'  يُشير إلى وقت مُحدد، و'will have been learning'  يُعبر عن استمرار تعلم هذه اللغة لمدة ثلاث سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/teach) at this university for long by the time she retires.",
    "options": ["won't teach", "won't be teaching", "will not have been teaching", "didn't teach"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل. 'By the time she retires'  يُشير إلى وقت مُحدد، و'will not have been teaching'  يُعبر عن عدم استمرار التدريس في هذه الجامعة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next summer, they ____ (travel) to many countries.",
    "options": ["will travel", "will be traveling", "will have been traveling", "have been traveling"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next summer'  يُشير إلى وقت مُحدد، و'will have been traveling'  يُعبر عن استمرار السفر إلى العديد من الدول حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) at that company for a year by the time they close it.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time they close it'  يُشير إلى وقت مُحدد في المستقبل، و'will not have been working'  يُعبر عن عدم استمرار العمل في تلك الشركة لمدة عام كامل حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this house for ten years by next year.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next year'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في هذا المنزل لمدة عشر سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) English for very long by the time the exam begins.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time the exam begins'  يُحدد وقتًا في المستقبل، و'will not have been studying'  يُعبر عن عدم استمرار دراسة اللغة الإنجليزية لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next month, they ____ (play) in the band for five years.",
    "options": ["will play", "will be playing", "will have been playing", "have been playing"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل. 'By next month'  يُحدد وقتًا في المستقبل، و'will have been playing'  يُعبر عن استمرار العزف في الفرقة لمدة خمس سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) at that company for long by the time it closes.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time it closes'  يُحدد وقتًا في المستقبل، و'will not have been working'  يُعبر عن عدم استمرار العمل في تلك الشركة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (learn) this subject for a year by the end of the course.",
    "options": ["will learn", "will be learning", "will have been learning", "have been learning"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the end of the course'  يُحدد وقتًا في المستقبل، و'will have been learning'  يُعبر عن استمرار تعلم هذا الموضوع لمدة عام حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/wait) for him for more than an hour by the time he arrives.",
    "options": ["won't wait", "won't be waiting", "will not have been waiting", "didn't wait"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he arrives'  يُحدد وقتًا في المستقبل، و'will not have been waiting'  يُعبر عن عدم استمرار انتظارها لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nThey ____ (play) video games for hours by the time their parents get home.",
    "options": ["will play", "will be playing", "will have been playing", "have been playing"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the time their parents get home'  يُحدد وقتًا في المستقبل، و'will have been playing'  يُعبر عن استمرار لعب ألعاب الفيديو لساعات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next year, they ____ (live) in this apartment for five years.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next year'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في هذه الشقة لمدة خمس سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/study) for the test for long by the time it begins.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل. 'By the time it begins'  يُحدد وقتًا في المستقبل، و'will not have been studying'  يُعبر عن عدم استمرار الدراسة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next month, they ____ (work) on this project for six months.",
    "options": ["will work", "will be working", "will have been working", "have been working"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل. 'By next month'  يُحدد وقتًا في المستقبل، و'will have been working'  يُعبر عن استمرار العمل على هذا المشروع لمدة ستة أشهر حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/teach) this course for a whole year by the time the semester ends.",
    "options": ["won't teach", "won't be teaching", "will not have been teaching", "didn't teach"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time the semester ends'  يُحدد وقتًا في المستقبل، و'will not have been teaching'  يُعبر عن عدم استمرار تدريس هذه الدورة لمدة عام كامل حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this apartment for a year by the time our lease is up.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the time our lease is up'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في هذه الشقة لمدة عام حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/study) English for a long time by the time he passes the exam.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل. 'By the time he passes the exam'  يُحدد وقتًا في المستقبل، و'will not have been studying'  يُعبر عن عدم استمرار دراسة اللغة الإنجليزية لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next year, they ____ (work) at this company for ten years.",
    "options": ["will work", "will be working", "will have been working", "have been working"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next year'  يُحدد وقتًا في المستقبل، و'will have been working'  يُعبر عن استمرار العمل في هذه الشركة لمدة عشر سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/wait) for her friend for very long by the time he gets here.",
    "options": ["won't wait", "won't be waiting", "will not have been waiting", "didn't wait"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he gets here'  يُحدد وقتًا في المستقبل، و'will not have been waiting'  يُعبر عن عدم استمرار انتظار صديقها لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this neighborhood for fifteen years by our next anniversary.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل. 'By our next anniversary'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في هذا الحي لمدة خمسة عشر عامًا حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/study) at this school for long by the time he graduates.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he graduates'  يُحدد وقتًا في المستقبل، و'will not have been studying'  يُعبر عن عدم استمرار الدراسة في هذه المدرسة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next summer, they ____ (travel) to many different countries.",
    "options": ["will travel", "will be traveling", "will have been traveling", "have been traveling"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next summer'  يُحدد وقتًا في المستقبل، و'will have been traveling'  يُعبر عن استمرار السفر إلى العديد من الدول المختلفة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/work) at that company for long by the time they go bankrupt.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل. 'By the time they go bankrupt'  يُحدد وقتًا في المستقبل، و'will not have been working'  يُعبر عن عدم استمرار العمل في تلك الشركة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this city for twenty years by the time we celebrate our golden wedding anniversary.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By our golden wedding anniversary'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في هذه المدينة لمدة عشرين سنة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/play) football for very long by the time the season finishes.",
    "options": ["won't play", "won't be playing", "will not have been playing", "didn't play"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل. 'By the time the season finishes'  يُحدد وقتًا في المستقبل، و'will not have been playing'  يُعبر عن عدم استمرار لعب كرة القدم لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next spring, they ____ (study) at this university for four years.",
    "options": ["will study", "will be studying", "will have been studying", "have been studying"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next spring'  يُحدد وقتًا في المستقبل، و'will have been studying'  يُعبر عن استمرار الدراسة في هذه الجامعة لمدة أربع سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/teach) English for five years by the time the school closes.",
    "options": ["won't teach", "won't be teaching", "will not have been teaching", "didn't teach"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time the school closes'  يُحدد وقتًا في المستقبل، و'will not have been teaching'  يُعبر عن عدم استمرار تدريس اللغة الإنجليزية لمدة خمس سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (learn) this language for two years by the time we travel to that country.",
    "options": ["will learn", "will be learning", "will have been learning", "have been learning"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the time we travel to that country'  يُحدد وقتًا في المستقبل، و'will have been learning'  يُعبر عن استمرار تعلم هذه اللغة لمدة عامين حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) at this company for a long time by the time they promote him.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time they promote him'  يُحدد وقتًا في المستقبل، و'will not have been working'  يُعبر عن عدم استمرار العمل في هذه الشركة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next December, they ____ (live) in that city for a decade.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next December'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في تلك المدينة لمدة عشر سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) this subject for a whole year by the time the course ends.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time the course ends'  يُحدد وقتًا في المستقبل، و'will not have been studying'  يُعبر عن عدم استمرار دراسة هذا الموضوع لمدة عام كامل حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this house for fifteen years by our silver wedding anniversary.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By our silver wedding anniversary'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في هذا المنزل لمدة خمسة عشر عامًا حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/play) in the band for long by the time they go on their world tour.",
    "options": ["won't play", "won't be playing", "will not have been playing", "didn't play"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time they go on their world tour'  يُحدد وقتًا في المستقبل، و'will not have been playing'  يُعبر عن عدم استمرار العزف في الفرقة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next spring, they ____ (work) at that company for five years.",
    "options": ["will work", "will be working", "will have been working", "have been working"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل. 'By next spring'  يُحدد وقتًا في المستقبل، و'will have been working'  يُعبر عن استمرار العمل في تلك الشركة لمدة خمس سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/teach) English for ten years by the time she retires.",
    "options": ["won't teach", "won't be teaching", "will not have been teaching", "didn't teach"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل. 'By the time she retires'  يُحدد وقتًا في المستقبل، و'will not have been teaching'  يُعبر عن عدم استمرار تدريس اللغة الإنجليزية لمدة عشر سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (learn) this new software for a year by the time the project is due.",
    "options": ["will learn", "will be learning", "will have been learning", "have been learning"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the time the project is due'  يُحدد وقتًا في المستقبل، و'will have been learning'  يُعبر عن استمرار تعلم هذا البرنامج الجديد لمدة عام حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/play) the piano for long by the time the concert starts.",
    "options": ["won't play", "won't be playing", "will not have been playing", "didn't play"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time the concert starts'  يُحدد وقتًا في المستقبل، و'will not have been playing'  يُعبر عن عدم استمرار العزف على البيانو لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next month, they ____ (live) in that city for twenty years.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next month'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في تلك المدينة لمدة عشرين سنة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) medicine for very long by the time she changes her major.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time she changes her major'  يُحدد وقتًا في المستقبل، و'will not have been studying'  يُعبر عن عدم استمرار دراسة الطب لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this country for a decade by the time we move abroad.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل. 'By the time we move abroad'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في هذا البلد لمدة عشر سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) in sales for very long by the time he gets transferred.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he gets transferred'  يُحدد وقتًا في المستقبل، و'will not have been working'  يُعبر عن عدم استمرار العمل في قسم المبيعات لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next year, they ____ (play) professional basketball for five years.",
    "options": ["will play", "will be playing", "will have been playing", "have been playing"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل. 'By next year'  يُحدد وقتًا في المستقبل، و'will have been playing'  يُعبر عن استمرار لعب كرة السلة الاحترافية لمدة خمس سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) at this school for long by the time she wins a scholarship.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل. 'By the time she wins a scholarship'  يُحدد وقتًا في المستقبل، و'will not have been studying'  يُعبر عن عدم استمرار الدراسة في هذه المدرسة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this city for ten years by the time our children graduate from high school.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the time our children graduate from high school'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في هذه المدينة لمدة عشر سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) in this field for long by the time he finds a new career path.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل. 'By the time he finds a new career path'  يُحدد وقتًا في المستقبل، و'will not have been working'  يُعبر عن عدم استمرار العمل في هذا المجال لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next year, they ____ (play) professional soccer for fifteen years.",
    "options": ["will play", "will be playing", "will have been playing", "have been playing"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next year'  يُحدد وقتًا في المستقبل، و'will have been playing'  يُعبر عن استمرار لعب كرة القدم الاحترافية لمدة خمسة عشر عامًا حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) for her doctorate for very long by the time she defends her dissertation.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time she defends her dissertation'  يُحدد وقتًا في المستقبل، و'will not have been studying'  يُعبر عن عدم استمرار دراسة الدكتوراه لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this country for thirty years by the time we retire.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By the time we retire'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في هذا البلد لمدة ثلاثين سنة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nHe ____ (not/work) in this field for very long by the time he changes careers.",
    "options": ["won't work", "won't be working", "will not have been working", "didn't work"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time he changes careers'  يُحدد وقتًا في المستقبل، و'will not have been working'  يُعبر عن عدم استمرار العمل في هذا المجال لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nBy next year, they ____ (play) professional music for a decade.",
    "options": ["will play", "will be playing", "will have been playing", "have been playing"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By next year'  يُحدد وقتًا في المستقبل، و'will have been playing'  يُعبر عن استمرار العزف الموسيقي الاحترافي لمدة عشر سنوات حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nShe ____ (not/study) at that university for long by the time she transfers to another.",
    "options": ["won't study", "won't be studying", "will not have been studying", "didn't study"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous منفي (will not have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ لن يستمرّ حتى وقت محدد في المستقبل.  'By the time she transfers to another'  يُحدد وقتًا في المستقبل، و'will not have been studying'  يُعبر عن عدم استمرار الدراسة في تلك الجامعة لفترة طويلة حتى ذلك الوقت."
  },
  {
    "question": "اختر الإجابة الصحيحة:\nWe ____ (live) in this house for fifteen years by our next family reunion.",
    "options": ["will live", "will be living", "will have been living", "have been living"],
    "correct_option_id": 2,
    "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعل مستمرّ حتى وقت محدد في المستقبل.  'By our next family reunion'  يُحدد وقتًا في المستقبل، و'will have been living'  يُعبر عن استمرار العيش في هذا المنزل لمدة خمسة عشر عامًا حتى ذلك الوقت."
  }
]
        }
    },
    "أجزاء الكلام":{
        "الأسماء": [
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is a noun? ",
        "options": ["quickly", "run", "cat", "happy"],
        "correct_option_id": 2,
        "explanation": "اسم الفاعل هو كلمة تشير إلى شخص أو حيوان أو مكان أو شيء أو فكرة.  'cat' هو اسم فاعل لأنّه يشير إلى حيوان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the noun in this sentence: The bird sings beautifully.",
        "options": ["sings", "beautifully", "bird", "The"],
        "correct_option_id": 2,
        "explanation": "اسم الفاعل في الجملة هو 'bird'  لأنه يشير إلى الشيء الذي يُغني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these is a proper noun?",
        "options": ["city", "country", "London", "river"],
        "correct_option_id": 2,
        "explanation": "الأسماء الصحيحة هي أسماء خاصة تبدأ بحرف كبير.  'London' اسم صحيح لأنّه اسم مدينة محددة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of noun is 'team'?",
        "options": ["concrete noun", "abstract noun", "collective noun", "proper noun"],
        "correct_option_id": 2,
        "explanation": "اسم الفريق (team)  هو اسم جمعيّ،  لأنه يشير إلى مجموعة من الأفراد يعملون معًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'happiness' a concrete or abstract noun?",
        "options": ["concrete noun", "abstract noun", "collective noun", "common noun"],
        "correct_option_id": 1,
        "explanation": "السعادة (happiness) هي فكرة مجردة، لذا فهي اسم مجرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the concrete noun:  The sweet smell of roses filled the air.",
        "options": ["smell", "sweet", "roses", "air"],
        "correct_option_id": 2,
        "explanation": "الورود (roses) اسم ملموس (شيء مادي يمكن رؤيته أو لمسه)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich is an abstract noun: courage, table, tree, book",
        "options": ["table", "tree", "courage", "book"],
        "correct_option_id": 2,
        "explanation": "الشجاعة (courage)  اسم مجرد،  فهي فكرة أو مفهوم وليس شيئًا ماديًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nGive the plural of 'child'.",
        "options": ["childs", "children", "childes", "childer"],
        "correct_option_id": 1,
        "explanation": "صيغة الجمع لكلمة child هي children."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'box'?",
        "options": ["boxs", "boxen", "boxes", "box"],
        "correct_option_id": 2,
        "explanation": "صيغة جمع box هي boxes. نضيف حرف s."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the singular of 'teeth'?",
        "options": ["tooth", "teeth", "tooths", "teet"],
        "correct_option_id": 0,
        "explanation": "مفرد teeth هو tooth."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the collective noun:  The flock of sheep grazed peacefully.",
        "options": ["flock", "sheep", "grazed", "peacefully"],
        "correct_option_id": 0,
        "explanation": "اسم الجمع (flock)  يشير إلى مجموعة من الأغنام."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is a common noun?",
        "options": ["Egypt", "River Nile", "country", "London"],
        "correct_option_id": 2,
        "explanation": "الأسماء الشائعة هي أسماء عامة ولا تبدأ بحرف كبير."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive form of 'cat'?",
        "options": ["cats", "cat's", "cats'", "catss"],
        "correct_option_id": 1,
        "explanation": "صيغة الملكية لـ cat هي cat's (قطة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive form of 'girls'?",
        "options": ["girls'", "girls's", "girl's", "girls"],
        "correct_option_id": 0,
        "explanation": "صيغة الملكية لـ girls هي girls' (للفتيات)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nFind the uncountable noun: water, book, chair, pen",
        "options": ["book", "water", "chair", "pen"],
        "correct_option_id": 1,
        "explanation": "الماء (water) اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is NOT a noun:  beauty, kindness, quickly, happiness",
        "options": ["beauty", "kindness", "happiness", "quickly"],
        "correct_option_id": 3,
        "explanation": "quickly ظرف وليس اسمًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct plural form of 'man'.",
        "options": ["mans", "men", "man's", "men's"],
        "correct_option_id": 1,
        "explanation": "جمع man هو men."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct plural form of 'woman'.",
        "options": ["womans", "women", "womans'", "womens"],
        "correct_option_id": 1,
        "explanation": "جمع woman هو women."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the singular of 'mice'?",
        "options": ["mouses", "mouse", "mice", "mices"],
        "correct_option_id": 1,
        "explanation": "مفرد mice هو mouse."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of noun is 'furniture'?",
        "options": ["countable noun", "uncountable noun", "proper noun", "collective noun"],
        "correct_option_id": 1,
        "explanation": "الأثاث (furniture) اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the abstract noun: love, car, tree, house",
        "options": ["car", "love", "tree", "house"],
        "correct_option_id": 1,
        "explanation": "الحب (love) اسم مجرد (فكرة أو مفهوم)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive form of 'children'?",
        "options": ["childrens'", "childrens", "children's", "child's"],
        "correct_option_id": 2,
        "explanation": "صيغة الملكية لـ children هي children's (للأطفال)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'information' a countable or uncountable noun?",
        "options": ["countable", "uncountable", "proper", "collective"],
        "correct_option_id": 1,
        "explanation": "المعلومات (information) اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich is a proper noun:  river, london, country, city",
        "options": ["river", "london", "country", "city"],
        "correct_option_id": 1,
        "explanation": "London اسم علم (اسم خاص)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'sheep'?",
        "options": ["sheeps", "sheep", "shepes", "sheapos"],
        "correct_option_id": 1,
        "explanation": "جمع sheep هو sheep (كلمة sheep  مفردها وجمعها متشابه)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'loaf'?",
        "options": ["loafs", "loaves", "loafes", "loafs"],
        "correct_option_id": 1,
        "explanation": "جمع loaf هو loaves."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the singular of 'geese'?",
        "options": ["goose", "geese", "gooses", "geeses"],
        "correct_option_id": 0,
        "explanation": "مفرد geese هو goose."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the collective noun: team, player, game, score",
        "options": ["player", "game", "score", "team"],
        "correct_option_id": 3,
        "explanation": "team اسم جمعيّ (يشير إلى مجموعة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive form of 'man'?",
        "options": ["man's", "mans'", "mans", "mens"],
        "correct_option_id": 0,
        "explanation": "صيغة الملكية لـ man هي man's (الرجل)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'tomato'?",
        "options": ["tomatos", "tomatoes", "tomato'", "tomatoe"],
        "correct_option_id": 1,
        "explanation": "جمع tomato هو tomatoes."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'potato'?",
        "options": ["potatos", "potatoes", "potato'", "potatos"],
        "correct_option_id": 1,
        "explanation": "جمع potato هو potatoes."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'foot'?",
        "options": ["foots", "feet", "foot's", "footes"],
        "correct_option_id": 1,
        "explanation": "جمع foot هو feet."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'tooth'?",
        "options": ["tooths", "teeth", "tooth's", "toothes"],
        "correct_option_id": 1,
        "explanation": "جمع tooth هو teeth."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'goose'?",
        "options": ["gooses", "geese", "goose's", "gooses'"],
        "correct_option_id": 1,
        "explanation": "جمع goose هو geese."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'mouse'?",
        "options": ["mouses", "mices", "mouse's", "mouses'"],
        "correct_option_id": 1,
        "explanation": "جمع mouse هو mice."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'life'?",
        "options": ["lifes", "lives", "life's", "lifes'"],
        "correct_option_id": 1,
        "explanation": "جمع life هو lives."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'knife'?",
        "options": ["knives", "knifes", "knife's", "knivess"],
        "correct_option_id": 0,
        "explanation": "جمع knife هو knives."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'shelf'?",
        "options": ["shelfs", "shelfes", "shelvies", "shelves"],
        "correct_option_id": 3,
        "explanation": "جمع shelf هو shelves."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'wolf'?",
        "options": ["wolfs", "wolves", "wolfs'", "wolfes"],
        "correct_option_id": 1,
        "explanation": "جمع wolf هو wolves."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'half'?",
        "options": ["halfs", "halfs'", "halves", "halve"],
        "correct_option_id": 2,
        "explanation": "جمع half هو halves."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'self'?",
        "options": ["selfs", "selves", "selfes", "selffs"],
        "correct_option_id": 1,
        "explanation": "جمع self هو selves."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the proper noun:  london, city, country, river",
        "options": ["city", "country", "river", "london"],
        "correct_option_id": 3,
        "explanation": "London اسم علم (اسم خاص)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive form of 'country'?",
        "options": ["countrys", "country's", "countries", "countrys'"],
        "correct_option_id": 1,
        "explanation": "صيغة الملكية لـ country هي country's."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive form of 'cities'?",
        "options": ["citys'", "cities'", "cities's", "citys"],
        "correct_option_id": 1,
        "explanation": "صيغة الملكية لـ cities هي cities'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'music' a countable or uncountable noun?",
        "options": ["countable", "uncountable", "proper", "collective"],
        "correct_option_id": 1,
        "explanation": "الموسيقى (music) اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat kind of noun is 'flock'?",
        "options": ["common noun", "collective noun", "proper noun", "abstract noun"],
        "correct_option_id": 1,
        "explanation": "Flock اسم جمعيّ (يشير إلى مجموعة من الأغنام أو الطيور)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'cactus'?",
        "options": ["cactuses", "cacti", "cactus'", "cactus"],
        "correct_option_id": 1,
        "explanation": "جمع cactus هو cacti."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'analysis'?",
        "options": ["analyses", "analysis'", "analises", "analysiss"],
        "correct_option_id": 0,
        "explanation": "جمع analysis هو analyses."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'axis'?",
        "options": ["axises", "axii", "axes", "axis'"],
        "correct_option_id": 2,
        "explanation": "جمع axis هو axes."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'basis'?",
        "options": ["bases", "basises", "basis'", "basiss"],
        "correct_option_id": 0,
        "explanation": "جمع basis هو bases."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'crisis'?",
        "options": ["crisises", "crises", "crisis'", "crisiss"],
        "correct_option_id": 1,
        "explanation": "جمع crisis هو crises."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'criterion'?",
        "options": ["criterions", "criteria", "criterion'", "criterions'"],
        "correct_option_id": 1,
        "explanation": "جمع criterion هو criteria."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'phenomenon'?",
        "options": ["phenomenons", "phenomena", "phenomenon'", "phenomenons'"],
        "correct_option_id": 1,
        "explanation": "جمع phenomenon هو phenomena."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'datum'?",
        "options": ["datums", "data", "datum'", "datums'"],
        "correct_option_id": 1,
        "explanation": "جمع datum هو data."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'medium'?",
        "options": ["mediums", "media", "medium'", "mediums'"],
        "correct_option_id": 1,
        "explanation": "جمع medium هو media."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'radius'?",
        "options": ["radiuses", "radii", "radius'", "radiuss"],
        "correct_option_id": 1,
        "explanation": "جمع radius هو radii."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the plural of 'syllabus'?",
        "options": ["syllabuses", "syllabuss", "syllabus'", "syllabuss'"],
        "correct_option_id": 0,
        "explanation": "جمع syllabus هو syllabuses."
    }
],
        
        "الأفعال" : [
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the verb in the sentence: 'The birds sang sweetly in the morning'.",
        "options": ["birds", "sweetly", "sang", "morning"],
        "correct_option_id": 2,
        "explanation": "الفعل في الجملة هو 'sang'  لأنه يُعبّر عن الفعل الذي قامت به الطيور (الغناء)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past tense of the verb 'to run'?",
        "options": ["runs", "running", "ran", "run"],
        "correct_option_id": 2,
        "explanation": "الماضي البسيط لفعل 'to run' هو 'ran'.  نستخدم الماضي البسيط للتعبير عن حدث انتهى في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these is the present participle of 'to swim'?",
        "options": ["swam", "swims", "swimming", "swim"],
        "correct_option_id": 2,
        "explanation": "المضارع المستمر (present participle) يُشكّل بإضافة '-ing' إلى الفعل الأساسي.  لذا، فإنّ present participle لـ 'to swim' هو 'swimming'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct past tense form of 'to eat'.",
        "options": ["eats", "ate", "eating", "eat"],
        "correct_option_id": 1,
        "explanation": "الماضي البسيط لفعل 'to eat' هو 'ate'.  'Ate'  تُشير إلى فعل تناول الطعام في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence correctly: 'Yesterday, I ______ to the park'.",
        "options": ["go", "goes", "went", "going"],
        "correct_option_id": 2,
        "explanation": "نستخدم الماضي البسيط لفعل 'to go' (went)  لأن الجملة تتحدث عن حدثٍ وقع في الماضي (أمس)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past participle of the verb 'to see'?",
        "options": ["sees", "seeing", "seen", "saw"],
        "correct_option_id": 2,
        "explanation": "الماضي المشارك (past participle) لفعل 'to see' هو 'seen'.  يُستخدم past participle في الأزمنة المركبة مثل present perfect و past perfect."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct sentence:  'He ____ a new car last week'.",
        "options": ["buy", "buys", "bought", "buying"],
        "correct_option_id": 2,
        "explanation": "الماضي البسيط لفعل 'to buy' هو 'bought'.  'bought'  تُشير إلى فعل الشراء الذي تمّ في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these is the correct present tense form of the verb 'to be' for the pronoun 'I'?",
        "options": ["is", "am", "are", "was"],
        "correct_option_id": 1,
        "explanation": "المضارع البسيط لفعل 'to be' مع ضمير 'I' هو 'am'. 'Am'  تُشير إلى حالة وجود أو كون."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct future tense form: 'I ____ study tomorrow'.",
        "options": ["will", "am", "will be", "going to"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'will' للتعبير عن المستقبل البسيط. 'will study'  تُشير إلى فعلٍ سيحدث في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the irregular verb:  walk, run, eat, sing",
        "options": ["walk", "run", "eat", "sing"],
        "correct_option_id": 2,
        "explanation": "فعل 'eat' فعل غير منتظم (irregular verb)  لأنه لا يتبع نمطًا منتظمًا في تكوين الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past tense of 'to make'?",
        "options": ["makes", "made", "making", "make"],
        "correct_option_id": 1,
        "explanation": "الماضي البسيط لفعل 'to make' هو 'made'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct past participle of 'to write'.",
        "options": ["writes", "written", "writing", "wrote"],
        "correct_option_id": 1,
        "explanation": "الماضي المشارك (past participle) لفعل 'to write' هو 'written'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nForm the present perfect tense: I ____ (finish) my work.",
        "options": ["finish", "finished", "have finished", "am finishing"],
        "correct_option_id": 2,
        "explanation": "Present Perfect (have/has + past participle) يُستخدم للتعبير عن حدثٍ انتهى في الماضي، وله تأثير على الحاضر.  'have finished' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past perfect tense of 'to go'?",
        "options": ["goes", "went", "had gone", "going"],
        "correct_option_id": 2,
        "explanation": "Past Perfect (had + past participle) يُستخدم للتعبير عن فعلٍ انتهى قبل فعلٍ آخر في الماضي.  'had gone' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct future continuous tense: 'They ____ (play) at 3 PM'.",
        "options": ["will play", "will be playing", "will have played", "play"],
        "correct_option_id": 1,
        "explanation": "Future Continuous (will be + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في وقت مُحدد في المستقبل. 'will be playing' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the future perfect tense of 'to arrive'?",
        "options": ["arrives", "arrived", "will arrive", "will have arrived"],
        "correct_option_id": 3,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعلٍ سيُكتمل قبل وقت مُحدد في المستقبل.  'will have arrived' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct present perfect continuous tense:  'They ____ (work) for three hours'.",
        "options": ["work", "worked", "have been working", "are working"],
        "correct_option_id": 2,
        "explanation": "Present Perfect Continuous (have/has been + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ بدأ في الماضي ولا يزال مستمرًا حتى الآن.  'have been working' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past perfect continuous tense of 'to study'?",
        "options": ["studies", "studied", "had been studying", "was studying"],
        "correct_option_id": 2,
        "explanation": "Past Perfect Continuous (had been + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ كان مستمرًا قبل وقت مُحدد في الماضي. 'had been studying' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence correctly: 'By next year, she ____ (live) here for 5 years'.",
        "options": ["will live", "will be living", "will have been living", "lives"],
        "correct_option_id": 2,
        "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعلٍ مستمرّ حتى وقت مُحدد في المستقبل. 'will have been living' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the future perfect continuous tense of 'to wait'?",
        "options": ["waits", "waited", "will have been waiting", "will be waiting"],
        "correct_option_id": 2,
        "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعلٍ مستمرّ حتى وقت مُحدد في المستقبل. 'will have been waiting' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the auxiliary verb in the sentence: 'He has been playing football'.",
        "options": ["He", "has", "been", "playing"],
        "correct_option_id": 1,
        "explanation": "الفعِل المساعد (auxiliary verb)  هو الفعل الذي يُستخدم مع الفعل الرئيسي لتكوين زمن معين.  في هذه الجملة، 'has' هو الفعل المساعد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the base form of the verb 'ran'?",
        "options": ["run", "running", "runs", "ran"],
        "correct_option_id": 0,
        "explanation": "هو الشكل الأساسي للفعل قبل إضافة أيّة علامات زمنية.  'ran' هو الماضي البسيط لـ 'run'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the infinitive form of the verb 'to sing'?",
        "options": ["sing", "sings", "sang", "singing"],
        "correct_option_id": 0,
        "explanation": "Infinitive form  هو الشكل الأساسي للفعل،  عادةً ما يسبقه 'to'.  'to sing' هو الصيغة الكاملة، و 'sing' هو الصيغة بدون to."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct sentence:  'She ____ a letter yesterday'.",
        "options": ["write", "writes", "wrote", "writing"],
        "correct_option_id": 2,
        "explanation": "استخدمنا الماضي البسيط (wrote) لأنّ الجملة تتحدث عن حدثٍ انتهى في الماضي (أمس)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nForm a sentence using the past perfect continuous tense: I ______ (study) for hours.",
        "options": ["study", "had studied", "had been studying", "was studying"],
        "correct_option_id": 2,
        "explanation": "Past Perfect Continuous (had been + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ انتهى قبل حدثٍ آخر في الماضي.  'had been studying' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  'By next year, we _____ (live) here for ten years'.",
        "options": ["will live", "will be living", "will have been living", "live"],
        "correct_option_id": 2,
        "explanation": "Future Perfect Continuous (will have been + present participle)  يُستخدم للتعبير عن مدة فعلٍ مستمرّ حتى وقت مُحدد في المستقبل.  'will have been living' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past continuous tense of 'to work'?",
        "options": ["works", "working", "worked", "was working"],
        "correct_option_id": 3,
        "explanation": "Past Continuous (was/were + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في الماضي.  'was working' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct present perfect tense:  'They ____ (go) to the market'.",
        "options": ["go", "went", "have gone", "going"],
        "correct_option_id": 2,
        "explanation": "Present Perfect (have/has + past participle) يُستخدم للتعبير عن حدثٍ انتهى في الماضي، وله تأثير على الحاضر.  'have gone'  هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the future simple tense of 'to arrive'?",
        "options": ["arrives", "arrived", "will arrive", "arriving"],
        "correct_option_id": 2,
        "explanation": "Future Simple (will + base verb) يُستخدم للتعبير عن فعلٍ سيحدث في المستقبل.  'will arrive'  هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of verb is 'to be'?",
        "options": ["action verb", "linking verb", "auxiliary verb", "All of the above"],
        "correct_option_id": 3,
        "explanation": "فعل 'to be'  هو فعل مساعد (auxiliary verb) وفعل ربط (linking verb) وله استخدامات كثيرة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence using the correct verb form: 'The children ____ happily in the playground'.",
        "options": ["play", "played", "plays", "are playing"],
        "correct_option_id": 3,
        "explanation": "Present Continuous tense (is/are + present participle) يصف حدثًا مستمرًا في الوقت الحالي.  'are playing' هي الصيغة الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past simple tense of 'to eat'?",
        "options": ["eats", "ate", "eating", "eat"],
        "correct_option_id": 1,
        "explanation": "الماضي البسيط لفعل 'to eat' هو 'ate'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct verb form: 'I ____ to the store yesterday'.",
        "options": ["go", "went", "going", "goes"],
        "correct_option_id": 1,
        "explanation": "نستخدم الماضي البسيط (went) للتعبير عن حدثٍ انتهى في الماضي (أمس)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the present perfect continuous tense of 'to study'?",
        "options": ["studies", "studied", "have been studying", "is studying"],
        "correct_option_id": 2,
        "explanation": "Present Perfect Continuous (have/has been + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ بدأ في الماضي ولا يزال مستمرًا حتى الآن."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nForm a sentence using the past perfect tense: They ____ (leave) before I arrived.",
        "options": ["leave", "left", "had left", "were leaving"],
        "correct_option_id": 2,
        "explanation": "Past Perfect (had + past participle) يُستخدم للتعبير عن فعلٍ انتهى قبل فعلٍ آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'By next year, she ____ (finish) university'.",
        "options": ["will finish", "will be finishing", "will have finished", "finishes"],
        "correct_option_id": 2,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعلٍ سيُكتمل قبل وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the future continuous tense of 'to work'?",
        "options": ["works", "working", "will be working", "will work"],
        "correct_option_id": 2,
        "explanation": "Future Continuous (will be + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct verb form to complete the sentence: 'They ____ (play) football tomorrow'.",
        "options": ["play", "played", "will play", "are playing"],
        "correct_option_id": 2,
        "explanation": "Future Simple (will + base verb)  يُستخدم للتعبير عن فعلٍ سيحدث في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past perfect continuous tense of 'to wait'?",
        "options": ["waits", "waited", "had been waiting", "was waiting"],
        "correct_option_id": 2,
        "explanation": "Past Perfect Continuous (had been + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ كان مستمرًا قبل وقت مُحدد في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct verb form for the sentence: 'I ____ (eat) dinner when the phone rang'.",
        "options": ["eat", "ate", "was eating", "am eating"],
        "correct_option_id": 2,
        "explanation": "Past Continuous (was/were + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في الماضي، والذي قُطِع بفعلٍ آخر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the base form of the verb 'sang'?",
        "options": ["sing", "sings", "singing", "sang"],
        "correct_option_id": 0,
        "explanation": "هو الشكل الأساسي للفعل قبل إضافة أيّة علامات زمنية.  'sang' هو الماضي البسيط لـ 'sing'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the infinitive form of the verb 'to walk'?",
        "options": ["walk", "walks", "walked", "walking"],
        "correct_option_id": 0,
        "explanation": "Infinitive form  هو الشكل الأساسي للفعل، عادةً ما يسبقه 'to'. 'to walk' هو الصيغة الكاملة، و 'walk' هو الصيغة بدون to."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct verb tense: 'They ____ (go) to the market yesterday'.",
        "options": ["go", "goes", "went", "going"],
        "correct_option_id": 2,
        "explanation": "استخدمنا الماضي البسيط (went) للتعبير عن حدثٍ انتهى في الماضي (أمس)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the present perfect tense of 'to study'?",
        "options": ["studies", "studied", "have studied", "is studying"],
        "correct_option_id": 2,
        "explanation": "Present Perfect (have/has + past participle) يُستخدم للتعبير عن حدثٍ انتهى في الماضي، وله تأثير على الحاضر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nForm a sentence using the past continuous tense: She ____ (read) a book.",
        "options": ["read", "reads", "was reading", "is reading"],
        "correct_option_id": 2,
        "explanation": "Past Continuous (was/were + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'They ____ (finish) their project by Friday'.",
        "options": ["will finish", "will be finishing", "will have finished", "finish"],
        "correct_option_id": 2,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعلٍ سيُكتمل قبل وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the future simple tense of 'to work'?",
        "options": ["works", "working", "will work", "is working"],
        "correct_option_id": 2,
        "explanation": "Future Simple (will + base verb) يُستخدم للتعبير عن فعلٍ سيحدث في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct verb form: 'He ____ (study) for the test all day'.",
        "options": ["studies", "studied", "has been studying", "is studying"],
        "correct_option_id": 2,
        "explanation": "Present Perfect Continuous (have/has been + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ بدأ في الماضي ولا يزال مستمرًا حتى الآن."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past simple tense of 'to make'?",
        "options": ["makes", "made", "making", "make"],
        "correct_option_id": 1,
        "explanation": "الماضي البسيط لفعل 'to make' هو 'made'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct past participle of 'to eat'.",
        "options": ["eats", "ate", "eating", "eaten"],
        "correct_option_id": 3,
        "explanation": "الماضي المشارك (past participle) لفعل 'to eat' هو 'eaten'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nForm a sentence using the present perfect continuous tense: She ____ (wait) for an hour.",
        "options": ["waits", "waited", "has been waiting", "is waiting"],
        "correct_option_id": 2,
        "explanation": "Present Perfect Continuous (have/has been + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ بدأ في الماضي ولا يزال مستمرًا حتى الآن."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'By next week, they ____ (finish) their project'.",
        "options": ["will finish", "will be finishing", "will have finished", "finish"],
        "correct_option_id": 2,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعلٍ سيُكتمل قبل وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the future continuous tense of 'to go'?",
        "options": ["goes", "going", "will be going", "will go"],
        "correct_option_id": 2,
        "explanation": "Future Continuous (will be + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct verb form to complete the sentence: 'He ____ (study) all day yesterday'.",
        "options": ["studies", "studied", "was studying", "has been studying"],
        "correct_option_id": 2,
        "explanation": "Past Continuous (was/were + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past perfect tense of 'to write'?",
        "options": ["writes", "wrote", "written", "had written"],
        "correct_option_id": 3,
        "explanation": "Past Perfect (had + past participle) يُستخدم للتعبير عن فعلٍ انتهى قبل فعلٍ آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct past participle of 'to bring'.",
        "options": ["brings", "bringing", "brought", "bring"],
        "correct_option_id": 2,
        "explanation": "الماضي المشارك (past participle) لفعل 'to bring' هو 'brought'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nForm a sentence using the future perfect continuous tense:  I ____ (work) for five years.",
        "options": ["will work", "will be working", "will have been working", "work"],
        "correct_option_id": 2,
        "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعلٍ مستمرّ حتى وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence using the correct tense: 'By tomorrow, she ____ (finish) her work'.",
        "options": ["will finish", "will be finishing", "will have finished", "finishes"],
        "correct_option_id": 2,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعلٍ سيُكتمل قبل وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past continuous tense of 'to go'?",
        "options": ["goes", "going", "went", "was going"],
        "correct_option_id": 3,
        "explanation": "Past Continuous (was/were + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct verb form to complete the sentence: 'He ____ (play) the guitar when I called'.",
        "options": ["plays", "played", "was playing", "will play"],
        "correct_option_id": 2,
        "explanation": "Past Continuous (was/were + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في الماضي، والذي قُطِع بفعلٍ آخر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past perfect tense of 'to sing'?",
        "options": ["sings", "sang", "singing", "had sung"],
        "correct_option_id": 3,
        "explanation": "Past Perfect (had + past participle) يُستخدم للتعبير عن فعلٍ انتهى قبل فعلٍ آخر في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct past participle of 'to run'.",
        "options": ["runs", "running", "ran", "run"],
        "correct_option_id": 3,
        "explanation": "الماضي المشارك (past participle) لفعل 'to run' هو 'run'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nForm a sentence using the future perfect continuous tense: They ____ (wait) for three hours.",
        "options": ["will wait", "will be waiting", "will have been waiting", "wait"],
        "correct_option_id": 2,
        "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعلٍ مستمرّ حتى وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'By next Friday, we ____ (finish) the report'.",
        "options": ["will finish", "will be finishing", "will have finished", "finish"],
        "correct_option_id": 2,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعلٍ سيُكتمل قبل وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past continuous tense of 'to be'?",
        "options": ["is", "am", "are", "was/were"],
        "correct_option_id": 3,
        "explanation": "Past Continuous (was/were + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct verb form: 'She ____ (go) to the market yesterday'.",
        "options": ["goes", "go", "went", "going"],
        "correct_option_id": 2,
        "explanation": "استخدمنا الماضي البسيط (went) للتعبير عن حدثٍ انتهى في الماضي (أمس)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the present perfect tense of 'to make'?",
        "options": ["makes", "made", "making", "have made"],
        "correct_option_id": 3,
        "explanation": "Present Perfect (have/has + past participle) يُستخدم للتعبير عن حدثٍ انتهى في الماضي، وله تأثير على الحاضر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nForm a sentence using the past continuous tense: The cat ____ (sleep) on the mat.",
        "options": ["sleeps", "slept", "was sleeping", "is sleeping"],
        "correct_option_id": 2,
        "explanation": "Past Continuous (was/were + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'By next month, they ____ (complete) the project'.",
        "options": ["will complete", "will be completing", "will have completed", "complete"],
        "correct_option_id": 2,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعلٍ سيُكتمل قبل وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the future continuous tense of 'to read'?",
        "options": ["reads", "reading", "will be reading", "will read"],
        "correct_option_id": 2,
        "explanation": "Future Continuous (will be + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct verb form: 'We ____ (travel) to France next year'.",
        "options": ["travel", "traveled", "will travel", "are traveling"],
        "correct_option_id": 2,
        "explanation": "Future Simple (will + base verb) يُستخدم للتعبير عن فعلٍ سيحدث في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past perfect continuous tense of 'to play'?",
        "options": ["plays", "played", "had been playing", "is playing"],
        "correct_option_id": 2,
        "explanation": "Past Perfect Continuous (had been + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ كان مستمرًا قبل وقت مُحدد في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct past participle of 'to go'.",
        "options": ["goes", "going", "went", "gone"],
        "correct_option_id": 3,
        "explanation": "الماضي المشارك (past participle) لفعل 'to go' هو 'gone'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nForm a sentence using the future perfect continuous tense:  She ____ (work) on this project for six months.",
        "options": ["will work", "will be working", "will have been working", "work"],
        "correct_option_id": 2,
        "explanation": "Future Perfect Continuous (will have been + present participle) يُستخدم للتعبير عن مدة فعلٍ مستمرّ حتى وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'By next spring, he ____ (finish) his studies'.",
        "options": ["will finish", "will be finishing", "will have finished", "finishes"],
        "correct_option_id": 2,
        "explanation": "Future Perfect (will have + past participle) يُستخدم للتعبير عن فعلٍ سيُكتمل قبل وقت مُحدد في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the past continuous tense of 'to sing'?",
        "options": ["sings", "singing", "sang", "was singing"],
        "correct_option_id": 3,
        "explanation": "Past Continuous (was/were + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct verb form: 'The sun ____ (shine) brightly yesterday'.",
        "options": ["shines", "shone", "was shining", "has shone"],
        "correct_option_id": 2,
        "explanation": "Past Continuous (was/were + present participle) يُستخدم للتعبير عن فعلٍ مستمرّ في الماضي."
    }
],
        "الصفات" : [
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is an adjective?",
        "options": ["quickly", "run", "big", "happy"],
        "correct_option_id": 2,
        "explanation": "الصفة (adjective) هي كلمة تصف اسمًا (noun) أو ضميرًا (pronoun).  في الخيارات المعروضة،  'quickly' ظرف، و'run' فعل، و'happy' صفة، و'big' صفة.  كلمة 'big'  صفة لأنها تصف حجم الشيء، بينما الكلمات الأخرى لا تصف أسماء.  تُستخدم الصفات لإضافة معلومات إضافية عن الأسماء، وتحديد خصائصها أو مواصفاتها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the adjective in the sentence: 'The red car is fast'.",
        "options": ["car", "fast", "red", "is"],
        "correct_option_id": 2,
        "explanation": "تُعدّ الكلمة 'red' صفةً (adjective) لأنها تصف لون السيارة (car).  الصفات تُضيف معلومات إضافية عن الأسماء التي تصفها، وتُحدد خصائصها أو مواصفاتها.  'fast' أيضًا صفة، لكن السؤال يطلب صفة واحدة فقط، و'red'  صفة لونية تصف لون السيارة بشكل مباشر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes size?",
        "options": ["happy", "small", "beautiful", "loud"],
        "correct_option_id": 1,
        "explanation": "الصفة 'small' تعني صغير، وهي صفة تصف الحجم أو المقاس.  تُستخدم الصفات لتحديد خصائص الأشياء،  و'small' تُحدد حجم الشيء على أنه صغير، على عكس الصفات الأخرى التي تصف مشاعر أو أصوات أو جمال.  هناك العديد من الصفات التي تصف الحجم، مثل: large, huge, tiny, gigantic إلخ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes color?",
        "options": ["happy", "big", "blue", "loud"],
        "correct_option_id": 2,
        "explanation": "صفة اللون (color adjective) تصف لون الشيء. 'blue'  صفة لون لأنها تُشير إلى اللون الأزرق.  تُستخدم الصفات اللونية لتحديد خاصية اللون في الأسماء، بينما الكلمات الأخرى تصف حجمًا أو صوتًا أو شعورًا.  تتضمن أمثلة أخرى لصفات الألوان: red, green, yellow, black, white، إلخ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes a feeling?",
        "options": ["happy", "big", "blue", "loud"],
        "correct_option_id": 0,
        "explanation": "صفة المشاعر (adjective of emotion) تصف حالة الشعور أو الانفعال.  'happy'  صفة تُعبّر عن الشعور بالسعادة.  تُستخدم صفات المشاعر لتحديد الحالة الانفعالية للأشخاص أو الحيوانات،  مثل: sad, angry, excited, tired، إلخ.  بينما الكلمات الأخرى تصف حجمًا أو لونًا أو صوتًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes sound?",
        "options": ["happy", "big", "blue", "loud"],
        "correct_option_id": 3,
        "explanation": "صفة الصوت (adjective of sound) تصف خصائص الصوت.  'loud'  صفة تُعبّر عن الصوت العالي.  تُستخدم صفات الصوت لتحديد مدى ارتفاع أو انخفاض الصوت أو شدته،  مثل: quiet, noisy, soft، إلخ.  بينما الكلمات الأخرى تصف حجمًا أو لونًا أو شعورًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes shape?",
        "options": ["round", "happy", "big", "blue"],
        "correct_option_id": 0,
        "explanation": "صفة الشكل (adjective of shape) تصف شكل الشيء الهندسي أو الخارجي. 'round'  صفة تُعبّر عن الشكل الدائري.  تُستخدم صفات الشكل لتحديد شكل الأشياء، مثل: square, rectangular, triangular، إلخ.  بينما الكلمات الأخرى تصف حجمًا أو شعورًا أو لونًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes age?",
        "options": ["old", "big", "happy", "red"],
        "correct_option_id": 0,
        "explanation": "صفة العمر (adjective of age) تصف عمر الشخص أو الشيء. 'old'  صفة تُعبّر عن الكبر في السن.  تُستخدم صفات العمر لتحديد عمر الأشخاص أو الأشياء،  مثل: young, new, ancient، إلخ.  بينما الكلمات الأخرى تصف حجمًا أو شعورًا أو لونًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes temperature?",
        "options": ["hot", "big", "happy", "red"],
        "correct_option_id": 0,
        "explanation": "صفة الحرارة (adjective of temperature) تصف درجة حرارة الشيء.  'hot'  صفة تُعبّر عن درجة حرارة عالية. تُستخدم صفات الحرارة لتحديد مدى سخونة أو برودة الشيء، مثل: cold, warm, freezing، إلخ.  بينما الكلمات الأخرى تصف حجمًا أو شعورًا أو لونًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes texture?",
        "options": ["smooth", "big", "happy", "red"],
        "correct_option_id": 0,
        "explanation": "صفة الملمس (adjective of texture) تصف  كيف يبدو سطح الشيء عند لمسه. 'smooth'  صفة تُعبّر عن سطح أملس. تُستخدم صفات الملمس لوصف  كيف يبدو سطح الشيء عند لمسه، مثل: rough, soft, hard، إلخ.  بينما الكلمات الأخرى تصف حجمًا أو شعورًا أو لونًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes taste?",
        "options": ["sweet", "big", "happy", "red"],
        "correct_option_id": 0,
        "explanation": "صفة الطعم (adjective of taste) تصف طعم الشيء.  'sweet'  صفة تُعبّر عن الطعم الحلو. تُستخدم صفات الطعم لوصف نكهة الطعام أو الشراب، مثل: sour, bitter, salty، إلخ.  بينما الكلمات الأخرى تصف حجمًا أو شعورًا أو لونًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes smell?",
        "options": ["fragrant", "big", "happy", "red"],
        "correct_option_id": 0,
        "explanation": "صفة الرائحة (adjective of smell) تصف رائحة الشيء.  'fragrant'  صفة تُعبّر عن رائحة عطرة. تُستخدم صفات الرائحة لوصف  رائحة الأشياء، مثل:  musty, pungent,  floral، إلخ.  بينما الكلمات الأخرى تصف حجمًا أو شعورًا أو لونًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'The ______ cat sat on the mat'.",
        "options": ["quickly", "black", "run", "happy"],
        "correct_option_id": 1,
        "explanation": "كلمة 'black' صفة (adjective) لأنها تصف لون القطة.  الصفات تصف الأسماء،  وتُضيف معلومات إضافية عنها.  'black'  صفة لون،  وتُحدد لون القطة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is an adjective: The bird flew high. ",
        "options": ["bird", "flew", "high", "the"],
        "correct_option_id": 2,
        "explanation": "كلمة 'high'  صفة (adjective) لأنها تصف  كيفية طيران الطائر (flew).  الصفات تُضيف معلومات إضافية عن الأسماء،  وتصف خصائصها أو حالتها.  في هذه الحالة،  'high'  صفة تصف  الارتفاع أو العلوّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these sentences contains an adjective?",
        "options": ["The boy runs.", "The tall girl sings.", "The dog barks.", "The car goes."],
        "correct_option_id": 1,
        "explanation": "الجملة 'The tall girl sings' تحتوي على الصفة 'tall' التي تصف الطول.  الصفات تُستخدم لوصف خصائص أو سمات الأسماء.  في هذه الجملة،  'tall'  تصفُّ الفتاة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these is an adjective describing personality?",
        "options": ["red", "tall", "kind", "round"],
        "correct_option_id": 2,
        "explanation": "كلمة 'kind'  صفة (adjective) تصف شخصية لطيفة.  صفات الشخصية تُصف سمات أو خصائص شخصية الأفراد، مثل: generous, honest, friendly، إلخ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is an adjective describing quantity?",
        "options": ["many", "run", "happy", "big"],
        "correct_option_id": 0,
        "explanation": "كلمة 'many'  صفة كمية (adjective of quantity) لأنها تُشير إلى عدد كبير من الأشياء.  تُستخدم صفات الكمية لوصف كمية غير محددة من الأسماء،  مثل: few, several, some، إلخ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the comparative form of 'big'?",
        "options": ["bigger", "bigest", "big", "biggest"],
        "correct_option_id": 0,
        "explanation": "الصيغة المقارنة (comparative form) للصفة 'big' هي 'bigger'. نستخدم الصيغة المقارنة للمقارنة بين شيئين، للدلالة على أنّ أحدهما أكبر من الآخر.  'bigger'  هي الصيغة الصحيحة للمقارنة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the superlative form of 'small'?",
        "options": ["smaller", "smallest", "small", "smalles"],
        "correct_option_id": 1,
        "explanation": "الصيغة المطلقة (superlative form) للصفة 'small' هي 'smallest'.  نستخدم الصيغة المطلقة للمقارنة بين ثلاثة أشياء أو أكثر، للدلالة على أنّ أحدها هو الأصغر بينها. 'smallest'  هي الصيغة الصحيحة للمقارنة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the comparative form of 'good'?",
        "options": ["better", "gooder", "good", "best"],
        "correct_option_id": 0,
        "explanation": "الصيغة المقارنة (comparative form) للصفة 'good' هي 'better'.  'better' تُستخدم للمقارنة بين شيئين، للدلالة على أنّ أحدهما أفضل من الآخر.  'better'  هي الصيغة الصحيحة للمقارنة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the superlative form of 'bad'?",
        "options": ["badder", "worse", "bad", "worst"],
        "correct_option_id": 3,
        "explanation": "الصيغة المطلقة (superlative form) للصفة 'bad' هي 'worst'.  'worst' تُستخدم للمقارنة بين ثلاثة أشياء أو أكثر، للدلالة على أنّ أحدها هو الأسوأ بينها. 'worst'  هي الصيغة الصحيحة للمقارنة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct sentence using comparative adjectives: The cat is ____ than the dog.",
        "options": ["big", "bigger", "biggest", "bigly"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'bigger'  لأنها الصيغة المقارنة (comparative) للصفة 'big'  وتُستخدم للمقارنة بين شيئين.  'bigger'  تُشير إلى أنّ القطة أكبر من الكلب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct sentence using superlative adjectives: This is the ____ house on the street.",
        "options": ["big", "bigger", "biggest", "bigly"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'biggest' لأنها الصيغة المطلقة (superlative) للصفة 'big'  وتُستخدم للمقارنة بين ثلاثة أشياء أو أكثر.  'biggest'  تُشير إلى أنّ هذا المنزل هو الأكبر في الشارع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the adjective in this sentence: The delicious cake is sweet.",
        "options": ["cake", "sweet", "is", "delicious"],
        "correct_option_id": 3,
        "explanation": "كلمتا 'delicious' و 'sweet' كلاهما صفتان (adjectives) تصفان الكعكة.  'delicious'  تصف طعم الكعكة، و'sweet'  تصف طعمها الحلو.  تُستخدم الصفات لتقديم المزيد من المعلومات حول الأسماء."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective is used to describe a person's height?",
        "options": ["tall", "beautiful", "happy", "kind"],
        "correct_option_id": 0,
        "explanation": "الصفة 'tall'  تُستخدم لوصف طول الشخص.  صفات الطول تُعبّر عن مدى ارتفاع الشخص،  مثل: short, high, long، إلخ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these words is NOT an adjective:  happy, quickly, sad, angry",
        "options": ["happy", "sad", "angry", "quickly"],
        "correct_option_id": 1,
        "explanation": "كلمة 'quickly'  ظرف (adverb) وليست صفة (adjective).  الظروف تُعدل الأفعال، بينما الصفات تُعدل الأسماء.  'quickly'  تُعدل الفعل، بينما الكلمات الأخرى تصف مشاعر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the comparative form of 'good'?",
        "options": ["gooder", "better", "best", "well"],
        "correct_option_id": 1,
        "explanation": "الصيغة المقارنة لـ 'good'  هي 'better'.  تُستخدم  'better'  للمقارنة بين شيئين،  وهي صفة غير منتظمة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the superlative form of 'bad'?",
        "options": ["badder", "worse", "worst", "badly"],
        "correct_option_id": 2,
        "explanation": "الصيغة المطلقة لـ 'bad' هي 'worst'. تُستخدم 'worst' للمقارنة بين ثلاثة أشياء أو أكثر، وهي صفة غير منتظمة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'The flower is ____ than the tree'.",
        "options": ["smaller", "smallest", "small", "more small"],
        "correct_option_id": 0,
        "explanation": "نستخدم الصفة المقارنة 'smaller'  لأنّنا نقارن بين شيئين (الزهرة والشجرة).  'smaller' تُشير إلى أنّ الزهرة أصغر من الشجرة،  وهذا يُعبّر عن المقارنة بين شيئين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'That is the ____ car in the show'.",
        "options": ["fast", "faster", "fastest", "more fast"],
        "correct_option_id": 2,
        "explanation": "نستخدم الصفة المطلقة 'fastest'  لأنّنا نقارن بين أكثر من شيئين (عدّة سيارات).  'fastest' تُشير إلى أنّ هذه السيارة هي الأسرع بينها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'beautiful'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 0,
        "explanation": "'Beautiful'  صفة نوعية (adjective of quality) لأنها تصف جودة الشيء (جماله).  صفات الجودة تصف خصائص الشيء من حيث الجمال، الحجم، الشكل، اللون، الخ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'five'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 2,
        "explanation": "'Five'  صفة عددية (adjective of number) لأنها تُعبّر عن عدد محدد (خمسة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'my'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 3,
        "explanation": "'My'  صفة ملكية (possessive adjective) لأنها تُشير إلى ملكية المتكلم (أنا)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'many'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 1,
        "explanation": "'Many'  صفة كمية (adjective of quantity) لأنها تُشير إلى كمية غير محددة ولكنها أكثر من اثنين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'The book is ____ than the magazine'.",
        "options": ["thinner", "thinest", "thin", "more thin"],
        "correct_option_id": 0,
        "explanation": "نستخدم الصفة المقارنة 'thinner'  لأننا نقارن بين شيئين (الكتاب والمجلة).  'thinner' تُشير إلى أنّ الكتاب أرق من المجلة،  وهذا يُعبّر عن المقارنة بين شيئين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'That is the ____ building in the city'.",
        "options": ["tall", "taller", "tallest", "more tall"],
        "correct_option_id": 2,
        "explanation": "نستخدم الصفة المطلقة 'tallest'  لأننا نقارن بين أكثر من شيئين (عدّة مبانٍ).  'tallest' تُشير إلى أنّ هذا المبنى هو الأطول بينها،  وهذا يُعبّر عن المقارنة بين ثلاثة أشياء أو أكثر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is an adjective: The quick brown fox jumps.",
        "options": ["jumps", "brown", "the", "quick"],
        "correct_option_id": 1,
        "explanation": "كلمتا 'quick' و 'brown'  كلاهما صفتان (adjectives) تصفان الثعلب. 'quick'  تصف سرعة الثعلب، و'brown'  تصف لونه.  تُستخدم الصفات لتقديم المزيد من المعلومات حول الأسماء."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes the size of something small?",
        "options": ["tiny", "huge", "gigantic", "massive"],
        "correct_option_id": 0,
        "explanation": "كلمة 'tiny'  صفة (adjective) تصف شيئًا صغيرًا جدّاً،  وهي من الصفات التي تُعبّر عن صغر الحجم بشكلٍ واضح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes a person's weight?",
        "options": ["heavy", "tall", "kind", "fast"],
        "correct_option_id": 0,
        "explanation": "الصفة 'heavy'  تُستخدم لوصف وزن الشخص.  تُعبّر صفات الوزن عن مدى ثقل أو خفة الشخص أو الشيء،  على عكس الصفات الأخرى التي تصف الطول أو الشخصية أو السرعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these words is NOT an adjective:  happy, quickly, sad, angry",
        "options": ["quickly", "happy", "sad", "angry"],
        "correct_option_id": 0,
        "explanation": "كلمة 'quickly'  ظرف (adverb) وليست صفة (adjective).  الظروف تُعدل الأفعال (تُشير إلى الكيفية أو الزمان أو المكان)، بينما الصفات تُعدل الأسماء.  'quickly'  تُعدل الفعل، بينما الكلمات الأخرى تصف مشاعر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the comparative form of 'thin'?",
        "options": ["thinner", "thinest", "thin", "more thin"],
        "correct_option_id": 0,
        "explanation": "الصيغة المقارنة للصفة 'thin' هي 'thinner'.  تُستخدم  'thinner'  للمقارنة بين شيئين،  للدلالة على أنّ أحدهما أنحف من الآخر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the superlative form of 'good'?",
        "options": ["gooder", "better", "well", "best"],
        "correct_option_id": 3,
        "explanation": "الصيغة المطلقة للصفة 'good' هي 'best'.  تُستخدم 'best' للمقارنة بين ثلاثة أشياء أو أكثر، للدلالة على أنّ أحدها هو الأفضل بينها.  'best'  هي صفة غير منتظمة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'The weather is ____ than yesterday'.",
        "options": ["warmer", "warmest", "warm", "more warm"],
        "correct_option_id": 0,
        "explanation": "نستخدم الصفة المقارنة 'warmer'  لأننا نقارن بين يومين (اليوم والأمس).  'warmer' تُشير إلى أنّ طقس اليوم أدفأ من طقس الأمس،  وهذا يُعبّر عن المقارنة بين شيئين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'That is the ____ cake I've ever tasted'.",
        "options": ["delicious", "more delicious", "deliciouser", "most delicious"],
        "correct_option_id": 3,
        "explanation": "نستخدم الصفة المطلقة 'most delicious'  لأننا نقارن بين أكثر من كعكة (جميع الكعك التي تذوقتها).  'most delicious'  تُشير إلى أنّ هذه الكعكة هي ألذّها،  وهذا يُعبّر عن المقارنة بين ثلاثة أشياء أو أكثر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'expensive'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 0,
        "explanation": "'Expensive'  صفة نوعية (adjective of quality)  لأنها تصف جودة الشيء (غلاء ثمنه).  صفات الجودة تصف خصائص الشيء من حيث الجمال، الحجم، الشكل، اللون، الطعم، الثمن، الخ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'several'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 1,
        "explanation": "'Several'  صفة كمية (adjective of quantity) لأنها تُعبّر عن كمية غير محددة ولكنها أكثر من اثنين.  تُستخدم صفات الكمية لوصف كمية غير محددة من الأسماء."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'her'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 3,
        "explanation": "'Her'  صفة ملكية (possessive adjective)  لأنها تُشير إلى ملكية أنثى.  الصفات المَلْكية تُستخدم للإشارة إلى ملكية شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'few'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 1,
        "explanation": "'Few'  صفة كمية (adjective of quantity) لأنها تُشير إلى كمية قليلة، ولكنها ليست صفرًا.  تُستخدم صفات الكمية لوصف كمية غير محددة من الأسماء."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'The coffee is ____ than the tea'.",
        "options": ["stronger", "strongest", "strong", "more strong"],
        "correct_option_id": 0,
        "explanation": "نستخدم الصفة المقارنة 'stronger'  لأننا نقارن بين شيئين (القهوة والشاي).  'stronger'  تُشير إلى أنّ القهوة أقوى من الشاي من حيث النكهة.  نستخدم الصفة المقارنة عند مقارنة شيئين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'That is the ____ film I've ever seen'.",
        "options": ["interesting", "more interesting", "most interesting", "interestingly"],
        "correct_option_id": 2,
        "explanation": "نستخدم الصفة المطلقة 'most interesting'  لأننا نقارن بين أكثر من فيلم (جميع الأفلام التي شاهدتها).  'most interesting'  تُشير إلى أنّ هذا الفيلم هو الأكثر إثارة للاهتمام.  نستخدم الصفة المطلقة عند مقارنة ثلاثة أشياء أو أكثر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the adjectives in the sentence: The big, fluffy cat slept soundly.",
        "options": ["slept", "soundly", "big", "fluffy"],
        "correct_option_id": 2,
        "explanation": "كلمتا 'big' و 'fluffy'  كلاهما صفتان (adjectives) تصفان القطة.  'big'  تصف حجم القطة (كبيرة)، و'fluffy'  تصف ملمس فروها (نَاعم ورقيق).  'soundly'  ظرف وليس صفة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adjective describes a feeling of happiness?",
        "options": ["joyful", "sad", "angry", "tired"],
        "correct_option_id": 0,
        "explanation": "الصفة 'joyful'  تُعبّر عن الشعور بالسعادة والفرح.  'joyful'  صفة  لأنها تصف المشاعر،  وهي من صفات المشاعر الإيجابية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these words is NOT an adjective:  happy, quickly, sad, angry",
        "options": ["quickly", "happy", "sad", "angry"],
        "correct_option_id": 0,
        "explanation": "كلمة 'quickly'  ظرف (adverb) وليست صفة (adjective).  الظروف تُعدل الأفعال (تُشير إلى الكيفية أو الزمان أو المكان)، بينما الصفات تُعدل الأسماء.  'quickly'  تُعدل الفعل، بينما الكلمات الأخرى تصف مشاعر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the comparative form of 'heavy'?",
        "options": ["heavier", "heaviest", "heavy", "more heavy"],
        "correct_option_id": 0,
        "explanation": "الصيغة المقارنة للصفة 'heavy' هي 'heavier'.  تُستخدم 'heavier'  للمقارنة بين شيئين،  للدلالة على أنّ أحدهما أثقل من الآخر.  'heavier'  هي الصيغة الصحيحة للمقارنة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the superlative form of 'thin'?",
        "options": ["thinner", "thinest", "thin", "more thin"],
        "correct_option_id": 1,
        "explanation": "الصيغة المطلقة للصفة 'thin' هي 'thinest'.  تُستخدم 'thinest'  للمقارنة بين ثلاثة أشياء أو أكثر، للدلالة على أنّ أحدها هو الأنحف بينها. 'thinest'  هي الصيغة الصحيحة للمقارنة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'The soup is ____ than the stew'.",
        "options": ["tastier", "tastiest", "tasty", "more tasty"],
        "correct_option_id": 0,
        "explanation": "نستخدم الصفة المقارنة 'tastier'  لأننا نقارن بين شيئين (الحساء واليخنة).  'tastier'  تُشير إلى أنّ الحساء ألذ من اليخنة من حيث الطعم.  نستخدم الصفة المقارنة عند مقارنة شيئين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'That is the ____ cake I've ever tasted'.",
        "options": ["delicious", "more delicious", "deliciouser", "most delicious"],
        "correct_option_id": 3,
        "explanation": "نستخدم الصفة المطلقة 'most delicious'  لأننا نقارن بين أكثر من كعكة (جميع الكعك التي تذوقتها).  'most delicious'  تُشير إلى أنّ هذه الكعكة هي ألذّها،  وهذا يُعبّر عن المقارنة بين ثلاثة أشياء أو أكثر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'delicious'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 0,
        "explanation": "'Delicious'  صفة نوعية (adjective of quality) لأنها تصف جودة الشيء (طعمه اللذيذ).  صفات الجودة تصف خصائص الشيء من حيث الجمال، الحجم، الشكل، اللون، الطعم، الخ.  'Delicious'  تصفُّ جودة الطعم."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'several'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 1,
        "explanation": "'Several'  صفة كمية (adjective of quantity) لأنها تُعبّر عن كمية غير محددة ولكنها أكثر من اثنين.  تُستخدم صفات الكمية لوصف كمية غير محددة من الأسماء،  مثل:  few، many، some، إلخ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'her'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 3,
        "explanation": "'Her'  صفة ملكية (possessive adjective)  لأنها تُشير إلى ملكية أنثى.  الصفات المَلْكية تُستخدم للإشارة إلى ملكية شيء ما،  وهي مرتبطة بضمير الملكية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of adjective is 'few'?",
        "options": ["adjective of quality", "adjective of quantity", "adjective of number", "possessive adjective"],
        "correct_option_id": 1,
        "explanation": "'Few'  صفة كمية (adjective of quantity) لأنها تُشير إلى كمية قليلة، ولكنها ليست صفرًا.  تُستخدم صفات الكمية لوصف كمية غير محددة من الأسماء،  مع الإشارة إلى أنّ الكمية قليلة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'The coffee is ____ than the tea'.",
        "options": ["stronger", "strongest", "strong", "more strong"],
        "correct_option_id": 0,
        "explanation": "نستخدم الصفة المقارنة 'stronger'  لأننا نقارن بين شيئين (القهوة والشاي).  'stronger'  تُشير إلى أنّ القهوة أقوى من الشاي من حيث النكهة.  نستخدم الصفة المقارنة عند مقارنة شيئين،  وهي تُشير إلى درجة أعلى من الصفة."
    },
        ],
    "الظرف-الحال": [
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the adverb in the sentence: 'The bird sang sweetly'.",
        "options": ["bird", "sang", "sweetly", "the"],
        "correct_option_id": 2,
        "explanation": "كلمة 'sweetly' هي ظرف (adverb) لأنها تُعدّل الفعل 'sang' (غنى).  الظروف تُضيف معنى إضافيًا للفعل،  وتُشير إلى الكيفية أو الزمان أو المكان أو التردد. في هذه الحالة،  'sweetly'  ظرف طريقة (adverb of manner) يُشير إلى *كيفية* غناء الطائر (أي:  بحلاوة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is an adverb of manner?",
        "options": ["quickly", "tomorrow", "here", "always"],
        "correct_option_id": 0,
        "explanation": "ظرف الطريقة (adverb of manner) يُشير إلى *كيفية* حدوث الفعل، أي كيف تمّ القيام به.  'quickly'  ظرف طريقة لأنه يُوضح *كيف* تمّ القيام بالعمل (أي: بسرعة).  الظروف الأخرى تُشير إلى زمن أو مكان أو تردد الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is an adverb of time?",
        "options": ["quickly", "tomorrow", "here", "always"],
        "correct_option_id": 1,
        "explanation": "ظرف الزمان (adverb of time) يُشير إلى *متى* حدث الفعل، أي وقت حدوثه.  'tomorrow'  ظرف زمان لأنه يُحدد وقت حدوث الفعل (أي: غدًا).  الظروف الأخرى تُشير إلى طريقة أو مكان أو تردد الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is an adverb of place?",
        "options": ["quickly", "tomorrow", "here", "always"],
        "correct_option_id": 2,
        "explanation": "ظرف المكان (adverb of place) يُشير إلى *أين* حدث الفعل، أي مكان حدوثه.  'here'  ظرف مكان لأنه يُحدد مكان حدوث الفعل (أي: هنا).  الظروف الأخرى تُشير إلى طريقة أو زمن أو تردد الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich word is an adverb of frequency?",
        "options": ["quickly", "tomorrow", "here", "always"],
        "correct_option_id": 3,
        "explanation": "ظرف التردد (adverb of frequency) يُشير إلى *كم مرة* تكرر الفعل، أي مدى تكراره. 'always'  ظرف تردد لأنه يُحدد مدى تكرار الفعل (أي: دائمًا).  الظروف الأخرى تُشير إلى طريقة أو زمن أو مكان الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the adverb in the sentence: 'He speaks English fluently'.",
        "options": ["He", "speaks", "English", "fluently"],
        "correct_option_id": 3,
        "explanation": " 'fluently'  ظرف طريقة (adverb of manner) لأنه يُعدّل الفعل 'speaks' (يتحدث) ويوضح الكيفية (بطلاقة).  يُضيف  'fluently'  معنىً إضافيًا للفعل،  مُحددًا كيف يتحدث الإنجليزية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adverb modifies the verb 'to sing' in the sentence: 'She sings beautifully'.",
        "options": ["She", "sings", "beautifully", "the"],
        "correct_option_id": 2,
        "explanation": "'beautifully'  ظرف طريقة (adverb of manner) لأنه يُعدّل الفعل 'sings' (تغني) ويوضح الكيفية (بجمال).  يُضيف  'beautifully'  معلومات إضافية عن كيفية غنائها،  مُحددًا أسلوب غنائها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adverb tells us when the action happened: 'He arrived yesterday'.",
        "options": ["He", "arrived", "yesterday", "the"],
        "correct_option_id": 2,
        "explanation": "'yesterday'  ظرف زمان (adverb of time) لأنه يُحدد متى وصل (arrived).  ظروف الزمان تُحدد وقت حدوث الفعل،  وتُشير إلى الماضي أو الحاضر أو المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adverb tells us where the action took place:  'They met there'.",
        "options": ["They", "met", "there", "the"],
        "correct_option_id": 2,
        "explanation": "'there'  ظرف مكان (adverb of place) لأنه يُحدد أين التقوا (met).  ظروف المكان تُحدد موقع حدوث الفعل،  وتُشير إلى مكان محدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich adverb shows how often the action is done: 'She always smiles'.",
        "options": ["She", "smiles", "always", "the"],
        "correct_option_id": 2,
        "explanation": "'always'  ظرف تردد (adverb of frequency)  لأنه يُحدد عدد مرات الابتسام (smiles).  ظروف التردد تُشير إلى مدى تكرار حدوث الفعل،  مثل: often, sometimes, rarely، إلخ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the adverb of manner:  'The car drives slowly'.",
        "options": ["car", "drives", "slowly", "the"],
        "correct_option_id": 2,
        "explanation": "'slowly'  ظرف طريقة (adverb of manner)  لأنه يُعدّل الفعل 'drives' (يقود) ويوضح الكيفية (ببطء).  يُضيف  'slowly'  معنىً إضافيًا للفعل،  مُحددًا سرعة القيادة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the adverb of time:  'We'll leave soon'.",
        "options": ["We'll", "leave", "soon", "the"],
        "correct_option_id": 2,
        "explanation": "'soon'  ظرف زمان (adverb of time) لأنه يُحدد متى سنغادر (leave).  'soon'  يُشير إلى وقت قريب في المستقبل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the adverb of place: 'The bird flew away'.",
        "options": ["bird", "flew", "away", "the"],
        "correct_option_id": 2,
        "explanation": "'away'  ظرف مكان (adverb of place) لأنه يُحدد إلى أين طار الطائر (flew).  'away'  تُشير إلى اتجاه بعيد عن نقطة البداية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the adverb of frequency:  'He rarely visits'.",
        "options": ["He", "visits", "rarely", "the"],
        "correct_option_id": 2,
        "explanation": "'rarely'  ظرف تردد (adverb of frequency)  لأنه يُحدد عدد مرات الزيارة (visits).  'rarely'  تُشير إلى أنّ الزيارات قليلة  ونادرة الحدوث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb of manner: He spoke ____.",
        "options": ["quickly", "tomorrow", "here", "always"],
        "correct_option_id": 0,
        "explanation": " 'quickly'  ظرف طريقة (adverb of manner) لأنه يُشير إلى *كيفية* الكلام (أي: بسرعة).  تُستخدم ظروف الطريقة لوصف الكيفية التي يتم بها الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb of time: The movie starts ____.",
        "options": ["quickly", "tomorrow", "here", "always"],
        "correct_option_id": 1,
        "explanation": "'tomorrow'  ظرف زمان (adverb of time) لأنه يُشير إلى وقت بداية الفيلم (أي: غدًا).  تُستخدم ظروف الزمان لتحديد وقت حدوث الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb of place: They are waiting ____.",
        "options": ["quickly", "tomorrow", "here", "always"],
        "correct_option_id": 2,
        "explanation": "'here'  ظرف مكان (adverb of place) لأنه يُشير إلى مكان الانتظار (أي: هنا).  تُستخدم ظروف المكان لتحديد مكان حدوث الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb of frequency: She ____ goes to the gym.",
        "options": ["quickly", "tomorrow", "here", "always"],
        "correct_option_id": 3,
        "explanation": "'always'  ظرف تردد (adverb of frequency)  لأنه يُشير إلى عدد مرات الذهاب إلى الصالة الرياضية (أي: دائمًا).  تُستخدم ظروف التردد لتحديد مدى تكرار حدوث الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThe children played happily.  'Happily' is what type of adverb?",
        "options": ["adverb of manner", "adverb of time", "adverb of place", "adverb of frequency"],
        "correct_option_id": 0,
        "explanation": "'Happily'  يُعدّل الفعل 'played' (لعب)  ويُشير إلى الكيفية (بسعادة)،  لذا هو ظرف طريقة (adverb of manner).  ظروف الطريقة تُشير إلى *كيف* تمّ القيام بالعمل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nShe arrived early. 'Early' is what type of adverb?",
        "options": ["adverb of manner", "adverb of time", "adverb of place", "adverb of frequency"],
        "correct_option_id": 1,
        "explanation": "'Early'  يُحدد متى وصلت (arrived)،  لذا هو ظرف زمان (adverb of time).  ظروف الزمان تُشير إلى *متى* حدث الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nThey live nearby.  'Nearby' is what type of adverb?",
        "options": ["adverb of manner", "adverb of time", "adverb of place", "adverb of frequency"],
        "correct_option_id": 2,
        "explanation": "'Nearby'  يُحدد أين يعيشون (live)،  لذا هو ظرف مكان (adverb of place).  ظروف المكان تُشير إلى *أين* حدث الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nHe often travels. 'Often' is what type of adverb?",
        "options": ["adverb of manner", "adverb of time", "adverb of place", "adverb of frequency"],
        "correct_option_id": 3,
        "explanation": "'Often'  يُحدد عدد مرات السفر (travels)،  لذا هو ظرف تردد (adverb of frequency).  ظروف التردد تُشير إلى *كم مرة* تكرر الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n'Very' is what kind of adverb?",
        "options": ["adverb of manner", "adverb of degree", "adverb of time", "adverb of place"],
        "correct_option_id": 1,
        "explanation": "'Very'  ظرف كمية (adverb of degree)  لأنه يُعدّل الصفات والأفعال الأخرى،  ويُشير إلى الدرجة أو الكمية.  مثال:  'very happy' (سعيد جدًّا)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n'Yesterday' is what kind of adverb?",
        "options": ["adverb of manner", "adverb of degree", "adverb of time", "adverb of place"],
        "correct_option_id": 2,
        "explanation": "'Yesterday'  ظرف زمان (adverb of time) لأنه يُشير إلى الزمن الذي حدث فيه الفعل (أي:  الأمس)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n'Here' is what kind of adverb?",
        "options": ["adverb of manner", "adverb of degree", "adverb of time", "adverb of place"],
        "correct_option_id": 3,
        "explanation": "'Here'  ظرف مكان (adverb of place) لأنه يُشير إلى مكان حدوث الفعل (أي: هنا)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\n'Usually' is what kind of adverb?",
        "options": ["adverb of manner", "adverb of degree", "adverb of time", "adverb of frequency"],
        "correct_option_id": 3,
        "explanation": "'Usually'  ظرف تردد (adverb of frequency) لأنه يُشير إلى مدى تكرار حدوث الفعل (أي: عادةً)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  She sings ____.",
        "options": ["beautiful", "beautifully", "beauty", "beautifulness"],
        "correct_option_id": 1,
        "explanation": " 'beautifully'  هو ظرف طريقة (adverb of manner)  يُعدّل الفعل 'sings' (تغني)  ويُشير إلى كيفية الغناء (أي: بجمال)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  He arrived ____.",
        "options": ["early", "earliness", "earlier", "earlyer"],
        "correct_option_id": 0,
        "explanation": "'early'  هو ظرف زمان (adverb of time)  يُشير إلى وقت الوصول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  They live ____.",
        "options": ["near", "nearly", "nearby", "nears"],
        "correct_option_id": 2,
        "explanation": "'nearby'  هو ظرف مكان (adverb of place)  يُشير إلى مكان سكنهم."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  He ____ visits his family.",
        "options": ["often", "oftenly", "oft", "oftenness"],
        "correct_option_id": 0,
        "explanation": "'often'  هو ظرف تردد (adverb of frequency)  يُشير إلى عدد مرات زيارته لعائلته."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb: The test was ____ difficult.",
        "options": ["extremely", "extreme", "extremer", "extremelyer"],
        "correct_option_id": 0,
        "explanation": "'extremely'  هو ظرف كمية (adverb of degree) يُشير إلى درجة شدة صعوبة الاختبار."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  She finished her work ____.",
        "options": ["quick", "quickly", "quicker", "quickest"],
        "correct_option_id": 1,
        "explanation": "'quickly'  هو ظرف طريقة (adverb of manner)  يُشير إلى كيفية إتمام العمل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  He walks ____.",
        "options": ["slow", "slowly", "slower", "slowest"],
        "correct_option_id": 1,
        "explanation": "'slowly'  هو ظرف طريقة (adverb of manner)  يُشير إلى كيفية مشيه."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  They arrived ____ late.",
        "options": ["extreme", "extremely", "extremer", "extremest"],
        "correct_option_id": 1,
        "explanation": "'extremely'  هو ظرف كمية (adverb of degree) يُشير إلى درجة تأخرهم."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  The sun shines ____.",
        "options": ["bright", "brightly", "brighter", "brightest"],
        "correct_option_id": 1,
        "explanation": "'brightly'  هو ظرف طريقة (adverb of manner)  يُشير إلى كيفية سطوع الشمس."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  She sings ____ well.",
        "options": ["extreme", "extremely", "extremer", "extremest"],
        "correct_option_id": 1,
        "explanation": "'extremely'  هو ظرف كمية (adverb of degree) يُشير إلى درجة جودة الغناء."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  He plays the piano ____.",
        "options": ["skillful", "skillfully", "skillfuller", "most skillful"],
        "correct_option_id": 1,
        "explanation": "'skillfully'  هو ظرف طريقة (adverb of manner)  يُشير إلى كيفية لعبه للبيانو."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  The bird flew ____.",
        "options": ["high", "highly", "higher", "highest"],
        "correct_option_id": 1,
        "explanation": "'highly'  هو ظرف طريقة (adverb of manner)  ويُشير إلى كيفية طيران الطائر (أي:  على ارتفاع عالٍ)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  They worked ____.",
        "options": ["hard", "hardly", "harder", "hardest"],
        "correct_option_id": 0,
        "explanation": "'hard'  هو ظرف طريقة (adverb of manner)  ويُستخدم مع العمل (worked) للدلالة على العمل الجادّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  She speaks English ____.",
        "options": ["fluent", "fluently", "more fluent", "most fluent"],
        "correct_option_id": 1,
        "explanation": "'fluently'  هو ظرف طريقة (adverb of manner)  يُشير إلى كيفية تحدثها الإنجليزية (أي: بطلاقة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb: He ate his lunch ____.",
        "options": ["quick", "quickly", "quicker", "quickest"],
        "correct_option_id": 1,
        "explanation": "'quickly'  هو ظرف طريقة (adverb of manner)  يُشير إلى كيفية تناوله طعامه (أي: بسرعة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  The children behaved ____.",
        "options": ["good", "well", "better", "best"],
        "correct_option_id": 1,
        "explanation": "'well'  هو ظرف طريقة (adverb of manner)  ويُستخدم مع الفعل 'behaved'  لأنه يُشير إلى كيفية تصرف الأطفال (أي:  حسنًا)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  She is ____ tired.",
        "options": ["extreme", "extremely", "extremer", "extremest"],
        "correct_option_id": 1,
        "explanation": "'extremely'  هو ظرف كمية (adverb of degree)  يُشير إلى درجة التعب الشديد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  He sings ____ beautifully.",
        "options": ["extreme", "extremely", "extremer", "extremest"],
        "correct_option_id": 1,
        "explanation": "'extremely'  هو ظرف كمية (adverb of degree) يُشير إلى درجة جمال الغناء."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  She danced ____.",
        "options": ["graceful", "gracefully", "more graceful", "most graceful"],
        "correct_option_id": 1,
        "explanation": "'gracefully'  هو ظرف طريقة (adverb of manner)  يُشير إلى كيفية رقصها (أي:  برقة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb: The dog barked ____.",
        "options": ["loud", "loudly", "louder", "loudest"],
        "correct_option_id": 1,
        "explanation": "'loudly'  هو ظرف طريقة (adverb of manner)  يُشير إلى كيفية نباح الكلب (أي:  بصوت عالٍ)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  She speaks French ____.",
        "options": ["fluent", "fluently", "more fluent", "most fluent"],
        "correct_option_id": 1,
        "explanation": "'fluently'  هو ظرف طريقة (adverb of manner)  يُشير إلى كيفية تحدثها الفرنسية (أي:  بطلاقة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb: They finished their work ____.",
        "options": ["fast", "faster", "fastest", "quickly"],
        "correct_option_id": 3,
        "explanation": "'quickly'  هو ظرف طريقة (adverb of manner)  يُشير إلى كيفية إتمام العمل (أي:  بسرعة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  She is ____ happy.",
        "options": ["very", "much", "more", "most"],
        "correct_option_id": 0,
        "explanation": "'very'  هو ظرف كمية (adverb of degree)  يُستخدم لتعديل الصفات،  ويُشير إلى درجة عالية من السعادة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence with an adverb:  He is ____ tall.",
        "options": ["very", "much", "more", "most"],
        "correct_option_id": 0,
        "explanation": "'very'  هو ظرف كمية (adverb of degree) يُستخدم لتعديل الصفات،  ويُشير إلى درجة عالية من الطول."
    },
    {
                "question": "اختر الإجابة الصحيحة:\nWhich word is an adverb?",
                "options": ["quick", "quietly", "run", "happy"],
                "correct_option_id": 1,
                "explanation": "الظرف (adverb) هو كلمة تصف الفعل (verb) أو الصفة (adjective) أو ظرف آخر، وغالبًا ما يوضح كيفية حدوث شيءٍ ما. في هذه الحالة، 'quietly' هو ظرف لأنه يصف كيف يحدث الفعل (بهدوء)، بينما 'quick' صفة، و'run' فعل، و'happy' صفة."
            },
            {
                "question": "اختر الظرف المناسب:\nShe runs ____ (fast).",
                "options": ["fast", "fastly", "quick", "quickly"],
                "correct_option_id": 0,
                "explanation": "الكلمة 'fast' يمكن أن تُستخدم كظرف يصف كيفية حدوث الفعل (الركض)، ولا تتغير صيغتها. الكلمة 'quickly' هي أيضًا ظرف، ولكنها لا تناسب هنا بنفس الطريقة التي تُستخدم بها 'fast'."
            },
            {
                "question": "اختر الإجابة الصحيحة:\nThe baby slept ____. (peaceful)",
                "options": ["peace", "peacefully", "peaceful", "peaceable"],
                "correct_option_id": 1,
                "explanation": "'Peacefully' هو الظرف الذي يصف كيفية حدوث الفعل (النوم). في هذه الحالة، نحتاج إلى ظرف يوضح كيف نام الطفل بسلام."
            },
            {
                "question": "اختر الظرف المناسب:\nShe ____ finished her homework before dinner. (already)",
                "options": ["already", "soon", "now", "early"],
                "correct_option_id": 0,
                "explanation": "الظرف 'already' يشير إلى أن الفعل قد اكتمل بالفعل في وقتٍ سابق. هو الظرف الأنسب هنا لأنه يعبر عن التوقيت."
            },
            {
                "question": "اختر الظرف المناسب:\nThey arrived ____ (late) to the meeting.",
                "options": ["lately", "late", "later", "last"],
                "correct_option_id": 1,
                "explanation": "الظرف 'late' يصف متى وصلوا إلى الاجتماع. 'Lately' يشير إلى الآونة الأخيرة ولكنه لا يُستخدم مع الحضور المتأخر، بينما 'later' يشير إلى وقت لاحق."
            },
            {
                "question": "اختر الإجابة الصحيحة:\nShe speaks ____ (fluent) Spanish.",
                "options": ["fluent", "fluently", "fluenting", "fluents"],
                "correct_option_id": 1,
                "explanation": "الظرف 'fluently' هو الكلمة الصحيحة هنا لأنه يصف كيفية تحدثها بالإسبانية. نحتاج إلى ظرف يوضح الطريقة (بطلاقة)."
            },
            {
                "question": "اختر الظرف المناسب:\nHe works ____. (hard)",
                "options": ["hardly", "hard", "harder", "hardest"],
                "correct_option_id": 1,
                "explanation": "الظرف 'hard' يُستخدم لوصف كيفية عمله (بجد). 'Hardly' يعني 'بالكاد' وهو معنى مختلف تمامًا."
            },
            {
                "question": "اختر الإجابة الصحيحة:\nThe cat moves ____. (silent)",
                "options": ["silently", "silent", "silents", "silented"],
                "correct_option_id": 0,
                "explanation": "'Silently' هو الظرف الذي يصف كيفية تحرك القطة. نحتاج إلى ظرف يوضح الطريقة (بصمت)."
            },
            {
                "question": "اختر الإجابة الصحيحة:\nThe sun shines ____ in the morning. (bright)",
                "options": ["brightly", "bright", "brights", "brighted"],
                "correct_option_id": 0,
                "explanation": "الظرف 'brightly' يصف كيف تشرق الشمس في الصباح. نستخدم الظرف هنا لتوضيح الطريقة (بسطوع)."
            },
            {
                "question": "اختر الإجابة الصحيحة:\nThey ____ agreed to the proposal. (quick)",
                "options": ["quickly", "quick", "quicker", "quickness"],
                "correct_option_id": 0,
                "explanation": "'Quickly' هو الظرف الذي يصف كيفية موافقتهم على الاقتراح (بسرعة)."
            },
        
        ],
    "الضمائر": [
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the pronoun in this sentence: 'She went to the store'.",
        "options": ["She", "went", "to", "store"],
        "correct_option_id": 0,
        "explanation": "الضمير (pronoun) هو كلمة تُستخدم بدلاً من اسم (noun) لتجنب التكرار.  في هذه الجملة،  'She' ضمير لأنّه يُشير إلى أنثى دون ذكر اسمها. الضمائر تُسهل الكلام وتجعله أكثر سلاسة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of pronoun is 'I'?",
        "options": ["personal pronoun", "possessive pronoun", "demonstrative pronoun", "relative pronoun"],
        "correct_option_id": 0,
        "explanation": "'I' ضمير شخصيّ (personal pronoun) من الضمائر المفردة، ويُستخدم للدلالة على المتكلم."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of pronoun is 'mine'?",
        "options": ["personal pronoun", "possessive pronoun", "demonstrative pronoun", "relative pronoun"],
        "correct_option_id": 1,
        "explanation": "'mine' ضمير ملكية (possessive pronoun)  يُشير إلى ملكية المتكلم."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of pronoun is 'this'?",
        "options": ["personal pronoun", "possessive pronoun", "demonstrative pronoun", "relative pronoun"],
        "correct_option_id": 2,
        "explanation": "'this' ضمير إشارة (demonstrative pronoun)  يُشير إلى شيء قريب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat type of pronoun is 'who'?",
        "options": ["personal pronoun", "possessive pronoun", "demonstrative pronoun", "relative pronoun"],
        "correct_option_id": 3,
        "explanation": "'who' ضمير موصول (relative pronoun)  يُستخدم لربط جملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nReplace the underlined noun with a pronoun: The cat sat on the mat. The cat was fluffy.",
        "options": ["It", "He", "She", "They"],
        "correct_option_id": 0,
        "explanation": "القطة (cat)  اسم مفرد مؤنث.  نستخدم ضمير 'it'  لأنه ضمير مفرد مُحايد  ويُستخدم للأسماء الجامدة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nReplace the underlined noun with a pronoun: John went to the park. John had fun.",
        "options": ["She", "He", "It", "They"],
        "correct_option_id": 1,
        "explanation": "John اسم مفرد مذكر.  نستخدم ضمير 'he' لأنه ضمير مفرد مذكر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nReplace the underlined nouns with pronouns:  The boys played football. The boys were tired.",
        "options": ["They", "Them", "He", "She"],
        "correct_option_id": 0,
        "explanation": " 'boys' اسم جمع مذكر.  نستخدم ضمير 'They' لأنه ضمير جمع مذكر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich pronoun refers to the speaker?",
        "options": ["I", "you", "he", "she"],
        "correct_option_id": 0,
        "explanation": "ضمير 'I' (أنا) يشير إلى المتكلم."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich pronoun refers to the person being spoken to?",
        "options": ["I", "you", "he", "she"],
        "correct_option_id": 1,
        "explanation": "ضمير 'you' (أنت أو أنتم)  يشير إلى المخاطَب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich pronoun refers to a male person?",
        "options": ["I", "you", "he", "she"],
        "correct_option_id": 2,
        "explanation": "ضمير 'he' (هو)  يشير إلى شخص مذكر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich pronoun refers to a female person?",
        "options": ["I", "you", "he", "she"],
        "correct_option_id": 3,
        "explanation": "ضمير 'she' (هي)  يشير إلى شخص مؤنث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich pronoun refers to things?",
        "options": ["I", "you", "it", "they"],
        "correct_option_id": 2,
        "explanation": "ضمير 'it' (هو/هي) يُستخدم للأسماء المفردة الجامدة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich pronoun refers to people or things in a plural sense?",
        "options": ["I", "you", "it", "they"],
        "correct_option_id": 3,
        "explanation": "ضمير 'they' (هم/هن) يُستخدم للأسماء الجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive pronoun of 'I'?",
        "options": ["me", "mine", "my", "myself"],
        "correct_option_id": 1,
        "explanation": "ضمير الملكية لـ 'I' هو 'mine'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive pronoun of 'she'?",
        "options": ["her", "hers", "herself", "she's"],
        "correct_option_id": 1,
        "explanation": "ضمير الملكية لـ 'she' هو 'hers'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive pronoun of 'they'?",
        "options": ["them", "theirs", "their", "themselves"],
        "correct_option_id": 1,
        "explanation": "ضمير الملكية لـ 'they' هو 'theirs'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive pronoun of 'we'?",
        "options": ["us", "ours", "our", "ourselves"],
        "correct_option_id": 1,
        "explanation": "ضمير الملكية لـ 'we' هو 'ours'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the possessive pronoun of 'you'?",
        "options": ["your", "yours", "yourself", "yourselves"],
        "correct_option_id": 1,
        "explanation": "ضمير الملكية لـ 'you' هو 'yours'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the reflexive pronoun of 'I'?",
        "options": ["me", "mine", "my", "myself"],
        "correct_option_id": 3,
        "explanation": "الضمير الانعكاسي لـ 'I' هو 'myself'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the reflexive pronoun of 'he'?",
        "options": ["him", "his", "himself", "he's"],
        "correct_option_id": 2,
        "explanation": "الضمير الانعكاسي لـ 'he' هو 'himself'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the reflexive pronoun of 'she'?",
        "options": ["her", "hers", "herself", "she's"],
        "correct_option_id": 2,
        "explanation": "الضمير الانعكاسي لـ 'she' هو 'herself'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the reflexive pronoun of 'it'?",
        "options": ["its", "it's", "itself", "itsself"],
        "correct_option_id": 2,
        "explanation": "الضمير الانعكاسي لـ 'it' هو 'itself'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the reflexive pronoun of 'we'?",
        "options": ["us", "ours", "our", "ourselves"],
        "correct_option_id": 3,
        "explanation": "الضمير الانعكاسي لـ 'we' هو 'ourselves'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the reflexive pronoun of 'you'?",
        "options": ["your", "yours", "yourself", "yourselves"],
        "correct_option_id": 2,
        "explanation": "الضمير الانعكاسي لـ 'you' هو 'yourself' (مفرد) أو 'yourselves' (جمع)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhat is the reflexive pronoun of 'they'?",
        "options": ["them", "theirs", "their", "themselves"],
        "correct_option_id": 3,
        "explanation": "الضمير الانعكاسي لـ 'they' هو 'themselves'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my book.",
        "options": ["He", "She", "This", "That"],
        "correct_option_id": 2,
        "explanation": "This هو ضمير إشارة (demonstrative pronoun)  ويُستخدم للإشارة إلى شيء قريب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is her bag.",
        "options": ["He", "She", "This", "That"],
        "correct_option_id": 1,
        "explanation": "She هو ضمير شخصي (personal pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  I gave the book to ____.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my friend.",
        "options": ["He", "Him", "His", "himself"],
        "correct_option_id": 0,
        "explanation": "He هو ضمير شخصي (personal pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  The book is ____.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 2,
        "explanation": "his هو ضمير ملكية (possessive pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  I bought it for ____.",
        "options": ["me", "I", "mine", "myself"],
        "correct_option_id": 0,
        "explanation": "me هو ضمير مفعول به (object pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my car.",
        "options": ["It", "He", "She", "They"],
        "correct_option_id": 0,
        "explanation": "It هو ضمير شخصي (personal pronoun) يُستخدم للجماد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ are my friends.",
        "options": ["He", "She", "They", "Them"],
        "correct_option_id": 2,
        "explanation": "They هو ضمير شخصي (personal pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I saw ____ at the park.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  The house is ____.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 2,
        "explanation": "his هو ضمير ملكية (possessive pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  She made it for ____.",
        "options": ["her", "she", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my sister.",
        "options": ["She", "Her", "Hers", "Herself"],
        "correct_option_id": 0,
        "explanation": "She هو ضمير شخصي (personal pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I gave the flowers to ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 1,
        "explanation": "her هو ضمير مفعول به (object pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The car is ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  He is talking to ____.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my book.",
        "options": ["This", "That", "These", "Those"],
        "correct_option_id": 0,
        "explanation": "This هو ضمير إشارة (demonstrative pronoun) يُستخدم للإشارة إلى شيء قريب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ are my pens.",
        "options": ["This", "That", "These", "Those"],
        "correct_option_id": 2,
        "explanation": "These هو ضمير إشارة (demonstrative pronoun) يُستخدم للإشارة إلى أشياء قريبة جمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I gave the present to ____.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my brother.",
        "options": ["Him", "He", "His", "himself"],
        "correct_option_id": 1,
        "explanation": "He هو ضمير شخصي (personal pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The bike is ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  The books are ____.",
        "options": ["them", "they", "their", "theirs"],
        "correct_option_id": 2,
        "explanation": "theirs هو ضمير ملكية (possessive pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I wrote a letter to ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 1,
        "explanation": "her هو ضمير مفعول به (object pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  The house is ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  I gave the flowers to ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 1,
        "explanation": "her هو ضمير مفعول به (object pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my cat.",
        "options": ["She", "Her", "Hers", "Herself"],
        "correct_option_id": 0,
        "explanation": "She هو ضمير شخصي (personal pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The dogs are ____.",
        "options": ["it", "its", "them", "they"],
        "correct_option_id": 2,
        "explanation": "them هو ضمير مفعول به (object pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  I spoke to ____ yesterday.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The pen is ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  I gave the book to ____.",
        "options": ["them", "they", "their", "theirs"],
        "correct_option_id": 2,
        "explanation": "theirs هو ضمير ملكية (possessive pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my friend.",
        "options": ["Him", "He", "His", "himself"],
        "correct_option_id": 1,
        "explanation": "He هو ضمير شخصي (personal pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The toys are ____.",
        "options": ["it", "its", "them", "they"],
        "correct_option_id": 2,
        "explanation": "them هو ضمير مفعول به (object pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  I talked to ____ on the phone.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 1,
        "explanation": "her هو ضمير مفعول به (object pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The bag is ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my mother.",
        "options": ["She", "Her", "Hers", "Herself"],
        "correct_option_id": 0,
        "explanation": "She هو ضمير شخصي (personal pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The pencils are ____.",
        "options": ["it", "its", "them", "they"],
        "correct_option_id": 2,
        "explanation": "them هو ضمير مفعول به (object pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  I helped ____ with their homework.",
        "options": ["them", "they", "their", "theirs"],
        "correct_option_id": 0,
        "explanation": "them هو ضمير مفعول به (object pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The car is ____.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 2,
        "explanation": "his هو ضمير ملكية (possessive pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I spoke to ____ on the phone.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The books belong to ____.",
        "options": ["them", "they", "their", "theirs"],
        "correct_option_id": 3,
        "explanation": "theirs هو ضمير ملكية (possessive pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my father.",
        "options": ["Him", "He", "His", "himself"],
        "correct_option_id": 1,
        "explanation": "He هو ضمير شخصي (personal pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I gave the gift to ____.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  The bicycle is ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد (although a bicycle is not grammatically feminine, this is a test of pronoun usage)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  The apples are ____.",
        "options": ["it", "its", "them", "they"],
        "correct_option_id": 2,
        "explanation": "them هو ضمير مفعول به (object pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  I will give it to ____.",
        "options": ["them", "they", "their", "theirs"],
        "correct_option_id": 0,
        "explanation": "them هو ضمير مفعول به (object pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The house is ____.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 2,
        "explanation": "his هو ضمير ملكية (possessive pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I sent a message to ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 1,
        "explanation": "her هو ضمير مفعول به (object pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: That is ____ book.",
        "options": ["This", "That", "These", "Those"],
        "correct_option_id": 1,
        "explanation": "That هو ضمير إشارة (demonstrative pronoun) يُستخدم للإشارة إلى شيء بعيد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: Those are ____ cars.",
        "options": ["This", "That", "These", "Those"],
        "correct_option_id": 3,
        "explanation": "Those هو ضمير إشارة (demonstrative pronoun) يُستخدم للإشارة إلى أشياء بعيدة جمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  The dog chased ____.",
        "options": ["it", "its", "them", "they"],
        "correct_option_id": 2,
        "explanation": "them هو ضمير مفعول به (object pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The shoes belong to ____.",
        "options": ["them", "they", "their", "theirs"],
        "correct_option_id": 3,
        "explanation": "theirs هو ضمير ملكية (possessive pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I talked to ____ about it.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The gift is ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my pen.",
        "options": ["She", "Her", "Hers", "Herself"],
        "correct_option_id": 2,
        "explanation": "Hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد،  و لكن يمكن استخدامها هنا للإشارة إلى ملكية غير محددة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The cats are ____.",
        "options": ["it", "its", "them", "they"],
        "correct_option_id": 2,
        "explanation": "them هو ضمير مفعول به (object pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I gave the toys to ____.",
        "options": ["them", "they", "their", "theirs"],
        "correct_option_id": 0,
        "explanation": "them هو ضمير مفعول به (object pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The books are ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد (although books are not grammatically feminine, this is a test of pronoun usage)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I saw ____ at the party.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The car belongs to ____.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 2,
        "explanation": "his هو ضمير ملكية (possessive pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I gave the cake to ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 1,
        "explanation": "her هو ضمير مفعول به (object pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The flowers are ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد (although flowers are not grammatically feminine, this is a test of pronoun usage)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I talked to ____ about the problem.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The bike is ____.",
        "options": ["she", "her", "hers", "herself"],
        "correct_option_id": 2,
        "explanation": "hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد (although a bicycle is not grammatically feminine, this is a test of pronoun usage)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: The books are ____.",
        "options": ["them", "they", "their", "theirs"],
        "correct_option_id": 3,
        "explanation": "theirs هو ضمير ملكية (possessive pronoun) للجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  I gave the present to ____.",
        "options": ["him", "he", "his", "himself"],
        "correct_option_id": 0,
        "explanation": "him هو ضمير مفعول به (object pronoun) للمذكر المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun:  ____ is my bag.",
        "options": ["She", "Her", "Hers", "Herself"],
        "correct_option_id": 2,
        "explanation": "Hers هو ضمير ملكية (possessive pronoun) للمؤنث المفرد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the correct pronoun: I helped ____ with the project.",
        "options": ["them", "they", "their", "theirs"],
        "correct_option_id": 0,
        "explanation": "them هو ضمير مفعول به (object pronoun) للجمع."
    },],
    "حروف الجر": [
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: The book is ____ the table.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنّه يُشير إلى وضع الشيء (الكتاب) على سطح آخر (الطاولة).  حروف الجرّ تُعبّر عن علاقة مكانية أو زمانية بين الكلمات في الجملة.  'On'  تُستخدم للتعبير عن  الوضع على سطح، بينما 'in'  للدلالة على الوضع داخل شيء ما، و'at'  للمكان، و'to'  للتحرك نحو مكان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The cat is sitting ____ the mat.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع القطة على سطح البساط.  حرف الجرّ 'on' يُعبّر عن علاقة مكانية، حيث يكون الشيء الموضوع على سطح آخر.  'At' تُشير إلى مكان محدد، و'in' تُشير إلى مكان مغلق، و'to'  تُشير إلى اتجاه."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: The pen is ____ the box.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنّه يُشير إلى وضع القلم داخل الصندوق.  حرف الجرّ 'in'  يُعبّر عن علاقة مكانية، حيث يكون الشيء الموضوع داخل شيء آخر.  'On'  تُستخدم للوضع على سطح، و'at'  للمكان، و'to'  للتحرك نحو مكان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I live ____ London.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنّه يُشير إلى  الموقع داخل مدينة.  حرف الجرّ 'in'  يُستخدم مع المدن والبلدان.  'On'  تُستخدم مع الأسطح، و'at'  مع الأماكن الصغيرة، و'to'  تُشير إلى  اتجاه."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: The meeting is ____ 2 PM.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى وقت مُحدد.  'at'  تُستخدم مع الأوقات المحددة.  'On'  تُستخدم مع أيام الأسبوع أو التواريخ، و'in'  مع الشهور أو السنوات، و'to'  للتحرك نحو مكان أو زمان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: The party is ____ Friday.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى يوم من أيام الأسبوع. 'on' تُستخدم مع أيام الأسبوع والتواريخ.  'At'  تُستخدم مع الأوقات المحددة، و'in'  مع الشهور أو السنوات، و'to'  للتحرك نحو مكان أو زمان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  My birthday is ____ December.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى شهر.  'in'  تُستخدم مع الشهور والسنوات.  'On'  تُستخدم مع أيام الأسبوع أو التواريخ، و'at'  مع الأوقات المحددة، و'to'  للتحرك نحو مكان أو زمان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I was born ____ 1990.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى سنة.  'in'  تُستخدم مع السنوات.  'On'  تُستخدم مع أيام الأسبوع أو التواريخ، و'at'  مع الأوقات المحددة، و'to'  للتحرك نحو مكان أو زمان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm going ____ the park.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 3,
        "explanation": "استخدمنا حرف الجرّ 'to'  لأنه يُشير إلى اتجاه الحركة.  'to' تُستخدم للتعبير عن اتجاه الحركة نحو مكان.  'On'  تُستخدم مع الأسطح، و'at'  مع الأماكن الصغيرة، و'in'  مع الأماكن الكبيرة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She walked ____ the road.",
        "options": ["on", "at", "in", "across"],
        "correct_option_id": 3,
        "explanation": "استخدمنا حرف الجرّ 'across' لأنه يُشير إلى الحركة من جانب إلى آخر عبر سطح.  'across'  تُعبّر عن الحركة العرضية عبر سطح،  بينما 'on'  تُعبّر عن الوضع على السطح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He sat ____ the chair.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الشخص على سطح الكرسي.  حرف الجرّ 'on' يُعبّر عن علاقة مكانية، حيث يكون الشيء الموضوع على سطح آخر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The picture is ____ the wall.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الصورة على سطح الحائط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The book is ____ the shelf.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الكتاب على سطح الرف."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The keys are ____ the table.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع المفاتيح على سطح الطاولة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: The cat is sleeping ____ the box.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى وضع القطة داخل الصندوق."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: The bird is singing ____ the tree.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الطائر على سطح الشجرة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I put the money ____ my pocket.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى وضع المال داخل الجيب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He is waiting ____ the bus stop.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى مكان محدد (موقف الحافلة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She lives ____ a small village.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى موقع داخل مكان (قرية)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The dog is running ____ the park.",
        "options": ["on", "at", "in", "through"],
        "correct_option_id": 3,
        "explanation": "استخدمنا حرف الجرّ 'through'  لأنه يُشير إلى الحركة من خلال مكان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I walked ____ the street.",
        "options": ["on", "at", "in", "down"],
        "correct_option_id": 3,
        "explanation": "استخدمنا حرف الجرّ 'down'  لأنه يُشير إلى الحركة  على طول الطريق."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She is sitting ____ the table.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الشخص على سطح الطاولة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The plane is flying ____ the clouds.",
        "options": ["on", "at", "above", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'above'  لأنه يُشير إلى مكان أعلى من مكان آخر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: The cat jumped ____ the wall.",
        "options": ["on", "at", "over", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'over'  لأنه يُشير إلى الحركة فوق شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I live ____ 10 Downing Street.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى مكان محدد (عنوان)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The meeting is scheduled ____ 3 PM.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى وقت مُحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm going to the store ____ the afternoon.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى فترة زمنية (بعد الظهر)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: The train arrived ____ time.",
        "options": ["in", "at", "on", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى وقت مُحدد (في الوقت المحدد)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The concert is ____ 7 PM.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى وقت مُحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm leaving ____ London next week.",
        "options": ["from", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'from'  لأنه يُشير إلى  البداية  او المنشأ  للحركة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She's traveling ____ Paris.",
        "options": ["to", "at", "in", "on"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'to'  لأنه يُشير إلى اتجاه  الحركة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The book fell ____ the table.",
        "options": ["on", "off", "in", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'off'  لأنه يُشير إلى الحركة من على سطح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He walked ____ the street.",
        "options": ["on", "at", "along", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'along'  لأنه يُشير إلى الحركة  على طول شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The bird flew ____ the trees.",
        "options": ["on", "at", "among", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'among'  لأنه يُشير إلى  الوضع  بين عدة أشياء."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The dog is hiding ____ the bed.",
        "options": ["on", "at", "under", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'under'  لأنه يُشير إلى  الوضع  تحت شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm going to meet my friend ____ the cafe.",
        "options": ["in", "at", "on", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى  مكان صغير ومحددّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She's going to work ____ bus.",
        "options": ["by", "on", "in", "at"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'by'  لأنه يُشير إلى وسيلة المواصلات."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The book is ____ the floor.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الكتاب على سطح الأرض."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm waiting ____ my friend.",
        "options": ["for", "to", "at", "on"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'for'  لأنه يُشير إلى الانتظار لشخص ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She's looking ____ her keys.",
        "options": ["for", "to", "at", "on"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'for'  لأنه يُشير إلى البحث عن شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He's talking ____ his friend.",
        "options": ["to", "at", "on", "with"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'to'  لأنه يُشير إلى التحدث مع شخص ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm listening ____ music.",
        "options": ["to", "at", "on", "with"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'to'  لأنه يُشير إلى الاستماع إلى شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She's walking ____ the park.",
        "options": ["through", "across", "along", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'along'  لأنه يُشير إلى الحركة على طول شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The plane flew ____ the mountains.",
        "options": ["over", "above", "on", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'over'  لأنه يُشير إلى الحركة فوق شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He jumped ____ the fence.",
        "options": ["over", "above", "on", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'over'  لأنه يُشير إلى الحركة فوق شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She's looking ____ a new job.",
        "options": ["for", "to", "at", "on"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'for'  لأنه يُشير إلى  البحث عن شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He's waiting ____ his friend.",
        "options": ["for", "to", "at", "on"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'for'  لأنه يُشير إلى  الانتظار لشخص ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The car is parked ____ the building.",
        "options": ["beside", "besides", "besides", "by"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'beside'  لأنه يُشير إلى  الوضع  بجانب شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The bird is sitting ____ a branch.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى  الوضع  على سطح  شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm going to travel ____ train.",
        "options": ["by", "on", "in", "at"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'by'  لأنه يُشير إلى وسيلة المواصلات."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: The cat is hiding ____ the sofa.",
        "options": ["behind", "before", "after", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'behind'  لأنه يُشير إلى  الوضع  خلف شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I'm walking ____ the street.",
        "options": ["along", "across", "through", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'along'  لأنه يُشير إلى  الحركة  على طول شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The book is ____ the desk.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الكتاب على سطح المكتب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The dog is playing ____ the garden.",
        "options": ["in", "at", "on", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى  الوضع  داخل مكان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm going to meet you ____ 5 o'clock.",
        "options": ["in", "at", "on", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى وقت محدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The plane is flying ____ the city.",
        "options": ["above", "over", "on", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'above'  لأنه يُشير إلى مكان أعلى من مكان آخر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm waiting ____ the bus.",
        "options": ["for", "to", "at", "on"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'for'  لأنه يُشير إلى الانتظار لشخص أو شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She's angry ____ me.",
        "options": ["to", "at", "on", "with"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى الغضب من شخص ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He's good ____ sports.",
        "options": ["at", "in", "on", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى  إتقان  شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She's interested ____ learning new languages.",
        "options": ["in", "at", "on", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى الاهتمام بشيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The dog is running ____ the street.",
        "options": ["across", "along", "through", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'across'  لأنه يُشير إلى الحركة من جانب إلى آخر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The bird is flying ____ the sky.",
        "options": ["through", "across", "along", "above"],
        "correct_option_id": 3,
        "explanation": "استخدمنا حرف الجرّ 'above'  لأنه يُشير إلى  الوضع  فوق شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm waiting ____ my friend to arrive.",
        "options": ["for", "to", "at", "on"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'for'  لأنه يُشير إلى  الانتظار لشخص ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He's looking ____ his keys.",
        "options": ["for", "to", "at", "on"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'for'  لأنه يُشير إلى  البحث عن شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The picture is ____ the wall.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الصورة على سطح الحائط.  'on' يُستخدم للوضع على سطح مستوٍ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The cat is sleeping ____ the bed.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع القطة على سطح السرير.  'on'  يُستخدم للوضع على سطح مستوٍ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He's sitting ____ a chair.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الشخص على سطح الكرسي.  'on'  يُستخدم للوضع على سطح مستوٍ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The book is ____ the table.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الكتاب على سطح الطاولة.  'on'  يُستخدم للوضع على سطح مستوٍ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: The keys are ____ the drawer.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى وضع المفاتيح داخل الدرج.  'in'  يُستخدم للوضع داخل مكان مغلق."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The pen is ____ the desk.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع القلم على سطح المكتب.  'on'  يُستخدم للوضع على سطح مستوٍ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The picture is ____ the wall.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع الصورة على سطح الحائط.  'on'  يُستخدم للوضع على سطح مستوٍ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The flower is ____ the vase.",
        "options": ["in", "at", "on", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى  الوضع  داخل شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The cat is sitting ____ the sofa.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'on'  لأنه يُشير إلى وضع القطة على سطح الأريكة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm going to meet you ____ the library.",
        "options": ["in", "at", "on", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى  مكان محددّ وصغير نسبيًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She arrived ____ the airport.",
        "options": ["in", "at", "on", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى  مكان محددّ وصغير نسبيًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He's waiting ____ the corner.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى  مكان محددّ وصغير نسبيًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The dog is running ____ the street.",
        "options": ["through", "across", "along", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'along'  لأنه يُشير إلى  الحركة  على طول شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She walked ____ the park.",
        "options": ["through", "across", "along", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'through'  لأنه يُشير إلى الحركة من خلال مكان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The bird is flying ____ the trees.",
        "options": ["on", "at", "among", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'among'  لأنه يُشير إلى  الوضع  بين عدة أشياء."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I'm walking ____ the street.",
        "options": ["along", "across", "through", "to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا حرف الجرّ 'along'  لأنه يُشير إلى الحركة على طول شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  The cat is hiding ____ the chair.",
        "options": ["on", "at", "in", "to"],
        "correct_option_id": 2,
        "explanation": "استخدمنا حرف الجرّ 'in'  لأنه يُشير إلى  الوضع  داخل شيء ما."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I'm going to meet you ____ the library.",
        "options": ["in", "at", "on", "to"],
        "correct_option_id": 1,
        "explanation": "استخدمنا حرف الجرّ 'at'  لأنه يُشير إلى  مكان محددّ وصغير نسبيًا."
    },],
    
    "حروف العطف": [
            {
        "question": "اختر الإجابة الصحيحة:\nIdentify the conjunction in the sentence: 'The sun is shining, and the birds are singing'.",
        "options": ["sun", "shining", "and", "birds"],
        "correct_option_id": 2,
        "explanation": "كلمة 'and'  حرف عطف (conjunction) لأنها تربط جملتين أو فكرتين مستقلتين.  حروف العطف تُستخدم لربط الكلمات أو الجمل أو الفقرات مع بعضها البعض،  وتُظهر العلاقة بينها.  'and'  تُشير إلى إضافة أو جمع فكرتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich conjunction shows a choice between two things?",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 2,
        "explanation": "حرف العطف 'or'  يُستخدم للتعبير عن الاختيار بين شيئين أو أكثر.  يُعطي  'or'  المتلقي خيارًا بين احتمالات مختلفة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich conjunction shows contrast or opposition?",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 1,
        "explanation": "حرف العطف 'but' يُستخدم للتعبير عن التناقض أو التضاد بين فكرتين.  'but'  يوضح وجود اختلاف أو تباين بين جملتين أو فكرتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich conjunction shows a result or consequence?",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "حرف العطف 'so' يُستخدم للتعبير عن نتيجة أو عاقبة فعلٍ ما.  'so'  يوضح وجود علاقة سببية بين جملتين،  حيث يكون الجملة الثانية نتيجة للجملة الأولى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich conjunction means 'because'?",
        "options": ["and", "but", "or", "because"],
        "correct_option_id": 3,
        "explanation": " 'because' حرف عطف سببيّ (subordinating conjunction) يُشير إلى السبب أو التفسير."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich conjunction means 'although'?",
        "options": ["although", "and", "but", "so"],
        "correct_option_id": 0,
        "explanation": "'although' حرف عطف تنازل (subordinating conjunction) يُشير إلى تنازل أو استثناء."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich conjunction means 'if'?",
        "options": ["if", "and", "but", "so"],
        "correct_option_id": 0,
        "explanation": "'if' حرف عطف شرط (subordinating conjunction) يُشير إلى شرط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich conjunction means 'when'?",
        "options": ["when", "and", "but", "so"],
        "correct_option_id": 0,
        "explanation": "'when' حرف عطف زمان (subordinating conjunction) يُشير إلى وقت حدوث الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich conjunction means 'since'?",
        "options": ["since", "and", "but", "so"],
        "correct_option_id": 0,
        "explanation": "'since' حرف عطف زمان (subordinating conjunction) يُشير إلى وقت بدء الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich conjunction means 'until'?",
        "options": ["until", "and", "but", "so"],
        "correct_option_id": 0,
        "explanation": "'until' حرف عطف زمان (subordinating conjunction) يُشير إلى وقت استمرار الفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'It was raining, ____ we stayed inside'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (البقاء في الداخل نتيجة المطر)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He was tired, ____ he went to bed'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (الذهاب إلى السرير نتيجة التعب)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She studied hard, ____ she passed the exam'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (النجاح في الامتحان نتيجة الدراسة الجادة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I like tea, ____ I don't like coffee'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'but'  لأنها تُعبّر عن التناقض بين إعجابي بالشاي وعدم إعجابي بالقهوة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'You can have tea, ____ you can have coffee'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'or'  لأنها تُعبّر عن الاختيار بين الشاي والقهوة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He is rich, ____ he is happy'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She is tired, ____ she will rest'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (الراحة نتيجة التعب)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He is tall, ____ his brother is short'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'but'  لأنها تُعبّر عن التناقض بين طول الأخ وقصر أخيه."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'Study hard, ____ you will pass the exam'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (النجاح نتيجة الدراسة الجادة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I will go to the party, ____ I'm busy'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'although'  لأنها تُعبّر عن تنازل (سأذهب رغم أنّي مشغول)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ it is raining, we will go out'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم المطر، سنخرج)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ you study hard, you will pass'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'If'  لأنها تُعبّر عن شرط (إذا درست بجد، ستنجح)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I will help you ____ you ask me'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'if'  لأنها تُعبّر عن شرط (سأساعدك إذا طلبت مني)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ I'm tired, I will finish my work'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم أنّي متعب، سأكمل عملي)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I will buy a car ____ I have enough money'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'if'  لأنها تُعبّر عن شرط (إذا كان لديّ مال كافٍ، سأشتري سيارة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He went home ____ he was tired'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'because'  لأنها تُعبّر عن سبب (ذهب إلى المنزل لأنه كان متعبًا)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ it was cold, she wore a coat'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنّها تُعبّر عن تنازل (رغم البرد، ارتدت معطفًا)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ you are busy, I will help you'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم انشغالك، سأساعدك)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I will go to the beach ____ the weather is nice'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'if'  لأنها تُعبّر عن شرط (إذا كان الطقس جيدًا، سأذهب إلى الشاطئ)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He is happy, ____ he is smiling'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تُعبّر عن إضافة جملة أخرى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She is tired, ____ she needs to rest'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (الراحة نتيجة التعب)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I like to read, ____ I like to watch movies'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He is studying, ____ his sister is playing'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين مستقلتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She is rich, ____ she is not happy'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'but'  لأنها تُعبّر عن التناقض بين الثراء وعدم السعادة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'They are hungry, ____ they will eat'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (الأكل نتيجة الجوع)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I will go to the park, ____ it rains'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'if'  لأنّها تُعبّر عن شرط (سأذهب إلى الحديقة إذا لم يمطر)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ he was tired, he finished the race'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم تعبه، أنهى السباق)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ it's cold outside, I'll wear a jacket'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم برودة الطقس، سأرتدي سترة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I'll buy a new phone ____ I save enough money'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'if'  لأنها تُعبّر عن شرط (إذا وفرت مالًا كافيًا، سأشتري هاتفًا جديدًا)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He's very happy, ____ he's smiling'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She's tired, ____ she's going to bed'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (الذهاب إلى السرير نتيجة التعب)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I want to eat, ____ I'm hungry'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (الرغبة في الأكل نتيجة الجوع)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He likes pizza, ____ he likes pasta'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She wants to go out, ____ she's busy'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'but'  لأنها تُعبّر عن التناقض بين الرغبة في الخروج والانشغال."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'Study hard, ____ you will fail the exam'.",
        "options": ["and", "but", "or", "otherwise"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'otherwise'  لأنها تُعبّر عن نتيجة عكسية (ستُفل إذا لم تدرس بجد)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I will go to the movies, ____ I have enough time'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'if'  لأنّها تُعبّر عن شرط (سأذهب إلى السينما إذا كان لديّ وقت كاف)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He stayed home ____ he was feeling ill'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'because'  لأنها تُعبّر عن سبب (بقي في المنزل لأنه كان يشعر بالمرض)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ she was tired, she continued working'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم تعبها، واصلت العمل)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ it's raining, we should take an umbrella'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم المطر، يجب أن نأخذ مظلة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I will go to the party, ____ I have to work late'.",
        "options": ["although", "because", "if", "even though"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'even though'  لأنها تُعبّر عن تنازل (سأذهب إلى الحفلة، رغم أنّي يجب أن أعمل متأخرًا)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He's very smart, ____ he's also very kind'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She's rich, ____ she's not generous'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'but'  لأنها تُعبّر عن التناقض بين الثراء وعدم الكرم."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I'm tired, ____ I'm going to sleep'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (الذهاب إلى النوم نتيجة التعب)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He likes to swim, ____ he likes to run'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She's happy, ____ she's smiling'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين تُعبّران عن نفس المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I will study hard, ____ I will pass the exam'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنّها تُعبّر عن نتيجة (النجاح هو نتيجة للدراسة الجادة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He is tall, ____ his sister is short'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'but'  لأنها تُعبّر عن التناقض بين طول الأخ وقصر أخته."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I'll go to the beach, ____ it doesn't rain'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'if'  لأنها تُعبّر عن شرط (سأذهب إلى الشاطئ إذا لم يمطر)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ he's tired, he'll finish the work'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم تعبه، سيكمل العمل)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ it's sunny, we'll go to the park'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم أنّ الجو مشمس، سنذهب إلى الحديقة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I want to buy a new car, ____ I don't have enough money'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'although'  لأنها تُعبّر عن تنازل (رغم أنّي أريد شراء سيارة جديدة، ليس لديّ مال كافٍ)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She's very happy, ____ she's smiling'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين،  وتُشير إلى إضافة معلومة أخرى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He's tall, ____ his brother is short'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'but'  لأنّها تُعبّر عن التناقض أو التباين بين طول الأخ وقصر أخيه."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I'm hungry, ____ I'm going to eat'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (سآكل لأنني جائع)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She likes to dance, ____ she likes to sing'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين تُعبّران عن هوايتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He's tired, ____ he's not going to work'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنّها تُعبّر عن نتيجة (عدم الذهاب إلى العمل نتيجة التعب)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I'll go to the beach, ____ the weather is good'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'if'  لأنها تُعبّر عن شرط (سأذهب إلى الشاطئ إذا كان الطقس جيدًا)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ it's raining, we'll stay inside'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم المطر، سنبقى في الداخل)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ he's busy, he'll call later'.",
        "options": ["Although", "Because", "If", "So"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'Although'  لأنها تُعبّر عن تنازل (رغم انشغاله، سيتصل لاحقًا)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I will buy a new car, ____ I save enough money'.",
        "options": ["although", "because", "if", "so"],
        "correct_option_id": 2,
        "explanation": "نستخدم 'if'  لأنها تُعبّر عن شرط (إذا وفرت مالًا كافيًا، سأشتري سيارة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She's very tired, ____ she's going to bed'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (الذهاب إلى السرير نتيجة التعب)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He's happy, ____ he's smiling'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين،  وتُشير إلى إضافة معلومة أخرى.  هناك علاقة ترابط بين الجملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She's intelligent, ____ she's not hardworking'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'but'  لأنها تُعبّر عن التناقض بين الذكاء وعدم الاجتهاد.  'but'  تُشير إلى وجود اختلاف بين جملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I'm hungry, ____ I'm going to eat something'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (الرغبة في الأكل نتيجة الجوع).  'so'  تُشير إلى وجود علاقة سببية بين جملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He likes to play football, ____ he likes to play basketball'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين،  وتُشير إلى إضافة هواية أخرى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She's very kind, ____ she's also very generous'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين تُعبّران عن صفتين إيجابيتين للشخص."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I'll study hard, ____ I'll pass the exam'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنّها تُعبّر عن نتيجة (النجاح هو نتيجة للدراسة الجادة)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'He's intelligent, ____ he's not hardworking'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 1,
        "explanation": "نستخدم 'but'  لأنها تُعبّر عن التناقض بين الذكاء وعدم الاجتهاد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I'm tired, ____ I'm going to bed'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'so'  لأنها تُعبّر عن نتيجة (الذهاب إلى السرير نتيجة التعب)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'I like coffee, ____ I also like tea'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين تُعبّران عن هوايتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'She's very kind, ____ she is also very helpful'.",
        "options": ["and", "but", "or", "so"],
        "correct_option_id": 0,
        "explanation": "نستخدم 'and'  لأنها تربط جملتين إيجابيتين تُعبّران عن صفتين إيجابيتين للشخص."
    },
    ],
    "أدوات التعريف": [
            {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I saw ____ dog in the park.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن.  'dog' اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (d)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I saw ____ elephant at the zoo.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  'elephant' اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (e)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____ sun is shining today.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  قبل اسم يُشار إليه بشكل محددّ.  الشمس شيء واحد معروف، لذا نستخدم 'the'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I like to drink ____ milk.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّ مادة (no article)  قبل الأسماء غير القابلة للعدّ.  'milk' اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is ____ teacher.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن.  'teacher' اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (t)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He is ____ honest man.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  'honest' اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (h)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  ____ Earth is round.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ الأرض شيء واحد معروف."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I like to eat ____ apples.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن. apples جمع، لذا لا نحتاج لأي مادة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He plays ____ guitar.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن.  guitar اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (g)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is reading ____ book.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن. book اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (b)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I need ____ umbrella.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن.  umbrella اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (u)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I saw ____ orange.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  orange اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (o)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  ____ Amazon River is very long.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ نهر الأمازون معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I like to drink ____ tea.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّ مادة (no article)  قبل الأسماء غير القابلة للعدّ. tea اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He is ____ engineer.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن.  engineer اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (e)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She is ____ honest person.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  honest اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (h)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____ Nile River is in Egypt.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ نهر النيل معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I like to eat ____ rice.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّ مادة (no article)  قبل الأسماء غير القابلة للعدّ.  rice اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He plays ____ piano.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  piano اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (p)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is reading ____ interesting book.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  interesting اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (i)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I need ____ apple.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن. apple اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (a)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I saw ____ bird in the tree.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن. bird اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (b)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I ate ____ orange for breakfast.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. orange اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (o)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____ Pacific Ocean is very large.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ المحيط الهاديّ معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I like to eat ____ bread.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّ مادة (no article)  قبل الأسماء غير القابلة للعدّ.  bread اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He is ____ doctor.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن.  doctor اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (d)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is ____ intelligent student.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  intelligent اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (i)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____ Amazon rainforest is very large.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ غابة الأمازون معروفة ومحددة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I drink ____ water every day.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّ مادة (no article)  قبل الأسماء غير القابلة للعدّ.  water اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He plays ____ basketball.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن. basketball اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (b)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is reading ____ book about history.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. book اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (i)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I need ____ hour to finish my work.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. hour اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (h)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  ____ Eiffel Tower is in Paris.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ برج إيفل معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I eat ____ apple every day.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن. apple اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (a)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is ____ university student.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. university اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (u)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____ Sahara Desert is very hot.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ صحراء الصحراء معروفة ومحددة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I like to drink ____ coffee.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّ مادة (no article)  قبل الأسماء غير القابلة للعدّ. coffee اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He is ____ teacher.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن. teacher اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (t)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She is ____ honest person.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  honest اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (h)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____ Mediterranean Sea is warm.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ البحر الأبيض المتوسط معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I like to eat ____ bananas.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أي مادة (no article) مع الأسماء  الجمع القابلة للعد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He plays ____ violin.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. violin اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (v)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is reading ____ interesting novel.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. novel اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (i)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I need ____ orange juice.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. orange اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (o)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I saw ____  unique bird in the forest.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  unique اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (u)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____ Red Sea is known for its warm water.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ البحر الأحمر معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I like to eat ____ pasta.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أي مادة (no article) مع الأسماء  غير قابلة للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He is ____ excellent student.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  excellent اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (e)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is ____ experienced teacher.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  experienced اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (e)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____ Mount Everest is the highest mountain in the world.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ جبل إيفرست معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I like to drink ____ juice.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّ مادة (no article)  قبل الأسماء غير القابلة للعدّ. juice اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He plays ____ guitar very well.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن. guitar اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (g)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is reading ____ interesting story.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  story اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (i)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I need ____  umbrella to stay dry.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن.  umbrella اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (u)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I saw ____ unique painting at the museum.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  unique اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (u)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____  Nile River is the longest river in Africa.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ نهر النيل معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I like to eat ____  soup.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أي مادة (no article) مع الأسماء  غير قابلة للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He is ____  experienced pilot.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. experienced اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (e)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is ____  intelligent girl.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  intelligent اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (i)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____  Amazon rainforest is home to many animals.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ غابة الأمازون معروفة ومحددة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I drink ____  milk every morning.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّة مادة (no article)  قبل الأسماء غير القابلة للعدّ. milk اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He plays ____  basketball every weekend.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن.  basketball اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (b)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She is reading ____  exciting book.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. exciting اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (e)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I need ____  hour to finish this exercise.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. hour اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (h)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  ____  Statue of Liberty is in New York.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ تمثال الحرية معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  I eat ____  banana every morning.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن. banana اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (b)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She is ____  ambitious woman.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  ambitious اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (a)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  ____  Great Wall of China is a famous landmark.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ سور الصين العظيم معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I like to drink ____  juice in the morning.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّة مادة (no article)  قبل الأسماء غير القابلة للعدّ.  juice اسم غير قابل للعدّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He is ____  honest boy.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. honest اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (h)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is ____  talented artist.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك. talented اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (a)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: ____  Eiffel Tower is a popular tourist attraction.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ برج إيفل معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I like to read ____ books.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّة مادة (no article) مع الأسماء  الجمع."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He plays ____  football every Sunday.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 0,
        "explanation": "نستخدم المادة غير المحددة 'a'  قبل اسم مفرد قابل للعدّ يبدأ بصوت ساكن.  football اسم مفرد قابل للعدّ ويبدأ بصوت ساكن (f)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She is learning to play ____  ukelele.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 1,
        "explanation": "نستخدم المادة غير المحددة 'an'  قبل اسم مفرد قابل للعدّ يبدأ بصوت متحرك.  ukelele اسم مفرد قابل للعدّ ويبدأ بصوت متحرك (u)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  ____  Amazon River flows through South America.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 2,
        "explanation": "نستخدم المادة المحددة 'the'  لأنّ نهر الأمازون معروف ومحدد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I prefer to drink ____ tea to coffee.",
        "options": ["a", "an", "the", "no article"],
        "correct_option_id": 3,
        "explanation": "لا نستخدم أيّة مادة (no article)  قبل الأسماء غير القابلة للعدّ.  tea اسم غير قابل للعدّ."
    },
    ],
    "الأفعال الناقصة": [
            {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I ____ go to the party tonight.",
        "options": ["can", "may", "might", "must"],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة، نستخدم الفعل  'can'  للتعبير عن القدرة أو الإمكانية.  'Can'  يُشير إلى امتلاك القدرة على القيام بالفعل،  وهو مناسب هنا لأنّ الجملة تتحدث عن إمكانية الذهاب إلى الحفلة.  'May'  تُشير إلى الإذن أو الاحتمال،  و'might'  إلى احتمال ضعيف، و'must'  إلى الوجوب أو الضرورة.  لذا، فإنّ  'can go'  هي  أكثر تعبيراً دقيقاً  في سياق هذه الجملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She ____ help you with your homework.",
        "options": ["can", "may", "might", "must"],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة، يُعبّر 'can' عن قدرة الفتاة على مساعدة الآخر في واجبه المنزلي.  'Can help'  تُشير إلى امتلاكها للقدرة والمهارة اللازمة للمساعدة.  تختلف الأفعال الشرطية الأخرى في المعنى: 'may'  تُعبّر عن الإذن أو الاحتمال،  و'might'  عن احتمال ضعيف، و'must'  عن الوجوب أو الضرورة.  لذا، فإن 'can help'  أكثر ملاءمةً  في هذا السياق."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: They ____ play football in the park.",
        "options": ["can", "may", "might", "must"],
        "correct_option_id": 0,
        "explanation": "في سياق هذه الجملة،  نستخدم 'can'  للتعبير عن إمكانية لعب كرة القدم في الحديقة.  'Can play'  تُشير إلى أنَّ لديهم القدرة والفرصة للعب،  وهو ما يناسب سياق الجملة.  الأفعال الشرطية الأخرى تحمل معانٍ مختلفة: 'may'  تُشير إلى الإذن أو الاحتمال،  و'might'  إلى احتمال ضعيف، و'must'  إلى الوجوب أو الضرورة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: We ____ go to the cinema later.",
        "options": ["may", "can", "might", "must"],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،  'may'  أكثر ملاءمةً للتعبير عن الاحتمال أو الإذن.  'May go'  تعني 'من المحتمل أن نذهب' أو 'يجوز لنا الذهاب'.  'Can'  يُشير إلى القدرة،  و'might'  إلى احتمال ضعيف، و'must'  إلى الوجوب.  لذا، فإن  'may' تُعبّر عن احتمالية الذهاب إلى السينما دون تأكيد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He ____ study harder for the exam.",
        "options": ["may", "can", "might", "must"],
        "correct_option_id": 3,
        "explanation": "نستخدم 'must'  لأنّ الجملة تُعبّر عن وجوب أو ضرورة الدراسة بجدّ من أجل النجاح في الامتحان.  'Must study'  تُشير إلى الالتزام بالدراسة الجادة.  'May'  تُشير إلى الاحتمال أو الإذن،  و'can'  إلى القدرة، و'might'  إلى احتمال ضعيف."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I ____ go to the doctor.",
        "options": ["must", "may", "might", "should"],
        "correct_option_id": 0,
        "explanation": " 'must go'  تُشير إلى وجوب أو ضرورة زيارة الطبيب، ربما بسبب وجود مشكلة صحية تستدعي ذلك.  'must'  يُعبّر عن  الالتزام أو الضرورة.  الأفعال الشرطية الأخرى تحمل معانٍ مختلفة: 'may'  تُشير إلى الإذن أو الاحتمال،  و'might'  إلى احتمال ضعيف، و'should'  إلى الاستشارة أو النصيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She ____ be at home now.",
        "options": ["might", "can", "may", "must"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'might'  للتعبير عن احتمال ضعيف لوجودها في المنزل الآن.  'Might be'  تُشير إلى احتمالية ضعيفة،  وليس يقينًا.  'Can'  يُعبّر عن القدرة،  و'may'  عن الإذن أو الاحتمال، و'must'  عن اليقين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: They ____ finish their work today.",
        "options": ["might", "can", "may", "should"],
        "correct_option_id": 3,
        "explanation": " 'should finish'  تُشير إلى أنّ من المستحسن أو المفضل أن يُنهوا عملهم اليوم،  ولكن ليس بالضرورة.  'should'  تُعبّر عن النصيحة أو الاستحباب،  وليس الوجوب أو اليقين.  'might'  تُشير إلى احتمال ضعيف،  و'can'  إلى القدرة، و'may'  إلى الإذن أو الاحتمال."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: We ____ leave now.",
        "options": ["should", "might", "may", "must"],
        "correct_option_id": 0,
        "explanation": " 'should leave'  تُشير إلى أنّ من المستحسن أو المفضل  المغادرة الآن.  'should'  تُعبّر عن  النصيحة أو الاستحباب،  وليس الوجوب أو اليقين.  'might'  تُشير إلى احتمال ضعيف،  و'may'  إلى الإذن أو الاحتمال، و'must'  إلى الوجوب أو الضرورة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He ____ be tired after that long journey.",
        "options": ["should", "might", "may", "must"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should'  للتعبير عن التوقع المنطقيّ.  بعد رحلة طويلة،  من المُتوقع أن يكون الشخص متعبًا.  'should be'  تُشير إلى  احتمالٍ كبير،  ولكن ليس يقينًا.  'might'  و'may'  تُشير أيضًا إلى الاحتمال، لكنّ 'should'  أكثر ملاءمةً  في هذا السياق،  لأنّ التعب نتيجة متوقعة للرحلة الطويلة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I ____ swim very well.",
        "options": ["can", "may", "might", "must"],
        "correct_option_id": 0,
        "explanation": "'can swim'  تُشير إلى قدرة المتكلم على السباحة.  'Can'  يُعبّر عن القدرة أو المهارة المكتسبة.  'May'  تُشير إلى الإذن أو الاحتمال،  و'might'  إلى احتمال ضعيف، و'must'  إلى الوجوب أو الضرورة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: She ____ come to the party.",
        "options": ["may", "can", "might", "must"],
        "correct_option_id": 2,
        "explanation": "استخدمنا 'might'  للتعبير عن احتمال ضعيف  لِحضورها الحفلة.  'Might come'  تُشير إلى احتمالية ضعيفة، وليس يقينًا.  'Can'  يُعبّر عن القدرة،  و'may'  عن الإذن أو الاحتمال الأقوى، و'must'  عن اليقين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: They ____ pass the exam.",
        "options": ["might", "can", "may", "should"],
        "correct_option_id": 2,
        "explanation": "استخدمنا 'may'  للتعبير عن احتمال نجاحهم في الامتحان.  'May pass'  تُشير إلى احتمالية النجاح،  وليس يقينًا.  'Might'  تُشير إلى احتمال ضعيف،  و'should'  إلى الاستحباب أو النصيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: We ____ go home now.",
        "options": ["should", "might", "may", "must"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should'  للتعبير عن  النصيحة أو الاستحباب.  'Should go'  تُشير إلى  أفضلية الذهاب إلى المنزل الآن،  ولكن ليس بالضرورة.  'Might'  و'may'  تُشير إلى  الاحتمال،  و'must'  إلى  الوجوب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He ____ be hungry after all that exercise.",
        "options": ["should", "might", "may", "must"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should'  للتعبير عن التوقع المنطقي.  بعد كل هذا التمرين،  من المُتوقع أن يكون الشخص جائعًا.  'Should be'  تُشير إلى احتمال كبير،  وليس يقينًا.  'Might'  و'may'  تُشير أيضًا إلى الاحتمال، لكنّ 'should'  أكثر ملاءمةً  في هذا السياق، لأنّ الجوع نتيجة متوقعة للتمرين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  You ____ smoke here.",
        "options": ["can", "may", "might", "must not"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'must not'  للتعبير عن  المنع الصريح.  'Must not smoke'  تعني 'يُمنع التدخين'  بشكل قاطع.  الأفعال الشرطية الأخرى  لا تُعبر عن  المنع بشكلٍ صريح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She ____  be at the library.",
        "options": ["might", "could", "would", "should"],
        "correct_option_id": 1,
        "explanation": "استخدمنا 'could'  للتعبير عن احتمال وجودها في المكتبة.  'Could be'  تُشير إلى إمكانية وجودها هناك،  وليس يقينًا.  'Might'  تُشير إلى احتمال ضعيف،  و'would'  إلى  الاستعداد، و'should'  إلى  الاستحباب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  They ____ finish the project by tomorrow.",
        "options": ["should", "might", "would", "ought to"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'ought to'  للتعبير عن  الواجب أو الاستحباب.  'Ought to finish'  تُشير إلى  وجوب  إتمام المشروع غدًا،  وهو تعبير قريب من 'should'  لكنّه أكثر رسميةً  في بعض الأحيان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: We ____  help her with her problem.",
        "options": ["should", "might", "could", "would"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should'  للتعبير عن  الاستحباب أو النصيحة.  'Should help'  تُشير إلى  أفضلية  مساعدتها،  ولكن ليس بالضرورة.  'Might'  تُشير إلى  إمكانية  المساعدة،  و'could'  إلى القدرة، و'would'  إلى  الاستعداد."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  He ____ be tired after running a marathon.",
        "options": ["should", "might", "may", "must"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'must'  للتعبير عن استنتاج قويّ.  بعد  ركضٍّ ماراثونيّ،  من  المتوقع  بشدة  أن يكون الشخص متعبًا.  'Must be'  تُشير إلى  يقينٍ  أو  استنتاجٍ قويّ  بناءً على  المعلومات  المتاحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I ____  go to work today, I'm sick.",
        "options": ["mustn't", "can't", "couldn't", "wouldn't"],
        "correct_option_id": 1,
        "explanation": "استخدمنا 'can't'  للتعبير عن عدم القدرة على الذهاب إلى العمل بسبب المرض.  'Can't go'  تُشير إلى  عدم  القدرة  الفيزيائية  أو  الظرفية  على القيام بالفعل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She ____ come to the meeting, she's busy.",
        "options": ["may not", "can't", "might not", "shouldn't"],
        "correct_option_id": 1,
        "explanation": "استخدمنا 'can't'  للتعبير عن عدم القدرة على الحضور بسبب انشغالها.  'Can't come'  تُشير إلى  عدم  وجود إمكانية للحضور،  لأنّها مشغولة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: They ____ be at home now, they're usually at work at this time.",
        "options": ["might not", "mustn't", "couldn't", "shouldn't"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'might not'  للتعبير عن احتمال ضعيف لوجودهم في المنزل الآن،  بناءً على  عادة  تواجدهم في العمل في هذا الوقت. 'Might not'  تُشير إلى  احتمال  ضعيف  وليس  يقينًا  أو  منعًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: We ____ go to the beach if the weather is good.",
        "options": ["should", "could", "would", "might"],
        "correct_option_id": 2,
        "explanation": "استخدمنا 'would'  للتعبير عن  الاحتمال  أو  النية  في  المستقبل  بشرط  تحقق  حدثٍ  آخر.  'Would go'  تُشير إلى نية الذهاب  إلى الشاطئ  إذا  سمح  الطقس  الجيد  بذلك."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He ____ help you if you ask him nicely.",
        "options": ["should", "could", "would", "might"],
        "correct_option_id": 2,
        "explanation": "استخدمنا 'would'  للتعبير عن  الاستعداد  للمساعدة  بشرط  طلب  المساعدة  بلطف. 'Would help'  تُشير إلى استعداده للمساعدة  إذا طلبت منه بلطف.  'Would'  يُستخدم  هنا  للتعبير عن شرط  و استعداد  مستقبليّ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: I ____  finish my work by tomorrow.",
        "options": ["will", "can", "ought to", "may"],
        "correct_option_id": 2,
        "explanation": "استخدمنا 'ought to'  للتعبير عن  الواجب  أو  الاستحباب.  'Ought to finish'  تُشير إلى  وجوب  إتمام العمل  غدًا،  وهو تعبير قريب من 'should'  لكنّه  أكثر رسميةً  في بعض الأحيان."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  She ____ be happy with her new job.",
        "options": ["ought to", "might", "should", "must"],
        "correct_option_id": 2,
        "explanation": "استخدمنا 'should'  للتعبير عن  التوقع  المنطقي.  من  المُتوقع  أن تكون سعيدة  بوظيفتها  الجديدة.  'Should be'  تُشير إلى  احتمالٍ  كبير،  ولكن  ليس  يقينًا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: They ____  go to the doctor, they're feeling ill.",
        "options": ["should", "might", "could", "would"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should'  للتعبير عن  النصيحة  أو  الاستحباب.  'Should go'  تُشير إلى  أفضلية  الذهاب  إلى  الطبيب  لأنّهم  يشعرون  بسوء  الصحة.  'Should'  تُعبّر  عن  نصيحةٍ  مُستحسنة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He ____ have finished his work by now.",
        "options": ["should", "would", "might", "ought to"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should'  للتعبير عن التوقع.  من المُتوقع  أن يكون قد انتهى من عمله  بحلول  الآن.  'Should have finished'  تُشير إلى  احتمالٍ  كبير  لحدوث  الفاعل  في الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  You ____  have studied harder for the test.",
        "options": ["ought to", "might have", "should have", "must have"],
        "correct_option_id": 2,
        "explanation": "استخدمنا 'should have'  للتعبير عن  اللوم  على  عدم  الدراسة  بجدّ  في  الماضي.  'Should have studied'  تُشير  إلى  أنّه  كان  يجب  عليه  أن  يدرس  أكثر،  وهو  يُعبّر عن  ندمٍ  أو  لومٍ  على  فعلٍ  ماضٍ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence:  They ____  have called by now.",
        "options": ["should have", "would have", "might have", "ought to have"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should have'  للتعبير عن  التوقع  المنطقيّ  في  الماضي.  من  المُتوقع  أن يكونوا  قد  اتصلوا  بحلول  الآن.  'Should have called'  تُشير إلى  احتمالٍ  كبير  لحدوث  الفعِل  في  الماضي،  ولكنّه  لم  يحدث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: We ____ have gone to the party.",
        "options": ["should have", "would have", "might have", "ought to have"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'ought to have'  للتعبير عن  اللوم  أو  الندم  على  عدم  الذهاب  إلى  الحفلة.  'Ought to have gone'  تُشير إلى  أنّه  كان  يجب  عليهما  أن  يذهبا،  وهو  يُعبّر عن  ندمٍ  أو  لومٍ  على  فعلٍ  ماضٍ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He ____ have been tired after the long walk.",
        "options": ["should have", "would have", "might have", "must have"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'must have'  للتعبير عن  الاستنتاج  القويّ  بناءً على  المعطيات.  بعد  مشيٍّ  طويل،  من  المُتوقع  بشدة  أن يكون  الشخص  متعبًا.  'Must have been'  تُشير  إلى  يقينٍ  أو  استنتاجٍ  قويّ  بناءً  على  المعلومات  المتاحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: You ____  told me earlier!",
        "options": ["should have", "would have", "might have", "ought to have"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should have'  للتعبير عن  اللوم  على  عدم  الإخبار  سابقًا.  'Should have told'  تُشير  إلى  أنّه  كان  يجب  عليه  أن  يخبر،  وهو  يُعبّر عن  ندمٍ  أو  لومٍ  على  فعلٍ  ماضٍ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: They ____ have finished the work by now.",
        "options": ["must have", "should have", "would have", "might have"],
        "correct_option_id": 1,
        "explanation": "استخدمنا 'should have'  للتعبير عن  التوقع  المنطقيّ  في  الماضي.  من  المُتوقع  أن يكونوا  قد  انتهوا  من  العمل  بحلول  الآن. 'Should have finished'  تُشير  إلى  احتمالٍ  كبير  لحدوث  الفعِل  في  الماضي،  ولكنّه  لم  يحدث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: We ____ have gone to the party.",
        "options": ["should have", "would have", "might have", "ought to have"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'ought to have'  للتعبير عن  اللوم  أو  الندم  على  عدم  الذهاب  إلى  الحفلة.  'Ought to have gone'  تُشير إلى  أنّه  كان  يجب  عليهما  أن  يذهبا،  وهو  يُعبّر عن  ندمٍ  أو  لومٍ  على  فعلٍ  ماضٍ،  مع  دلالة  أقوى  على  الواجب  من  'should have'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He ____ have been tired after the long walk.",
        "options": ["should have", "would have", "might have", "must have"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'must have'  للتعبير عن  الاستنتاج  القويّ  بناءً على  المعطيات.  بعد  مشيٍّ  طويل،  من  المُتوقع  بشدة  أن يكون  الشخص  متعبًا.  'Must have been'  تُشير  إلى  يقينٍ  أو  استنتاجٍ  قويّ  بناءً  على  المعلومات  المتاحة،  ويُعبّر  عن  درجة  عالية  من  الاحتمال."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: You ____  told me earlier!",
        "options": ["should have", "would have", "might have", "ought to have"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should have'  للتعبير عن  اللوم  على  عدم  الإخبار  سابقًا.  'Should have told'  تُشير  إلى  أنّه  كان  يجب  عليه  أن  يخبر،  وهو  يُعبّر عن  ندمٍ  أو  لومٍ  على  فعلٍ  ماضٍ.  'Should have'  تُستخدم  للتعبير عن  اللوم  أو  النصيحة  في  الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: They ____ have finished the work by now.",
        "options": ["must have", "should have", "would have", "might have"],
        "correct_option_id": 1,
        "explanation": "استخدمنا 'should have'  للتعبير عن  التوقع  المنطقيّ  في  الماضي.  من  المُتوقع  أن يكونوا  قد  انتهوا  من  العمل  بحلول  الآن. 'Should have finished'  تُشير  إلى  احتمالٍ  كبير  لحدوث  الفعِل  في  الماضي،  ولكنّه  لم  يحدث.  يُشير  هذا  التعبير  إلى  توقعٍ  معقولٍ  في  الماضي  لم  يتحقق."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: We ____ have gone to the party.",
        "options": ["should have", "would have", "might have", "ought to have"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'ought to have'  للتعبير عن  اللوم  أو  الندم  على  عدم  الذهاب  إلى  الحفلة.  'Ought to have gone'  تُشير إلى  أنّه  كان  يجب  عليهما  أن  يذهبا،  وهو  يُعبّر عن  ندمٍ  أو  لومٍ  على  فعلٍ  ماضٍ،  مع  دلالة  أقوى  على  الواجب  من  'should have'.  يُستخدم  'ought to have'  للتعبير  عن  الواجب  الذي  لم  يُنفّذ  في  الماضي."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He ____ have been tired after the long walk.",
        "options": ["should have", "would have", "might have", "must have"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'must have'  للتعبير عن  الاستنتاج  القويّ  بناءً على  المعطيات.  بعد  مشيٍّ  طويل،  من  المُتوقع  بشدة  أن يكون  الشخص  متعبًا.  'Must have been'  تُشير  إلى  يقينٍ  أو  استنتاجٍ  قويّ  بناءً  على  المعلومات  المتاحة،  ويُعبّر  عن  درجة  عالية  من  الاحتمال  وتقريبًا  يقين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: You ____  told me earlier!",
        "options": ["should have", "would have", "might have", "ought to have"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should have'  للتعبير عن  اللوم  على  عدم  الإخبار  سابقًا.  'Should have told'  تُشير  إلى  أنّه  كان  يجب  عليه  أن  يخبر،  وهو  يُعبّر عن  ندمٍ  أو  لومٍ  على  فعلٍ  ماضٍ.  'Should have'  تُستخدم  للتعبير عن  اللوم  أو  النصيحة  في  الماضي،  مع  دلالة  أقل  على  الواجب  من  'ought to have'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: They ____ have finished the work by now.",
        "options": ["must have", "should have", "would have", "might have"],
        "correct_option_id": 1,
        "explanation": "استخدمنا 'should have'  للتعبير عن  التوقع  المنطقيّ  في  الماضي.  من  المُتوقع  أن يكونوا  قد  انتهوا  من  العمل  بحلول  الآن. 'Should have finished'  تُشير  إلى  احتمالٍ  كبير  لحدوث  الفعِل  في  الماضي،  ولكنّه  لم  يحدث.  يُشير  هذا  التعبير  إلى  توقعٍ  معقولٍ  في  الماضي  لم  يتحقق،  وهو  أكثر  ترجيحًا  من  'might have'  و  أقل  شدّة  من  'must have'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: We ____ have gone to the party.",
        "options": ["should have", "would have", "might have", "ought to have"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'ought to have'  للتعبير عن  اللوم  أو  الندم  على  عدم  الذهاب  إلى  الحفلة.  'Ought to have gone'  تُشير إلى  أنّه  كان  يجب  عليهما  أن  يذهبا،  وهو  يُعبّر عن  ندمٍ  أو  لومٍ  على  فعلٍ  ماضٍ،  مع  دلالة  أقوى  على  الواجب  من  'should have'.  يُستخدم  'ought to have'  للتعبير  عن  الواجب  الذي  لم  يُنفّذ  في  الماضي،  مع  دلالة  أكثر  رسمية  من  'should have'."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: He ____ have been tired after the long walk.",
        "options": ["should have", "would have", "might have", "must have"],
        "correct_option_id": 3,
        "explanation": "استخدمنا 'must have'  للتعبير عن  الاستنتاج  القويّ  بناءً على  المعطيات.  بعد  مشيٍّ  طويل،  من  المُتوقع  بشدة  أن يكون  الشخص  متعبًا.  'Must have been'  تُشير  إلى  يقينٍ  أو  استنتاجٍ  قويّ  بناءً  على  المعلومات  المتاحة،  ويُعبّر  عن  درجة  عالية  من  الاحتمال  وتقريبًا  يقين.  في  هذه  الحالة،  التعب  هو  نتيجة  متوقعة  للمشي  الطويل،  لذا  'must have been'  هي  الإجابة  الأكثر  ملاءمةً."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: You ____  told me earlier!",
        "options": ["should have", "would have", "might have", "ought to have"],
        "correct_option_id": 0,
        "explanation": "استخدمنا 'should have'  للتعبير عن  اللوم  على  عدم  الإخبار  سابقًا.  'Should have told'  تُشير  إلى  أنّه  كان  يجب  عليه  أن  يخبر،  وهو  يُعبّر عن  ندمٍ  أو  لومٍ  على  فعلٍ  ماضٍ.  'Should have'  تُستخدم  للتعبير عن  اللوم  أو  النصيحة  في  الماضي،  مع  دلالة  أقل  على  الواجب  من  'ought to have'.  يُعبّر  هذا  التعبير  عن  ندمٍ  أو  لومٍ  لعدم  إخبار  المتكلم  في  الماضي."
    },
    ],
"الجمل الشرطية": [
        {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses the zero conditional?",
        "options": ["A. If you heat ice, it melts.", "B. If you heat ice, it will melt.", "C. If you heated ice, it would melt.", "D. If you had heated ice, it would have melted."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الجملة الصفرية الشرطية (zero conditional) تُستخدم للتعبير عن حقائق عامة أو قوانين طبيعية.  صيغتها:  \"If + present simple, present simple\".  الخيار الصحيح هو: \"If you heat ice, it melts.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence using the first conditional: 'If I study hard, ____.'",
        "options": ["A. I will pass the exam.", "B. I would pass the exam.", "C. I passed the exam.", "D. I would have passed the exam."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الأول (first conditional) يُستخدم للتعبير عن حدث محتمل في المستقبل.  صيغته:  \"If + present simple, will + base verb\".  الخيار الصحيح هو: \"If I study hard, I will pass the exam.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses the second conditional correctly:",
        "options": ["A. If I were rich, I would buy a big house.", "B. If I am rich, I will buy a big house.", "C. If I was rich, I would buy a big house.", "D. If I had been rich, I would have bought a big house."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الثاني (second conditional) يُستخدم للتعبير عن حدث غير محتمل أو خيالي في الحاضر أو المستقبل.  صيغته:  \"If + past simple, would + base verb\".  الخيار الصحيح هو: \"If I were rich, I would buy a big house.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence using the third conditional: 'If I had studied harder, ____.'",
        "options": ["A. I will pass the exam.", "B. I would pass the exam.", "C. I would have passed the exam.", "D. I had passed the exam."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الثالث (third conditional) يُستخدم للتعبير عن حدث مستحيل في الماضي.  صيغته:  \"If + past perfect, would have + past participle\".  الخيار الصحيح هو: \"If I had studied harder, I would have passed the exam.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses the mixed conditional?",
        "options": ["A. If I were taller, I would have been a basketball player.", "B. If I am taller, I will be a basketball player.", "C. If I was taller, I would be a basketball player.", "D. If I had been taller, I would be a basketball player."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط المختلط (mixed conditional) يُستخدم للربط بين حدث مستحيل في الماضي ونتيجة محتملة في الحاضر.  صيغته:  \"If + past perfect, would + base verb\".  الخيار الصحيح هو: \"If I had been taller, I would be a basketball player.\""
    },
    # -------------------------------------------------- 6 - 10
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a general truth or a fact?",
        "options": ["A. If you mix blue and yellow, you get green.", "B. If you mix blue and yellow, you will get green.", "C. If you mixed blue and yellow, you would get green.", "D. If you had mixed blue and yellow, you would have gotten green."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الجملة الصفرية الشرطية (zero conditional)  تُستخدم للتعبير عن حقائق عامة  أو قوانين طبيعية.  الخيار \"If you mix blue and yellow, you get green.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للجملة الصفرية الشرطية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I had enough money, ____.'",
        "options": ["A. I will travel the world.", "B. I traveled the world.", "C. I travel the world.", "D. I would travel the world."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الجملة تُعبّر عن رغبة  أو حلم غير مُتحقق  لذلك نستخدم الشرط الثاني (second conditional).  الخيار الصحيح هو: \"If I had enough money, I would travel the world.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses the first conditional correctly:",
        "options": ["A. If I see him, I will tell him.", "B. If I saw him, I would tell him.", "C.  If I had seen him, I would have told him.", "D.  If I see him, I tell him."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الأول (first conditional)  يُستخدم للتعبير عن حدث مُحتمل في المستقبل.   الخيار  \"If I see him, I will tell him.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If she had studied harder, ____.'",
        "options": ["A. she will pass the test.", "B. she would pass the test.", "C. she would have passed the test.", "D. she had passed the test."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن ندم على حدث في الماضي،  لذلك نستخدم الشرط الثالث (third conditional).   الخيار الصحيح هو: \"If she had studied harder, she would have passed the test.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses the mixed conditional?",
        "options": ["A. If I had won the lottery, I am rich now.", "B. If I had won the lottery, I will be rich now.", "C. If I win the lottery, I would be rich now.", "D. If I had won the lottery, I would be rich now."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط المختلط (mixed conditional)   يُستخدم للربط بين حدث مستحيل في الماضي  (winning the lottery)   ونتائجه المحتملة في الحاضر (being rich).   الخيار الصحيح هو: \"If I had won the lottery, I would be rich now.\""
    },
    # -------------------------------------------------- 11 - 15
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a hypothetical situation in the present?",
        "options": ["A. If I had a car, I would drive to the beach.", "B. If I have a car, I will drive to the beach.", "C. If I had had a car, I would have driven to the beach.", "D. If I have time, I drive to the beach."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الثاني (second conditional)  يُستخدم للتعبير عن حدث غير محتمل  أو خيالي في الحاضر.   الخيار  \"If I had a car, I would drive to the beach.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I ____ (be) you, I would apologize.'",
        "options": ["A. am", "B. was", "C. were", "D. had been"],
        "correct_option_id": 2,  # Index 2
        "explanation": "في جمل الشرط الثاني  نستخدم \"were\"  مع جميع الضمائر  حتى  \"I\"  و\"he\"  و\"she\"  و\"it\".  الخيار الصحيح هو:  \"If I were you, I would apologize.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses the third conditional correctly:",
        "options": ["A. If you had called me, I had helped you.", "B. If you had called me, I would help you.", "C. If you called me, I would have helped you.", "D. If you had called me, I would have helped you."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط الثالث  (third conditional)  يُستخدم للتعبير عن حدث مستحيل في الماضي.   الخيار \"If you had called me, I would have helped you.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثالث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If it ____ (rain) tomorrow, we will stay home.'",
        "options": ["A. will rain", "B. rains", "C. rained", "D. would rain"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الشرط الأول  (first conditional)   يُستخدم للتعبير عن حدث مُحتمل في المستقبل.   الخيار  \"If it rains tomorrow, we will stay home.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the zero conditional correctly?",
        "options": ["A. If water boils, it will evaporate.", "B. If water boils, it evaporates.", "C. If water boiled, it would evaporate.", "D. If water had boiled, it would have evaporated."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة الصفرية الشرطية  (zero conditional)   تُستخدم للتعبير عن حقائق عامة  أو قوانين طبيعية.   الخيار  \"If water boils, it evaporates.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للجملة الصفرية الشرطية."
    },
    # -------------------------------------------------- 16 - 20
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I had known you were coming, ____.'",
        "options": ["A. I will cook dinner.", "B. I would cook dinner.", "C. I would have cooked dinner.", "D. I cook dinner."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن ندم على حدث في الماضي  (not knowing you were coming)  لذلك نستخدم الشرط الثالث  (third conditional).  الخيار الصحيح هو: \"If I had known you were coming, I would have cooked dinner.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'unless' correctly:",
        "options": ["A. Unless you study, you will pass the exam.", "B. Unless you don't study, you will fail the exam.", "C. Unless you study, you will fail the exam.", "D. Unless you study, you won't pass the exam."],
        "correct_option_id": 3,  # Index 3
        "explanation": "\"Unless\"  تعني  \"if not\".   الخيار  \"Unless you study, you won't pass the exam.\"  هو الجملة الوحيدة التي تستخدم  \"unless\"  بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a real possibility in the future?",
        "options": ["A. If I had wings, I would fly.", "B. If it snows tomorrow, we will go skiing.", "C. If I were a doctor, I would help people.", "D. If I had studied harder, I would have passed the exam."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الشرط الأول  (first conditional)  يُستخدم للتعبير عن حدث مُحتمل في المستقبل.   الخيار  \"If it snows tomorrow, we will go skiing.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ you leave now, you will miss the bus.'",
        "options": ["A. Unless", "B. If", "C. When", "D. As soon as"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة تُعبّر عن شرط (leaving now)  ونتائجه (missing the bus)،  لذلك نستخدم  \"If\".  الخيار الصحيح هو:  \"If you leave now, you will miss the bus.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the second conditional correctly?",
        "options": ["A. If I am a bird, I would fly.", "B. If I were a bird, I will fly.", "C. If I were a bird, I would fly.", "D. If I had been a bird, I would have flown."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الثاني  (second conditional)  يُستخدم للتعبير عن حدث غير محتمل  أو خيالي في الحاضر.   الخيار  \"If I were a bird, I would fly.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    # -------------------------------------------------- 21 - 25
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If you ____ (see) him, tell him I said hello.'",
        "options": ["A. saw", "B. will see", "C. see", "D. had seen"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الأول  (first conditional)   يُستخدم للتعبير عن حدث مُحتمل في المستقبل.   الخيار  \"If you see him, tell him I said hello.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'provided that' correctly:",
        "options": ["A. Provided that you study hard, you pass the exam.", "B. Provided that you don't study hard, you will pass the exam.", "C. Provided that you study hard, you will pass the exam.", "D. Provided that you study hard, you will fail the exam."],
        "correct_option_id": 2,  # Index 2
        "explanation": "\"Provided that\"  تعني  \"if\"  أو  \"on the condition that\".   الخيار  \"Provided that you study hard, you will pass the exam.\"   هو الجملة الوحيدة التي تستخدم  \"provided that\"   بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a regret about a past situation?",
        "options": ["A. If I had gone to bed early, I wouldn't be tired now.", "B. If I go to bed early, I won't be tired tomorrow.", "C. If I were tired, I would go to bed.", "D. If I had gone to bed early, I wouldn't have been tired this morning."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط الثالث  (third conditional)  يُستخدم للتعبير عن ندم  أو أسف على حدث في الماضي.   الخيار \"If I had gone to bed early, I wouldn't have been tired this morning.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثالث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ she is sick, she will stay home.'",
        "options": ["A. Unless", "B. Provided that", "C. If", "D. As long as"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن شرط (being sick)   ونتائجه (staying home)، لذلك نستخدم  \"If\".  الخيار الصحيح هو:  \"If she is sick, she will stay home.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the zero conditional correctly?",
        "options": ["A. If you put water in the freezer, it will freeze.", "B. If you put water in the freezer, it freezes.", "C. If you put water in the freezer, it would freeze.", "D. If you had put water in the freezer, it would have frozen."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة الصفرية الشرطية  (zero conditional)   تُستخدم للتعبير عن حقائق عامة  أو قوانين طبيعية.   الخيار  \"If you put water in the freezer, it freezes.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للجملة الصفرية الشرطية."
    },
    # -------------------------------------------------- 26 - 30
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I ____ (win) the lottery, I would buy a new house.'",
        "options": ["A. win", "B. will win", "C. won", "D. had won"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الثاني  (second conditional)   يُستخدم للتعبير عن حدث غير محتمل  أو خيالي في الحاضر.  الخيار  \"If I won the lottery, I would buy a new house.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'as long as' correctly:",
        "options": ["A. As long as you are happy, I'm happy.", "B. As long as you are not happy, I'm happy.", "C. As long as you are happy, I'm not happy.", "D. As long as you are not happy, I'm not happy."],
        "correct_option_id": 0,  # Index 0
        "explanation": "\"As long as\"  تعني  \"provided that\"  أو  \"on the condition that\".  الخيار  \"As long as you are happy, I'm happy.\"  هو الجملة الوحيدة التي تستخدم  \"as long as\"  بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a hypothetical situation in the past?",
        "options": ["A. If I had gone to the party, I would have met her.", "B. If I go to the party, I will meet her.", "C. If I were at the party, I would meet her.", "D. If I had been at the party, I would have met her."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط الثالث  (third conditional)  يُستخدم للتعبير عن حدث مستحيل في الماضي.   الخيار  \"If I had been at the party, I would have met her.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثالث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ the sun shines, we will go to the beach.'",
        "options": ["A. Unless", "B. If", "C. When", "D. As soon as"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة تُعبّر عن شرط (the sun shining)  ونتائجه (going to the beach)،  لذلك نستخدم \"If\".   الخيار الصحيح هو:  \"If the sun shines, we will go to the beach.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the first conditional correctly?",
        "options": ["A. If I am hungry, I eat.", "B. If I am hungry, I will eat.", "C. If I was hungry, I would eat.", "D. If I had been hungry, I would have eaten."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الشرط الأول  (first conditional)   يُستخدم للتعبير عن حدث مُحتمل في المستقبل.   الخيار  \"If I am hungry, I will eat.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    # -------------------------------------------------- 31 - 35
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If you had asked me, ____.'",
        "options": ["A. I will help you.", "B. I would help you.", "C. I would have helped you.", "D. I had helped you."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن ندم على حدث في الماضي  (not being asked)،  لذلك نستخدم الشرط الثالث  (third conditional).  الخيار الصحيح هو:  \"If you had asked me, I would have helped you.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'unless' correctly:",
        "options": ["A. I will go to the party unless it rains.", "B. I will go to the party unless it doesn't rain.", "C. I will not go to the party unless it rains.", "D. I will not go to the party unless it doesn't rain."],
        "correct_option_id": 0,  # Index 0
        "explanation": "\"Unless\"  تعني \"if not\".  الخيار  \"I will go to the party unless it rains.\"  هو الجملة الوحيدة التي تستخدم \"unless\"  بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a general truth?",
        "options": ["A. If you drop a ball, it will fall.", "B. If you dropped a ball, it would fall.", "C. If you had dropped a ball, it would have fallen.", "D. If you drop a ball, it falls."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الجملة الصفرية الشرطية  (zero conditional)  تُستخدم للتعبير عن حقائق عامة أو قوانين طبيعية.  الخيار  \"If you drop a ball, it falls.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للجملة الصفرية الشرطية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ you apologize, she will not forgive you.'",
        "options": ["A. Unless", "B. Provided that", "C. If", "D. As long as"],
        "correct_option_id": 0,  # Index 0
        "explanation": "\"Unless\"  تعني  \"if not\".  الخيار الصحيح هو: \"Unless you apologize, she will not forgive you.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the third conditional correctly?",
        "options": ["A. If I have studied harder, I would have passed the exam.", "B. If I had studied harder, I would pass the exam.", "C. If I study harder, I will pass the exam.", "D. If I had studied harder, I would have passed the exam."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط الثالث  (third conditional)  يُستخدم للتعبير عن حدث مستحيل في الماضي.  الخيار  \"If I had studied harder, I would have passed the exam.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثالث."
    },
    # -------------------------------------------------- 36 - 40
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I ____ (speak) Spanish, I would move to Spain.'",
        "options": ["A. speak", "B. will speak", "C. spoke", "D. had spoken"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الثاني (second conditional) يُستخدم للتعبير عن حدث غير محتمل أو خيالي في الحاضر.  الخيار \"If I spoke Spanish, I would move to Spain.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'provided that' correctly:",
        "options": ["A. Provided that you finish your work, you can go to the party.", "B. Provided that you don't finish your work, you can go to the party.", "C. Provided that you finish your work, you cannot go to the party.", "D. Provided that you don't finish your work, you cannot go to the party."],
        "correct_option_id": 0,  # Index 0
        "explanation": "\"Provided that\"  تعني  \"if\"  أو  \"on the condition that\".   الخيار  \"Provided that you finish your work, you can go to the party.\"  هو الجملة الوحيدة التي تستخدم  \"provided that\"  بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a real possibility in the future?",
        "options": ["A. If I had a million dollars, I would buy a yacht.", "B. If I were a bird, I would fly to the moon.", "C. If I see a shooting star, I will make a wish.", "D.  If I had seen a shooting star, I would have made a wish."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الأول (first conditional) يُستخدم للتعبير عن حدث مُحتمل في المستقبل.  الخيار \"If I see a shooting star, I will make a wish.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ you are ready, we can leave.'",
        "options": ["A. Unless", "B. Provided that", "C. When", "D. As long as"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن زمن  (being ready)  ونتيجة (leaving)،  لذلك نستخدم \"When\".   الخيار الصحيح هو:  \"When you are ready, we can leave.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the second conditional correctly?",
        "options": ["A. If I am rich, I buy a big house.", "B. If I were rich, I would buy a big house.", "C. If I was rich, I will buy a big house.", "D. If I had been rich, I would have bought a big house."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الشرط الثاني (second conditional)  يُستخدم للتعبير عن حدث غير محتمل أو خيالي في الحاضر.  الخيار \"If I were rich, I would buy a big house.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    # -------------------------------------------------- 41 - 45
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I ____ (have) more time, I would learn a new language.'",
        "options": ["A. have", "B. will have", "C. had", "D. would have"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الثاني  (second conditional)   يُستخدم للتعبير عن حدث غير محتمل أو خيالي في الحاضر.  الخيار \"If I had more time, I would learn a new language.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'as long as' correctly:",
        "options": ["A. As long as you don't eat your vegetables, you can have dessert.", "B. As long as you eat your vegetables, you can have dessert.", "C. As long as you eat your vegetables, you cannot have dessert.", "D. As long as you don't eat your vegetables, you cannot have dessert."],
        "correct_option_id": 1,  # Index 1
        "explanation": "\"As long as\"  تعني  \"provided that\"   أو  \"on the condition that\".  الخيار  \"As long as you eat your vegetables, you can have dessert.\"   هو الجملة الوحيدة التي تستخدم  \"as long as\"  بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a regret about a past action?",
        "options": ["A. If I had saved more money, I could buy a car now.", "B. If I save more money, I will buy a car next year.", "C. If I were saving money, I could buy a car.", "D.  If I had saved more money, I could have bought a car last year."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط الثالث (third conditional) يُستخدم للتعبير عن ندم على حدث في الماضي.  الخيار  \"If I had saved more money, I could have bought a car last year.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثالث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ you call me, I will come over.'",
        "options": ["A.  Unless", "B.  As soon as", "C.  When", "D. Provided that"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة تُعبّر عن زمن حدوث حدث (calling) ونتيجته (coming over)، لذلك نستخدم \"As soon as\".  الخيار الصحيح هو: \"As soon as you call me, I will come over.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the zero conditional correctly?",
        "options": ["A. If you don't water plants, they will die.", "B. If you don't water plants, they die.", "C. If you didn't water plants, they would die.", "D. If you hadn't watered plants, they would have died."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة الصفرية الشرطية (zero conditional) تُستخدم للتعبير عن حقائق عامة أو قوانين طبيعية.   الخيار \"If you don't water plants, they die.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للجملة الصفرية الشرطية."
    },
    # -------------------------------------------------- 46 - 50
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I ____ (go) to bed early tonight, I will feel refreshed tomorrow.'",
        "options": ["A. go", "B. will go", "C. went", "D. had gone"],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الأول (first conditional) يُستخدم للتعبير عن حدث مُحتمل في المستقبل.  الخيار \"If I go to bed early tonight, I will feel refreshed tomorrow.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'unless' correctly:",
        "options": ["A.  Unless you hurry, you will miss the train.", "B.  Unless you don't hurry, you will miss the train.", "C. Unless you hurry, you will not miss the train.", "D. Unless you don't hurry, you will not miss the train."],
        "correct_option_id": 0,  # Index 0
        "explanation": "\"Unless\" تعني  \"if not\".  الخيار \"Unless you hurry, you will miss the train.\"  هو الجملة الوحيدة التي تستخدم \"unless\" بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses an unreal situation in the present?",
        "options": ["A.  If I were a millionaire, I would travel the world.", "B. If I am a millionaire, I will travel the world.", "C. If I had been a millionaire, I would have traveled the world.", "D. If I am a millionaire, I travel the world."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الثاني (second conditional) يُستخدم للتعبير عن حدث غير محتمل أو خيالي في الحاضر.  الخيار \"If I were a millionaire, I would travel the world.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses the zero conditional?",
        "options": ["A. If you heat ice, it melts.", "B. If you heat ice, it will melt.", "C. If you heated ice, it would melt.", "D. If you had heated ice, it would have melted."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الجملة الصفرية الشرطية (zero conditional) تُستخدم للتعبير عن حقائق عامة أو قوانين طبيعية.  صيغتها:  \"If + present simple, present simple\".  الخيار الصحيح هو: \"If you heat ice, it melts.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence using the first conditional: 'If I study hard, ____.'",
        "options": ["A. I will pass the exam.", "B. I would pass the exam.", "C. I passed the exam.", "D. I would have passed the exam."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الأول (first conditional) يُستخدم للتعبير عن حدث محتمل في المستقبل.  صيغته:  \"If + present simple, will + base verb\".  الخيار الصحيح هو: \"If I study hard, I will pass the exam.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses the second conditional correctly:",
        "options": ["A. If I were rich, I would buy a big house.", "B. If I am rich, I will buy a big house.", "C. If I was rich, I would buy a big house.", "D. If I had been rich, I would have bought a big house."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الثاني (second conditional) يُستخدم للتعبير عن حدث غير محتمل أو خيالي في الحاضر أو المستقبل.  صيغته:  \"If + past simple, would + base verb\".  الخيار الصحيح هو: \"If I were rich, I would buy a big house.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence using the third conditional: 'If I had studied harder, ____.'",
        "options": ["A. I will pass the exam.", "B. I would pass the exam.", "C. I would have passed the exam.", "D. I had passed the exam."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الثالث (third conditional) يُستخدم للتعبير عن حدث مستحيل في الماضي.  صيغته:  \"If + past perfect, would have + past participle\".  الخيار الصحيح هو: \"If I had studied harder, I would have passed the exam.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses the mixed conditional?",
        "options": ["A. If I were taller, I would have been a basketball player.", "B. If I am taller, I will be a basketball player.", "C. If I was taller, I would be a basketball player.", "D. If I had been taller, I would be a basketball player."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط المختلط (mixed conditional) يُستخدم للربط بين حدث مستحيل في الماضي ونتيجة محتملة في الحاضر.  صيغته:  \"If + past perfect, would + base verb\".  الخيار الصحيح هو: \"If I had been taller, I would be a basketball player.\""
    },
    # -------------------------------------------------- 6 - 10
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a general truth or a fact?",
        "options": ["A. If you mix blue and yellow, you get green.", "B. If you mix blue and yellow, you will get green.", "C. If you mixed blue and yellow, you would get green.", "D. If you had mixed blue and yellow, you would have gotten green."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الجملة الصفرية الشرطية (zero conditional)  تُستخدم للتعبير عن حقائق عامة  أو قوانين طبيعية.  الخيار \"If you mix blue and yellow, you get green.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للجملة الصفرية الشرطية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I had enough money, ____.'",
        "options": ["A. I will travel the world.", "B. I traveled the world.", "C. I travel the world.", "D. I would travel the world."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الجملة تُعبّر عن رغبة  أو حلم غير مُتحقق  لذلك نستخدم الشرط الثاني (second conditional).  الخيار الصحيح هو: \"If I had enough money, I would travel the world.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses the first conditional correctly:",
        "options": ["A. If I see him, I will tell him.", "B. If I saw him, I would tell him.", "C.  If I had seen him, I would have told him.", "D.  If I see him, I tell him."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الأول (first conditional)  يُستخدم للتعبير عن حدث مُحتمل في المستقبل.   الخيار  \"If I see him, I will tell him.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If she had studied harder, ____.'",
        "options": ["A. she will pass the test.", "B. she would pass the test.", "C. she would have passed the test.", "D. she had passed the test."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن ندم على حدث في الماضي،  لذلك نستخدم الشرط الثالث (third conditional).   الخيار الصحيح هو: \"If she had studied harder, she would have passed the test.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses the mixed conditional?",
        "options": ["A. If I had won the lottery, I am rich now.", "B. If I had won the lottery, I will be rich now.", "C. If I win the lottery, I would be rich now.", "D. If I had won the lottery, I would be rich now."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط المختلط (mixed conditional)   يُستخدم للربط بين حدث مستحيل في الماضي  (winning the lottery)   ونتائجه المحتملة في الحاضر (being rich).   الخيار الصحيح هو: \"If I had won the lottery, I would be rich now.\""
    },
    # -------------------------------------------------- 11 - 15
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a hypothetical situation in the present?",
        "options": ["A. If I had a car, I would drive to the beach.", "B. If I have a car, I will drive to the beach.", "C. If I had had a car, I would have driven to the beach.", "D. If I have time, I drive to the beach."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الثاني (second conditional)  يُستخدم للتعبير عن حدث غير محتمل  أو خيالي في الحاضر.   الخيار  \"If I had a car, I would drive to the beach.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I ____ (be) you, I would apologize.'",
        "options": ["A. am", "B. was", "C. were", "D. had been"],
        "correct_option_id": 2,  # Index 2
        "explanation": "في جمل الشرط الثاني  نستخدم \"were\"  مع جميع الضمائر  حتى  \"I\"  و\"he\"  و\"she\"  و\"it\".  الخيار الصحيح هو:  \"If I were you, I would apologize.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses the third conditional correctly:",
        "options": ["A. If you had called me, I had helped you.", "B. If you had called me, I would help you.", "C. If you called me, I would have helped you.", "D. If you had called me, I would have helped you."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط الثالث  (third conditional)  يُستخدم للتعبير عن حدث مستحيل في الماضي.   الخيار \"If you had called me, I would have helped you.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثالث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If it ____ (rain) tomorrow, we will stay home.'",
        "options": ["A. will rain", "B. rains", "C. rained", "D. would rain"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الشرط الأول  (first conditional)   يُستخدم للتعبير عن حدث مُحتمل في المستقبل.   الخيار  \"If it rains tomorrow, we will stay home.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the zero conditional correctly?",
        "options": ["A. If water boils, it will evaporate.", "B. If water boils, it evaporates.", "C. If water boiled, it would evaporate.", "D. If water had boiled, it would have evaporated."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة الصفرية الشرطية  (zero conditional)   تُستخدم للتعبير عن حقائق عامة  أو قوانين طبيعية.   الخيار  \"If water boils, it evaporates.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للجملة الصفرية الشرطية."
    },
    # -------------------------------------------------- 16 - 20
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I had known you were coming, ____.'",
        "options": ["A. I will cook dinner.", "B. I would cook dinner.", "C. I would have cooked dinner.", "D. I cook dinner."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن ندم على حدث في الماضي  (not knowing you were coming)  لذلك نستخدم الشرط الثالث  (third conditional).  الخيار الصحيح هو: \"If I had known you were coming, I would have cooked dinner.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'unless' correctly:",
        "options": ["A. Unless you study, you will pass the exam.", "B. Unless you don't study, you will fail the exam.", "C. Unless you study, you will fail the exam.", "D. Unless you study, you won't pass the exam."],
        "correct_option_id": 3,  # Index 3
        "explanation": "\"Unless\"  تعني  \"if not\".   الخيار  \"Unless you study, you won't pass the exam.\"  هو الجملة الوحيدة التي تستخدم  \"unless\"  بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a real possibility in the future?",
        "options": ["A. If I had wings, I would fly.", "B. If it snows tomorrow, we will go skiing.", "C. If I were a doctor, I would help people.", "D. If I had studied harder, I would have passed the exam."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الشرط الأول  (first conditional)  يُستخدم للتعبير عن حدث مُحتمل في المستقبل.   الخيار  \"If it snows tomorrow, we will go skiing.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ you leave now, you will miss the bus.'",
        "options": ["A. Unless", "B. If", "C. When", "D. As soon as"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة تُعبّر عن شرط (leaving now)  ونتائجه (missing the bus)،  لذلك نستخدم  \"If\".  الخيار الصحيح هو:  \"If you leave now, you will miss the bus.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the second conditional correctly?",
        "options": ["A. If I am a bird, I would fly.", "B. If I were a bird, I will fly.", "C. If I were a bird, I would fly.", "D. If I had been a bird, I would have flown."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الثاني  (second conditional)  يُستخدم للتعبير عن حدث غير محتمل  أو خيالي في الحاضر.   الخيار  \"If I were a bird, I would fly.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    # -------------------------------------------------- 21 - 25
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If you ____ (see) him, tell him I said hello.'",
        "options": ["A. saw", "B. will see", "C. see", "D. had seen"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الأول  (first conditional)   يُستخدم للتعبير عن حدث مُحتمل في المستقبل.   الخيار  \"If you see him, tell him I said hello.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'provided that' correctly:",
        "options": ["A. Provided that you study hard, you pass the exam.", "B. Provided that you don't study hard, you will pass the exam.", "C. Provided that you study hard, you will pass the exam.", "D. Provided that you study hard, you will fail the exam."],
        "correct_option_id": 2,  # Index 2
        "explanation": "\"Provided that\"  تعني  \"if\"  أو  \"on the condition that\".   الخيار  \"Provided that you study hard, you will pass the exam.\"   هو الجملة الوحيدة التي تستخدم  \"provided that\"   بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a regret about a past situation?",
        "options": ["A. If I had gone to bed early, I wouldn't be tired now.", "B. If I go to bed early, I won't be tired tomorrow.", "C. If I were tired, I would go to bed.", "D. If I had gone to bed early, I wouldn't have been tired this morning."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط الثالث  (third conditional)  يُستخدم للتعبير عن ندم  أو أسف على حدث في الماضي.   الخيار \"If I had gone to bed early, I wouldn't have been tired this morning.\"   هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثالث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ she is sick, she will stay home.'",
        "options": ["A. Unless", "B. Provided that", "C. If", "D. As long as"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن شرط (being sick)   ونتائجه (staying home)، لذلك نستخدم  \"If\".  الخيار الصحيح هو:  \"If she is sick, she will stay home.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the zero conditional correctly?",
        "options": ["A. If you put water in the freezer, it will freeze.", "B. If you put water in the freezer, it freezes.", "C. If you put water in the freezer, it would freeze.", "D. If you had put water in the freezer, it would have frozen."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة الصفرية الشرطية  (zero conditional)   تُستخدم للتعبير عن حقائق عامة  أو قوانين طبيعية.   الخيار  \"If you put water in the freezer, it freezes.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للجملة الصفرية الشرطية."
    },
    # -------------------------------------------------- 26 - 30
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I ____ (win) the lottery, I would buy a new house.'",
        "options": ["A. win", "B. will win", "C. won", "D. had won"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الثاني  (second conditional)   يُستخدم للتعبير عن حدث غير محتمل  أو خيالي في الحاضر.  الخيار  \"If I won the lottery, I would buy a new house.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'as long as' correctly:",
        "options": ["A. As long as you are happy, I'm happy.", "B. As long as you are not happy, I'm happy.", "C. As long as you are happy, I'm not happy.", "D. As long as you are not happy, I'm not happy."],
        "correct_option_id": 0,  # Index 0
        "explanation": "\"As long as\"  تعني  \"provided that\"  أو  \"on the condition that\".  الخيار  \"As long as you are happy, I'm happy.\"  هو الجملة الوحيدة التي تستخدم  \"as long as\"  بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a hypothetical situation in the past?",
        "options": ["A. If I had gone to the party, I would have met her.", "B. If I go to the party, I will meet her.", "C. If I were at the party, I would meet her.", "D. If I had been at the party, I would have met her."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط الثالث  (third conditional)  يُستخدم للتعبير عن حدث مستحيل في الماضي.   الخيار  \"If I had been at the party, I would have met her.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثالث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ the sun shines, we will go to the beach.'",
        "options": ["A. Unless", "B. If", "C. When", "D. As soon as"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة تُعبّر عن شرط (the sun shining)  ونتائجه (going to the beach)،  لذلك نستخدم \"If\".   الخيار الصحيح هو:  \"If the sun shines, we will go to the beach.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the first conditional correctly?",
        "options": ["A. If I am hungry, I eat.", "B. If I am hungry, I will eat.", "C. If I was hungry, I would eat.", "D. If I had been hungry, I would have eaten."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الشرط الأول  (first conditional)   يُستخدم للتعبير عن حدث مُحتمل في المستقبل.   الخيار  \"If I am hungry, I will eat.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    # -------------------------------------------------- 31 - 35
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If you had asked me, ____.'",
        "options": ["A. I will help you.", "B. I would help you.", "C. I would have helped you.", "D. I had helped you."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن ندم على حدث في الماضي  (not being asked)،  لذلك نستخدم الشرط الثالث  (third conditional).  الخيار الصحيح هو:  \"If you had asked me, I would have helped you.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'unless' correctly:",
        "options": ["A. I will go to the party unless it rains.", "B. I will go to the party unless it doesn't rain.", "C. I will not go to the party unless it rains.", "D. I will not go to the party unless it doesn't rain."],
        "correct_option_id": 0,  # Index 0
        "explanation": "\"Unless\"  تعني \"if not\".  الخيار  \"I will go to the party unless it rains.\"  هو الجملة الوحيدة التي تستخدم \"unless\"  بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a general truth?",
        "options": ["A. If you drop a ball, it will fall.", "B. If you dropped a ball, it would fall.", "C. If you had dropped a ball, it would have fallen.", "D. If you drop a ball, it falls."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الجملة الصفرية الشرطية  (zero conditional)  تُستخدم للتعبير عن حقائق عامة أو قوانين طبيعية.  الخيار  \"If you drop a ball, it falls.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للجملة الصفرية الشرطية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ you apologize, she will not forgive you.'",
        "options": ["A. Unless", "B. Provided that", "C. If", "D. As long as"],
        "correct_option_id": 0,  # Index 0
        "explanation": "\"Unless\"  تعني  \"if not\".  الخيار الصحيح هو: \"Unless you apologize, she will not forgive you.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the third conditional correctly?",
        "options": ["A. If I have studied harder, I would have passed the exam.", "B. If I had studied harder, I would pass the exam.", "C. If I study harder, I will pass the exam.", "D. If I had studied harder, I would have passed the exam."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط الثالث  (third conditional)  يُستخدم للتعبير عن حدث مستحيل في الماضي.  الخيار  \"If I had studied harder, I would have passed the exam.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثالث."
    },
    # -------------------------------------------------- 36 - 40
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I ____ (speak) Spanish, I would move to Spain.'",
        "options": ["A. speak", "B. will speak", "C. spoke", "D. had spoken"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الثاني (second conditional) يُستخدم للتعبير عن حدث غير محتمل أو خيالي في الحاضر.  الخيار \"If I spoke Spanish, I would move to Spain.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'provided that' correctly:",
        "options": ["A. Provided that you finish your work, you can go to the party.", "B. Provided that you don't finish your work, you can go to the party.", "C. Provided that you finish your work, you cannot go to the party.", "D. Provided that you don't finish your work, you cannot go to the party."],
        "correct_option_id": 0,  # Index 0
        "explanation": "\"Provided that\"  تعني  \"if\"  أو  \"on the condition that\".   الخيار  \"Provided that you finish your work, you can go to the party.\"  هو الجملة الوحيدة التي تستخدم  \"provided that\"  بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a real possibility in the future?",
        "options": ["A. If I had a million dollars, I would buy a yacht.", "B. If I were a bird, I would fly to the moon.", "C. If I see a shooting star, I will make a wish.", "D.  If I had seen a shooting star, I would have made a wish."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الأول (first conditional) يُستخدم للتعبير عن حدث مُحتمل في المستقبل.  الخيار \"If I see a shooting star, I will make a wish.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ you are ready, we can leave.'",
        "options": ["A. Unless", "B. Provided that", "C. When", "D. As long as"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن زمن  (being ready)  ونتيجة (leaving)،  لذلك نستخدم \"When\".   الخيار الصحيح هو:  \"When you are ready, we can leave.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the second conditional correctly?",
        "options": ["A. If I am rich, I buy a big house.", "B. If I were rich, I would buy a big house.", "C. If I was rich, I will buy a big house.", "D. If I had been rich, I would have bought a big house."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الشرط الثاني (second conditional)  يُستخدم للتعبير عن حدث غير محتمل أو خيالي في الحاضر.  الخيار \"If I were rich, I would buy a big house.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    # -------------------------------------------------- 41 - 45
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I ____ (have) more time, I would learn a new language.'",
        "options": ["A. have", "B. will have", "C. had", "D. would have"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الشرط الثاني  (second conditional)   يُستخدم للتعبير عن حدث غير محتمل أو خيالي في الحاضر.  الخيار \"If I had more time, I would learn a new language.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'as long as' correctly:",
        "options": ["A. As long as you don't eat your vegetables, you can have dessert.", "B. As long as you eat your vegetables, you can have dessert.", "C. As long as you eat your vegetables, you cannot have dessert.", "D. As long as you don't eat your vegetables, you cannot have dessert."],
        "correct_option_id": 1,  # Index 1
        "explanation": "\"As long as\"  تعني  \"provided that\"   أو  \"on the condition that\".  الخيار  \"As long as you eat your vegetables, you can have dessert.\"   هو الجملة الوحيدة التي تستخدم  \"as long as\"  بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a regret about a past action?",
        "options": ["A. If I had saved more money, I could buy a car now.", "B. If I save more money, I will buy a car next year.", "C. If I were saving money, I could buy a car.", "D.  If I had saved more money, I could have bought a car last year."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الشرط الثالث (third conditional) يُستخدم للتعبير عن ندم على حدث في الماضي.  الخيار  \"If I had saved more money, I could have bought a car last year.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثالث."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: '____ you call me, I will come over.'",
        "options": ["A.  Unless", "B.  As soon as", "C.  When", "D. Provided that"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة تُعبّر عن زمن حدوث حدث (calling) ونتيجته (coming over)، لذلك نستخدم \"As soon as\".  الخيار الصحيح هو: \"As soon as you call me, I will come over.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses the zero conditional correctly?",
        "options": ["A. If you don't water plants, they will die.", "B. If you don't water plants, they die.", "C. If you didn't water plants, they would die.", "D. If you hadn't watered plants, they would have died."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة الصفرية الشرطية (zero conditional) تُستخدم للتعبير عن حقائق عامة أو قوانين طبيعية.   الخيار \"If you don't water plants, they die.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للجملة الصفرية الشرطية."
    },
    # -------------------------------------------------- 46 - 50
    {
        "question": "اختر الإجابة الصحيحة:\nComplete the sentence: 'If I ____ (go) to bed early tonight, I will feel refreshed tomorrow.'",
        "options": ["A. go", "B. will go", "C. went", "D. had gone"],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الأول (first conditional) يُستخدم للتعبير عن حدث مُحتمل في المستقبل.  الخيار \"If I go to bed early tonight, I will feel refreshed tomorrow.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الأول."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence that uses 'unless' correctly:",
        "options": ["A.  Unless you hurry, you will miss the train.", "B.  Unless you don't hurry, you will miss the train.", "C. Unless you hurry, you will not miss the train.", "D. Unless you don't hurry, you will not miss the train."],
        "correct_option_id": 0,  # Index 0
        "explanation": "\"Unless\" تعني  \"if not\".  الخيار \"Unless you hurry, you will miss the train.\"  هو الجملة الوحيدة التي تستخدم \"unless\" بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses an unreal situation in the present?",
        "options": ["A.  If I were a millionaire, I would travel the world.", "B. If I am a millionaire, I will travel the world.", "C. If I had been a millionaire, I would have traveled the world.", "D. If I am a millionaire, I travel the world."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرط الثاني (second conditional) يُستخدم للتعبير عن حدث غير محتمل أو خيالي في الحاضر.  الخيار \"If I were a millionaire, I would travel the world.\"  هو الجملة الوحيدة التي تستخدم الصيغة الصحيحة للشرط الثاني."
    },
],

},
"تركيب الجملة":{
    "الجمل البسيطة": [
        
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence contains only one independent clause (one complete thought)?",
        "options": ["The dog barked, and the cat ran.", "Although it rained, the sun peeked through.", "She sings beautifully, dances gracefully.", "The quick brown fox jumps."],
        "correct_option_id": 3,
        "explanation": "الجملة الصحيحة هي \"The quick brown fox jumps.\" لأنها تحتوي على فاعل واحد (fox) و فعل واحد (jumps) وتُعبّر عن فكرة كاملة بذاتها، دون حاجة لإضافة جمل أخرى.  أما الخيارات الأخرى، فتحتوي على أكثر من فكرة أو جملة مستقلة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence:",
        "options": ["The sun set, painting the sky with vibrant colors.", "He ate dinner, then watched TV.", "Despite the storm, they continued their journey.", "Birds chirped."],
        "correct_option_id": 3,
        "explanation": "الجملة \"Birds chirped\" هي جملة بسيطة لأنها تحتوي على فاعل واحد (Birds) ومسند واحد (chirped) وتُعبّر عن فكرة كاملة. الخيارات الأخرى تتكون من جملتين أو أكثر أو جمل تتضمن جملًا تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a simple sentence?",
        "options": ["The cat slept.", "The dog barked loudly, and the cat hissed.", "She smiled happily.", "He walked to the store."],
        "correct_option_id": 1,
        "explanation": "الجملة \"The dog barked loudly, and the cat hissed\" ليست جملة بسيطة لأنها تحتوي على جملتين بسيطتين متصلتين بواسطة الرابط \"and\".  الجملة البسيطة تحتوي على فاعل واحد و فعل واحد فقط يعبر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the simple sentence that describes an action:",
        "options": ["The playful puppy jumped.", "Although it was raining, they played.", "The car stopped suddenly, causing an accident.", "After the rain, the sun shone."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The playful puppy jumped\"  هي جملة بسيطة تصف فعلًا واحدًا (jumped) وفاعلًا واحدًا (puppy).  الخيارات الأخرى تحتوي على جمل أو أفكار متعددة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence best exemplifies a simple sentence?",
        "options": ["The old woman sat quietly, knitting a warm scarf.", "He studied hard; he passed the exam.", "The flowers bloomed.", "Before leaving, he locked the door."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The flowers bloomed\" هي جملة بسيطة لأنها تحتوي على فاعل واحد (flowers) و فعل واحد (bloomed) ويعبر عن فكرة واحدة فقط.  الخيارات الأخرى تحتوي على جمل منفصلة أو جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence about a bird:",
        "options": ["The bird sang sweetly in the tree.", "The bird flew high above the clouds, singing a melody.", "Because it was sunny, the bird sang.", "While flying, the bird sang."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The bird sang sweetly in the tree\" هي جملة بسيطة.  تتضمن فاعلًا واحدًا (The bird) و فعلًا واحدًا (sang)  وتعبر عن فكرة كاملة.  الخيارات الأخرى تحتوي على جمل تابعة أو جمل متعددة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these is NOT a simple sentence?",
        "options": ["The children played.", "The sun shone brightly, warming the earth.", "She read a book.", "He ate a sandwich and drank milk."],
        "correct_option_id": 1,
        "explanation": "الجملة \"The sun shone brightly, warming the earth\" ليست جملة بسيطة رغم أنها تبدو كذلك في البداية.  الجزء \"warming the earth\" عبارة عن جملة تابعة تصف الفعل الرئيسي، مما يجعلها جملة مركبة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a simple sentence using 'cat', 'sat', and 'mat':",
        "options": ["The cat sat on the mat.", "The cat sat on the mat, purring contentedly.", "Because it was tired, the cat sat on the mat.", "The cat, which was very tired, sat on the mat."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The cat sat on the mat\" هي جملة بسيطة.  تتضمن فاعلًا (cat) و فعلًا (sat)  وتعبر عن فكرة واحدة فقط دون جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The dog ran quickly.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، \"The dog ran quickly.\" هي جملة بسيطة لأنها تحتوي على فاعل واحد (dog) و فعل واحد (ran)  وتعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is a simple sentence describing a sunset?",
        "options": ["The sun set slowly, painting the sky with beautiful colors.", "As the sun dipped below the horizon, the birds flew to their nests.", "The sky turned orange and red.", "After the sun set, the stars appeared."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The sky turned orange and red\" هي جملة بسيطة وتعبر عن فكرة واحدة فقط. الخيارات الأخرى تحتوي على جمل متعددة أو جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is NOT a simple sentence?",
        "options": ["The birds sang.", "The flowers bloomed in the garden.", "The boy ran fast, and the girl walked slowly.", "The cat slept."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The boy ran fast, and the girl walked slowly\"  ليست جملة بسيطة، لأنها تتكون من جملتين منفصلتين متصلتين بـ\"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWrite a simple sentence about a child sleeping:",
        "options": ["The child slept soundly in his bed.", "The tired child slept soundly, dreaming sweet dreams.", "After playing all day, the child slept soundly.", "While the child slept, the moon shone brightly."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The child slept soundly in his bed\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد (child) و فعل واحد (slept) وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence: A.  The car sped down the highway, then it crashed. B. The driver braked hard. C. Although the brakes failed, the driver survived. D. After the crash, the police arrived.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The driver braked hard\"  هي جملة بسيطة لأنها تحتوي على فاعل واحد و فعل واحد، وتُعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a simple sentence? A. The chef prepared a delicious meal; the guests enjoyed it. B. The cake was delicious. C. Because it was raining, they stayed inside. D.  While she was singing, he played the guitar.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The cake was delicious\"  هي جملة بسيطة لأنها تحتوي على فاعل واحد (cake) و فعل واحد (was)  وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The big red ball bounced high.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، \"The big red ball bounced high\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد (ball) و فعل واحد (bounced) وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a simple sentence? A. The happy child laughed. B. The sun rose, and the birds started singing. C. The old house stood empty. D. The playful kitten pounced.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The sun rose, and the birds started singing\" ليست جملة بسيطة، لأنها تتكون من جملتين منفصلتين مرتبطتين بـ\"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nRewrite 'Because it was cold, she wore a coat' as a simple sentence.",
        "options": ["She wore a coat because of the cold.", "The cold made her wear a coat.", "She wore a warm coat.", "She wore a coat."],
        "correct_option_id": 2,
        "explanation": "الجملة \"She wore a warm coat\" هي جملة بسيطة  وتنقل الفكرة الرئيسية بشكل مختصر. الخيارات الأخرى تحتوي على جمل تابعة أو تفاصيل إضافية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence contains only one independent clause?",
        "options": ["The dog barked, and the cat hid.", "Although it was hot, he drank some water.", "She is kind and intelligent.", "The train arrived late."],
        "correct_option_id": 3,
        "explanation": "الجملة \"The train arrived late\"  تتكون من جملة مستقلة واحدة فقط. الخيارات الأخرى تتضمن جملًا تابعة أو جملًا منفصلة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence: A. The boy ran quickly; he wanted to catch the bus. B. The bus arrived on time. C.  Because he was late, he missed the bus. D. After missing the bus, he walked home.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The bus arrived on time\"  هي جملة بسيطة لأنها تتضمن فاعلًا واحدًا (bus) و فعلًا واحدًا (arrived) وتُعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a simple sentence? A. The sun shone brightly, and the birds sang sweetly. B. The birds sang sweetly. C.  While the sun shone, the birds sang. D.  If it rains, we will stay inside.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The birds sang sweetly\" هي جملة بسيطة، لأنها تتضمن فاعلًا واحدًا (birds) و فعلًا واحدًا (sang) وتُعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nRewrite 'Despite feeling tired, she finished her work' as a simple sentence.",
        "options": ["She was tired, but she finished her work.", "She finished her work despite being tired.", "She finished her work.", "Her tiredness didn't stop her."],
        "correct_option_id": 2,
        "explanation": "الجملة \"She finished her work\" هي جملة بسيطة،  وتنقل الفكرة الرئيسية بشكل مختصر. الخيارات الأخرى تحتوي على تفاصيل إضافية أو جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a simple sentence? A. The cat purred softly. B. The dog barked loudly, and the cat jumped. C. The bird flew away. D. The sun set.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The dog barked loudly, and the cat jumped\" ليست جملة بسيطة، لأنها تتكون من جملتين منفصلتين مرتبطتين بـ\"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The playful kitten chased the red ball.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، \"The playful kitten chased the red ball\" هي جملة بسيطة لأنها تحتوي على فاعل واحد (kitten) و فعل واحد (chased) وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these sentences is a simple sentence? A. The old car needed a repair; the mechanic fixed it. B. The mechanic fixed the car. C.  Because the car was old, it needed repair. D.  After the repair, the car ran well.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The mechanic fixed the car\"  هي جملة بسيطة لأنها تتضمن فاعلًا واحدًا (mechanic) و فعلًا واحدًا (fixed) وتُعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWrite a simple sentence about a person eating an apple.",
        "options": ["The person ate a delicious apple.", "The person ate a juicy, red apple with great enjoyment.", "While walking, the person ate a crisp apple.", "Because he was hungry, the person ate an apple."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The person ate a delicious apple\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد (person) و فعل واحد (ate) وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence among these options: A. The wind blew strongly, and the rain fell heavily. B. The leaves fell from the trees. C.  Because of the storm, the trees fell. D.  After the storm, the sun shone brightly.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The leaves fell from the trees\" هي جملة بسيطة لأنها تتضمن فاعلًا واحدًا (leaves) و فعلًا واحدًا (fell) وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The happy bird chirped merrily.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، \"The happy bird chirped merrily\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد (bird) و فعل واحد (chirped) وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is a simple sentence? A.  The artist painted a beautiful picture; it won an award. B. The picture won an award. C. While she painted, music played softly. D. If she wins, she'll be happy.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The picture won an award\"  هي جملة بسيطة لأنها تتضمن فاعلًا واحدًا (picture) و فعلًا واحدًا (won) وتُعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nRewrite 'Although he was tired, he finished the race' as a simple sentence.",
        "options": ["He was tired but finished the race.", "He finished the race despite his tiredness.", "He finished the tiring race.", "He finished the race."],
        "correct_option_id": 2,
        "explanation": "الجملة \"He finished the tiring race\" هي جملة بسيطة، وتنقل الفكرة الرئيسية بشكل مختصر. الخيارات الأخرى تحتوي على تفاصيل إضافية أو جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a simple sentence? A. The train left the station. B. The passengers boarded the train. C.  The train left, and the passengers waved goodbye. D. The journey began.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 2,
        "explanation": "الجملة \"The train left, and the passengers waved goodbye\" ليست جملة بسيطة، لأنها تتكون من جملتين منفصلتين مرتبطتين بـ\"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWrite a simple sentence about a student studying.",
        "options": ["The student studied diligently.", "The student studied diligently for the upcoming exam.", "While listening to music, the student studied.", "Because the test was important, the student studied hard."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The student studied diligently\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد (student) و فعل واحد (studied) وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence among these options: A. The chef cooked a delicious meal, and the guests were delighted. B. The food was delicious. C.  Because the food was tasty, they ate heartily. D.  After dinner, they relaxed.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The food was delicious\" هي جملة بسيطة، لأنها تتضمن فاعلًا واحدًا (food) و فعل واحد (was) وتُعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The fluffy cat slept soundly in a sunbeam.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، \"The fluffy cat slept soundly in a sunbeam\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد (cat) و فعل واحد (slept) وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is a simple sentence? A. The singer sang beautifully; the audience cheered loudly. B. The audience cheered. C.  While the singer sang, the audience listened intently. D.  If the singer performs well, she will win the competition.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The audience cheered\"  هي جملة بسيطة لأنها تتضمن فاعلًا واحدًا (audience) و فعلًا واحدًا (cheered) وتُعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nRewrite 'Despite the heavy snow, they reached their destination' as a simple sentence.",
        "options": ["They reached their destination despite the heavy snow.", "The heavy snow didn't stop them.", "They reached their destination in the heavy snow.", "They reached their snowy destination."],
        "correct_option_id": 2,
        "explanation": "الجملة \"They reached their destination in the heavy snow\" هي جملة بسيطة، وتنقل الفكرة الرئيسية بشكل مختصر. الخيارات الأخرى تحتوي على تفاصيل إضافية أو جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a simple sentence? A. The river flowed swiftly. B. The birds flew south for the winter. C. The sun set, and the moon rose. D. The trees swayed gently.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 2,
        "explanation": "الجملة \"The sun set, and the moon rose\" ليست جملة بسيطة، لأنها تتكون من جملتين منفصلتين مرتبطتين بـ\"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWrite a simple sentence about a car driving.",
        "options": ["The car drove quickly down the road.", "The red car drove swiftly, speeding down the highway.", "While driving, the person enjoyed the scenery.", "Because he was late, the person drove quickly."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The car drove quickly down the road\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد (car) و فعل واحد (drove) وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence among these options: A. The children played happily, and their parents watched proudly. B. The children played happily. C.  While the children played, their parents relaxed. D.  After playing, the children went home.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The children played happily\" هي جملة بسيطة، لأنها تتضمن فاعلًا واحدًا (children) و فعلًا واحدًا (played) وتُعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The little girl skipped happily down the lane.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، \"The little girl skipped happily down the lane\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد (girl) و فعل واحد (skipped) وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is a simple sentence? A. The teacher explained the lesson clearly; the students understood it well. B. The students understood the lesson. C.  While the teacher explained, the students listened attentively. D. If the students study hard, they will pass the test.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The students understood the lesson\"  هي جملة بسيطة لأنها تتضمن فاعلًا واحدًا (students) و فعلًا واحدًا (understood) وتُعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence expresses a single complete thought?",
        "options": ["The bird sang a beautiful song, and the flowers bloomed brightly.", "Although it was raining, the children played outside.", "The cat sat on the mat.", "Before the game, the players warmed up."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The cat sat on the mat\"  تُعبّر عن فكرة واحدة كاملة ومستقلة.  الخيارات الأخرى تحتوي على أكثر من فكرة أو جملة تابعة (مثل: Although, Before, and). الجملة البسيطة تتكون من فاعل واحد ومسند واحد فقط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with one independent clause:",
        "options": ["The sun shone, and the birds sang.", "Despite the cold, she went for a walk.", "He laughed heartily.", "After the rain, the flowers bloomed."],
        "correct_option_id": 2,
        "explanation": "الجملة \"He laughed heartily\" تتكون من جملة واحدة مستقلة فقط (جملة رئيسية).  الجمل الأخرى تحتوي على جمل رئيسية وجمل تابعة، أو جملتين رئيسيتين مرتبطتين بـ (and, but, or). "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a simple sentence?",
        "options": ["The dog barked.", "The cat slept soundly on the rug.", "He ran quickly, and she walked slowly.", "The bird flew high."],
        "correct_option_id": 2,
        "explanation": "الجملة \"He ran quickly, and she walked slowly\" ليست جملة بسيطة، لأنها تتكون من جملتين بسيطتين متصلتين بـ\"and\".  الجملة البسيطة تحتوي على فاعل واحد ومسند واحد فقط، تُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the simple sentence that describes a state of being:",
        "options": ["The puppy played fetch.", "The sky is blue.", "She sings beautifully, dances gracefully.", "He walked to the store, and bought milk."],
        "correct_option_id": 1,
        "explanation": "الجملة \"The sky is blue\" تصف حالة (being)  بسيطة.  الخيارات الأخرى تصف أفعالًا أو تتضمن أكثر من فكرة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is the best example of a simple sentence?",
        "options": ["The old house stood on a hill overlooking the valley.", "She read a book while listening to music.", "Time flies.", "Although he was tired, he continued running."],
        "correct_option_id": 2,
        "explanation": "الجملة \"Time flies\" هي جملة بسيطة ونقية، تحتوي على فاعل واحد (Time) ومسند واحد (flies).  الخيارات الأخرى أكثر تعقيدًا وتحتوي على جمل تابعة أو جمل متعددة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich simple sentence describes an action performed by a specific subject?",
        "options": ["The children played.", "The sun is shining.", "The car is red.", "The flowers are beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The children played\" تصف فعلًا (played) قام به فاعل محدد (children). الجمل الأخرى تصف حالة أو صفة، دون فعل رئيسي واضح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is NOT a simple sentence?",
        "options": ["The dog ran.", "The cat sat on the mat, and the bird sang.", "She smiled.", "He walked."],
        "correct_option_id": 1,
        "explanation": "الجملة \"The cat sat on the mat, and the bird sang\"  ليست جملة بسيطة، لأنها تتكون من جملتين بسيطتين مرتبطتين بـ\"and\".  تتكون الجملة البسيطة من فاعل واحد ومسند واحد فقط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a simple sentence using 'birds', 'sing', and 'trees':",
        "options": ["The birds sing in the trees.", "The birds sing beautifully in the tall trees.", "While the sun shone, the birds sang in the trees.", "Because it was morning, the birds sang in the trees."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The birds sing in the trees\" هي جملة بسيطة.  الخيارات الأخرى تحتوي على جمل تابعة أو صفات إضافية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The rain fell.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، \"The rain fell.\" هي جملة بسيطة لأنها تحتوي على فاعل واحد (rain) و فعل واحد (fell) وتُعبّر عن فكرة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is a simple sentence describing a cloudy day?",
        "options": ["The sky was cloudy, and it began to rain.", "The clouds covered the sun.", "It was a cloudy day, and I stayed inside.", "After the clouds cleared, the sun shone brightly."],
        "correct_option_id": 1,
        "explanation": "الجملة \"The clouds covered the sun\" هي جملة بسيطة. الخيارات الأخرى تحتوي على أكثر من فكرة أو جملة تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is NOT a simple sentence?",
        "options": ["The flowers bloomed.", "The dog wagged its tail happily.", "He ate lunch, and then he went to work.", "The cat purred."],
        "correct_option_id": 2,
        "explanation": "الجملة \"He ate lunch, and then he went to work\" ليست جملة بسيطة؛ لأنها تتضمن جملتين بسيطتين متصلتين بـ\"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWrite a simple sentence about a car driving fast:",
        "options": ["The car drove fast down the highway.", "The fast car sped down the highway.", "The red car drove fast, and the blue car followed.", "Although it was raining, the car drove fast."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The car drove fast down the highway\" هي جملة بسيطة وتتضمن فاعل واحد (car) و فعل واحد (drove). الخيارات الأخرى تحتوي على جمل تابعة أو تفاصيل إضافية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence: A. The bird flew high above the trees, singing a sweet song. B.  The bird sang sweetly. C. Because it was a beautiful day, the bird sang. D.  While flying, the bird sang.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The bird sang sweetly\" هي جملة بسيطة.  الجمل الأخرى تحتوي على جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a simple sentence? A. The children played in the park; they had a lot of fun. B. The children played happily. C. Because it was sunny, the children played. D.  After playing, the children went home.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The children played happily\" هي جملة بسيطة.  الجمل الأخرى تحتوي على جمل تابعة أو جمل منفصلة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The small brown rabbit hopped quickly.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، هذه جملة بسيطة.  تتضمن فاعل واحد (rabbit) و فعل واحد (hopped)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a simple sentence? A. The sun shone brightly. B. The birds sang in the trees, and the wind blew gently. C.  The flowers bloomed. D. The cat slept soundly.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The birds sang in the trees, and the wind blew gently\" ليست جملة بسيطة؛ لأنها تتضمن جملتين بسيطتين مرتبطتين بـ\"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nRewrite 'Although he was tired, he finished his work' as a simple sentence.",
        "options": ["He was tired, but he finished his work.", "He finished his work although he was tired.", "He finished his work.", "He finished his tiring work."],
        "correct_option_id": 2,
        "explanation": "الجملة \"He finished his work\" هي أبسط شكل للجملة، وتنقل الفكرة الأساسية بشكل مختصر ودون جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence contains only one independent clause?",
        "options": ["The dog barked, and the cat meowed.", "Although it was late, he went to the store.", "She is tall and slim.", "The birds are singing."],
        "correct_option_id": 3,
        "explanation": "الجملة \"The birds are singing\" تتكون من جملة مستقلة واحدة فقط.  الجمل الأخرى تحتوي على جمل تابعة أو جمل منفصلة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence: A. The children played in the park, and then they went home. B. While they were playing, it began to rain. C.  The car stopped suddenly. D. After the accident, they called the police.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 2,
        "explanation": "الجملة \"The car stopped suddenly\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد ومسند واحد، وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a simple sentence? A. The runner finished first; the crowd cheered loudly. B. The crowd cheered. C.  Because he won, the runner celebrated. D.  After the race, he received a medal.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The crowd cheered\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد ومسند واحد، وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nRewrite 'Despite the heavy rain, the game continued' as a simple sentence.",
        "options": ["The game continued despite heavy rain.", "The heavy rain didn't stop the game.", "The game continued in the heavy rain.", "The game continued."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The game continued in the heavy rain\"  هي جملة بسيطة، وتنقل الفكرة الأساسية بشكل مختصر، دون جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The playful kitten jumped on the soft cushion.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، هذه جملة بسيطة، لأنها تحتوي على فاعل واحد (kitten) و فعل واحد (jumped)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence contains only one independent clause? A. The cat sat on the mat, and the dog slept on the rug. B. After the rain stopped, the sun came out. C. The bird built a nest. D. Because it was cold, she put on her coat.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 2,
        "explanation": "الجملة \"The bird built a nest\" تتكون من جملة مستقلة واحدة فقط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these is NOT a simple sentence? A. The students studied diligently. B. The teacher gave a test. C. The students studied, and the teacher graded papers. D.  The book was interesting.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 2,
        "explanation": "الجملة \"The students studied, and the teacher graded papers\" ليست جملة بسيطة، لأنها تتضمن جملتين بسيطتين مرتبطتين بـ\"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWrite a simple sentence about a person walking in the park.",
        "options": ["The person walked in the park.", "The person walked peacefully in the sunny park.", "While walking, the person enjoyed the fresh air.", "Because it was a nice day, the person walked in the park."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The person walked in the park\" هي جملة بسيطة، وتتضمن فاعل واحد (person) و فعل واحد (walked).  الخيارات الأخرى تحتوي على جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence among the following: A. The chef cooked a delicious meal, and the guests ate heartily. B. The food was delicious. C.  Although it was late, they finished their work. D.  Before going to bed, they brushed their teeth.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The food was delicious\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد ومسند واحد، وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is a simple sentence? A. The train arrived late, causing delays for many passengers. B. The sun rose in the east. C. While he was waiting, he read a book. D.  If you hurry, you'll catch the bus.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The sun rose in the east\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد ومسند واحد، وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nRewrite the sentence 'Despite feeling unwell, she went to work' as a simple sentence.",
        "options": ["She went to work despite feeling unwell.", "She went to work although she felt unwell.", "She went to work feeling unwell.", "She went to work."],
        "correct_option_id": 2,
        "explanation": "الجملة \"She went to work feeling unwell\" هي جملة بسيطة، وتنقل الفكرة الأساسية بشكل مختصر."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a simple sentence? A. The cat sat on the windowsill. B. The bird sang sweetly, and the flowers bloomed. C. The dog barked loudly. D. The child slept soundly.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The bird sang sweetly, and the flowers bloomed\" ليست جملة بسيطة؛ لأنها تتضمن جملتين بسيطتين مرتبطتين بـ\"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The playful puppy chased its tail excitedly.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، هذه جملة بسيطة، لأنها تحتوي على فاعل واحد (puppy) و فعل واحد (chased)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of these sentences is a simple sentence? A. The musician played a beautiful melody; the audience was mesmerized. B. The audience listened intently. C. While the music played, the audience relaxed. D. If the music is good, people will enjoy it.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The audience listened intently\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد ومسند واحد، وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWrite a simple sentence about a person swimming in the ocean.",
        "options": ["The person swam in the ocean.", "The person swam gracefully in the clear blue ocean.", "While swimming, the person saw a dolphin.", "Because the water was warm, the person swam in the ocean."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The person swam in the ocean\" هي جملة بسيطة، وتتضمن فاعل واحد (person) و فعل واحد (swam).  الخيارات الأخرى تحتوي على جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the simple sentence among these options: A. The children laughed and played joyfully in the park. B. The happy dog barked excitedly. C. While they were eating, the phone rang. D. After the game, they went home.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The happy dog barked excitedly\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد ومسند واحد، وتُعبّر عن فكرة واحدة كاملة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The large grey elephant walked slowly.' a simple sentence?",
        "options": ["Yes", "No", "Maybe", "It's a compound sentence"],
        "correct_option_id": 0,
        "explanation": "نعم، هذه جملة بسيطة، لأنها تحتوي على فاعل واحد (elephant) و فعل واحد (walked)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is a simple sentence? A. The students studied diligently for the exam, and they all passed. B. The cat sat lazily in the sun. C. Although it was raining, they played soccer. D. Before leaving, he locked the door.",
        "options": ["A", "B", "C", "D"],
        "correct_option_id": 1,
        "explanation": "الجملة \"The cat sat lazily in the sun\" هي جملة بسيطة، لأنها تحتوي على فاعل واحد ومسند واحد، وتُعبّر عن فكرة واحدة كاملة."
    }

],
    "الجمل المركبة":[
        {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following sentences is a compound sentence, correctly joined by a coordinating conjunction?",
        "options": ["A. The dog barked loudly; the cat hissed.", "B.  The sun was shining, and the birds were singing.", "C. Although it was raining, they played outside.", "D.  Before the race, the runners stretched."],
        "correct_option_id": 1,
        "explanation": "الجملة \"The sun was shining, and the birds were singing\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين (The sun was shining و The birds were singing) مستقلتين بذاتهما، أي كل منهما جملة تامة المعنى، ومرتبطتين برابطة وصل تنسيقية (coordinating conjunction) وهي (and)  في هذه الحالة.  يجب أن تسبق رابطة الوصل هذه بفاصلة.  الخيارات الأخرى إما جمل بسيطة أو جمل مركبة تحتوي على جمل تابعة (مثل Although, Before) بدلاً من جمل رئيسية مستقلة مرتبطة برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence using a semicolon to connect two independent clauses without a conjunction:",
        "options": ["A. The rain fell; the wind blew.", "B. It was raining; therefore, I stayed inside.", "C. She laughed; and he cried.", "D. The car was red; it was fast."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The rain fell; the wind blew\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (The rain fell و The wind blew) ، مرتبطتين بفاصلة منقوطة (;)  بدون أي رابطة وصل (conjunction).  يستخدم هذا التركيب عندما تكون الجملتان وثيقتي الصلة في المعنى،  وأن استخدام الفاصلة المنقوطة يضيف وضوحاً ويسهل قراءة الجملة.  الخيارات الأخرى إما تستخدم روابط وصل، أو تحتوي على جمل تابعة، أو هي جمل بسيطة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. He studied hard, but he still failed the test.", "B. She sang beautifully, and he played the piano.", "C. The dog barked loudly.", "D.  They went to the park, then they went home."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked loudly\" جملة بسيطة، لأنها تتكون من فاعل واحد (dog) ومسند واحد (barked loudly).  الجمل المركبة تتكون من جملتين رئيسيتين أو أكثر، كل منها جملة تامة المعنى بذاتها، ومرتبطة برابطة وصل (conjunction) أو بفاصلة منقوطة (;) . الخيارات الأخرى جمل مركبة، إما باستخدام روابط وصل (and, but) أو فاصلة منقوطة مع جمل رئيسية مستقلة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the compound sentence correctly using the conjunction 'or':",
        "options": ["A. Study hard, or you will fail the exam.", "B. He ate dinner, or she went to the cinema.", "C. The sun is shining, or the weather is cloudy.", "D. The flowers bloomed; the bees came."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Study hard, or you will fail the exam\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (Study hard و You will fail the exam)  مرتبطتين برابطة وصل (or) التي تدل على الاختيار بين الحالتين.  يجب أن تسبق رابطة الوصل هذه بفاصلة.  الخيارات الأخرى إما جمل بسيطة أو جمل مركبة غير مرتبطة بشكل صحيح أو باستخدام علامات ترقيم غير مناسبة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following sentences uses 'for' as a coordinating conjunction to show a reason or cause?",
        "options": ["A. He ran quickly, for he was late.", "B. She sang beautifully, and the audience applauded.", "C. Although it was raining, they continued their walk.", "D. Before he left, he locked the door."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He ran quickly, for he was late\" هي جملة مركبة صحيحة تستخدم \"for\" كرابطة وصل تنسيقية (coordinating conjunction)  لربط جملتين رئيسيتين مستقلتين (He ran quickly و he was late).  \"for\" في هذه الحالة تدل على السبب أو التفسير.  الخيارات الأخرى تحتوي على جمل تابعة، مما يجعلها جمل مركبة (complex sentences) وليست جملًا مركبة (compound sentences) من النوع الذي نبحث عنه."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence that uses 'nor' to express a negative condition:",
        "options": ["A. He didn't study, nor did he attend class.", "B. She is kind, and she is generous.", "C. The sun is shining, so it is warm.", "D. The birds sang sweetly, yet the wind howled."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He didn't study, nor did he attend class\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (He didn't study و He didn't attend class)  ومرتبطتين برابطة وصل تنسيقية (nor) التي تعبر عن حالة سلبية مزدوجة. لاحظ أن الفعل المساعد (did) متكرر في الجملتين  لأن الفعل الرئيسي (study, attend) في كلا الجملتين فعل في زمن الماضي البسيط. الخيارات الأخرى جمل مركبة أو بسيطة باستخدام روابط وصل أخرى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is a compound sentence joined correctly using a semicolon and no coordinating conjunction?",
        "options": ["A. The rain fell; the wind howled.", "B. The sun was shining; and the birds were singing.", "C. He was tired; but he finished the race.", "D.  She laughed; then she cried."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The rain fell; the wind howled\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (The rain fell و The wind howled)،  ومرتبطتين بفاصلة منقوطة (;)  دون استخدام أي رابطة وصل (conjunction).  الفاصلة المنقوطة تستخدم لربط جملتين رئيسيتين وثيقتي الصلة، عندما يكون المعنى واضحًا بدون الحاجة لرابطة وصل.  الخيارات الأخرى إما تستخدم روابط وصل، أو تحتوي على جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs the following sentence a compound sentence?  'She sang a song, and he played the guitar.'",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، الجملة \"She sang a song, and he played the guitar\" هي جملة مركبة.  تتكون من جملتين رئيسيتين مستقلتين (She sang a song و He played the guitar) مرتبطتين برابطة وصل تنسيقية (and).  كل جملة من الجملتين يمكن أن تقف بمفردها كجملة تامة المعنى.  الفاصلة قبل رابطة الوصل ضرورية في هذه الحالة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following sentences is NOT a compound sentence?",
        "options": ["A. The sun was shining, and the birds were singing.", "B. He ate dinner, then he watched TV.", "C.  The cat sat on the mat.", "D.  She laughed, but he cried."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The cat sat on the mat\" هي جملة بسيطة، لأنها تتكون من فاعل واحد (cat) ومسند واحد (sat on the mat).  الجمل المركبة تتكون من جملتين أو أكثر من الجمل البسيطة المستقلة التي يمكن أن تقف وحدها كجمل تامة المعنى.  الخيارات الأخرى جمل مركبة لأنها تحتوي على جملتين رئيسيتين مستقلتين مرتبطتين برابطة وصل أو فاصلة منقوطة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below demonstrates the correct use of a compound sentence with 'so' to show consequence?",
        "options": ["A.  It was raining, so I stayed inside.", "B. He is tall, so he plays basketball.", "C. She is kind, so she helps others.", "D. The sun is shining, so the birds are singing."],
        "correct_option_id": 0,
        "explanation": "الجملة \"It was raining, so I stayed inside\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (It was raining و I stayed inside)، ويربطهما \"so\"  التي تُعبّر عن نتيجة أو تبعية.  الجملة الأولى هي السبب، والجملة الثانية هي النتيجة.  الخيارات الأخرى قد تبدو جملًا مركبة، لكن العلاقة بين الجملتين ليست علاقة نتيجة واضحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound sentence using the words 'run', 'fast', 'tired', and 'rest':",
        "options": ["A. He ran fast, but he got tired, so he needed to rest.", "B. He ran fast and got tired.", "C. He was tired, so he rested.", "D. He ran."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He ran fast, but he got tired, so he needed to rest\" هي جملة مركبة صحيحة.  تتكون من ثلاث جمل رئيسية مستقلة مرتبطة برابطتي وصل (but, so).  تُعبّر الجملة عن تسلسل من الأحداث ونتائجها.  التركيب يوضح استخدام روابط وصل متعددة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound sentence joined by a coordinating conjunction and a comma?",
        "options": ["A.  The sun was shining, and the birds were singing.", "B. The rain fell heavily; the wind howled fiercely.", "C. Although it was late, he went to the store.", "D. Before the game, the players warmed up."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The sun was shining, and the birds were singing\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (The sun was shining و The birds were singing) مرتبطتين برابطة وصل تنسيقية (and)  مع فاصلة قبل الرابطة.  هذا التركيب هو الصحيح لربط جملتين بسيطتين مستقلة في جملة مركبة.  الخيارات الأخرى جمل بسيطة أو جمل مركبة باستخدام علامات ترقيم مختلفة أو جمل تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs the sentence 'The cat sat on the mat; the dog lay on the rug.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم،  الجملة \"The cat sat on the mat; the dog lay on the rug\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (The cat sat on the mat و The dog lay on the rug)  مرتبطتين بفاصلة منقوطة (;)  دون استخدام رابطة وصل.  هذا الاستخدام صحيح عندما تكون الجملتان وثيقتي الصلة في المعنى،  وتُعبر كل منهما عن فكرة مستقلة تامة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is NOT a compound sentence?",
        "options": ["A.  He worked hard, and he succeeded.", "B. She studied diligently, yet she failed the test.", "C. The rain was falling.", "D. They laughed, then they cried."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The rain was falling\" هي جملة بسيطة، لأنها تتكون من فاعل واحد (rain) ومسند واحد (was falling).  الجملة المركبة تتكون من جملتين رئيسيتين مستقلتين أو أكثر،  مرتبطة برابطة وصل أو فاصلة منقوطة.  الخيارات الأخرى جمل مركبة لأنها تحتوي على جملتين رئيسيتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nConstruct a compound sentence using 'read', 'book', 'watch', and 'movie':",
        "options": ["A. I read a book, and then I watched a movie.", "B. I read a book, and it was interesting.", "C. I watched a movie; it was exciting.", "D. The movie was good."],
        "correct_option_id": 0,
        "explanation": "الجملة \"I read a book, and then I watched a movie\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (I read a book و I watched a movie) مرتبطتين برابطة وصل (and) مع فاصلة قبل الرابطة.  هذا التركيب هو الصحيح لربط جملتين رئيسيتين مستقلتين في جملة مركبة.  الخيارات الأخرى جمل بسيطة أو مركبة لكن ليست بنفس البنية الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses 'so' to indicate a cause-and-effect relationship?",
        "options": ["A.  The sun was shining, so we went for a walk.", "B. He was tired, so he went to bed.", "C. She was happy, so she smiled.", "D. The birds were singing, so the flowers were blooming."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The sun was shining, so we went for a walk\" هي جملة مركبة صحيحة.  \"so\" تُستخدم هنا لتوضيح علاقة السببية بين الجملتين.  الجملة الأولى (The sun was shining) هي السبب، والجملة الثانية (we went for a walk) هي النتيجة. الخيارات الأخرى قد تبدو جملًا مركبة، لكن العلاقة بين الجملتين ليست علاقة سبب ونتيجة واضحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence that uses 'nor' correctly:",
        "options": ["A. He didn't eat, nor did he drink.", "B. She is not tall, nor is she short.", "C. The car is not fast, nor is it slow.", "D.  The sun is not shining, nor it is raining."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He didn't eat, nor did he drink\" هي جملة مركبة صحيحة.  تستخدم \"nor\" لربط جملتين رئيسيتين سلبيتين (He didn't eat و He didn't drink).  استخدام الفعل المساعد \"did\"  في كلا الجزئين ضروري  لأن الفعل الرئيسي في كلا الجملتين هو فعل في زمن الماضي البسيط. الخيارات الأخرى إما جمل بسيطة، أو جمل مركبة لكن استخدام nor غير صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following sentences is a compound sentence with two independent clauses joined by a comma and 'but'?",
        "options": ["A. The cat slept soundly, but the dog barked loudly.", "B.  Although it was late, he still went to the store.", "C. Because it was raining, they stayed inside.", "D.  Before the race started, the athletes stretched."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The cat slept soundly, but the dog barked loudly\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (The cat slept soundly و The dog barked loudly) مرتبطتين برابطة وصل تنسيقية (but)  مع فاصلة قبل الرابطة.  هذا التركيب هو الصحيح لربط جملتين بسيطتين مستقلة في جملة مركبة، حيث تعبر (but) عن التناقض بين الجملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs the sentence 'She went to the store; she bought milk.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، الجملة \"She went to the store; she bought milk\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (She went to the store و She bought milk) مرتبطتين بفاصلة منقوطة (;)  دون استخدام رابطة وصل.  هذا الاستخدام صحيح عندما تكون الجملتان وثيقتي الصلة في المعنى،  وتُعبّر كل منهما عن فكرة مستقلة تامة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is NOT a compound sentence?",
        "options": ["A. He worked hard, and he received a promotion.", "B. She studied diligently, but she still failed the exam.", "C.  The bird sang a beautiful song.", "D. They laughed, then they cried."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The bird sang a beautiful song\" هي جملة بسيطة، لأنها تتكون من فاعل واحد (bird) ومسند واحد (sang a beautiful song).  الجملة المركبة تتكون من جملتين رئيسيتين مستقلتين أو أكثر،  مرتبطة برابطة وصل أو فاصلة منقوطة.  الخيارات الأخرى جمل مركبة لأنها تحتوي على جملتين رئيسيتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nConstruct a compound sentence using 'eat', 'dinner', 'watch', and 'movie':",
        "options": ["A. I ate dinner, and then I watched a movie.", "B. I ate dinner, and it was delicious.", "C. I watched a movie; it was exciting.", "D. The movie was good."],
        "correct_option_id": 0,
        "explanation": "الجملة \"I ate dinner, and then I watched a movie\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (I ate dinner و I watched a movie) مرتبطتين برابطة وصل (and) مع فاصلة قبل الرابطة.  هذا التركيب هو الصحيح لربط جملتين رئيسيتين مستقلتين في جملة مركبة.  الخيارات الأخرى جمل بسيطة أو مركبة لكن ليست بنفس البنية الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses 'so' to show a clear cause-and-effect relationship?",
        "options": ["A. It was raining heavily, so we cancelled the picnic.", "B. He was tired, so he slept.", "C. She was happy, so she smiled.", "D. The birds were singing, so the sun was shining."],
        "correct_option_id": 0,
        "explanation": "الجملة \"It was raining heavily, so we cancelled the picnic\" هي جملة مركبة صحيحة.  \"so\" تُستخدم هنا لتوضيح علاقة السببية بين الجملتين.  الجملة الأولى (It was raining heavily) هي السبب، والجملة الثانية (we cancelled the picnic) هي النتيجة. الخيارات الأخرى قد تبدو جملًا مركبة، لكن العلاقة بين الجملتين ليست علاقة سبب ونتيجة واضحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence that uses 'nor' correctly to join two negative clauses:",
        "options": ["A. He did not go, nor did she.", "B. She is not tall, nor is she short.", "C. The car is not fast, nor is it slow.", "D. The sun is not shining, nor is it raining."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He did not go, nor did she\" هي جملة مركبة صحيحة.  \"nor\" تُستخدم لربط جملتين رئيسيتين سلبيتين.  استخدام الفعل المساعد \"did\" في كلا الجملتين ضروري  لأن الفعل الرئيسي (go) هو فعل في زمن الماضي البسيط.  الخيارات الأخرى إما جمل بسيطة، أو جمل مركبة لكن استخدام nor غير صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following sentences is a compound sentence with two independent clauses joined by a comma and 'but'?",
        "options": ["A. The cat slept peacefully, but the dog barked loudly.", "B. Although the sun was shining, it was cold.", "C. Because the food was delicious, they ate quickly.", "D. Before the movie started, they bought popcorn."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The cat slept peacefully, but the dog barked loudly\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (The cat slept peacefully و The dog barked loudly) مرتبطتين برابطة وصل تنسيقية (but)  مع فاصلة قبل الرابطة.  هذا التركيب هو الصحيح لربط جملتين بسيطتين مستقلة في جملة مركبة، حيث تعبر (but) عن التناقض بين الجملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs the sentence 'He went to the park; he played soccer.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، الجملة \"He went to the park; he played soccer\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (He went to the park و He played soccer) مرتبطتين بفاصلة منقوطة (;)  دون استخدام رابطة وصل.  هذا الاستخدام صحيح عندما تكون الجملتان وثيقتي الصلة في المعنى،  وتُعبّر كل منهما عن فكرة مستقلة تامة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is NOT a compound sentence?",
        "options": ["A. He worked hard, and he received a promotion.", "B. She studied diligently, but she still failed the exam.", "C. The bird flew high in the sky.", "D. They laughed, then they cried."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The bird flew high in the sky\" هي جملة بسيطة، لأنها تتكون من فاعل واحد (bird) ومسند واحد (flew high in the sky).  الجملة المركبة تتكون من جملتين رئيسيتين مستقلتين أو أكثر،  مرتبطة برابطة وصل أو فاصلة منقوطة.  الخيارات الأخرى جمل مركبة لأنها تحتوي على جملتين رئيسيتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nConstruct a compound sentence using 'eat', 'dinner', 'watch', and 'movie':",
        "options": ["A. I ate dinner, and then I watched a movie.", "B. I ate dinner, and it was delicious.", "C. I watched a movie; it was exciting.", "D. The movie was good."],
        "correct_option_id": 0,
        "explanation": "الجملة \"I ate dinner, and then I watched a movie\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (I ate dinner و I watched a movie) مرتبطتين برابطة وصل (and) مع فاصلة قبل الرابطة.  هذا التركيب هو الصحيح لربط جملتين رئيسيتين مستقلتين في جملة مركبة.  الخيارات الأخرى جمل بسيطة أو مركبة لكن ليست بنفس البنية الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses 'so' to show a clear cause-and-effect relationship?",
        "options": ["A. It was raining heavily, so we cancelled the picnic.", "B. He was tired, so he went to bed.", "C. She was happy, so she smiled.", "D. The birds were singing, so the sun was shining."],
        "correct_option_id": 0,
        "explanation": "الجملة \"It was raining heavily, so we cancelled the picnic\" هي جملة مركبة صحيحة.  \"so\" تُستخدم هنا لتوضيح علاقة السببية بين الجملتين.  الجملة الأولى (It was raining heavily) هي السبب، والجملة الثانية (we cancelled the picnic) هي النتيجة. الخيارات الأخرى قد تبدو جملًا مركبة، لكن العلاقة بين الجملتين ليست علاقة سبب ونتيجة واضحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence that uses 'nor' correctly to join two negative clauses:",
        "options": ["A. He did not go, nor did she.", "B. She is not tall, nor is she short.", "C. The car is not fast, nor is it slow.", "D. The sun is not shining, nor it is raining."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He did not go, nor did she\" هي جملة مركبة صحيحة.  \"nor\" تُستخدم لربط جملتين رئيسيتين سلبيتين.  استخدام الفعل المساعد \"did\" في كلا الجملتين ضروري  لأن الفعل الرئيسي (go) هو فعل في زمن الماضي البسيط.  الخيارات الأخرى إما جمل بسيطة، أو جمل مركبة لكن استخدام nor غير صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following sentences is a compound sentence with two independent clauses joined by a comma and 'but'?",
        "options": ["A. The cat slept peacefully, but the dog barked loudly.", "B. Although the sun was shining, it was cold.", "C. Because the food was delicious, they ate quickly.", "D. Before the movie started, they bought popcorn."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The cat slept peacefully, but the dog barked loudly\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (The cat slept peacefully و The dog barked loudly) مرتبطتين برابطة وصل تنسيقية (but)  مع فاصلة قبل الرابطة.  هذا التركيب هو الصحيح لربط جملتين بسيطتين مستقلة في جملة مركبة، حيث تعبر (but) عن التناقض بين الجملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs the sentence 'He went to the park; he played soccer.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، الجملة \"He went to the park; he played soccer\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (He went to the park و He played soccer) مرتبطتين بفاصلة منقوطة (;)  دون استخدام رابطة وصل.  هذا الاستخدام صحيح عندما تكون الجملتان وثيقتي الصلة في المعنى،  وتُعبّر كل منهما عن فكرة مستقلة تامة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is NOT a compound sentence?",
        "options": ["A. He worked hard, and he received a promotion.", "B. She studied diligently, but she still failed the exam.", "C. The bird sang a beautiful song.", "D. They laughed, then they cried."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The bird sang a beautiful song\" هي جملة بسيطة، لأنها تتكون من فاعل واحد (bird) ومسند واحد (sang a beautiful song).  الجملة المركبة تتكون من جملتين رئيسيتين مستقلتين أو أكثر،  مرتبطة برابطة وصل أو فاصلة منقوطة.  الخيارات الأخرى جمل مركبة لأنها تحتوي على جملتين رئيسيتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nConstruct a compound sentence using 'eat', 'dinner', 'watch', and 'movie':",
        "options": ["A. I ate dinner, and then I watched a movie.", "B. I ate dinner, and it was delicious.", "C. I watched a movie; it was exciting.", "D. The movie was good."],
        "correct_option_id": 0,
        "explanation": "الجملة \"I ate dinner, and then I watched a movie\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (I ate dinner و I watched a movie) مرتبطتين برابطة وصل (and) مع فاصلة قبل الرابطة.  هذا التركيب هو الصحيح لربط جملتين رئيسيتين مستقلتين في جملة مركبة.  الخيارات الأخرى جمل بسيطة أو مركبة لكن ليست بنفس البنية الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses 'so' to show a clear cause-and-effect relationship?",
        "options": ["A. It was raining heavily, so we cancelled the picnic.", "B. He was tired, so he went to bed.", "C. She was happy, so she smiled.", "D. The birds were singing, so the sun was shining."],
        "correct_option_id": 0,
        "explanation": "الجملة \"It was raining heavily, so we cancelled the picnic\" هي جملة مركبة صحيحة.  \"so\" تُستخدم هنا لتوضيح علاقة السببية بين الجملتين.  الجملة الأولى (It was raining heavily) هي السبب، والجملة الثانية (we cancelled the picnic) هي النتيجة. الخيارات الأخرى قد تبدو جملًا مركبة، لكن العلاقة بين الجملتين ليست علاقة سبب ونتيجة واضحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence that uses 'nor' correctly to join two negative clauses:",
        "options": ["A. He did not go, nor did she.", "B. She is not tall, nor is she short.", "C. The car is not fast, nor is it slow.", "D. The sun is not shining, nor it is raining."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He did not go, nor did she\" هي جملة مركبة صحيحة.  \"nor\" تُستخدم لربط جملتين رئيسيتين سلبيتين.  استخدام الفعل المساعد \"did\" في كلا الجملتين ضروري  لأن الفعل الرئيسي (go) هو فعل في زمن الماضي البسيط.  الخيارات الأخرى إما جمل بسيطة، أو جمل مركبة لكن استخدام nor غير صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following sentences is a compound sentence with two independent clauses joined by a comma and 'but'?",
        "options": ["A. The cat slept peacefully, but the dog barked loudly.", "B. Although the sun was shining, it was cold.", "C. Because the food was delicious, they ate quickly.", "D. Before the movie started, they bought popcorn."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The cat slept peacefully, but the dog barked loudly\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (The cat slept peacefully و The dog barked loudly) مرتبطتين برابطة وصل تنسيقية (but)  مع فاصلة قبل الرابطة.  هذا التركيب هو الصحيح لربط جملتين بسيطتين مستقلة في جملة مركبة، حيث تعبر (but) عن التناقض بين الجملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs the sentence 'He went to the park; he played soccer.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، الجملة \"He went to the park; he played soccer\" هي جملة مركبة صحيحة.  تتكون من جملتين رئيسيتين مستقلتين (He went to the park و He played soccer) مرتبطتين بفاصلة منقوطة (;)  دون استخدام رابطة وصل.  هذا الاستخدام صحيح عندما تكون الجملتان وثيقتي الصلة في المعنى،  وتُعبّر كل منهما عن فكرة مستقلة تامة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is a compound sentence?",
        "options": ["A. The dog barked loudly.", "B. The cat slept peacefully.", "C. The sun shone brightly, and the birds sang merrily.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The sun shone brightly, and the birds sang merrily\" هي جملة مركبة لأنها تتكون من جملتين بسيطتين مستقلتين (The sun shone brightly و The birds sang merrily) مرتبطتين برابطة وصل (and).  الجملة المركبة تتكون من جملتين أو أكثر من الجمل البسيطة المستقلة التي يمكن أن تقف وحدها كجمل تامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence:",
        "options": ["A. The bird flew high.", "B. The wind howled fiercely.", "C. The flowers bloomed, but the rain fell.", "D. The car was red."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The flowers bloomed, but the rain fell\"  جملة مركبة تتكون من جملتين رئيسيتين (The flowers bloomed و The rain fell)  مرتبطتين برابطة وصل (but) تُعبر كل منهما عن فكرة كاملة مستقلة.  الروابط المستخدمة في الجمل المركبة (and, but, or, nor, for, so, yet)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. She sang, and he danced.", "B. The sun was shining, yet it was cold.", "C. The tree is tall.", "D. They laughed, then cried."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The tree is tall\" جملة بسيطة، فهي تتكون من فاعل واحد (tree) ومسند واحد (is tall). الجمل المركبة تتكون من جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the compound sentence that uses a semicolon and no conjunction:",
        "options": ["A. The rain fell; the wind blew.", "B. He ate; she slept.", "C. The sun shone; and the birds sang.", "D. The cat sat; on the mat."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The rain fell; the wind blew\" هي جملة مركبة تستخدم الفاصلة المنقوطة (;) لربط جملتين بسيطتين مستقلتين وثيقتي الصلة.  الفصلة المنقوطة تستخدم لربط جملتين مرتبطتين ببعضهما البعض دون الحاجة لرابطة وصل مثل and, but, or.."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses the conjunction 'but'?",
        "options": ["A. He tried hard, but he failed.", "B. She laughed, and he cried.", "C. The sky is blue, and the grass is green.", "D. The sun is shining, so it is warm."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He tried hard, but he failed.\"  جملة مركبة تستخدم الرابطة \"but\"  لربط جملتين بسيطتين مستقلتين تُعبّر كل منهما عن فكرة تامة المعنى.  الرابطة \"but\" تُشير إلى التناقض أو التباين بين الجملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence using 'or':",
        "options": ["A. Study hard, or you will fail.", "B. He ate, and she drank.", "C. The car is fast, but it's expensive.", "D. The bird sings, so the flowers bloom."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Study hard, or you will fail.\" هي جملة مركبة تستخدم الرابطة \"or\"  لربط جملتين بسيطتين مستقلتين تُعبّر كل منهما عن فكرة تامة المعنى.  الرابطة \"or\"  تشير إلى الخيار بين الجملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is a compound sentence with a coordinating conjunction?",
        "options": ["A. The sun was setting, and the birds were returning to their nests.", "B. Although it was raining, the children played.", "C. The dog barked loudly at the mailman.", "D. Before leaving, he locked the door."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The sun was setting, and the birds were returning to their nests\" هي جملة مركبة لأنها تحتوي على جملتين رئيسيتين مستقلة مرتبطتين برابطة وصل (and). الرابطة \"and\"  هي رابطة تنسيقية (coordinating conjunction)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The cat slept, and the dog barked.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، هذه جملة مركبة لأنها تتكون من جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل (and).  كل جملة من الجملتين قادرة على الوقوف وحدها كجملة تامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. She laughed, and he cried.", "B. The sky was blue, and the birds were singing.", "C. The tree is tall.", "D. They ran, then stopped."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The tree is tall\" جملة بسيطة، لأنها تحتوي على فاعل واحد (tree) ومسند واحد (is tall).  الجمل المركبة تتكون من جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound sentence using 'rain', 'wind', and 'storm':",
        "options": ["A. The rain fell heavily, and the wind howled fiercely during the storm.", "B. The storm raged.", "C. The wind blew.", "D. It rained."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The rain fell heavily, and the wind howled fiercely during the storm\" جملة مركبة لأنها تحتوي على جملتين رئيسيتين مرتبطتين برابطة وصل (and).  كل جملة من الجملتين قادرة على الوقوف وحدها كجملة تامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses the conjunction 'for'?",
        "options": ["A. He studied hard, for he wanted to succeed.", "B. She sang a song, and he played the guitar.", "C. The sun was shining, so it was warm.", "D. The rain fell, but the sun shone."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He studied hard, for he wanted to succeed\" هي جملة مركبة لأنها تحتوي على جملتين رئيسيتين مرتبطتين برابطة وصل (for).  \"for\" تُعبّر عن السبب أو التفسير."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence with a semicolon and no conjunction:",
        "options": ["A. The sun was shining; the birds were singing.", "B. He ate lunch; then he went to work.", "C. The car is red; and it is fast.", "D. The cat sat; on the mat."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The sun was shining; the birds were singing\" جملة مركبة تستخدم الفاصلة المنقوطة لربط جملتين بسيطتين وثيقتي الصلة، بدون استخدام رابطة وصل (conjunction)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound sentence?",
        "options": ["A. The cat slept.", "B. The dog barked loudly.", "C. The birds chirped, and the sun shone.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The birds chirped, and the sun shone\" هي جملة مركبة، لأنها تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and). كل جملة من الجملتين مستقلة وتامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'She laughed, but he cried.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It is a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين بسيطتين مستقلتين (She laughed و he cried) مرتبطتين برابطة وصل (but) التي تعبر عن التناقض."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. She laughed, and he cried.", "B. The sky was blue, and the birds were singing.", "C. The tree is tall.", "D. They ran, then stopped."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The tree is tall\" جملة بسيطة.  الجمل المركبة تحتوي على جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound sentence using 'read', 'book', and 'slept':",
        "options": ["A. She read a book, and then she slept.", "B. She read a book.", "C. She slept soundly.", "D. The book was interesting."],
        "correct_option_id": 0,
        "explanation": "الجملة \"She read a book, and then she slept\" هي جملة مركبة تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and).  كل جملة تامة المعنى بذاتها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses the conjunction 'so'?",
        "options": ["A. It was raining, so I stayed inside.", "B. He is tall, and she is short.", "C. The sun shone, but it was cold.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"It was raining, so I stayed inside\"  جملة مركبة تربط جملتين بسيطتين (It was raining و I stayed inside)  برابطة وصل (so) التي تعبر عن نتيجة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence using 'yet':",
        "options": ["A. He was tired, yet he continued working.", "B. She is kind, and he is generous.", "C. The food was delicious, so we ate quickly.", "D. The car is fast, or it is slow."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He was tired, yet he continued working\"  جملة مركبة تربط جملتين بسيطتين (He was tired و he continued working)  برابطة وصل (yet) التي تعبر عن التناقض."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound sentence?",
        "options": ["A. The bird flew away.", "B. The cat jumped on the table.", "C. The dog barked, and the cat ran.", "D. The sun is setting."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked, and the cat ran\" هي جملة مركبة، لأنها تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and). كل جملة من الجملتين مستقلة وتامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'He studied hard, for he wanted to pass the exam.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It is a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين بسيطتين مستقلتين (He studied hard و he wanted to pass the exam) مرتبطتين برابطة وصل (for) التي تعبر عن السبب أو التفسير."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. The flowers bloomed, and the bees buzzed.", "B. The rain fell, but the sun shone.", "C. The bird sang a beautiful song.", "D. The children played, and then they ate."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The bird sang a beautiful song\" جملة بسيطة.  الجمل المركبة تحتوي على جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound sentence using 'walk', 'park', and 'rain':",
        "options": ["A. We walked in the park, but then it started to rain.", "B. It rained in the park.", "C. We walked.", "D. The park was beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"We walked in the park, but then it started to rain\" جملة مركبة لأنها تتكون من جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل (but).  كل جملة تامة المعنى بذاتها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses a semicolon to connect two closely related independent clauses?",
        "options": ["A. The storm raged; the trees swayed.", "B. The sun shone; and the birds sang.", "C. The car is red; it is fast.", "D. The cat sat; on the mat."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The storm raged; the trees swayed\"  جملة مركبة، تستخدم الفاصلة المنقوطة لربط جملتين رئيسيتين وثيقتي الصلة.  لا تحتاج إلى رابطة وصل (conjunction)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound sentence?",
        "options": ["A. The cat slept.", "B. The dog barked loudly.", "C. The birds chirped, and the sun shone.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The birds chirped, and the sun shone\" هي جملة مركبة، لأنها تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and). كل جملة من الجملتين مستقلة وتامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'She laughed, but he cried.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It is a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين بسيطتين مستقلتين (She laughed و he cried) مرتبطتين برابطة وصل (but) التي تعبر عن التناقض."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. She laughed, and he cried.", "B. The sky was blue, and the birds were singing.", "C. The tree is tall.", "D. They ran, then stopped."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The tree is tall\" جملة بسيطة.  الجمل المركبة تحتوي على جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound sentence using 'read', 'book', and 'slept':",
        "options": ["A. She read a book, and then she slept.", "B. She read a book.", "C. She slept soundly.", "D. The book was interesting."],
        "correct_option_id": 0,
        "explanation": "الجملة \"She read a book, and then she slept\" هي جملة مركبة تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and).  كل جملة تامة المعنى بذاتها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses the conjunction 'so'?",
        "options": ["A. It was raining, so I stayed inside.", "B. He is tall, and she is short.", "C. The sun shone, but it was cold.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"It was raining, so I stayed inside\"  جملة مركبة تربط جملتين بسيطتين (It was raining و I stayed inside)  برابطة وصل (so) التي تعبر عن نتيجة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence using 'yet':",
        "options": ["A. He was tired, yet he continued working.", "B. She is kind, and he is generous.", "C. The food was delicious, so we ate quickly.", "D. The car is fast, or it is slow."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He was tired, yet he continued working\"  جملة مركبة تربط جملتين بسيطتين (He was tired و he continued working)  برابطة وصل (yet) التي تعبر عن التناقض."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound sentence?",
        "options": ["A. The bird flew away.", "B. The cat jumped on the table.", "C. The dog barked, and the cat ran.", "D. The sun is setting."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked, and the cat ran\" هي جملة مركبة، لأنها تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and). كل جملة من الجملتين مستقلة وتامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'He studied hard, for he wanted to pass the exam.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It is a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين بسيطتين مستقلتين (He studied hard و he wanted to pass the exam) مرتبطتين برابطة وصل (for) التي تعبر عن السبب أو التفسير."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. The flowers bloomed, and the bees buzzed.", "B. The rain fell, but the sun shone.", "C. The bird sang a beautiful song.", "D. The children played, and then they ate."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The bird sang a beautiful song\" جملة بسيطة.  الجمل المركبة تحتوي على جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound sentence using 'walk', 'park', and 'rain':",
        "options": ["A. We walked in the park, but then it started to rain.", "B. It rained in the park.", "C. We walked.", "D. The park was beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"We walked in the park, but then it started to rain\" جملة مركبة لأنها تتكون من جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل (but).  كل جملة تامة المعنى بذاتها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses a semicolon to connect two closely related independent clauses?",
        "options": ["A. The storm raged; the trees swayed.", "B. The sun shone; and the birds sang.", "C. The car is red; it is fast.", "D. The cat sat; on the mat."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The storm raged; the trees swayed\"  جملة مركبة، تستخدم الفاصلة المنقوطة لربط جملتين رئيسيتين وثيقتي الصلة.  لا تحتاج إلى رابطة وصل (conjunction)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound sentence?",
        "options": ["A. The cat slept.", "B. The dog barked loudly.", "C. The birds chirped, and the sun shone.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The birds chirped, and the sun shone\" هي جملة مركبة، لأنها تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and). كل جملة من الجملتين مستقلة وتامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'She laughed, but he cried.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It is a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين بسيطتين مستقلتين (She laughed و he cried) مرتبطتين برابطة وصل (but) التي تعبر عن التناقض."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. She laughed, and he cried.", "B. The sky was blue, and the birds were singing.", "C. The tree is tall.", "D. They ran, then stopped."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The tree is tall\" جملة بسيطة.  الجمل المركبة تحتوي على جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound sentence using 'read', 'book', and 'slept':",
        "options": ["A. She read a book, and then she slept.", "B. She read a book.", "C. She slept soundly.", "D. The book was interesting."],
        "correct_option_id": 0,
        "explanation": "الجملة \"She read a book, and then she slept\" هي جملة مركبة تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and).  كل جملة تامة المعنى بذاتها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses the conjunction 'so'?",
        "options": ["A. It was raining, so I stayed inside.", "B. He is tall, and she is short.", "C. The sun shone, but it was cold.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"It was raining, so I stayed inside\"  جملة مركبة تربط جملتين بسيطتين (It was raining و I stayed inside)  برابطة وصل (so) التي تعبر عن نتيجة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence using 'yet':",
        "options": ["A. He was tired, yet he continued working.", "B. She is kind, and he is generous.", "C. The food was delicious, so we ate quickly.", "D. The car is fast, or it is slow."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He was tired, yet he continued working\"  جملة مركبة تربط جملتين بسيطتين (He was tired و he continued working)  برابطة وصل (yet) التي تعبر عن التناقض."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound sentence?",
        "options": ["A. The bird flew away.", "B. The cat jumped on the table.", "C. The dog barked, and the cat ran.", "D. The sun is setting."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked, and the cat ran\" هي جملة مركبة، لأنها تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and). كل جملة من الجملتين مستقلة وتامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'He studied hard, for he wanted to pass the exam.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It is a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين بسيطتين مستقلتين (He studied hard و he wanted to pass the exam) مرتبطتين برابطة وصل (for) التي تعبر عن السبب أو التفسير."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. The flowers bloomed, and the bees buzzed.", "B. The rain fell, but the sun shone.", "C. The bird sang a beautiful song.", "D. The children played, and then they ate."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The bird sang a beautiful song\" جملة بسيطة.  الجمل المركبة تحتوي على جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound sentence using 'walk', 'park', and 'rain':",
        "options": ["A. We walked in the park, but then it started to rain.", "B. It rained in the park.", "C. We walked.", "D. The park was beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"We walked in the park, but then it started to rain\" جملة مركبة لأنها تتكون من جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل (but).  كل جملة تامة المعنى بذاتها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses a semicolon to connect two closely related independent clauses?",
        "options": ["A. The storm raged; the trees swayed.", "B. The sun shone; and the birds sang.", "C. The car is red; it is fast.", "D. The cat sat; on the mat."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The storm raged; the trees swayed\"  جملة مركبة، تستخدم الفاصلة المنقوطة لربط جملتين رئيسيتين وثيقتي الصلة.  لا تحتاج إلى رابطة وصل (conjunction)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound sentence?",
        "options": ["A. The cat slept.", "B. The dog barked loudly.", "C. The birds chirped, and the sun shone.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The birds chirped, and the sun shone\" هي جملة مركبة، لأنها تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and). كل جملة من الجملتين مستقلة وتامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'She laughed, but he cried.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It is a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين بسيطتين مستقلتين (She laughed و he cried) مرتبطتين برابطة وصل (but) التي تعبر عن التناقض."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. She laughed, and he cried.", "B. The sky was blue, and the birds were singing.", "C. The tree is tall.", "D. They ran, then stopped."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The tree is tall\" جملة بسيطة.  الجمل المركبة تحتوي على جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound sentence using 'read', 'book', and 'slept':",
        "options": ["A. She read a book, and then she slept.", "B. She read a book.", "C. She slept soundly.", "D. The book was interesting."],
        "correct_option_id": 0,
        "explanation": "الجملة \"She read a book, and then she slept\" هي جملة مركبة تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and).  كل جملة تامة المعنى بذاتها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound sentence uses the conjunction 'so'?",
        "options": ["A. It was raining, so I stayed inside.", "B. He is tall, and she is short.", "C. The sun shone, but it was cold.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"It was raining, so I stayed inside\"  جملة مركبة تربط جملتين بسيطتين (It was raining و I stayed inside)  برابطة وصل (so) التي تعبر عن نتيجة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound sentence using 'yet':",
        "options": ["A. He was tired, yet he continued working.", "B. She is kind, and he is generous.", "C. The food was delicious, so we ate quickly.", "D. The car is fast, or it is slow."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He was tired, yet he continued working\"  جملة مركبة تربط جملتين بسيطتين (He was tired و he continued working)  برابطة وصل (yet) التي تعبر عن التناقض."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound sentence?",
        "options": ["A. The bird flew away.", "B. The cat jumped on the table.", "C. The dog barked, and the cat ran.", "D. The sun is setting."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked, and the cat ran\" هي جملة مركبة، لأنها تتكون من جملتين بسيطتين مرتبطتين برابطة وصل (and). كل جملة من الجملتين مستقلة وتامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'He studied hard, for he wanted to pass the exam.' a compound sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It is a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين بسيطتين مستقلتين (He studied hard و he wanted to pass the exam) مرتبطتين برابطة وصل (for) التي تعبر عن السبب أو التفسير."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound sentence?",
        "options": ["A. The flowers bloomed, and the bees buzzed.", "B. The rain fell, but the sun shone.", "C. The bird sang a beautiful song.", "D. The children played, and then they ate."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The bird sang a beautiful song\" جملة بسيطة.  الجمل المركبة تحتوي على جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound sentence using 'walk', 'park', and 'rain':",
        "options": ["A. We walked in the park, but then it started to rain.", "B. It rained in the park.", "C. We walked.", "D. The park was beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"We walked in the park, but then it started to rain\" جملة مركبة لأنها تتكون من جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل (but).  كل جملة تامة المعنى بذاتها."
    },
    ],
    "الجمل المعقدة": [
                {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is a complex sentence?",
        "options": ["A. The dog barked, and the cat ran.", "B. Although it was raining, he went for a walk.", "C. She laughed, then she cried.", "D. The sun shone brightly."],
        "correct_option_id": 1,
        "explanation": "الجملة \"Although it was raining, he went for a walk\" هي جملة مركبة، لأنها تتكون من جملة رئيسية (He went for a walk) وجملة تابعة (Although it was raining).  الجملة التابعة تعتمد على الجملة الرئيسية وتُعدّ جزءاً لا يتجزأ منها.  الخيارات الأخرى جمل بسيطة أو جمل مركبة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the complex sentence containing a subordinate clause introduced by 'because':",
        "options": ["A. He went home because he was tired.", "B. She sang, and he danced.", "C. The sun was shining, and the birds were singing.", "D.  The car is fast; it's expensive."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He went home because he was tired\" هي جملة مركبة تحتوي على جملة رئيسية (He went home) وجملة تابعة (because he was tired).  الجملة التابعة توضح سبب الفعل في الجملة الرئيسية.  الخيارات الأخرى جمل بسيطة أو جمل مركبة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a complex sentence?",
        "options": ["A. While he slept, the phone rang.", "B. Because it was cold, she put on her coat.", "C. The dog barked loudly.", "D.  If it rains, we will stay inside."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked loudly\" هي جملة بسيطة، لأنها تتكون من فاعل واحد (dog) ومسند واحد (barked loudly) ولا تحتوي على جملة تابعة.  الخيارات الأخرى جمل مركبة لأنها تتضمن جملًا تابعة تعتمد على الجملة الرئيسية في بنائها ومعناها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the complex sentence that uses a relative pronoun:",
        "options": ["A. The book that I borrowed is interesting.", "B. She laughed, and he cried.", "C. The sun was shining, but it was cold.", "D. The car is fast; it's expensive."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The book that I borrowed is interesting\" هي جملة مركبة تحتوي على جملة رئيسية (The book is interesting) وجملة تابعة (that I borrowed).  الضمير النسبي \"that\" يربط الجملة التابعة بالجملة الرئيسية ويشير إلى \"book\".  الخيارات الأخرى جمل بسيطة أو مركبة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich complex sentence contains an adverbial clause?",
        "options": ["A.  After the rain stopped, the sun came out.", "B. The dog barked at the mailman.", "C. She sang a beautiful song.", "D. The car is red and fast."],
        "correct_option_id": 0,
        "explanation": "الجملة \"After the rain stopped, the sun came out\" هي جملة مركبة تحتوي على جملة رئيسية (The sun came out) وجملة تابعة ظرفية (After the rain stopped).  الجملة التابعة الظرفية تُحدد الزمن الذي حدث فيه الفعل في الجملة الرئيسية.  الخيارات الأخرى جمل بسيطة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the complex sentence with a noun clause as the subject:",
        "options": ["A. What she said was surprising.", "B. The cat sat on the mat, and the dog barked.", "C. She laughed, but he cried.", "D. The bird sang sweetly; it was beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"What she said was surprising\" هي جملة مركبة حيث إنّ الجملة التابعة الاسمية (What she said) تعمل كموضوع للجملة الرئيسية (was surprising).  الخيارات الأخرى جمل بسيطة أو جمل مركبة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence below is a complex sentence with a subordinate clause introduced by 'if'?",
        "options": ["A. If it rains, we will stay inside.", "B. He went to the store, and he bought milk.", "C. The sun is shining, and the birds are singing.", "D. The car is fast; it is expensive."],
        "correct_option_id": 0,
        "explanation": "الجملة \"If it rains, we will stay inside\" هي جملة مركبة تحتوي على جملة رئيسية (we will stay inside) وجملة تابعة شرطية (If it rains).  الجملة التابعة الشرطية تُعبّر عن شرطٍ لحدوث الفعل في الجملة الرئيسية.  الخيارات الأخرى جمل بسيطة أو مركبة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'Because it was late, he hurried home.' a complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a compound sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، الجملة \"Because it was late, he hurried home\" هي جملة مركبة.  تحتوي على جملة رئيسية (He hurried home) وجملة تابعة سببية (Because it was late).  الجملة التابعة تُبيّن سبب الفعل في الجملة الرئيسية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a complex sentence?",
        "options": ["A. While she sang, he played the guitar.", "B. Although it was cold, they went for a walk.", "C. He ate dinner, and then he went to bed.", "D.  If you study hard, you will succeed."],
        "correct_option_id": 2,
        "explanation": "الجملة \"He ate dinner, and then he went to bed\" هي جملة مركبة،  وليس جملة مركبة لأنها تتكون من جملتين بسيطتين مستقلتين مرتبطتين برابطة وصل (and).  الخيارات الأخرى جمل مركبة لأنها تتضمن جملًا تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a complex sentence using 'rain', 'play', and 'outside':",
        "options": ["A. Because it was raining, we couldn't play outside.", "B. It was raining, and we played outside.", "C. We played outside, and it rained.", "D. It was raining outside."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Because it was raining, we couldn't play outside\" هي جملة مركبة تحتوي على جملة رئيسية (we couldn't play outside) وجملة تابعة سببية (Because it was raining).  الخيارات الأخرى جمل بسيطة أو مركبة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich complex sentence uses 'since' to introduce a subordinate clause?",
        "options": ["A. Since it was a beautiful day, we went for a picnic.", "B. He is tall, and she is short.", "C. The car is fast, but it is expensive.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Since it was a beautiful day, we went for a picnic\" هي جملة مركبة تحتوي على جملة رئيسية (we went for a picnic) وجملة تابعة زمانية (Since it was a beautiful day). \"Since\" تُشير إلى الزمن."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the complex sentence using 'although' to show contrast:",
        "options": ["A. Although it was raining, the game continued.", "B. He is tall, and she is short.", "C. The car is fast, but it is expensive.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Although it was raining, the game continued\" هي جملة مركبة.  تحتوي على جملة رئيسية (the game continued) وجملة تابعة تقارنية (Although it was raining) تُبيّن التناقض."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a complex sentence?",
        "options": ["A. The cat slept.", "B. The dog barked loudly.", "C. Because it was late, he hurried home.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"Because it was late, he hurried home\" هي جملة مركبة لأنها تتضمن جملة رئيسية (He hurried home) وجملة تابعة (Because it was late). "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'After the movie ended, they went home.' a complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a compound sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، هذه جملة مركبة لأنها تتضمن جملة رئيسية (they went home) وجملة تابعة ظرفية (After the movie ended) تُحدد الزمن."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a complex sentence?",
        "options": ["A. While she was singing, he played the piano.", "B. If it snows, we will build a snowman.", "C. The sun is shining brightly.", "D. Because he was tired, he went to bed."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The sun is shining brightly\" هي جملة بسيطة، لأنها لا تحتوي على جملة تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a complex sentence using 'study', 'hard', and 'succeed':",
        "options": ["A. If you study hard, you will succeed.", "B. You studied hard, and you succeeded.", "C. Studying hard leads to success.", "D. Success comes from hard work."],
        "correct_option_id": 0,
        "explanation": "الجملة \"If you study hard, you will succeed\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (you will succeed) وجملة تابعة شرطية (If you study hard)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich complex sentence uses 'since' to indicate a reason?",
        "options": ["A. Since he was tired, he went to bed.", "B. He is tall, and she is short.", "C. The car is fast; it's expensive.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Since he was tired, he went to bed\" هي جملة مركبة. \"Since\"  تُشير إلى السبب هنا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the complex sentence with a noun clause as the object:",
        "options": ["A. I know that he is happy.", "B. The cat sat on the mat.", "C. She laughed, and he cried.", "D. The bird sang sweetly."],
        "correct_option_id": 0,
        "explanation": "الجملة \"I know that he is happy\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (I know) وجملة تابعة اسمية (that he is happy) تعمل كمفعول به."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a complex sentence?",
        "options": ["A. The cat sat on the mat.", "B. The dog barked loudly.", "C.  Because the sun was shining, we went for a walk.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"Because the sun was shining, we went for a walk\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (we went for a walk) وجملة تابعة سببية (Because the sun was shining)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'While he was sleeping, the phone rang.' a complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a compound sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تحتوي على جملة رئيسية (the phone rang) وجملة تابعة ظرفية (While he was sleeping)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a complex sentence?",
        "options": ["A. Although it was cold, she wore a coat.", "B. If you study hard, you will pass the exam.", "C. The dog barked at the stranger.", "D. Because it was raining, the game was cancelled."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked at the stranger\" هي جملة بسيطة، لأنها لا تحتوي على جملة تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a complex sentence using 'read', 'book', and 'tired':",
        "options": ["A. Because I was tired, I stopped reading the book.", "B. I read a book, and then I went to sleep.", "C. I read the book; it was interesting.", "D. The book was long."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Because I was tired, I stopped reading the book\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (I stopped reading the book) وجملة تابعة سببية (Because I was tired)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich complex sentence uses 'since' to show a time relationship?",
        "options": ["A. Since I was a child, I have loved to read.", "B. He is tall, and she is short.", "C. The car is fast, but it is expensive.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Since I was a child, I have loved to read\" هي جملة مركبة. \"Since\" تُشير إلى الزمن هنا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the complex sentence with a noun clause as the subject:",
        "options": ["A. That he won the race surprised everyone.", "B. The cat sat on the mat, and the dog barked.", "C. She laughed, but he cried.", "D. The bird sang sweetly; it was beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"That he won the race surprised everyone\" هي جملة مركبة  لأنّ الجملة التابعة الاسمية (That he won the race) تعمل كموضوع للجملة الرئيسية (surprised everyone)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a complex sentence?",
        "options": ["A. The cat sat on the mat.", "B. The dog barked loudly.", "C.  Although it was cold, they went for a walk.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"Although it was cold, they went for a walk\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (they went for a walk) وجملة تابعة تقارنية (Although it was cold)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'While she was cooking, he was reading a book.' a complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a compound sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تحتوي على جملة رئيسية (he was reading a book) وجملة تابعة ظرفية (While she was cooking)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a complex sentence?",
        "options": ["A. Because it was late, he hurried home.", "B. If you try hard, you will succeed.", "C. The car is blue and shiny.", "D. Although she was tired, she finished her work."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The car is blue and shiny\" هي جملة بسيطة، لأنها لا تحتوي على جملة تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a complex sentence using 'eat', 'dinner', and 'tired':",
        "options": ["A. After I ate dinner, I felt tired.", "B. I ate dinner, and then I went to bed.", "C. I ate dinner; it was delicious.", "D. Dinner was ready."],
        "correct_option_id": 0,
        "explanation": "الجملة \"After I ate dinner, I felt tired\" هي جملة مركبة لأنها تحتوي على جملة رئيسية (I felt tired) وجملة تابعة ظرفية (After I ate dinner)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich complex sentence uses 'since' to indicate a point in time?",
        "options": ["A. Since I last saw you, much has changed.", "B. He is tall, and she is short.", "C. The car is fast, but it's expensive.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Since I last saw you, much has changed\" هي جملة مركبة. \"Since\" تُشير إلى نقطة زمنية محددة هنا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the complex sentence with a noun clause as the object:",
        "options": ["A. She said that she was happy.", "B. The cat sat on the mat.", "C. He laughed, and she cried.", "D. The bird sang sweetly."],
        "correct_option_id": 0,
        "explanation": "الجملة \"She said that she was happy\" هي جملة مركبة لأنها تحتوي على جملة رئيسية (She said) وجملة تابعة اسمية (that she was happy) تعمل كمفعول به."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a complex sentence?",
        "options": ["A. The cat sat on the mat.", "B. The dog barked loudly.", "C. Because it was late, he hurried home.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"Because it was late, he hurried home\" هي جملة مركبة لأنها تتضمن جملة رئيسية (He hurried home) وجملة تابعة (Because it was late)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'While she was sleeping, the phone rang.' a complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a compound sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تحتوي على جملة رئيسية (the phone rang) وجملة تابعة ظرفية (While she was sleeping)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a complex sentence?",
        "options": ["A. Although it was cold, she wore a coat.", "B. If you study hard, you will pass the exam.", "C. The dog barked at the stranger.", "D. Because it was raining, the game was cancelled."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked at the stranger\" هي جملة بسيطة، لأنها لا تحتوي على جملة تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a complex sentence using 'read', 'book', and 'tired':",
        "options": ["A. Because I was tired, I stopped reading the book.", "B. I read a book, and then I went to sleep.", "C. I read the book; it was interesting.", "D. The book was long."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Because I was tired, I stopped reading the book\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (I stopped reading the book) وجملة تابعة سببية (Because I was tired)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich complex sentence uses 'since' to show a time relationship?",
        "options": ["A. Since I was a child, I have loved to read.", "B. He is tall, and she is short.", "C. The car is fast, but it is expensive.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Since I was a child, I have loved to read\" هي جملة مركبة. \"Since\" تُشير إلى الزمن هنا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the complex sentence with a noun clause as the subject:",
        "options": ["A. That he won the race surprised everyone.", "B. The cat sat on the mat, and the dog barked.", "C. She laughed, but he cried.", "D. The bird sang sweetly; it was beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"That he won the race surprised everyone\" هي جملة مركبة  لأنّ الجملة التابعة الاسمية (That he won the race) تعمل كموضوع للجملة الرئيسية (surprised everyone)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a complex sentence?",
        "options": ["A. The cat sat on the mat.", "B. The dog barked loudly.", "C. Although it was cold, they went for a walk.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"Although it was cold, they went for a walk\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (they went for a walk) وجملة تابعة تقارنية (Although it was cold)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'While she was sleeping, the phone rang.' a complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a compound sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تحتوي على جملة رئيسية (the phone rang) وجملة تابعة ظرفية (While she was sleeping)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a complex sentence?",
        "options": ["A. Although it was cold, she wore a coat.", "B. If you study hard, you will pass the exam.", "C. The dog barked at the stranger.", "D. Because it was raining, the game was cancelled."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked at the stranger\" هي جملة بسيطة، لأنها لا تحتوي على جملة تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a complex sentence using 'read', 'book', and 'tired':",
        "options": ["A. Because I was tired, I stopped reading the book.", "B. I read a book, and then I went to sleep.", "C. I read the book; it was interesting.", "D. The book was long."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Because I was tired, I stopped reading the book\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (I stopped reading the book) وجملة تابعة سببية (Because I was tired)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich complex sentence uses 'since' to show a time relationship?",
        "options": ["A. Since I was a child, I have loved to read.", "B. He is tall, and she is short.", "C. The car is fast, but it is expensive.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Since I was a child, I have loved to read\" هي جملة مركبة. \"Since\" تُشير إلى الزمن هنا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the complex sentence with a noun clause as the subject:",
        "options": ["A. That he won the race surprised everyone.", "B. The cat sat on the mat, and the dog barked.", "C. She laughed, but he cried.", "D. The bird sang sweetly; it was beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"That he won the race surprised everyone\" هي جملة مركبة  لأنّ الجملة التابعة الاسمية (That he won the race) تعمل كموضوع للجملة الرئيسية (surprised everyone)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a complex sentence?",
        "options": ["A. The cat sat on the mat.", "B. The dog barked loudly.", "C. Although it was cold, they went for a walk.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"Although it was cold, they went for a walk\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (they went for a walk) وجملة تابعة تقارنية (Although it was cold)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'While she was sleeping, the phone rang.' a complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a compound sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تحتوي على جملة رئيسية (the phone rang) وجملة تابعة ظرفية (While she was sleeping)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a complex sentence?",
        "options": ["A. Although it was cold, she wore a coat.", "B. If you study hard, you will pass the exam.", "C. The dog barked at the stranger.", "D. Because it was raining, the game was cancelled."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked at the stranger\" هي جملة بسيطة، لأنها لا تحتوي على جملة تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a complex sentence using 'read', 'book', and 'tired':",
        "options": ["A. Because I was tired, I stopped reading the book.", "B. I read a book, and then I went to sleep.", "C. I read the book; it was interesting.", "D. The book was long."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Because I was tired, I stopped reading the book\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (I stopped reading the book) وجملة تابعة سببية (Because I was tired)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich complex sentence uses 'since' to show a time relationship?",
        "options": ["A. Since I was a child, I have loved to read.", "B. He is tall, and she is short.", "C. The car is fast, but it is expensive.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Since I was a child, I have loved to read\" هي جملة مركبة. \"Since\" تُشير إلى الزمن هنا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the complex sentence with a noun clause as the subject:",
        "options": ["A. That he won the race surprised everyone.", "B. The cat sat on the mat, and the dog barked.", "C. She laughed, but he cried.", "D. The bird sang sweetly; it was beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"That he won the race surprised everyone\" هي جملة مركبة  لأنّ الجملة التابعة الاسمية (That he won the race) تعمل كموضوع للجملة الرئيسية (surprised everyone)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a complex sentence?",
        "options": ["A. The cat sat on the mat.", "B. The dog barked loudly.", "C. Although it was cold, they went for a walk.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"Although it was cold, they went for a walk\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (they went for a walk) وجملة تابعة تقارنية (Although it was cold)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'While she was sleeping, the phone rang.' a complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a compound sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تحتوي على جملة رئيسية (the phone rang) وجملة تابعة ظرفية (While she was sleeping)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a complex sentence?",
        "options": ["A. Although it was cold, she wore a coat.", "B. If you study hard, you will pass the exam.", "C. The dog barked at the stranger.", "D. Because it was raining, the game was cancelled."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked at the stranger\" هي جملة بسيطة، لأنها لا تحتوي على جملة تابعة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a complex sentence using 'read', 'book', and 'tired':",
        "options": ["A. Because I was tired, I stopped reading the book.", "B. I read a book, and then I went to sleep.", "C. I read the book; it was interesting.", "D. The book was long."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Because I was tired, I stopped reading the book\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (I stopped reading the book) وجملة تابعة سببية (Because I was tired)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich complex sentence uses 'since' to show a time relationship?",
        "options": ["A. Since I was a child, I have loved to read.", "B. He is tall, and she is short.", "C. The car is fast, but it is expensive.", "D. The birds sang, or the wind blew."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Since I was a child, I have loved to read\" هي جملة مركبة. \"Since\" تُشير إلى الزمن هنا."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the complex sentence with a noun clause as the subject:",
        "options": ["A. That he won the race surprised everyone.", "B. The cat sat on the mat, and the dog barked.", "C. She laughed, but he cried.", "D. The bird sang sweetly; it was beautiful."],
        "correct_option_id": 0,
        "explanation": "الجملة \"That he won the race surprised everyone\" هي جملة مركبة  لأنّ الجملة التابعة الاسمية (That he won the race) تعمل كموضوع للجملة الرئيسية (surprised everyone)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a complex sentence?",
        "options": ["A. The cat sat on the mat.", "B. The dog barked loudly.", "C. Although it was cold, they went for a walk.", "D. The rain fell softly."],
        "correct_option_id": 2,
        "explanation": "الجملة \"Although it was cold, they went for a walk\" هي جملة مركبة  لأنها تحتوي على جملة رئيسية (they went for a walk) وجملة تابعة تقارنية (Although it was cold)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'While she was sleeping, the phone rang.' a complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a compound sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تحتوي على جملة رئيسية (the phone rang) وجملة تابعة ظرفية (While she was sleeping)."
    },
    ],
    "الجمل المركبة المعقدة": [
            {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is a compound-complex sentence?",
        "options": ["A. The dog barked, and the cat ran away.", "B. Although it was raining, he went for a walk, and he enjoyed the fresh air.", "C. She laughed, then she cried.", "D. The sun shone brightly."],
        "correct_option_id": 1,
        "explanation": "الجملة \"Although it was raining, he went for a walk, and he enjoyed the fresh air\"  هي جملة مركبة معقدة لأنها تتكون من جملتين رئيسيتين (he went for a walk و he enjoyed the fresh air)  مرتبطتين برابطة وصل (and)، بالإضافة إلى جملة تابعة (Although it was raining).  الخيارات الأخرى جمل بسيطة أو جمل مركبة فقط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound-complex sentence:",
        "options": ["A. He went home because he was tired.", "B. She sang, and he danced.", "C. The rain stopped, but the ground was still wet because it had poured for hours.", "D. The car is fast; it's expensive."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The rain stopped, but the ground was still wet because it had poured for hours\" هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (The rain stopped و the ground was still wet) مرتبطتين برابطة وصل (but)  وجملة تابعة (because it had poured for hours).  الخيارات الأخرى جمل بسيطة أو جمل مركبة فقط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound-complex sentence?",
        "options": ["A. While he slept, the phone rang, but he didn't hear it.", "B. Because it was cold, she put on her coat, and she went outside.", "C. The dog barked loudly.", "D. If it rains, we will stay inside, and we will play games."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The dog barked loudly\" هي جملة بسيطة، لأنها لا تحتوي على جمل رئيسية متعددة أو جمل تابعة.  الجمل المركبة المعقدة تحتوي على جملتين رئيسيتين على الأقل وجملة تابعة واحدة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the compound-complex sentence that uses a semicolon:",
        "options": ["A. The book that I borrowed is interesting; I finished it in one day.", "B. She laughed, and he cried.", "C. The sun was shining, but it was cold.", "D.  The car is fast, or it is slow."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The book that I borrowed is interesting; I finished it in one day\"  هي جملة مركبة معقدة تستخدم الفاصلة المنقوطة (;)  لربط جملتين رئيسيتين مستقلتين.  تحتوي الجملة الأولى أيضًا على جملة تابعة (that I borrowed).  الخيارات الأخرى جمل بسيطة أو جمل مركبة فقط."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound-complex sentence uses the conjunction 'but' to connect two independent clauses?",
        "options": ["A. He tried hard, but he failed, even though he studied for hours.", "B. She laughed, and he cried.", "C. The sun is shining, so we will go for a walk.", "D.  The flowers bloomed, and the bees buzzed."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He tried hard, but he failed, even though he studied for hours\" هي جملة مركبة معقدة.  \"but\"  تربط جملتين رئيسيتين  (He tried hard و he failed).  بالإضافة إلى ذلك،  تحتوي الجملة على جملة تابعة (even though he studied for hours)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound-complex sentence using 'or':",
        "options": ["A. Study hard, or you will fail the exam, which would be disappointing.", "B. He ate, and she drank.", "C. The car is fast, but it is expensive.", "D. The bird sings, because it is happy."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Study hard, or you will fail the exam, which would be disappointing\" هي جملة مركبة معقدة.  \"or\" تربط جملتين رئيسيتين (Study hard و you will fail the exam).  بالإضافة إلى ذلك،  تحتوي الجملة على جملة تابعة (which would be disappointing)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is a compound-complex sentence with at least two independent clauses and one dependent clause?",
        "options": ["A.  Although it was raining, they went to the beach, and they had a great time.", "B. He studied hard; he passed the test.", "C. The dog barked at the mailman.", "D.  Before the game, the players warmed up."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Although it was raining, they went to the beach, and they had a great time\" هي جملة مركبة معقدة، لأنها تحتوي على جملتين رئيسيتين (they went to the beach و they had a great time) مرتبطتين برابطة وصل (and)، بالإضافة إلى جملة تابعة (Although it was raining)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'The cat slept while the dog barked, and the bird sang.' a compound-complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم،  الجملة \"The cat slept while the dog barked, and the bird sang\" هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (The cat slept و the bird sang)  مرتبطتين برابطة وصل (and)  وجملة تابعة (while the dog barked).  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound-complex sentence?",
        "options": ["A.  Because it was raining, the picnic was cancelled, and everyone went home.", "B.  She studied hard, but she still failed the exam, even though she asked for help.", "C.  The cat sat on the mat.", "D.  If you practice every day, you will improve, and you will enjoy playing the piano more."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The cat sat on the mat\" هي جملة بسيطة.  الجمل المركبة المعقدة تتضمن جملتين رئيسيتين على الأقل وجملة تابعة واحدة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound-complex sentence using 'run', 'fast', 'tired', and 'win':",
        "options": ["A. Although he was tired, he ran fast, and he won the race.", "B. He ran fast and got tired.", "C. He was tired, so he rested.", "D. He ran and won."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Although he was tired, he ran fast, and he won the race\" هي جملة مركبة معقدة، لأنها تحتوي على جملتين رئيسيتين (he ran fast و he won the race) مرتبطتين برابطة وصل (and)، بالإضافة إلى جملة تابعة (Although he was tired)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound-complex sentence uses 'for' as a coordinating conjunction to connect two independent clauses?",
        "options": ["A. She went to the store, for she needed milk, and she also wanted to buy bread.", "B. He is tall, and she is short.", "C. The sun shone, but it was cold.", "D. The birds sang, yet the wind howled."],
        "correct_option_id": 0,
        "explanation": "الجملة \"She went to the store, for she needed milk, and she also wanted to buy bread\" هي جملة مركبة معقدة  لأنها تحتوي على جملتين رئيسيتين مرتبطتين بـ \"for\"  (She went to the store و she needed milk)  بالإضافة إلى جملة رئيسية أخرى (she also wanted to buy bread) مرتبطة بـ \"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound-complex sentence using a semicolon to connect two independent clauses:",
        "options": ["A. The children played in the park; their parents watched from a nearby bench.", "B. He ate lunch, then he went to work.", "C. Although it was late, they continued driving.", "D. Before the concert, they tuned their instruments."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The children played in the park; their parents watched from a nearby bench\"  هي جملة مركبة معقدة.  تستخدم الفاصلة المنقوطة (;)  لربط جملتين رئيسيتين مستقلتين.  كل جملة من الجملتين قادرة على الوقوف وحدها كجملة تامة المعنى.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound-complex sentence?",
        "options": ["A. The cat slept.", "B. Although it was raining, he decided to walk to the store, and he enjoyed the fresh air.", "C. The dog barked loudly.", "D. The rain fell softly."],
        "correct_option_id": 1,
        "explanation": "الجملة \"Although it was raining, he decided to walk to the store, and he enjoyed the fresh air\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (he decided to walk to the store و he enjoyed the fresh air)  وجملة تابعة (Although it was raining)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'She baked a cake while her children played, and they all enjoyed it later.' a compound-complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين رئيسيتين (She baked a cake و they all enjoyed it later) وجملة تابعة (while her children played). "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound-complex sentence?",
        "options": ["A.  He finished his homework, but he was tired, so he went to bed.", "B.  She went to the library, although it was raining, and she borrowed a book.", "C.  The car is red.", "D.  While the sun was shining, the birds sang, and the flowers bloomed."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The car is red\"  هي جملة بسيطة.  الجمل المركبة المعقدة تحتوي على جملتين رئيسيتين على الأقل وجملة تابعة واحدة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound-complex sentence using 'study', 'hard', 'pass', and 'celebrate':",
        "options": ["A.  Because they studied hard, they passed the exam, and they celebrated their success.", "B.  They studied hard, and they passed the exam.", "C. They celebrated their success.", "D. The exam was difficult."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Because they studied hard, they passed the exam, and they celebrated their success\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (they passed the exam و they celebrated their success) وجملة تابعة (Because they studied hard). "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound-complex sentence uses 'so' to show a result or consequence?",
        "options": ["A.  It was raining heavily, so they decided to stay home, and they watched a movie.", "B. He studied, so he passed.", "C. She ate, so she was full.", "D. The bird sang, so the flowers bloomed."],
        "correct_option_id": 0,
        "explanation": "الجملة \"It was raining heavily, so they decided to stay home, and they watched a movie\" هي جملة مركبة معقدة  لأنها تحتوي على جملتين رئيسيتين (they decided to stay home و they watched a movie) مرتبطتين بـ \"and\"  بالإضافة إلى جملة تابعة (It was raining heavily) مرتبطة بـ\"so\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound-complex sentence using 'yet' to indicate contrast:",
        "options": ["A.  He worked all day, yet he was still energetic, and he went for a run.", "B. He worked all day, yet he was tired.", "C. She is small, yet strong.", "D. The food was good, yet he didn't eat."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He worked all day, yet he was still energetic, and he went for a run\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (he was still energetic و he went for a run) مرتبطتين بـ \"and\" بالإضافة إلى جملة رئيسية أخرى (He worked all day) مرتبطة بـ \"yet\" التي تُعبّر عن التناقض. "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound-complex sentence?",
        "options": ["A. The cat is sleeping.", "B. The birds chirped merrily while the sun shone brightly, and a gentle breeze blew through the trees.", "C. The car is blue.", "D. The house is large."],
        "correct_option_id": 1,
        "explanation": "الجملة \"The birds chirped merrily while the sun shone brightly, and a gentle breeze blew through the trees\" هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (The birds chirped merrily و a gentle breeze blew through the trees) مرتبطتين بـ \"and\" وجملة تابعة (while the sun shone brightly).  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'After they ate dinner, they went for a walk, because the weather was pleasant.' a compound-complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين رئيسيتين (they went for a walk و the weather was pleasant) وجملة تابعة (After they ate dinner)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound-complex sentence?",
        "options": ["A. The children played in the park while their parents watched, and they all enjoyed the beautiful day.", "B.  She studied hard, yet she failed the test, even though she asked for help.", "C.  The rain is falling.", "D.  Although it was late, he finished his work, and he went to bed."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The rain is falling\" هي جملة بسيطة.  الجمل المركبة المعقدة تتضمن جملتين رئيسيتين على الأقل وجملة تابعة واحدة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound-complex sentence using 'read', 'book', 'enjoy', and 'learn':",
        "options": ["A.  She read a book that she enjoyed, and she learned a lot from it.", "B. She read a book and enjoyed it.", "C. She enjoyed the book.", "D. She learned a lot."],
        "correct_option_id": 0,
        "explanation": "الجملة \"She read a book that she enjoyed, and she learned a lot from it\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (She read a book و she learned a lot from it) وجملة تابعة (that she enjoyed)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound-complex sentence uses 'nor' as a coordinating conjunction?",
        "options": ["A. He didn't go to the party, nor did he call to explain, although he knew it was important.", "B. He didn't go, nor did he call.", "C. She doesn't like coffee, nor tea.", "D. He didn't study, nor did he pass."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He didn't go to the party, nor did he call to explain, although he knew it was important\" هي جملة مركبة معقدة  لأنها تحتوي على جملتين رئيسيتين (He didn't go to the party و he didn't call to explain) مرتبطتين بـ \"nor\"  بالإضافة إلى جملة تابعة (although he knew it was important)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound-complex sentence with a comma and a coordinating conjunction connecting two independent clauses:",
        "options": ["A.  Although it was late, he finished his work, and he went to bed.", "B. He ate dinner, and then he went for a walk.", "C. The rain stopped, but the ground was wet.", "D. The car is red; it is fast."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Although it was late, he finished his work, and he went to bed\"  هي جملة مركبة معقدة.  تستخدم الفاصلة و رابطة الوصل (and) لربط جملتين رئيسيتين (he finished his work و he went to bed).  بالإضافة إلى ذلك،  تحتوي الجملة على جملة تابعة (Although it was late)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound-complex sentence?",
        "options": ["A. The sun is shining.", "B. Even though it was raining, we decided to go for a walk, and we enjoyed the fresh air.", "C. The dog barked.", "D. The cat meowed."],
        "correct_option_id": 1,
        "explanation": "الجملة \"Even though it was raining, we decided to go for a walk, and we enjoyed the fresh air\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (we decided to go for a walk و we enjoyed the fresh air)  وجملة تابعة (Even though it was raining)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'Before they left, they packed their bags, and they checked the weather forecast.' a compound-complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين رئيسيتين (they packed their bags و they checked the weather forecast) وجملة تابعة (Before they left)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound-complex sentence?",
        "options": ["A. The students studied hard for the test, but they were still nervous, even though they had prepared well.", "B. She ate lunch, and then she went for a walk.", "C. The flowers are blooming.", "D. While he was sleeping, the phone rang, and he missed the call."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The flowers are blooming\"  هي جملة بسيطة.  الجمل المركبة المعقدة تتضمن جملتين رئيسيتين على الأقل وجملة تابعة واحدة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound-complex sentence using 'play', 'piano', 'practice', and 'improve':",
        "options": ["A. If you practice playing the piano every day, you will improve, and you will enjoy it more.", "B. They practiced, and they improved.", "C. He played the piano.", "D. He improved."],
        "correct_option_id": 0,
        "explanation": "الجملة \"If you practice playing the piano every day, you will improve, and you will enjoy it more\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (you will improve و you will enjoy it more) وجملة تابعة (If you practice playing the piano every day). "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound-complex sentence uses 'so' to show consequence?",
        "options": ["A.  The team played well, so they won the game, and their fans celebrated.", "B. The team played well, so they won.", "C. They won, so they celebrated.", "D. The team won, so the fans celebrated."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The team played well, so they won the game, and their fans celebrated\" هي جملة مركبة معقدة  لأنها تحتوي على جملتين رئيسيتين (they won the game و their fans celebrated) مرتبطتين بـ \"and\" بالإضافة إلى جملة رئيسية أخرى (The team played well) مرتبطة بـ \"so\" التي تُعبّر عن السبب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound-complex sentence using 'yet' to indicate contrast:",
        "options": ["A.  Although she was tired, she went to the party, yet she left early because she didn't feel well.", "B. She was tired, yet she went to the party.", "C. He is small, yet he is strong.", "D. The food was good, yet he didn't eat."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Although she was tired, she went to the party, yet she left early because she didn't feel well\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (she went to the party و she left early) مرتبطتين بـ \"yet\" بالإضافة إلى جملة تابعة (Although she was tired) وجملة تابعة أخرى (because she didn't feel well)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound-complex sentence?",
        "options": ["A. The dog is barking.", "B. The cat meowed, but the dog barked loudly because it saw a squirrel.", "C. The bird is singing.", "D. The sun is shining."],
        "correct_option_id": 1,
        "explanation": "الجملة \"The cat meowed, but the dog barked loudly because it saw a squirrel\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (The cat meowed و the dog barked loudly) وجملة تابعة (because it saw a squirrel)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'They went to the beach, even though it was cloudy, and they built a sandcastle.' a compound-complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين رئيسيتين (They went to the beach و they built a sandcastle) وجملة تابعة (even though it was cloudy)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound-complex sentence?",
        "options": ["A. He studied hard for the exam, and he passed with flying colors, which made him very happy.", "B. She danced gracefully, and he played the piano beautifully.", "C. The house is painted white.", "D. Although it was raining, we decided to go for a walk, and we enjoyed the fresh air."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The house is painted white\"  هي جملة بسيطة.  الجمل المركبة المعقدة تتضمن جملتين رئيسيتين على الأقل وجملة تابعة واحدة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound-complex sentence using 'eat', 'lunch', 'delicious', and 'hungry':",
        "options": ["A.  Because they were hungry, they ate lunch quickly, and it was delicious.", "B. They were hungry and ate lunch.", "C. The lunch was delicious.", "D. They were hungry."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Because they were hungry, they ate lunch quickly, and it was delicious\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (they ate lunch quickly و it was delicious) وجملة تابعة (Because they were hungry)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound-complex sentence uses 'for' as a coordinating conjunction?",
        "options": ["A. He went to the library, for he needed to borrow a book, and he wanted to study for his exam.", "B. He went to the library, for he needed a book.", "C. She went to the store, for she needed milk.", "D. He went home, for he was tired."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He went to the library, for he needed to borrow a book, and he wanted to study for his exam\" هي جملة مركبة معقدة  لأنها تحتوي على جملتين رئيسيتين (He went to the library و he needed to borrow a book) مرتبطتين بـ \"for\"  بالإضافة إلى جملة رئيسية أخرى (he wanted to study for his exam) مرتبطة بـ \"and\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound-complex sentence with a semicolon connecting two independent clauses:",
        "options": ["A. The wind was howling; the rain was beating against the windows.", "B. It was raining; therefore, I stayed inside.", "C. She laughed, but he cried.", "D. The car is red; and it is fast."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The wind was howling; the rain was beating against the windows\"  هي جملة مركبة معقدة.  تستخدم الفاصلة المنقوطة (;)  لربط جملتين رئيسيتين مستقلتين.  كل جملة من الجملتين قادرة على الوقوف وحدها كجملة تامة المعنى."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound-complex sentence?",
        "options": ["A. The cat purred.", "B. While the sun was shining, the birds sang, and the flowers bloomed.", "C. The dog barked.", "D. The rain fell."],
        "correct_option_id": 1,
        "explanation": "الجملة \"While the sun was shining, the birds sang, and the flowers bloomed\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (the birds sang و the flowers bloomed)  وجملة تابعة (While the sun was shining)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'They ate dinner quickly because they were hungry, and then they went to the movies.' a compound-complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين رئيسيتين (They ate dinner quickly و they went to the movies) وجملة تابعة (because they were hungry)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound-complex sentence?",
        "options": ["A.  Even though it was cold, they went for a walk, and they enjoyed the fresh air.", "B.  She finished her work, but she was still tired, so she went to bed.", "C.  The bird is singing.", "D.  Because he was late, he ran to catch the bus, and he made it just in time."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The bird is singing\" هي جملة بسيطة.  الجمل المركبة المعقدة تتضمن جملتين رئيسيتين على الأقل وجملة تابعة واحدة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nCreate a compound-complex sentence using 'study', 'exam', 'difficult', and 'succeed':",
        "options": ["A. Although the exam was difficult, she studied hard, and she succeeded.", "B. The exam was difficult, but she studied hard.", "C. She succeeded on the exam.", "D. She studied hard."],
        "correct_option_id": 0,
        "explanation": "الجملة \"Although the exam was difficult, she studied hard, and she succeeded\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (she studied hard و she succeeded) وجملة تابعة (Although the exam was difficult)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich compound-complex sentence uses 'so' to show a result?",
        "options": ["A.  The traffic was heavy, so they arrived late, and they missed the beginning of the movie.", "B. The traffic was heavy, so they were late.", "C. They missed the beginning, because they were late.", "D. They were late, and they missed the beginning."],
        "correct_option_id": 0,
        "explanation": "الجملة \"The traffic was heavy, so they arrived late, and they missed the beginning of the movie\"  هي جملة مركبة معقدة  لأنها تحتوي على جملتين رئيسيتين (they arrived late و they missed the beginning of the movie) مرتبطتين بـ \"and\"  بالإضافة إلى جملة رئيسية أخرى (The traffic was heavy) مرتبطة بـ \"so\" التي تُعبّر عن السبب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the compound-complex sentence using 'yet' to show contrast:",
        "options": ["A. He was exhausted from the long journey, yet he was happy to be home, and he couldn't wait to see his family.", "B.  He was exhausted, yet he was happy.", "C. He was happy, yet he was tired.", "D. The journey was long, yet he was happy."],
        "correct_option_id": 0,
        "explanation": "الجملة \"He was exhausted from the long journey, yet he was happy to be home, and he couldn't wait to see his family\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (he was happy to be home و he couldn't wait to see his family) مرتبطتين بـ \"and\"  بالإضافة إلى جملة رئيسية أخرى (He was exhausted from the long journey) مرتبطة بـ \"yet\" التي تُعبّر عن التناقض.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich of the following is a compound-complex sentence?",
        "options": ["A. The dog barked.", "B. The sun was shining.", "C. The cat slept on the sofa while the dog barked, and the bird sang in its cage.", "D. The rain fell."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The cat slept on the sofa while the dog barked, and the bird sang in its cage\"  هي جملة مركبة معقدة.  تتكون من جملتين رئيسيتين (The cat slept on the sofa و the bird sang in its cage)  وجملة تابعة (while the dog barked)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIs 'Although they were tired, they continued hiking, and they reached the summit before sunset.' a compound-complex sentence?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. It's a complex sentence."],
        "correct_option_id": 0,
        "explanation": "نعم، لأنها تتكون من جملتين رئيسيتين (they continued hiking و they reached the summit before sunset) وجملة تابعة (Although they were tired)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is NOT a compound-complex sentence?",
        "options": ["A. He studied hard for the exam, and he passed with a high score, which made his parents proud.", "B. The flowers are blooming, and the birds are singing.", "C. The sky is blue.", "D. While they were playing, the phone rang, but no one answered."],
        "correct_option_id": 2,
        "explanation": "الجملة \"The sky is blue\"  هي جملة بسيطة.  الجمل المركبة المعقدة تتضمن جملتين رئيسيتين على الأقل وجملة تابعة واحدة."
    },
    ],

} ,  
"علامات الترقيم":{
    "(,) الفاصلة": [
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses commas correctly?",
        "options": ["A. The dog, a golden retriever, wagged its tail excitedly.", "B. The dog a golden retriever wagged its tail excitedly.", "C. The dog, a golden retriever wagged, its tail excitedly.", "D. The dog a golden retriever, wagged its tail excitedly."],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،  \"a golden retriever\"  عبارة وصفية غير أساسية (non-essential appositive)  لأنها تعطي معلومات إضافية عن الكلب،  ويمكن حذفها دون التأثير على المعنى الرئيسي للجملة.  لذلك، يجب فصلها بفاصلتين من كلا الجانبين.  الخيارات الأخرى  تضع الفواصل في أماكن غير صحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should the comma be placed in this sentence: 'She bought apples bananas and oranges.'",
        "options": ["A. She bought apples, bananas and oranges.", "B. She bought apples bananas, and oranges.", "C. She bought apples, bananas, and oranges.", "D. She bought apples bananas and oranges."],
        "correct_option_id": 2,
        "explanation": "تُستخدم الفاصلة في هذه الجملة لفصل العناصر في سلسلة (series).  يجب وضع فاصلة بعد كل عنصر في السلسلة،  بما في ذلك العنصر الأخير قبل \"and\".  لذلك، فإنّ الخيار الصحيح هو \"She bought apples, bananas, and oranges.\""
    },
   
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a comma after an introductory phrase?",
        "options": ["A. Before leaving the house, he checked the weather.", "B. Before leaving the house he checked the weather.", "C. Before leaving the house, he, checked the weather.", "D. Before, leaving the house he checked the weather."],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،  \"Before leaving the house\" عبارة تمهيدية (introductory phrase)،  يجب فصلها بفاصلة عن باقي الجملة.  الخيارات الأخرى  إما لا تضع الفاصلة أو تضعها في أماكن خاطئة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should commas be placed in this sentence: 'He went to the store bought milk and came home.'",
        "options": ["A. He went to the store, bought milk, and came home.", "B. He went to the store bought milk and came home.", "C. He went to the store, bought milk and, came home.", "D. He, went to the store bought milk and came home."],
        "correct_option_id": 0,
        "explanation": "الجملة تتكون من ثلاثة أفعال متتالية: \"went\"، \"bought\"، و \"came\".  يجب فصل هذه الأفعال بفاصلات  لجعل الجملة واضحة وسهلة القراءة.  الخيارات الأخرى  إما لا تضع الفواصل أو تضعها في أماكن خاطئة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct comma usage:",
        "options": ["A.  However, he still went to the party.", "B. However he still went to the party.", "C. However, he, still went to the party.", "D. However he still went, to the party."],
        "correct_option_id": 0,
        "explanation": "تُستخدم الفاصلة في هذه الجملة لفصل الكلمة \"However\"  عن باقي الجملة.  يجب وضع الفاصلة بعد \"However\"  عندما تكون في بداية الجملة.  الخيارات الأخرى  تضع الفاصلة في أماكن غير صحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses commas to set off a non-essential appositive?",
        "options": ["A. My brother, John, is a doctor.", "B. My brother John, is a doctor.", "C. My brother John is a doctor.", "D. My brother, John is a doctor."],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،  \"John\" عبارة وصفية غير أساسية (non-essential appositive)  لأنها تعطي معلومات إضافية عن الأخ،  ويمكن حذفها دون التأثير على المعنى الرئيسي للجملة.  لذلك،  يجب فصلها بفاصلتين من كلا الجانبين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a comma be placed in this sentence: 'She is a talented singer dancer and actress.'",
        "options": ["A. She is a talented, singer, dancer, and actress.", "B. She is a talented singer dancer and actress.", "C. She is a talented singer, dancer, and actress.", "D. She is a talented singer dancer, and actress."],
        "correct_option_id": 2,
        "explanation": "الجملة تتضمن سلسلة من الصفات تصف الشخص: \"singer\"، \"dancer\"، و \"actress\".  يجب وضع فاصلة بعد كل صفة في السلسلة،  بما في ذلك الصفة الأخيرة قبل \"and\".  الخيارات الأخرى  لا تضع الفواصل في الأماكن الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect comma placement:",
        "options": ["A.  He went to the store, bought some milk, and came home.", "B. She is, a talented singer, dancer, and actress.", "C.  Before leaving, he checked the weather.", "D.  Although it was raining, they went for a walk."],
        "correct_option_id": 1,
        "explanation": "في الجملة \"She is, a talented singer, dancer, and actress.\"  تم وضع فاصلة بعد \"is\"  وهو خطأ.  يجب عدم وضع فاصلة بين فعل الربط (\"is\")  والصفة أو الوصف الذي يتبعه.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses commas to set off a parenthetical element?",
        "options": ["A.  The weather, as you know, can be unpredictable.", "B. The weather as you know, can be unpredictable.", "C. The weather, as you know can be, unpredictable.", "D. The weather as you know can be unpredictable."],
        "correct_option_id": 0,
        "explanation": "في الجملة \"The weather, as you know, can be unpredictable.\"،  العبارة \"as you know\"  عبارة اعتراضية (parenthetical element)   يمكن حذفها دون التأثير على المعنى الرئيسي للجملة.  لذلك،  يجب فصلها بفاصلتين من كلا الجانبين.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a comma be placed in this sentence: 'He studied hard for the test therefore he passed.'",
        "options": ["A. He studied hard for the test, therefore, he passed.", "B. He studied hard for the test therefore he passed.", "C. He studied hard, for the test therefore he passed.", "D. He studied hard for the test therefore, he passed."],
        "correct_option_id": 0,
        "explanation": "تُستخدم الفاصلة في هذه الجملة لفصل الكلمة \"therefore\"  عن باقي الجملة.  يجب وضع الفاصلة قبل وبعد \"therefore\"  عندما تُستخدم كرابط منطقي بين جملتين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct comma placement:",
        "options": ["A. The dog, which was very friendly, wagged its tail.", "B. The dog, which was very friendly wagged its tail.", "C. The dog which was very friendly, wagged its tail.", "D. The dog which was very friendly wagged, its tail."],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،  \"which was very friendly\"   عبارة وصفية غير أساسية (non-essential relative clause)  لأنها تعطي معلومات إضافية عن الكلب،  ويمكن حذفها دون التأثير على المعنى الرئيسي للجملة.  لذلك،  يجب فصلها بفاصلتين من كلا الجانبين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses commas to separate items in a series?",
        "options": ["A. She bought milk, bread, and eggs from the store.", "B. She bought milk bread and eggs from the store.", "C. She bought milk bread, and eggs from the store.", "D. She bought milk, bread and eggs, from the store."],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،   تُستخدم الفاصلة لفصل العناصر في سلسلة: \"milk\"، \"bread\"، و \"eggs\".  يجب وضع فاصلة بعد كل عنصر في السلسلة،  بما في ذلك العنصر الأخير قبل \"and\".  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a comma be placed in this sentence: 'He is tall dark and handsome.'",
        "options": ["A. He is tall dark, and handsome.", "B. He is tall, dark, and handsome.", "C. He is tall dark and handsome.", "D. He is tall, dark and handsome."],
        "correct_option_id": 1,
        "explanation": "الجملة تتضمن سلسلة من الصفات تصف الشخص: \"tall\"، \"dark\"، و \"handsome\".  يجب وضع فاصلة بعد كل صفة في السلسلة،  بما في ذلك الصفة الأخيرة قبل \"and\".  الخيارات الأخرى  لا تضع الفواصل في الأماكن الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect comma placement:",
        "options": ["A. Before the game started, the players warmed up.", "B. He went to the store, he bought some milk.", "C. Although it was raining, they went for a walk.", "D.  If you practice every day, you will improve."],
        "correct_option_id": 1,
        "explanation": "في الجملة \"He went to the store, he bought some milk.\", تم استخدام فاصلة لربط جملتين مستقلتين بدون استخدام رابط وصل.  يجب استخدام فاصلة منقوطة (;)  أو رابط وصل مناسب (مثل and, but, so)  في هذه الحالة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses commas to set off a direct address?",
        "options": ["A.  John, could you please pass the salt?", "B. John could you please pass the salt?", "C. John could you please, pass the salt?", "D. John could you please pass, the salt?"],
        "correct_option_id": 0,
        "explanation": "في الجملة \"John, could you please pass the salt?\"،  \"John\"  هو اسم الشخص الذي يتم مخاطبته بشكل مباشر.  يجب فصل اسم المخاطب بفاصلة من كلا الجانبين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a comma be placed in this sentence: 'She likes to read write and paint.'",
        "options": ["A. She likes to read, write, and paint.", "B. She likes to read write and paint.", "C. She likes to read write, and paint.", "D. She likes to read, write and paint."],
        "correct_option_id": 0,
        "explanation": "الجملة تتضمن سلسلة من الأفعال: \"read\"، \"write\"، و \"paint\".  يجب وضع فاصلة بعد كل فعل في السلسلة،  بما في ذلك الفعل الأخير قبل \"and\".  الخيارات الأخرى  لا تضع الفواصل في الأماكن الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct comma placement:",
        "options": ["A.  The cat, which was sleeping soundly, didn't hear the doorbell.", "B. The cat, which was sleeping soundly didn't hear the doorbell.", "C. The cat which was sleeping soundly, didn't hear the doorbell.", "D. The cat which was sleeping soundly didn't, hear the doorbell."],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،  \"which was sleeping soundly\"  عبارة وصفية غير أساسية،  يجب فصلها بفاصلتين من كلا الجانبين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses commas to separate a dependent clause from an independent clause?",
        "options": ["A. Because it was raining, they stayed inside.", "B. Because it was raining they stayed inside.", "C. Because, it was raining they stayed inside.", "D. Because it was raining they, stayed inside."],
        "correct_option_id": 0,
        "explanation": "في الجملة \"Because it was raining, they stayed inside.\",  \"Because it was raining\"  جملة تابعة (dependent clause)  و \"they stayed inside\"  جملة رئيسية (independent clause).  يجب وضع فاصلة بعد الجملة التابعة عندما تسبق الجملة الرئيسية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a comma be placed in this sentence: 'He is a kind generous and thoughtful person.'",
        "options": ["A. He is a kind, generous, and thoughtful person.", "B. He is a kind generous and thoughtful person.", "C. He is a kind generous, and thoughtful person.", "D. He is a kind, generous and thoughtful, person."],
        "correct_option_id": 0,
        "explanation": "الجملة تتضمن سلسلة من الصفات تصف الشخص: \"kind\"، \"generous\"، و \"thoughtful\".  يجب وضع فاصلة بعد كل صفة في السلسلة،  بما في ذلك الصفة الأخيرة قبل \"and\".  الخيارات الأخرى  لا تضع الفواصل في الأماكن الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect comma placement:",
        "options": ["A. Before leaving, she locked the door.", "B. Although it was raining, they decided to go for a walk.", "C. She is a talented, singer dancer and actress.", "D.  He went to the store, bought some milk, and came home."],
        "correct_option_id": 2,
        "explanation": "في الجملة \"She is a talented, singer dancer and actress.\",  الفاصلة  وضعت فقط بعد كلمة  \"talented\"  وليس بين الكلمات \"singer\" و \"dancer\".  يجب فصل جميع العناصر في السلسلة بفاصلات."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses commas with a direct quotation?",
        "options": ["A. \"I am going to the store,\" she said.", "B. \"I am going to the store\" she said.", "C. \"I am going to the store, she said.\"", "D. \"I am going to the store\" she, said."],
        "correct_option_id": 0,
        "explanation": "في الجملة \"I am going to the store,\" she said.  تم وضع علامات التنصيص بشكل صحيح حول الجملة المنقولة، وتم وضع فاصلة بعد الجملة المنقولة وقبل كلمة \"said\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a comma be placed in this sentence: 'The dog a Labrador retriever loves to play fetch.'",
        "options": ["A. The dog, a Labrador retriever, loves to play fetch.", "B. The dog a Labrador retriever, loves to play fetch.", "C. The dog, a Labrador retriever loves to play fetch.", "D. The dog a Labrador retriever loves, to play fetch."],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،  \"a Labrador retriever\"  عبارة وصفية غير أساسية (non-essential appositive)  لأنها تعطي معلومات إضافية عن الكلب،  ويمكن حذفها دون التأثير على المعنى الرئيسي للجملة.  لذلك، يجب فصلها بفاصلتين من كلا الجانبين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct comma usage:",
        "options": ["A. The car, which is red, is fast.", "B. The car which is red is fast.", "C. The car, which is red is, fast.", "D. The car which is red, is fast."],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،  \"which is red\"  عبارة وصفية غير أساسية  يجب فصلها بفاصلتين من كلا الجانبين."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses commas to set off a contrasting element?",
        "options": ["A. He is kind, not cruel.", "B. He is kind not cruel.", "C. He is kind, not, cruel.", "D. He is kind not, cruel."],
        "correct_option_id": 0,
        "explanation": "في الجملة \"He is kind, not cruel.\",   تستخدم الفاصلة لفصل العنصر المتناقض \"not cruel\"  عن باقي الجملة. "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should commas be placed in this sentence: 'He went to the store bought milk eggs and bread.'",
        "options": ["A. He went to the store, bought milk, eggs, and bread.", "B. He went to the store bought milk eggs, and bread.", "C. He went to the store, bought milk eggs and bread.", "D. He went to the store bought, milk, eggs, and bread."],
        "correct_option_id": 0,
        "explanation": "الجملة تتكون من فعلين  (\"went\" و \"bought\")  وسلسلة من الأسماء: \"milk\"، \"eggs\"، و \"bread\".  يجب فصل العناصر في السلسلة بفاصلات،  بالإضافة إلى وضع فاصلة بعد الفعل الأول قبل بدء السلسلة.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect comma placement:",
        "options": ["A. She sang a song, and he played the guitar.", "B. While the sun was shining, the birds were singing.", "C.  He is a kind, generous and thoughtful, person.", "D. Before leaving, he checked the weather."],
        "correct_option_id": 2,
        "explanation": "في الجملة \"He is a kind, generous and thoughtful, person.\",   الفاصلة الأخيرة قبل كلمة \"person\"  غير ضرورية.  يجب فصل العناصر في السلسلة بفاصلات،  ولكن لا نضع فاصلة بعد العنصر الأخير."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses commas to set off a nonrestrictive clause?",
        "options": ["A. My car, which is blue, needs a wash.", "B. My car which is blue needs a wash.", "C. My car which is blue, needs a wash.", "D. My car, which is blue needs a wash."],
        "correct_option_id": 0,
        "explanation": "في الجملة \"My car, which is blue, needs a wash.\",  العبارة  \"which is blue\"  عبارة وصفية غير أساسية  (nonrestrictive clause)  لأنها تعطي معلومات إضافية عن السيارة،  ويمكن حذفها دون التأثير على المعنى الرئيسي للجملة.  لذلك،  يجب فصلها بفاصلتين من كلا الجانبين. "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a comma be placed in this sentence: 'She is a skilled artist writer and musician.'",
        "options": ["A. She is a skilled artist writer, and musician.", "B. She is a skilled artist, writer, and musician.", "C. She is a skilled, artist, writer, and musician.", "D. She is a skilled artist writer and musician."],
        "correct_option_id": 1,
        "explanation": "الجملة تتضمن سلسلة من الأسماء تصف الشخص: \"artist\"، \"writer\"، و \"musician\".  يجب وضع فاصلة بعد كل اسم في السلسلة،  بما في ذلك الاسم الأخير قبل \"and\".  الخيارات الأخرى  لا تضع الفواصل في الأماكن الصحيحة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct comma placement:",
        "options": ["A. The dog barked, and the cat, which was startled, jumped.", "B. The dog barked, and the cat which was startled, jumped.", "C. The dog barked, and the cat which was startled jumped.", "D. The dog barked, and, the cat which was startled jumped."],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،   تُستخدم الفاصلة لفصل  \"which was startled\"  وهي عبارة وصفية غير أساسية.  تُستخدم الفاصلة أيضًا لفصل جملتين بسيطتين مرتبطتين برابطة وصل (and)."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses commas to separate a direct quotation from the rest of the sentence?",
        "options": ["A. \"I will be there soon,\" he said.", "B. \"I will be there soon\" he said.", "C.  \"I will be there soon, he said.\"", "D. \"I will be there soon\" he, said."],
        "correct_option_id": 0,
        "explanation": "في الجملة \"I will be there soon,\" he said.  تم وضع علامات التنصيص بشكل صحيح حول الجملة المنقولة، وتم وضع فاصلة بعد الجملة المنقولة وقبل كلمة \"said\"."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should commas be placed in this sentence: 'London England is a beautiful city.'",
        "options": ["A. London, England, is a beautiful city.", "B. London England, is a beautiful city.", "C. London England is a beautiful city.", "D. London, England is a beautiful city."],
        "correct_option_id": 0,
        "explanation": "في هذه الجملة،  \"England\"  تُعدّ  مُكمّلاً  لـ \"London\"   وتعمل على توضيحها،  لذلك يجب فصلها بفاصلتين."
    }],
    "(.) نقطة نهاية الجملة": [
        {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a period?",
        "options": ["A. The cat sat on the mat", "B. The dog barked loudly", "C. She went to the store.", "D. The sun is shining"],
        "correct_option_id": 2,
        "explanation": "تُستخدم النقطة (.)  في نهاية الجملة التقريرية (declarative sentence) التي تُعبّر عن جملة كاملة.  الخيار  \"She went to the store.\"  هو الجملة الوحيدة التي تنتهي بنقطة بشكل صحيح.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a period be placed in this sentence: 'He went to the store He bought milk'",
        "options": ["A. He went to the store. He bought milk.", "B. He went to the store.He bought milk.", "C. He went to the store He bought milk.", "D. He went to the store He bought. milk."],
        "correct_option_id": 0,
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بنقطة.  الخيار الصحيح هو: \"He went to the store. He bought milk.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect period usage:",
        "options": ["A. The dog barked. The cat ran.", "B. She read a book. He watched TV.", "C. They went to the park. And they played games", "D. The sun is setting."],
        "correct_option_id": 2,
        "explanation": "في الجملة  \"They went to the park. And they played games\"   تم وضع نقطة بعد \"park\"   وهو خطأ.  العبارة  \"And they played games\"   هي جزء من الجملة الأولى  ويجب عدم فصلها بنقطة.  يجب استخدام فاصلة بدلاً من النقطة.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a period after an abbreviation?",
        "options": ["A. Dr. Smith is a good doctor.", "B.  Dr Smith is a good doctor.", "C. Dr, Smith is a good doctor.", "D. Dr Smith is a, good doctor."],
        "correct_option_id": 0,
        "explanation": "تُستخدم النقطة بعد الاختصارات،  مثل \"Dr.\"  في هذه الحالة.  الخيارات الأخرى لا تضع النقطة بشكل صحيح.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should periods be placed in this sentence: 'Mr Jones went to the store He bought milk and eggs'",
        "options": ["A. Mr Jones went to the store. He bought milk and eggs.", "B. Mr. Jones went to the store. He bought milk and eggs.", "C. Mr Jones went to the store He bought milk and eggs.", "D. Mr Jones went to the store He bought milk. and eggs."],
        "correct_option_id": 1,
        "explanation": "تستخدم النقطة بعد الاختصارات مثل \"Mr.\"   كما تُستخدم لفصل الجمل.  الخيار الصحيح هو: \"Mr. Jones went to the store. He bought milk and eggs.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct period usage:",
        "options": ["A.  She is reading a book.", "B. She is reading a book", "C.  She is reading a. book", "D. She is reading, a book."],
        "correct_option_id": 0,
        "explanation": "الجملة  \"She is reading a book.\"  هي الجملة الوحيدة التي تنتهي بنقطة بشكل صحيح.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a period at the end of a declarative sentence?",
        "options": ["A. The cat is sleeping on the mat.", "B. The cat is sleeping on the mat", "C. The cat is, sleeping on the mat.", "D.  The cat, is sleeping on the mat."],
        "correct_option_id": 0,
        "explanation": "النقطة تُستخدم في نهاية الجملة التقريرية  التي تنقل معلومة أو تصف حالة.  الخيار الصحيح هو:  \"The cat is sleeping on the mat.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a period be placed in this sentence: 'I went to the park I saw many birds'",
        "options": ["A. I went to the park. I saw many birds.", "B. I went to the park.I saw many birds.", "C. I went to the park I saw many birds.", "D. I went to the park I saw many. birds."],
        "correct_option_id": 0,
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بنقطة.  الخيار الصحيح هو:  \"I went to the park. I saw many birds.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect period usage:",
        "options": ["A. She is happy. He is sad.", "B. The dog barked. The cat meowed.", "C. The car is red. It is fast.", "D. They went for a walk. Because it was a beautiful day"],
        "correct_option_id": 3,
        "explanation": "في الجملة  \"They went for a walk. Because it was a beautiful day\"،   تم وضع نقطة بعد \"walk\"   وهو خطأ.   العبارة  \"Because it was a beautiful day\"   هي جملة تابعة  وتكمل معنى الجملة الأولى.  يجب عدم فصلها بنقطة.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a period after an initial?",
        "options": ["A. J. K. Rowling is a famous author.", "B. J K Rowling is a famous author.", "C. J.K Rowling is a famous author.", "D. J K. Rowling is a famous author."],
        "correct_option_id": 0,
        "explanation": "تُستخدم النقطة بعد الأحرف الأولى من الأسماء،  مثل \"J.\"  و \"K.\"  في هذه الحالة.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should periods be placed in this sentence: 'The meeting is at 3 00 PM Please be on time'",
        "options": ["A. The meeting is at 3:00 P.M. Please be on time.", "B. The meeting is at 3.00 PM Please be on time.", "C. The meeting is at 3 00 PM. Please be on time.", "D. The meeting is at 3 00 PM Please be on time."],
        "correct_option_id": 0,
        "explanation": "تُستخدم النقطة بعد الأحرف الأولى من  \"P.M.\"  كما تُستخدم لفصل الجمل.  الخيار الصحيح هو:  \"The meeting is at 3:00 P.M. Please be on time.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct period usage:",
        "options": ["A.  He is watching TV", "B. He is watching TV.", "C.  He is watching. TV", "D.  He is watching, TV."],
        "correct_option_id": 1,
        "explanation": "الجملة \"He is watching TV.\"  هي الجملة الوحيدة التي تنتهي بنقطة بشكل صحيح. "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a period at the end of an imperative sentence?",
        "options": ["A. Close the door.", "B. Close the door", "C. Close, the door.", "D. Close the door,"],
        "correct_option_id": 0,
        "explanation": "الجملة  \"Close the door.\"  هي جملة أمرية (imperative sentence)  وتُستخدم النقطة في نهايتها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a period be placed in this sentence: 'She went to the library She borrowed a book'",
        "options": ["A.  She went to the library. She borrowed a book.", "B. She went to the library.She borrowed a book.", "C. She went to the library She borrowed a book.", "D. She went to the library She borrowed. a book."],
        "correct_option_id": 0,
        "explanation": "الجملة تحتوي على جملتين مستقلتين يجب فصلهما بنقطة.  الخيار الصحيح هو:  \"She went to the library. She borrowed a book.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect period usage:",
        "options": ["A. The train arrived on time.", "B. The birds were singing. The sun was shining.", "C. He went to the store. And bought some milk.", "D.  The weather is beautiful."],
        "correct_option_id": 2,
        "explanation": "في الجملة  \"He went to the store. And bought some milk.\"،   تم وضع نقطة بعد \"store\"   وهو خطأ.  العبارة  \"And bought some milk\"   هي جزء من الجملة الأولى  ويجب عدم فصلها بنقطة.  يجب استخدام فاصلة بدلاً من النقطة.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a period after a polite request?",
        "options": ["A. Could you please pass the salt.", "B. Could you please pass the salt", "C. Could you please pass, the salt.", "D. Could you, please pass the salt."],
        "correct_option_id": 0,
        "explanation": "في الجملة \"Could you please pass the salt.\",  رغم أنها جملة استفهام  إلا أنها تُعبّر عن طلب بلطف  وتنتهي بنقطة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a period be placed in this sentence: 'She is a talented artist She paints beautiful pictures'",
        "options": ["A.  She is a talented artist. She paints beautiful pictures.", "B.  She is a talented artist.She paints beautiful pictures.", "C. She is a talented artist She paints beautiful pictures.", "D. She is a talented artist She paints beautiful. pictures."],
        "correct_option_id": 0,
        "explanation": "الجملة تحتوي على جملتين مستقلتين يجب فصلهما بنقطة.  الخيار الصحيح هو:  \"She is a talented artist. She paints beautiful pictures.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct period usage:",
        "options": ["A.  They are playing in the park", "B.  They are playing in the park.", "C. They are playing. in the park", "D. They are playing, in the park."],
        "correct_option_id": 1,
        "explanation": "الجملة \"They are playing in the park.\"  هي الجملة الوحيدة التي تنتهي بنقطة بشكل صحيح.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a period at the end of an indirect question?",
        "options": ["A.  He asked where the library was.", "B.  He asked where the library was", "C.  He asked, where the library was.", "D. He asked where the library, was."],
        "correct_option_id": 0,
        "explanation": "في الجملة \"He asked where the library was.\",  الجملة تنقل سؤالًا غير مباشر  (indirect question)  وتنتهي بنقطة. "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a period be placed in this sentence: 'He went to school He learned many things'",
        "options": ["A.  He went to school. He learned many things.", "B. He went to school.He learned many things.", "C. He went to school He learned many things.", "D. He went to school He learned many. things."],
        "correct_option_id": 0,
        "explanation": "الجملة تحتوي على جملتين مستقلتين يجب فصلهما بنقطة.  الخيار الصحيح هو:  \"He went to school. He learned many things.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect period usage:",
        "options": ["A. The sun set. The moon rose.", "B.  The dog wagged its tail. The cat purred.", "C.  The car is blue. And the house is white.", "D.  The children played in the park."],
        "correct_option_id": 2,
        "explanation": "في الجملة  \"The car is blue. And the house is white.\"،  تم وضع نقطة بعد \"blue\"  وهو خطأ.   العبارة \"And the house is white\" هي جزء من الجملة الأولى ويجب عدم فصلها بنقطة.  يجب استخدام فاصلة بدلاً من النقطة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a period to end a sentence fragment used for emphasis?",
        "options": ["A.  Silence.", "B. Silence", "C.  Silence,.", "D. .Silence"],
        "correct_option_id": 0,
        "explanation": "في الجملة \"Silence.\",   تستخدم النقطة بعد كلمة واحدة  للتأكيد على المعنى  وإضافة تأثير درامي.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a period be placed in this sentence: 'He studied for the exam He hoped to pass'",
        "options": ["A.  He studied for the exam. He hoped to pass.", "B. He studied for the exam.He hoped to pass.", "C. He studied for the exam He hoped to pass.", "D. He studied for the exam He hoped to. pass."],
        "correct_option_id": 0,
        "explanation": "الجملة تحتوي على جملتين مستقلتين يجب فصلهما بنقطة.  الخيار الصحيح هو: \"He studied for the exam. He hoped to pass.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct period usage:",
        "options": ["A.  The children are sleeping", "B. The children are sleeping.", "C. The children are sleeping,.", "D. The children, are sleeping."],
        "correct_option_id": 1,
        "explanation": "الجملة \"The children are sleeping.\"  هي الجملة الوحيدة التي تنتهي بنقطة بشكل صحيح. "
    }
],
    "(؟) علامة الإستفهام": [
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a question mark?",
        "options": ["A. What time is it?", "B. What time is it", "C. What time is it.", "D. What time, is it."],
        "correct_option_id": 0,
        "explanation": "علامة الاستفهام (?)  تُستخدم في نهاية الجملة الاستفهامية (interrogative sentence) التي تطرح سؤالًا مباشرًا.  الخيار \"What time is it?\"  هو الجملة الوحيدة التي تنتهي بعلامة استفهام بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a question mark be placed in this sentence: 'Are you coming to the party tonight'",
        "options": ["A. Are you coming to the party tonight?", "B. Are you coming to the party tonight", "C. Are you coming to the party? tonight", "D. Are you coming to the party tonight."],
        "correct_option_id": 0,
        "explanation": "الجملة تطرح سؤالًا مباشرًا،  لذلك يجب أن تنتهي بعلامة استفهام.  الخيار الصحيح هو: \"Are you coming to the party tonight?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect question mark usage:",
        "options": ["A.  What is your name.", "B. How are you?", "C.  Where are you going?", "D.  What time is it?"],
        "correct_option_id": 0,
        "explanation": "الجملة \"What is your name.\"   هي جملة استفهامية،  لكنها تنتهي بنقطة بدلاً من علامة استفهام.  يجب تصحيحها إلى: \"What is your name?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses a question mark correctly in a tag question?",
        "options": ["A. You are coming to the party, aren't you?", "B.  You are coming to the party, aren't you", "C. You are coming to the party aren't you?", "D. You are coming to the party, aren't you."],
        "correct_option_id": 0,
        "explanation": "السؤال المُلحق (tag question)   هو جملة قصيرة تُضاف إلى نهاية الجملة التقريرية لتحويلها إلى سؤال.  يجب وضع فاصلة قبل السؤال المُلحق،  وينتهي السؤال المُلحق بعلامة استفهام.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a question mark be placed in this sentence: 'Do you like pizza or pasta'",
        "options": ["A. Do you like pizza or pasta?", "B. Do you like pizza or pasta", "C. Do you like pizza or? pasta", "D. Do you like pizza, or pasta?"],
        "correct_option_id": 0,
        "explanation": "الجملة تطرح سؤالًا مباشرًا،  لذلك يجب أن تنتهي بعلامة استفهام.  الخيار الصحيح هو: \"Do you like pizza or pasta?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct question mark usage:",
        "options": ["A.  Can you help me.", "B.  How old are you?", "C. Where is the library", "D.  What is the capital of France."],
        "correct_option_id": 1,
        "explanation": "الجملة \"How old are you?\"  هي الجملة الوحيدة التي تنتهي بعلامة استفهام بشكل صحيح.  الخيارات الأخرى إما تنتهي بنقطة أو لا تنتهي بعلامة ترقيم."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a question mark in a direct question?",
        "options": ["A. What is the meaning of life?", "B. What is the meaning of life", "C. What is the, meaning of life?", "D. What, is the meaning of life?"],
        "correct_option_id": 0,
        "explanation": "السؤال المباشر (direct question)   هو سؤال يُطرح بشكل واضح ومباشر،  وينتهي دائمًا بعلامة استفهام.  الخيار  \"What is the meaning of life?\"  هو الجملة الوحيدة التي تنتهي بعلامة استفهام بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a question mark be placed in this sentence: 'Is it raining outside'",
        "options": ["A. Is it raining outside?", "B. Is it raining outside", "C. Is it raining, outside?", "D. Is, it raining outside?"],
        "correct_option_id": 0,
        "explanation": "الجملة تطرح سؤالًا مباشرًا،  لذلك يجب أن تنتهي بعلامة استفهام.  الخيار الصحيح هو:  \"Is it raining outside?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect question mark usage:",
        "options": ["A.  How was your day?", "B.  Where did you go.", "C.  What are you doing?", "D.  Why are you here?"],
        "correct_option_id": 1,
        "explanation": "الجملة \"Where did you go.\"  هي جملة استفهامية،  لكنها تنتهي بنقطة بدلاً من علامة استفهام.  يجب تصحيحها إلى:  \"Where did you go?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses a question mark correctly with a question starting with a preposition?",
        "options": ["A. At what time will you arrive?", "B. At what time will you arrive", "C. At what time, will you arrive?", "D. At what time will you, arrive?"],
        "correct_option_id": 0,
        "explanation": "حتى لو بدأ السؤال بحرف جر (preposition)  مثل \"At\"  في هذه الحالة،  لا يزال يجب أن ينتهي بعلامة استفهام.  الخيار الصحيح هو:  \"At what time will you arrive?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a question mark be placed in this sentence: 'Can you please pass the salt'",
        "options": ["A. Can you please pass the salt?", "B.  Can you please pass the salt", "C. Can you please pass the, salt?", "D. Can you, please pass the salt?"],
        "correct_option_id": 0,
        "explanation": "رغم أن الجملة تُعبّر عن طلب،  إلا أنها تُصاغ كسؤال  وتنتهي بعلامة استفهام.  الخيار الصحيح هو:  \"Can you please pass the salt?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct question mark usage:",
        "options": ["A.  What is your favorite color", "B.  Is it hot outside?", "C.  How are you feeling.", "D.  Why did you leave."],
        "correct_option_id": 1,
        "explanation": "الجملة \"Is it hot outside?\"  هي الجملة الوحيدة التي تنتهي بعلامة استفهام بشكل صحيح.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses a question mark correctly in an indirect question?",
        "options": ["A. I wonder what time it is.", "B. I wonder what time it is", "C. I wonder what time it is?", "D. I, wonder what time it is?"],
        "correct_option_id": 0,
        "explanation": "السؤال غير المباشر (indirect question)  هو سؤال يُطرح بشكل غير مباشر ضمن جملة أخرى.  لا ينتهي السؤال غير المباشر بعلامة استفهام.  الخيار \"I wonder what time it is.\"  هو الجملة الوحيدة التي لا تنتهي بعلامة استفهام."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a question mark be placed in this sentence: 'Did you finish your homework'",
        "options": ["A. Did you finish your homework?", "B. Did you finish your homework", "C. Did you finish your? homework", "D. Did you finish, your homework?"],
        "correct_option_id": 0,
        "explanation": "الجملة تطرح سؤالًا مباشرًا،  لذلك يجب أن تنتهي بعلامة استفهام.  الخيار الصحيح هو: \"Did you finish your homework?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect question mark usage:",
        "options": ["A. Are you coming to the party?", "B. What did you say?", "C.  How do you know that.", "D.  Why are you laughing?"],
        "correct_option_id": 2,
        "explanation": "الجملة \"How do you know that.\"  هي جملة استفهامية،  لكنها تنتهي بنقطة بدلاً من علامة استفهام.  يجب تصحيحها إلى:  \"How do you know that?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a question mark in a rhetorical question?",
        "options": ["A.  Who knows?", "B.  Who knows", "C.  Who knows.", "D. Who, knows?"],
        "correct_option_id": 0,
        "explanation": "السؤال الخطابي (rhetorical question)  هو سؤال يُطرح للتأكيد على نقطة معينة،  ولا يتوقع إجابة حقيقية عليه.  ينتهي السؤال الخطابي بعلامة استفهام.  الخيار \"Who knows?\"  هو الجملة الوحيدة التي تنتهي بعلامة استفهام بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a question mark be placed in this sentence: 'What is your favorite book'",
        "options": ["A. What is your favorite book?", "B. What is your favorite book", "C. What is your favorite, book?", "D. What, is your favorite book?"],
        "correct_option_id": 0,
        "explanation": "الجملة تطرح سؤالًا مباشرًا،  لذلك يجب أن تنتهي بعلامة استفهام.  الخيار الصحيح هو:  \"What is your favorite book?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct question mark usage:",
        "options": ["A.  What are you doing.", "B.  Why are you here?", "C.  How did you get here", "D.  Is it cold outside."],
        "correct_option_id": 1,
        "explanation": "الجملة \"Why are you here?\"   هي الجملة الوحيدة التي تنتهي بعلامة استفهام بشكل صحيح.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses a question mark correctly after a series of questions?",
        "options": ["A.  What is your name? Where are you from? What do you do?", "B. What is your name? Where are you from? What do you do", "C. What is your name? where are you from? what do you do?", "D.  What is your name?, Where are you from?, What do you do?"],
        "correct_option_id": 0,
        "explanation": "عندما تطرح سلسلة من الأسئلة القصيرة  يجب وضع علامة استفهام بعد كل سؤال.  الخيار  \"What is your name? Where are you from? What do you do?\"  هو الجملة الوحيدة التي تستخدم علامات الاستفهام بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a question mark be placed in this sentence: 'Have you seen my keys'",
        "options": ["A. Have you seen my keys?", "B.  Have you seen my keys", "C. Have you seen my, keys?", "D. Have, you seen my keys?"],
        "correct_option_id": 0,
        "explanation": "الجملة تطرح سؤالًا مباشرًا،  لذلك يجب أن تنتهي بعلامة استفهام.  الخيار الصحيح هو:  \"Have you seen my keys?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect question mark usage:",
        "options": ["A.  Did you finish the project?", "B.  Why is the sky blue.", "C.  What time does the movie start?", "D.  How much does it cost?"],
        "correct_option_id": 1,
        "explanation": "الجملة \"Why is the sky blue.\"  هي جملة استفهامية،  لكنها تنتهي بنقطة بدلاً من علامة استفهام.  يجب تصحيحها إلى:  \"Why is the sky blue?\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses a question mark correctly in a question expressing doubt?",
        "options": ["A. Is that really true?", "B. Is that really true", "C. Is that really, true?", "D. Is, that really true?"],
        "correct_option_id": 0,
        "explanation": "عندما يُعبّر السؤال عن شك أو عدم تأكد  يجب أن ينتهي بعلامة استفهام.  الخيار الصحيح هو:  \"Is that really true?\""
    }
],
    "(!) علامة التعجب": [
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses an exclamation point?",
        "options": ["A. Wow! That's amazing!", "B. Wow. That's amazing.", "C. Wow, that's amazing!", "D. Wow That's amazing!"],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم علامة التعجب (!)  للتعبير عن انفعال قوي، مثل الدهشة أو الفرح أو الغضب.  الخيار \"Wow! That's amazing!\"  هو الجملة الوحيدة التي تستخدم علامة التعجب بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should an exclamation point be placed in this sentence: 'Help I'm falling'",
        "options": ["A. Help, I'm falling!", "B. Help! I'm falling!", "C. Help I'm falling!", "D. Help I'm falling."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة تُعبّر عن طلب استغاثة  وهو انفعال قوي.  لذلك، يجب أن تنتهي بعلامة تعجب.  الخيار الصحيح هو: \"Help! I'm falling!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect exclamation point usage:",
        "options": ["A. Look out!", "B.  Fire!", "C.  Run!", "D. Ouch. That hurt."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الجملة \"Ouch. That hurt.\"  تُعبّر عن ألم  وهو انفعال،  لكنها تنتهي بنقطة بدلاً من علامة تعجب.  يجب تصحيحها إلى:  \"Ouch! That hurt!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses an exclamation point correctly to express strong emotion?",
        "options": ["A.  I can't believe I won.", "B. I can't believe I won!", "C. I can't believe I won", "D.  I can't, believe I won!"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة \"I can't believe I won!\"  تُعبّر عن دهشة وفرح  وهي انفعالات قوية،  لذلك  تستخدم علامة التعجب بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should an exclamation point be placed in this sentence: 'That's a fantastic idea'",
        "options": ["A. That's a fantastic, idea!", "B. That's a, fantastic idea!", "C. That's a fantastic idea!", "D. That's a fantastic idea"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن حماس وإعجاب  وهي انفعالات،  لذلك يجب أن تنتهي بعلامة تعجب.  الخيار الصحيح هو:  \"That's a fantastic idea!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct exclamation point usage:",
        "options": ["A.  Be careful.", "B.  What a beautiful day", "C.  Happy birthday!", "D.  I'm so tired."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة \"Happy birthday!\"  هي الجملة الوحيدة التي تستخدم علامة التعجب بشكل صحيح.  الخيارات الأخرى إما جمل تقريرية أو جمل تعجبية منقوصة."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses an exclamation point after an interjection?",
        "options": ["A. Oh no I forgot my keys!", "B. Oh, no! I forgot my keys!", "C. Oh no! I forgot my keys!", "D. Oh no, I forgot my keys!"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الكلمة  \"Oh no!\"   هي كلمة تعجب (interjection)  تُعبّر عن انفعال،  لذلك يجب أن تنتهي بعلامة تعجب.  الخيار  \"Oh no! I forgot my keys!\"  هو الجملة الوحيدة التي تستخدم علامة التعجب بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should an exclamation point be placed in this sentence: 'You scared me'",
        "options": ["A. You scared, me!", "B. You, scared me!", "C. You scared me", "D. You scared me!"],
        "correct_option_id": 3,  # Index 3
        "explanation": "الجملة تُعبّر عن مفاجأة وخوف  وهي انفعالات قوية،  لذلك يجب أن تنتهي بعلامة تعجب.  الخيار الصحيح هو:  \"You scared me!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect exclamation point usage:",
        "options": ["A. Hooray! We won!", "B.  That's incredible!", "C.  Watch out!", "D. Congratulations."],
        "correct_option_id": 3,  # Index 3
        "explanation": "الجملة  \"Congratulations.\"   تُعبّر عن تهنئة  وهي انفعال،  لكنها تنتهي بنقطة بدلاً من علامة تعجب.  يجب تصحيحها إلى: \"Congratulations!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses an exclamation point to express a command?",
        "options": ["A. Stop", "B.  Stop.", "C. Stop!", "D. Stop,"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة \"Stop!\"   هي جملة أمرية  (command)   تُستخدم للتعبير عن أمر  وتنتهي بعلامة تعجب.  الخيار \"Stop!\"   هو الجملة الوحيدة التي تستخدم علامة التعجب بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should an exclamation point be placed in this sentence: 'This is the best day ever'",
        "options": ["A. This is the best day ever", "B. This is the, best day ever!", "C. This is the best day, ever!", "D. This is the best day ever!"],
        "correct_option_id": 3,  # Index 3
        "explanation": "الجملة تُعبّر عن فرح وسعادة  وهي انفعالات قوية،  لذلك يجب أن تنتهي بعلامة تعجب.  الخيار الصحيح هو: \"This is the best day ever!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct exclamation point usage:",
        "options": ["A. That's so funny!", "B.  Please be quiet", "C.  What a surprise.", "D. I need help."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الجملة \"That's so funny!\"  هي الجملة الوحيدة التي تستخدم علامة التعجب بشكل صحيح.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses an exclamation point to emphasize a single word?",
        "options": ["A. Amazing", "B.  Amazing!", "C. Amazing.", "D. Amazing,"],
        "correct_option_id": 1,  # Index 1
        "explanation": "يمكن استخدام علامة التعجب للتأكيد على كلمة واحدة  للتعبير عن انفعال قوي.  الخيار  \"Amazing!\"  هو الجملة الوحيدة التي تستخدم علامة التعجب بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should an exclamation point be placed in this sentence: 'I can't wait to see you'",
        "options": ["A. I can't wait to see, you!", "B.  I can't wait to see you!", "C. I can't wait to see you", "D. I can't wait, to see you!"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة تُعبّر عن حماس وشوق  وهي انفعالات  لذلك يجب أن تنتهي بعلامة تعجب.  الخيار الصحيح هو:  \"I can't wait to see you!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect exclamation point usage:",
        "options": ["A.  Be careful!", "B.  Wow, that was close.", "C.  I am so excited!", "D. Look at that beautiful sunset!"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة  \"Wow, that was close.\"   تُعبّر عن مفاجأة أو ارتياح  وهي انفعالات،  لكنها تنتهي بنقطة بدلاً من علامة تعجب.  يجب تصحيحها إلى: \"Wow! That was close!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses an exclamation point correctly to express a warning?",
        "options": ["A. Watch out for that car", "B.  Watch out for that car.", "C.  Watch out for that car!", "D.  Watch out, for that car!"],
        "correct_option_id": 2,  # Index 2
        "explanation": "التحذير يُعبّر عن انفعال قوي  لذلك يجب أن ينتهي بعلامة تعجب.  الخيار \"Watch out for that car!\"  هو الجملة الوحيدة التي تستخدم علامة التعجب بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should an exclamation point be placed in this sentence: 'That was an incredible performance'",
        "options": ["A.  That was an incredible performance", "B. That was an incredible, performance!", "C.  That was an incredible performance!", "D. That was an, incredible performance!"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة تُعبّر عن إعجاب  وهو انفعال  لذلك يجب أن تنتهي بعلامة تعجب.  الخيار الصحيح هو:  \"That was an incredible performance!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct exclamation point usage:",
        "options": ["A.  How could you do that.", "B.  I'm feeling sick.", "C. That is so unfair!", "D. Please help me."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة \"That is so unfair!\"  هي الجملة الوحيدة التي تستخدم علامة التعجب بشكل صحيح. "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence does NOT need an exclamation point?",
        "options": ["A. Fire!", "B. He said, \"Hello.\"", "C.  Help!", "D. Wow!"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة \"He said, \"Hello.\"\"   هي جملة تقريرية تنقل حوارًا  ولا تحتاج إلى علامة تعجب.  الخيارات الأخرى تُعبّر عن انفعالات  وتحتاج إلى علامة تعجب.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly expresses surprise?",
        "options": ["A. You surprised me.", "B. You surprised me!", "C. You surprised me", "D. You surprised, me!"],
        "correct_option_id": 1,  # Index 1
        "explanation": "للتعبير عن الدهشة، نستخدم علامة التعجب. الخيار الصحيح هو: \"You surprised me!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the sentence with the correct placement of the exclamation point:",
        "options": ["A. What a beautiful view! ", "B. What a beautiful view", "C. What a beautiful, view!", "D. What a, beautiful view!"],
        "correct_option_id": 0,  # Index 0
        "explanation": "علامة التعجب توضع في نهاية الجملة التي تعبر عن انفعال قوي.  الخيار الصحيح هو: \"What a beautiful view!\" "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence incorrectly uses an exclamation point?",
        "options": ["A. The food is delicious!", "B.  I love this song.", "C.  Congratulations!", "D.  Be careful!"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة \"I love this song.\" هي جملة خبرية، ولا تعبر عن انفعال قوي، لذلك لا تحتاج علامة تعجب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nSelect the sentence that needs an exclamation point:",
        "options": ["A. What a disaster", "B.  The cat is sleeping.", "C.  She is reading a book.", "D.  He is playing the piano."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الجملة \"What a disaster\" تعبر عن انفعال قوي (كارثة) وتحتاج علامة تعجب في نهايتها."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nChoose the grammatically correct sentence:",
        "options": ["A.  I can't believe it. ", "B. I can't believe it!", "C.  I can't believe it", "D.  I can't believe, it!"],
        "correct_option_id": 1,  # Index 1
        "explanation": "علامة التعجب ضرورية في نهاية الجملة للتعبير عن الدهشة. الخيار الصحيح هو: \"I can't believe it!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence incorrectly uses an exclamation point?",
        "options": ["A.  That's amazing!", "B.  I won the lottery!", "C.  Please help! ", "D.  The sky is blue! "],
        "correct_option_id": 3,  # Index 3
        "explanation": "الجملة \"The sky is blue!\" هي جملة خبرية، ولا تعبر عن انفعال قوي، لذلك لا تحتاج علامة تعجب."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nSelect the sentence that uses an exclamation point to express excitement:",
        "options": ["A. We're going to Disney World!", "B.  We are going on vacation.", "C.  The trip will be fun.", "D.  We will see Mickey Mouse."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الجملة \"We're going to Disney World!\" تعبر عن حماس وفرح، لذلك تستخدم علامة التعجب بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence uses an exclamation point to give a command?",
        "options": ["A. Be quiet", "B. Be quiet.", "C. Be quiet!", "D. Be, quiet!"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الأوامر القوية تنتهي بعلامة تعجب. الخيار الصحيح هو: \"Be quiet!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence is a correctly punctuated exclamatory sentence?",
        "options": ["A.  What a wonderful day. ", "B.  What a wonderful day! ", "C.  What a wonderful, day!", "D. What a, wonderful day!"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجمل التعجبية  (exclamatory sentences)  تنتهي بعلامة تعجب.  الخيار الصحيح هو: \"What a wonderful day!\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence does NOT need an exclamation point?",
        "options": ["A.  Ouch!", "B.  Hooray!", "C.  She said, \"Thank you.\"", "D.  Help!"],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة \"She said, \"Thank you.\"\"  هي جملة خبرية تنقل حوارًا، ولا تحتاج إلى علامة تعجب."
    }
],
    "(;) فاصلة منقوطة": [
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a semicolon?",
        "options": ["A. The dog barked; the cat ran away.", "B. The dog barked, the cat ran away.", "C. The dog barked. The cat ran away.", "D. The dog barked and the cat ran away."],
        "correct_option_id": 0, # Index 0
        "explanation": "تُستخدم الفاصلة المنقوطة (;)  لربط جملتين مستقلتين وثيقتي الصلة  دون استخدام رابط وصل (conjunction).  الخيار \"The dog barked; the cat ran away.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a semicolon be placed in this sentence: 'She loves to read he prefers to watch movies'",
        "options": ["A. She loves to read he prefers to watch movies.", "B. She loves to read, he prefers to watch movies.", "C. She loves to read; he prefers to watch movies.", "D. She loves to read. He prefers to watch movies."],
        "correct_option_id": 2, # Index 2
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بفاصلة منقوطة  لأنهما وثيقتا الصلة  ولا يوجد رابط وصل بينهما.  الخيار الصحيح هو:  \"She loves to read; he prefers to watch movies.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect semicolon usage:",
        "options": ["A. The sun is shining; the birds are singing.", "B.  He went to the store, and he bought some milk.", "C. She likes to read novels; he prefers biographies.", "D. The car is red; and it is fast."],
        "correct_option_id": 3, # Index 3
        "explanation": "في الجملة  \"The car is red; and it is fast.\"،  تم استخدام الفاصلة المنقوطة مع رابط وصل (and).  هذا خطأ،  لأنه يجب استخدام إما الفاصلة المنقوطة  أو رابط الوصل  وليس كليهما معًا.  الخيار الصحيح هو: \"The car is red; it is fast.\"  أو  \"The car is red, and it is fast.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a semicolon to separate items in a complex series?",
        "options": ["A.  She traveled to Paris, France; Rome, Italy; and London, England.", "B. She traveled to Paris, France, Rome, Italy, and London, England.", "C. She traveled to Paris, France. Rome, Italy. And London, England.", "D.  She traveled to Paris France, Rome Italy, and London England."],
        "correct_option_id": 0, # Index 0
        "explanation": "تُستخدم الفاصلة المنقوطة لفصل عناصر سلسلة معقدة  تحتوي على فواصل داخليا.  الخيار  \"She traveled to Paris, France; Rome, Italy; and London, England.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a semicolon be placed in this sentence: 'The meeting starts at 2 00 PM please be on time'",
        "options": ["A. The meeting starts at 2:00 PM; please be on time.", "B. The meeting starts at 2:00 PM, please be on time.", "C. The meeting starts at 2:00 PM. Please be on time.", "D. The meeting starts at 2:00 PM please be on time."],
        "correct_option_id": 0, # Index 0
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بفاصلة منقوطة  لأنهما وثيقتا الصلة  ولا يوجد رابط وصل بينهما.  الخيار الصحيح هو: \"The meeting starts at 2:00 PM; please be on time.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct semicolon usage:",
        "options": ["A. I like to read; however, I don't have much time.", "B. I like to read; however I don't have much time.", "C. I like to read, however, I don't have much time.", "D. I like to read however; I don't have much time."],
        "correct_option_id": 0, # Index 0
        "explanation": "تُستخدم الفاصلة المنقوطة قبل  \"however\"  عندما تفصل جملتين مستقلتين،  وتُستخدم فاصلة بعد \"however\".   الخيار  \"I like to read; however, I don't have much time.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a semicolon to connect two closely related independent clauses?",
        "options": ["A.  The cake was delicious. It was chocolate.", "B. The cake was delicious; it was chocolate.", "C. The cake was delicious, it was chocolate.", "D. The cake was delicious and it was chocolate."],
        "correct_option_id": 1, # Index 1
        "explanation": "الفصلة المنقوطة تربط جملتين مستقلتين وثيقتي الصلة  دون استخدام رابط وصل.  الخيار  \"The cake was delicious; it was chocolate.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a semicolon be placed in this sentence: 'He studied hard for the test he aced it'",
        "options": ["A. He studied hard for the test he aced it.", "B. He studied hard for the test, he aced it.", "C. He studied hard for the test; he aced it.", "D. He studied hard for the test. He aced it."],
        "correct_option_id": 2, # Index 2
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بفاصلة منقوطة  لأنهما وثيقتا الصلة  ولا يوجد رابط وصل بينهما.  الخيار الصحيح هو:  \"He studied hard for the test; he aced it.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect semicolon usage:",
        "options": ["A. The dog barked, but the cat ran away.", "B. The sun is shining; the birds are singing.", "C. She likes to travel; her favorite destination is Italy.", "D.  He went to the store; and bought some milk."],
        "correct_option_id": 3, # Index 3
        "explanation": "في الجملة  \"He went to the store; and bought some milk.\",  تم استخدام الفاصلة المنقوطة مع رابط وصل (and).  هذا خطأ،  لأنه يجب استخدام إما الفاصلة المنقوطة  أو رابط الوصل، وليس كليهما معًا.  الخيار الصحيح هو:  \"He went to the store; he bought some milk.\"  أو  \"He went to the store, and he bought some milk.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a semicolon before a conjunctive adverb?",
        "options": ["A. She wanted to go to the beach. Therefore, she packed her swimsuit.", "B. She wanted to go to the beach; therefore, she packed her swimsuit.", "C. She wanted to go to the beach, therefore she packed her swimsuit.", "D. She wanted to go to the beach, therefore; she packed her swimsuit."],
        "correct_option_id": 1, # Index 1
        "explanation": "تُستخدم الفاصلة المنقوطة قبل الظرف الرابط (conjunctive adverb) مثل  \"therefore\"  في هذه الحالة،  وتُستخدم فاصلة بعد الظرف الرابط.  الخيار \"She wanted to go to the beach; therefore, she packed her swimsuit.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a semicolon be placed in this sentence: 'I love to cook my husband prefers to order takeout'",
        "options": ["A. I love to cook my husband prefers to order takeout.", "B. I love to cook, my husband prefers to order takeout.", "C. I love to cook. My husband prefers to order takeout.", "D. I love to cook; my husband prefers to order takeout."],
        "correct_option_id": 3, # Index 3
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بفاصلة منقوطة  لأنهما وثيقتا الصلة  ولا يوجد رابط وصل بينهما.  الخيار الصحيح هو:  \"I love to cook; my husband prefers to order takeout.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct semicolon usage:",
        "options": ["A. It was a beautiful day however, it was too hot to go outside.", "B. It was a beautiful day, however, it was too hot to go outside.", "C. It was a beautiful day; however, it was too hot to go outside.", "D. It was a beautiful day; however it was too hot to go outside."],
        "correct_option_id": 2, # Index 2
        "explanation": "تُستخدم الفاصلة المنقوطة قبل  \"however\"   عندما تفصل جملتين مستقلتين،  وتُستخدم فاصلة بعد \"however\".  الخيار  \"It was a beautiful day; however, it was too hot to go outside.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a semicolon to avoid confusion in a sentence with internal commas?",
        "options": ["A.  He visited his family in London, England, Paris, France, and Rome, Italy.", "B. He visited his family in London, England; Paris, France; and Rome, Italy.", "C. He visited his family in London England; Paris France; and Rome Italy.", "D.  He visited his family in London, England. Paris, France. And Rome, Italy."],
        "correct_option_id": 1, # Index 1
        "explanation": "تُستخدم الفاصلة المنقوطة لفصل عناصر سلسلة معقدة  تحتوي على فواصل داخليا  لتجنب الالتباس.  الخيار  \"He visited his family in London, England; Paris, France; and Rome, Italy.\"   هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a semicolon be placed in this sentence: 'She is a talented artist she paints beautiful landscapes'",
        "options": ["A. She is a talented artist she paints beautiful landscapes.", "B. She is a talented artist, she paints beautiful landscapes.", "C. She is a talented artist; she paints beautiful landscapes.", "D. She is a talented artist. She paints beautiful landscapes."],
        "correct_option_id": 2, # Index 2
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بفاصلة منقوطة  لأنهما وثيقتا الصلة  ولا يوجد رابط وصل بينهما.  الخيار الصحيح هو:  \"She is a talented artist; she paints beautiful landscapes.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect semicolon usage:",
        "options": ["A. He went to the store; he bought some milk.", "B. The sun is shining; however, it is cold.", "C. She loves to travel; her favorite destination is Paris.", "D.  The dog barked; and the cat meowed."],
        "correct_option_id": 3, # Index 3
        "explanation": "في الجملة  \"The dog barked; and the cat meowed.\",  تم استخدام الفاصلة المنقوطة مع رابط وصل (and).   هذا خطأ  لأنه يجب استخدام إما الفاصلة المنقوطة  أو رابط الوصل،  وليس كليهما معًا.  الخيار الصحيح هو:  \"The dog barked; the cat meowed.\"   أو  \"The dog barked, and the cat meowed.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a semicolon?",
        "options": ["A. The dog barked; the cat ran away.", "B. The dog barked, the cat ran away.", "C. The dog barked. The cat ran away.", "D. The dog barked and the cat ran away."],
        "correct_option_id": 0, # Index 0
        "explanation": "تُستخدم الفاصلة المنقوطة (;)  لربط جملتين مستقلتين وثيقتي الصلة  دون استخدام رابط وصل (conjunction).  الخيار \"The dog barked; the cat ran away.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a semicolon be placed in this sentence: 'She loves to read he prefers to watch movies'",
        "options": ["A. She loves to read he prefers to watch movies.", "B. She loves to read, he prefers to watch movies.", "C. She loves to read; he prefers to watch movies.", "D. She loves to read. He prefers to watch movies."],
        "correct_option_id": 2, # Index 2
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بفاصلة منقوطة  لأنهما وثيقتا الصلة  ولا يوجد رابط وصل بينهما.  الخيار الصحيح هو:  \"She loves to read; he prefers to watch movies.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect semicolon usage:",
        "options": ["A. The sun is shining; the birds are singing.", "B.  He went to the store, and he bought some milk.", "C. She likes to read novels; he prefers biographies.", "D. The car is red; and it is fast."],
        "correct_option_id": 3, # Index 3
        "explanation": "في الجملة  \"The car is red; and it is fast.\"،  تم استخدام الفاصلة المنقوطة مع رابط وصل (and).  هذا خطأ،  لأنه يجب استخدام إما الفاصلة المنقوطة  أو رابط الوصل  وليس كليهما معًا.  الخيار الصحيح هو: \"The car is red; it is fast.\"  أو  \"The car is red, and it is fast.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a semicolon to separate items in a complex series?",
        "options": ["A.  She traveled to Paris, France; Rome, Italy; and London, England.", "B. She traveled to Paris, France, Rome, Italy, and London, England.", "C. She traveled to Paris, France. Rome, Italy. And London, England.", "D.  She traveled to Paris France, Rome Italy, and London England."],
        "correct_option_id": 0, # Index 0
        "explanation": "تُستخدم الفاصلة المنقوطة لفصل عناصر سلسلة معقدة  تحتوي على فواصل داخليا.  الخيار  \"She traveled to Paris, France; Rome, Italy; and London, England.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a semicolon be placed in this sentence: 'The meeting starts at 2 00 PM please be on time'",
        "options": ["A. The meeting starts at 2:00 PM; please be on time.", "B. The meeting starts at 2:00 PM, please be on time.", "C. The meeting starts at 2:00 PM. Please be on time.", "D. The meeting starts at 2:00 PM please be on time."],
        "correct_option_id": 0, # Index 0
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بفاصلة منقوطة  لأنهما وثيقتا الصلة  ولا يوجد رابط وصل بينهما.  الخيار الصحيح هو: \"The meeting starts at 2:00 PM; please be on time.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct semicolon usage:",
        "options": ["A. I like to read; however, I don't have much time.", "B. I like to read; however I don't have much time.", "C. I like to read, however, I don't have much time.", "D. I like to read however; I don't have much time."],
        "correct_option_id": 0, # Index 0
        "explanation": "تُستخدم الفاصلة المنقوطة قبل  \"however\"  عندما تفصل جملتين مستقلتين،  وتُستخدم فاصلة بعد \"however\".   الخيار  \"I like to read; however, I don't have much time.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a semicolon to connect two closely related independent clauses?",
        "options": ["A.  The cake was delicious. It was chocolate.", "B. The cake was delicious; it was chocolate.", "C. The cake was delicious, it was chocolate.", "D. The cake was delicious and it was chocolate."],
        "correct_option_id": 1, # Index 1
        "explanation": "الفصلة المنقوطة تربط جملتين مستقلتين وثيقتي الصلة  دون استخدام رابط وصل.  الخيار  \"The cake was delicious; it was chocolate.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a semicolon be placed in this sentence: 'He studied hard for the test he aced it'",
        "options": ["A. He studied hard for the test he aced it.", "B. He studied hard for the test, he aced it.", "C. He studied hard for the test; he aced it.", "D. He studied hard for the test. He aced it."],
        "correct_option_id": 2, # Index 2
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بفاصلة منقوطة  لأنهما وثيقتا الصلة  ولا يوجد رابط وصل بينهما.  الخيار الصحيح هو:  \"He studied hard for the test; he aced it.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect semicolon usage:",
        "options": ["A. The dog barked, but the cat ran away.", "B. The sun is shining; the birds are singing.", "C. She likes to travel; her favorite destination is Italy.", "D.  He went to the store; and bought some milk."],
        "correct_option_id": 3, # Index 3
        "explanation": "في الجملة  \"He went to the store; and bought some milk.\",  تم استخدام الفاصلة المنقوطة مع رابط وصل (and).  هذا خطأ،  لأنه يجب استخدام إما الفاصلة المنقوطة  أو رابط الوصل، وليس كليهما معًا.  الخيار الصحيح هو:  \"He went to the store; he bought some milk.\"  أو  \"He went to the store, and he bought some milk.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a semicolon before a conjunctive adverb?",
        "options": ["A. She wanted to go to the beach. Therefore, she packed her swimsuit.", "B. She wanted to go to the beach; therefore, she packed her swimsuit.", "C. She wanted to go to the beach, therefore she packed her swimsuit.", "D. She wanted to go to the beach, therefore; she packed her swimsuit."],
        "correct_option_id": 1, # Index 1
        "explanation": "تُستخدم الفاصلة المنقوطة قبل الظرف الرابط (conjunctive adverb) مثل  \"therefore\"  في هذه الحالة،  وتُستخدم فاصلة بعد الظرف الرابط.  الخيار \"She wanted to go to the beach; therefore, she packed her swimsuit.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a semicolon be placed in this sentence: 'I love to cook my husband prefers to order takeout'",
        "options": ["A. I love to cook my husband prefers to order takeout.", "B. I love to cook, my husband prefers to order takeout.", "C. I love to cook. My husband prefers to order takeout.", "D. I love to cook; my husband prefers to order takeout."],
        "correct_option_id": 3, # Index 3
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بفاصلة منقوطة  لأنهما وثيقتا الصلة  ولا يوجد رابط وصل بينهما.  الخيار الصحيح هو:  \"I love to cook; my husband prefers to order takeout.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct semicolon usage:",
        "options": ["A. It was a beautiful day however, it was too hot to go outside.", "B. It was a beautiful day, however, it was too hot to go outside.", "C. It was a beautiful day; however, it was too hot to go outside.", "D. It was a beautiful day; however it was too hot to go outside."],
        "correct_option_id": 2, # Index 2
        "explanation": "تُستخدم الفاصلة المنقوطة قبل  \"however\"   عندما تفصل جملتين مستقلتين،  وتُستخدم فاصلة بعد \"however\".  الخيار  \"It was a beautiful day; however, it was too hot to go outside.\"  هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a semicolon to avoid confusion in a sentence with internal commas?",
        "options": ["A.  He visited his family in London, England, Paris, France, and Rome, Italy.", "B. He visited his family in London, England; Paris, France; and Rome, Italy.", "C. He visited his family in London England; Paris France; and Rome Italy.", "D.  He visited his family in London, England. Paris, France. And Rome, Italy."],
        "correct_option_id": 1, # Index 1
        "explanation": "تُستخدم الفاصلة المنقوطة لفصل عناصر سلسلة معقدة  تحتوي على فواصل داخليا  لتجنب الالتباس.  الخيار  \"He visited his family in London, England; Paris, France; and Rome, Italy.\"   هو الجملة الوحيدة التي تستخدم الفاصلة المنقوطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a semicolon be placed in this sentence: 'She is a talented artist she paints beautiful landscapes'",
        "options": ["A. She is a talented artist she paints beautiful landscapes.", "B. She is a talented artist, she paints beautiful landscapes.", "C. She is a talented artist; she paints beautiful landscapes.", "D. She is a talented artist. She paints beautiful landscapes."],
        "correct_option_id": 2, # Index 2
        "explanation": "الجملة تحتوي على جملتين مستقلتين  يجب فصلهما بفاصلة منقوطة  لأنهما وثيقتا الصلة  ولا يوجد رابط وصل بينهما.  الخيار الصحيح هو:  \"She is a talented artist; she paints beautiful landscapes.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect semicolon usage:",
        "options": ["A. He went to the store; he bought some milk.", "B. The sun is shining; however, it is cold.", "C. She loves to travel; her favorite destination is Paris.", "D.  The dog barked; and the cat meowed."],
        "correct_option_id": 3, # Index 3
        "explanation": "في الجملة  \"The dog barked; and the cat meowed.\",  تم استخدام الفاصلة المنقوطة مع رابط وصل (and).   هذا خطأ  لأنه يجب استخدام إما الفاصلة المنقوطة  أو رابط الوصل،  وليس كليهما معًا.  الخيار الصحيح هو:  \"The dog barked; the cat meowed.\"   أو  \"The dog barked, and the cat meowed.\""
    },
],
    "(:) نقطتان": [
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a colon?",
        "options": ["A. I need to buy the following groceries milk, bread, and eggs.", "B. I need to buy the following groceries: milk, bread, and eggs.", "C. I need to buy the following groceries, milk, bread, and eggs.", "D. I need to buy: the following groceries milk, bread, and eggs."],
        "correct_option_id": 1,  # Index 1
        "explanation": "تُستخدم النقطتان الرأسيتان (:)  لإدخال قائمة  أو شرح  أو توضيح.  في هذه الجملة  تُستخدم النقطتان الرأسيتان لإدخال قائمة المشتريات.  الخيار الصحيح هو:  \"I need to buy the following groceries: milk, bread, and eggs.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a colon be placed in this sentence: 'He had one goal in mind to win the championship'",
        "options": ["A. He had one goal in mind: to win the championship.", "B. He had one goal: in mind to win the championship.", "C. He had one goal in mind to win the championship.", "D. He had one goal in mind to win: the championship."],
        "correct_option_id": 0,  # Index 0
        "explanation": "في هذه الجملة  تُستخدم النقطتان الرأسيتان لإدخال شرح  أو توضيح للهدف.   الخيار الصحيح هو:  \"He had one goal in mind: to win the championship.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect colon usage:",
        "options": ["A. The recipe called for: flour, sugar, and eggs.", "B. She has two favorite hobbies: reading and painting.", "C.  The movie starts at: 7:00 PM.", "D.  He had one important task: to deliver the message."],
        "correct_option_id": 0,  # Index 0
        "explanation": "لا تُستخدم النقطتان الرأسيتان عادةً بعد فعل  أو حرف جر.   الخيار  \"The recipe called for: flour, sugar, and eggs.\"  يستخدم النقطتان الرأسيتان بعد فعل  وهو خطأ.  يجب حذف النقطتان الرأسيتان.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a colon to introduce a quotation?",
        "options": ["A.  She said: \"I'm going to the store.\"", "B.  She said, \"I'm going to the store.\"", "C. She said \"I'm going to the store.\"", "D. She said \"I'm going to the store\":"],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم النقطتان الرأسيتان لإدخال اقتباس  عندما يكون الاقتباس جملة كاملة  أو أكثر.  الخيار  \"She said: \"I'm going to the store.\"\"  هو الجملة الوحيدة التي تستخدم النقطتان الرأسيتان بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a colon be placed in this sentence: 'The following items are required passport, visa, and ticket'",
        "options": ["A. The following items are required passport, visa, and ticket.", "B. The following items are required, passport, visa, and ticket.", "C. The following items are required: passport, visa, and ticket.", "D.  The following: items are required passport, visa, and ticket."],
        "correct_option_id": 2,  # Index 2
        "explanation": "في هذه الجملة  تُستخدم النقطتان الرأسيتان لإدخال قائمة  بالعناصر المطلوبة.  الخيار الصحيح هو:  \"The following items are required: passport, visa, and ticket.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct colon usage:",
        "options": ["A. He has three pets: a dog, a cat, and a bird.", "B.  He has three pets a dog, a cat, and a bird.", "C.  He has three pets, a dog, a cat, and a bird.", "D. He has: three pets a dog, a cat, and a bird."],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم النقطتان الرأسيتان لإدخال قائمة.  الخيار \"He has three pets: a dog, a cat, and a bird.\"  هو الجملة الوحيدة التي تستخدم النقطتان الرأسيتان بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a colon to introduce a list?",
        "options": ["A. My favorite colors are: blue, green, and purple.", "B. My favorite colors are blue, green, and purple.", "C. My favorite colors are blue: green: and purple.", "D. My favorite colors are, blue, green, and purple."],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم النقطتان الرأسيتان لإدخال قائمة.  الخيار  \"My favorite colors are: blue, green, and purple.\"  هو الجملة الوحيدة التي تستخدم النقطتان الرأسيتان بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a colon be placed in this sentence: 'She gave him a simple instruction be kind'",
        "options": ["A. She gave him a simple instruction be kind.", "B. She gave him a simple instruction: be kind.", "C. She gave him a simple instruction, be kind.", "D. She gave him a: simple instruction be kind."],
        "correct_option_id": 1,  # Index 1
        "explanation": "في هذه الجملة  تُستخدم النقطتان الرأسيتان لإدخال شرح  أو توضيح للتعليمات.   الخيار الصحيح هو:  \"She gave him a simple instruction: be kind.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect colon usage:",
        "options": ["A. The meeting will begin at: 2:00 PM.", "B.  He has one dream: to travel the world.", "C.  The store sells: clothes, shoes, and accessories.", "D.  The train arrived at exactly: 3:45."],
        "correct_option_id": 0,  # Index 0
        "explanation": "لا تُستخدم النقطتان الرأسيتان عادةً بعد حرف جر  أو قبل التوقيت.  الخيار  \"The meeting will begin at: 2:00 PM.\"  يستخدم النقطتان الرأسيتان بعد حرف جر  وهو خطأ.  يجب حذف النقطتان الرأسيتان.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a colon to introduce a restatement or explanation?",
        "options": ["A. He was exhausted: he hadn't slept in days.", "B.  He was exhausted he hadn't slept in days.", "C. He was exhausted; he hadn't slept in days.", "D. He was exhausted he hadn't slept: in days."],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم النقطتان الرأسيتان لإدخال إعادة صياغة  أو شرح  للجملة السابقة.   الخيار \"He was exhausted: he hadn't slept in days.\"   هو الجملة الوحيدة التي تستخدم النقطتان الرأسيتان بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a colon be placed in this sentence: 'There is one thing I need from you honesty'",
        "options": ["A.  There is one thing I need from you honesty.", "B.  There is one thing I need from you, honesty.", "C.  There is one thing: I need from you honesty.", "D.  There is one thing I need from you: honesty."],
        "correct_option_id": 3,  # Index 3
        "explanation": "في هذه الجملة،   تُستخدم النقطتان الرأسيتان لإدخال شرح  أو توضيح  للشيء المطلوب.   الخيار الصحيح هو: \"There is one thing I need from you: honesty.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct colon usage:",
        "options": ["A. The bus will arrive at 4:30.", "B.  The bus will arrive at: 4:30.", "C. The bus will arrive: at 4:30.", "D. The bus will arrive at 4:30:."],
        "correct_option_id": 0,  # Index 0
        "explanation": "لا تُستخدم النقطتان الرأسيتان قبل التوقيت.  الخيار \"The bus will arrive at 4:30.\"  هو الجملة الوحيدة التي لا تستخدم النقطتان الرأسيتان بشكل خاطئ."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a colon to introduce a formal statement or announcement?",
        "options": ["A. Attention: all passengers must board the plane now.", "B. Attention, all passengers must board the plane now.", "C. Attention all passengers must board the plane now.", "D. Attention all passengers must: board the plane now."],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم النقطتان الرأسيتان لإدخال بيان  أو إعلان رسمي.   الخيار  \"Attention: all passengers must board the plane now.\"  هو الجملة الوحيدة التي تستخدم النقطتان الرأسيتان بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a colon be placed in this sentence: 'My favorite subjects are math, science, and history'",
        "options": ["A. My favorite subjects: are math, science, and history.", "B. My favorite subjects are math: science: and history.", "C.  My favorite subjects are: math, science, and history.", "D. My favorite subjects are math, science, and history."],
        "correct_option_id": 2,  # Index 2
        "explanation": "في هذه الجملة  تُستخدم النقطتان الرأسيتان لإدخال قائمة  بالمواد الدراسية المفضلة.  الخيار الصحيح هو:  \"My favorite subjects are: math, science, and history.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect colon usage:",
        "options": ["A. The store is open from: 9:00 AM to 5:00 PM.", "B. She has two cats: one is black, and the other is white.", "C. He loves to play sports: basketball, soccer, and tennis.", "D.  The doctor's advice was simple: get plenty of rest."],
        "correct_option_id": 0,  # Index 0
        "explanation": "لا تُستخدم النقطتان الرأسيتان قبل التوقيت.  الخيار \"The store is open from: 9:00 AM to 5:00 PM.\"  يستخدم النقطتان الرأسيتان قبل التوقيت  وهو خطأ.  يجب حذف النقطتان الرأسيتان. "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a colon to separate a title from a subtitle?",
        "options": ["A. The Lord of the Rings: The Fellowship of the Ring", "B. The Lord of the Rings, The Fellowship of the Ring", "C.  The Lord of the Rings. The Fellowship of the Ring", "D. The Lord of the Rings The Fellowship of the Ring"],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم النقطتان الرأسيتان لفصل عنوان الكتاب أو الفيلم عن عنوانه الفرعي.  الخيار \"The Lord of the Rings: The Fellowship of the Ring\"   هو الجملة الوحيدة التي تستخدم النقطتان الرأسيتان بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a colon be placed in this sentence: 'The ingredients for the cake are flour, sugar, eggs, and milk'",
        "options": ["A. The ingredients for the cake are: flour, sugar, eggs, and milk.", "B.  The ingredients for the cake: are flour, sugar, eggs, and milk.", "C. The ingredients for the cake are flour, sugar, eggs, and milk.", "D. The ingredients: for the cake are flour, sugar, eggs, and milk."],
        "correct_option_id": 0,  # Index 0
        "explanation": "في هذه الجملة  تُستخدم النقطتان الرأسيتان لإدخال قائمة  بمكونات الكعكة.   الخيار الصحيح هو:  \"The ingredients for the cake are: flour, sugar, eggs, and milk.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect colon usage:",
        "options": ["A.  She has one goal in life: to be happy.", "B. The game starts at 7:00 PM.", "C.  The recipe requires: two cups of flour, one cup of sugar, and two eggs.", "D.  The train arrived at: 8:15."],
        "correct_option_id": 3,  # Index 3
        "explanation": "لا تُستخدم النقطتان الرأسيتان قبل التوقيت.  الخيار  \"The train arrived at: 8:15.\"  يستخدم النقطتان الرأسيتان قبل التوقيت  وهو خطأ.  يجب حذف النقطتان الرأسيتان. "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a colon to introduce a series of appositives?",
        "options": ["A. He has many talents, playing the piano, singing, and dancing.", "B. He has many talents: playing the piano, singing, and dancing.", "C. He has many talents playing the piano, singing, and dancing.", "D. He has many talents: playing the piano; singing; and dancing."],
        "correct_option_id": 1,  # Index 1
        "explanation": "تُستخدم النقطتان الرأسيتان لإدخال سلسلة من التعابير الوصفية (appositives)  التي تُوضّح  أو تُفسّر  اسمًا  أو عبارة  سبق ذكرها.  الخيار  \"He has many talents: playing the piano, singing, and dancing.\"  هو الجملة الوحيدة التي تستخدم النقطتان الرأسيتان بشكل صحيح."
    }
],
    '("") علامة الاقتباس': [
            {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses quotation marks?",
        "options": ["A. “Where are you going?” she asked.", "B.  “Where are you going? she asked.”", "C. “Where are you going?”” she asked.", "D.  “Where are you going”? she asked."],
        "correct_option_id": 0,  # Index 0
        "explanation": "علامات التنصيص (“ ”) تُستخدم لإحاطة الكلام المنقول  (direct speech).  يجب وضع علامة استفهام  أو نقطة  أو علامة تعجب  داخل علامات التنصيص  إذا كانت جزءًا من الكلام المنقول.  الخيار  \"“Where are you going?” she asked.\"   هو الجملة الوحيدة التي تستخدم علامات التنصيص بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should quotation marks be placed in this sentence: He said I'm going to the store",
        "options": ["A. He said “I’m going to the store.”", "B. He said, “I’m going to the store.”", "C. “He said” I’m going to the store.", "D. He said, I’m going to the store."],
        "correct_option_id": 1,  # Index 1
        "explanation": "في هذه الجملة، يجب وضع علامات التنصيص حول الكلام المنقول  \"I'm going to the store\".  يجب أيضًا وضع فاصلة  بعد الفعل \"said\"   وقبل علامة التنصيص الافتتاحية.  الخيار الصحيح هو: \"He said, “I’m going to the store.”\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect quotation mark usage:",
        "options": ["A. “I love that song!” she exclaimed.", "B.  “Did you see the game?” he asked.", "C.  She said “I’m tired.”", "D.  “Be careful,” he warned. “The floor is slippery.”"],
        "correct_option_id": 2,  # Index 2
        "explanation": "في الجملة  \"She said “I’m tired.”\"   يجب وضع فاصلة بعد  \"said\"   وقبل علامة التنصيص الافتتاحية.  الخيار الصحيح هو:  \"She said, “I’m tired.”\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses single quotation marks within double quotation marks?",
        "options": ["A. He said, “She told me, ‘I’m not coming.’”", "B. He said, “She told me, “I’m not coming.””", "C. He said, ‘She told me, “I’m not coming.”’", "D. He said, “She told me, “I’m not coming.”"],
        "correct_option_id": 0,  # Index 0
        "explanation": "عند وجود اقتباس داخل اقتباس  نستخدم علامات تنصيص مفردة (')  داخل علامات تنصيص مزدوجة (“”).  الخيار  \"He said, “She told me, ‘I’m not coming.’”\"   هو الجملة الوحيدة التي تستخدم علامات التنصيص بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should quotation marks be placed in this sentence: The teacher said Class is dismissed",
        "options": ["A. The teacher said, ‘Class is dismissed.’", "B. The teacher said “Class is dismissed.”", "C.  “The teacher said” Class is dismissed.", "D.  The teacher said, “Class is dismissed"],
        "correct_option_id": 0,  # Index 0
        "explanation": "في هذه الجملة،   يجب وضع علامات التنصيص حول الكلام المنقول  \"Class is dismissed\".  يجب أيضًا وضع فاصلة  بعد الفعل  \"said\"   وقبل علامة التنصيص الافتتاحية.  الخيار الصحيح هو: \"The teacher said, ‘Class is dismissed.’”"
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct quotation mark usage:",
        "options": ["A.  “Did you do your homework? the teacher asked.”", "B. “What is the capital of France?” she asked.", "C.  He said, I am going to the park.", "D.  “Be quiet! she shouted.”"],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة \"“What is the capital of France?” she asked.\"   هي الجملة الوحيدة التي تستخدم علامات التنصيص بشكل صحيح.  الخيارات الأخرى  إما تضع علامات الترقيم في أماكن خاطئة  أو تفتقد فاصلة ضرورية."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses quotation marks to enclose a title of a short story?",
        "options": ["A. Have you read “The Gift of the Magi”?", "B.  Have you read The Gift of the Magi?", "C.  Have you read “The Gift of the Magi?”", "D. Have you read “The Gift of the Magi”?"],
        "correct_option_id": 0,  # Index 0
        "explanation": "علامات التنصيص تُستخدم لإحاطة عناوين القصص القصيرة  والمقالات  والأغاني  وفصول الكتب.  الخيار  \"Have you read “The Gift of the Magi”?”  هو الجملة الوحيدة التي تستخدم علامات التنصيص بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should quotation marks be placed in this sentence: The sign read No parking",
        "options": ["A.  The sign read “No parking.”", "B. The sign read “No parking”.", "C.  The sign “read” No parking.", "D.  “The sign read” No parking."],
        "correct_option_id": 0,  # Index 0
        "explanation": "في هذه الجملة،   يجب وضع علامات التنصيص حول الكلام المنقول  \"No parking\".  الخيار الصحيح هو:  \"The sign read “No parking.”\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect quotation mark usage:",
        "options": ["A. “The dog barked loudly”, he said.", "B.  “Please be quiet,” she whispered.", "C.  “What time is it?” he asked.", "D. “I am going to the store,” she said."],
        "correct_option_id": 0,  # Index 0
        "explanation": "في الجملة  \"The dog barked loudly”, he said.\"،   تم وضع الفاصلة خارج علامات التنصيص  وهو خطأ.  يجب وضع الفاصلة داخل علامات التنصيص.   الخيار الصحيح هو:  \"“The dog barked loudly,” he said.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses quotation marks to show sarcasm or irony?",
        "options": ["A.  He said, “That was a ‘great’ idea.”", "B.  He said, “That was a great idea.”", "C. He said, “That was a ‘great idea.’”", "D. He said, ‘That was a “great” idea.’"],
        "correct_option_id": 0,  # Index 0
        "explanation": "يمكن استخدام علامات تنصيص مفردة (')  داخل علامات تنصيص مزدوجة (“”)  للتعبير عن سخرية  أو تهكم.   الخيار  \"He said, “That was a ‘great’ idea.”\"  هو الجملة الوحيدة التي تستخدم علامات التنصيص بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should quotation marks be placed in this sentence: My favorite poem is The Road Not Taken",
        "options": ["A. My favorite poem is “The Road Not Taken.”", "B.  My favorite poem is “The Road Not Taken”.", "C.  “My favorite poem is” The Road Not Taken.", "D.  My favorite poem is, “The Road Not Taken.”"],
        "correct_option_id": 0,  # Index 0
        "explanation": "في هذه الجملة،   يجب وضع علامات التنصيص حول عنوان القصيدة  \"The Road Not Taken\".  الخيار الصحيح هو:  \"My favorite poem is “The Road Not Taken.”\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct quotation mark usage:",
        "options": ["A.  “I am so happy!” she exclaimed", "B.  “Please help me,” he pleaded.”", "C. “Where are you going?” he asked.", "D.  She said, “I love to read”."],
        "correct_option_id": 2,  # Index 2
        "explanation": "الجملة  \"“Where are you going?” he asked.\"   هي الجملة الوحيدة التي تستخدم علامات التنصيص وعلامات الترقيم بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses quotation marks to enclose a title of a song?",
        "options": ["A. Her favorite song is “Imagine.”", "B.  Her favorite song is Imagine.", "C. Her favorite song is “Imagine”.", "D. “Her favorite song is” Imagine."],
        "correct_option_id": 0,  # Index 0
        "explanation": "علامات التنصيص تُستخدم لإحاطة عناوين الأغاني.   الخيار  \"Her favorite song is “Imagine.”\"  هو الجملة الوحيدة التي تستخدم علامات التنصيص بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should quotation marks be placed in this sentence: The word 'love' has many different meanings",
        "options": ["A. The word ‘love’ has many different meanings.", "B. “The word ‘love’ has many different meanings.", "C. The word “love” has many different meanings.", "D.  The word “love” has many different meanings."],
        "correct_option_id": 2,  # Index 2
        "explanation": "في هذه الجملة،  يجب وضع علامات التنصيص حول الكلمة  \"love\".  الخيار الصحيح هو:  \"The word “love” has many different meanings.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect quotation mark usage:",
        "options": ["A. “The cat is on the roof.” she said.", "B. “What a beautiful day!” he exclaimed.", "C. “I am going to the store, she said.", "D. “Please be careful,” he warned."],
        "correct_option_id": 2,  # Index 2
        "explanation": "في الجملة  \"I am going to the store, she said.”،  يجب وضع فاصلة بعد  \"store\"  وقبل علامة التنصيص الختامية.   الخيار الصحيح هو:  \"“I am going to the store,” she said.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses quotation marks to set off a definition?",
        "options": ["A. The word “loquacious” means “tending to talk a great deal; talkative.”", "B. The word loquacious means “tending to talk a great deal; talkative.”", "C. The word “loquacious” means “tending to talk a great deal; talkative”.", "D. The word “loquacious” means tending to talk a great deal; talkative."],
        "correct_option_id": 0,  # Index 0
        "explanation": "علامات التنصيص تُستخدم لإحاطة تعريف كلمة.  الخيار  \"The word “loquacious” means “tending to talk a great deal; talkative.”\"  هو الجملة الوحيدة التي تستخدم علامات التنصيص بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should quotation marks be placed in this sentence: He whispered, I love you",
        "options": ["A.  He whispered, “I love you.”", "B. He whispered, “I love you”.", "C. “He whispered,” I love you.", "D. He whispered “I love you.”"],
        "correct_option_id": 0,  # Index 0
        "explanation": "في هذه الجملة،   يجب وضع علامات التنصيص حول الكلام المنقول   \"I love you\".  يجب أيضًا وضع فاصلة  بعد الفعل \"whispered\"   وقبل علامة التنصيص الافتتاحية.   الخيار الصحيح هو:  \"He whispered, “I love you.”\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct quotation mark usage:",
        "options": ["A.  “Do you want to go to the movies?” she asked.", "B.  She said, “I'm going to the store.”", "C. He said, “I'm feeling tired.”", "D. “What are you doing?” he asked."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الجملة \"She said, \"I'm going to the store.\"\"   هي الجملة الوحيدة التي تستخدم علامات التنصيص وعلامات الترقيم بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses quotation marks to enclose a title of a chapter in a book?",
        "options": ["A. The first chapter is titled “The Beginning.”", "B.  The first chapter is titled, “The Beginning.”", "C.  The first chapter is titled, The Beginning.", "D.  “The first chapter is titled” The Beginning."],
        "correct_option_id": 0,  # Index 0
        "explanation": "علامات التنصيص تُستخدم لإحاطة عناوين فصول الكتب.   الخيار   \"The first chapter is titled “The Beginning.”\"   هو الجملة الوحيدة التي تستخدم علامات التنصيص بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should quotation marks be placed in this sentence: The article was titled The Future of Technology",
        "options": ["A. The article was titled “The Future of Technology”.", "B. The article was titled, “The Future of Technology.”", "C. “The article was titled” The Future of Technology.", "D. The article was titled “The Future of Technology.”"],
        "correct_option_id": 3,  # Index 3
        "explanation": "في هذه الجملة،   يجب وضع علامات التنصيص حول عنوان المقال  \"The Future of Technology\".  الخيار الصحيح هو:  \"The article was titled “The Future of Technology.”\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect quotation mark usage:",
        "options": ["A. “Have you seen my keys? she asked.”", "B.  He said, “I am going to the park.”", "C.  “The food is delicious!” she exclaimed.", "D.  “Be careful,” he warned. “The floor is wet.”"],
        "correct_option_id": 0,  # Index 0
        "explanation": "في الجملة  \"Have you seen my keys? she asked.”،   تم وضع علامة الاستفهام خارج علامات التنصيص   وهو خطأ.  يجب وضع علامة الاستفهام داخل علامات التنصيص.   الخيار الصحيح هو:   \"“Have you seen my keys?” she asked.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses quotation marks with a split quotation?",
        "options": ["A.  “I’m going to the store,” she said, “to buy some milk.”", "B.  “I’m going to the store,” she said. “To buy some milk.”", "C.  “I’m going to the store, she said, to buy some milk.”", "D.  “I’m going to the store” she said “to buy some milk.”"],
        "correct_option_id": 0,  # Index 0
        "explanation": "عندما يكون الاقتباس مُقسّمًا إلى جزأين  نضع علامات تنصيص افتتاحية وختامية  حول كل جزء.   الخيار  \"“I’m going to the store,” she said, “to buy some milk.”\"  هو الجملة الوحيدة التي تستخدم علامات التنصيص بشكل صحيح."
    }

    ],
    "(-) الشرطة": [
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a dash?",
        "options": ["A.  She loves to travel - especially to exotic destinations.", "B.  She loves to travel-especially to exotic destinations.", "C.  She loves to travel especially - to exotic destinations.", "D.  She loves to travel especially to exotic destinations."],
        "correct_option_id": 0,  # Index 0
        "explanation": "الشرطة (-)  تُستخدم لفصل جزء من الجملة  للتأكيد عليه  أو لإضافة معلومة إضافية.  يجب ترك مسافة قبل وبعد الشرطة.  الخيار \"She loves to travel - especially to exotic destinations.\"  هو الجملة الوحيدة التي تستخدم الشرطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a dash be placed in this sentence: 'The party was a success everyone had a great time'",
        "options": ["A. The party was a success everyone had a great time.", "B. The party was a success - everyone had a great time.", "C. The party was a success everyone- had a great time.", "D. The party - was a success everyone had a great time."],
        "correct_option_id": 1,  # Index 1
        "explanation": "في هذه الجملة،  تُستخدم الشرطة لفصل الجزء الثاني  \"everyone had a great time\"   للتأكيد على نجاح الحفلة.   الخيار الصحيح هو: \"The party was a success - everyone had a great time.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect dash usage:",
        "options": ["A. He loves to read—especially history books.", "B.  She has two cats - a Siamese and a Persian.", "C.  The meeting will be held at - 3:00 PM.", "D.  The store is open Monday - Friday."],
        "correct_option_id": 2,  # Index 2
        "explanation": "لا تُستخدم الشرطة عادةً قبل التوقيت  أو قبل حرف الجر.   الخيار \"The meeting will be held at - 3:00 PM.\"  يستخدم الشرطة قبل التوقيت  وهو خطأ.  يجب حذف الشرطة  أو استخدام نقطتين رأسيتين بدلاً منها. "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a dash to set off a parenthetical element?",
        "options": ["A.  My favorite color—blue—is often associated with peace and tranquility.", "B. My favorite color - blue - is often associated with peace and tranquility.", "C. My favorite color blue—is often associated with peace and tranquility.", "D. My favorite color, blue, is often associated with peace and tranquility."],
        "correct_option_id": 1,  # Index 1
        "explanation": "تُستخدم الشرطة لإحاطة عنصر اعتراضي (parenthetical element)  داخل الجملة.  الخيار \"My favorite color - blue - is often associated with peace and tranquility.\"  هو الجملة الوحيدة التي تستخدم الشرطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a dash be placed in this sentence: 'He has everything he could ever want money, fame, and love'",
        "options": ["A. He has everything he could ever want money, fame, and love.", "B. He has everything he could ever want: money, fame, and love.", "C. He has everything he could ever want—money, fame, and love.", "D. He has everything - he could ever want money, fame, and love."],
        "correct_option_id": 2,  # Index 2
        "explanation": "في هذه الجملة  تُستخدم الشرطة لفصل قائمة الأشياء التي يمتلكها  للتأكيد عليها.  الخيار الصحيح هو: \"He has everything he could ever want—money, fame, and love.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct dash usage:",
        "options": ["A. She loves to read - novels, biographies, and poetry.", "B.  The game was close - the score was tied until the last minute.", "C.  The meeting is scheduled for—10:00 AM tomorrow.", "D.  He has one major flaw-he's always late."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الخيار  \"The game was close - the score was tied until the last minute.\"   هو الجملة الوحيدة التي تستخدم الشرطة بشكل صحيح  لإضافة معلومة إضافية  أو شرح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a dash to indicate an abrupt change in thought?",
        "options": ["A. I was going to go to the store—but then I decided to stay home.", "B. I was going to go to the store but then I decided to stay home.", "C. I was going to go to the store, but then I decided to stay home.", "D. I was going to go to the store but-then I decided to stay home."],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم الشرطة للإشارة إلى تغير مفاجئ في الفكرة  أو الجملة.  الخيار  \"I was going to go to the store—but then I decided to stay home.\"  هو الجملة الوحيدة التي تستخدم الشرطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a dash be placed in this sentence: 'He was happy but not too happy to see her'",
        "options": ["A. He was happy but - not too happy to see her.", "B. He was happy but not too happy - to see her.", "C. He was happy - but not too happy - to see her.", "D. He was happy but not too happy to see - her."],
        "correct_option_id": 2,  # Index 2
        "explanation": "في هذه الجملة،  تُستخدم الشرطة لإحاطة العبارة  \"but not too happy\"   للتأكيد على درجة سعادته.  الخيار الصحيح هو:  \"He was happy - but not too happy - to see her.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect dash usage:",
        "options": ["A.  She has everything she needs—a loving family, a good job, and a comfortable home.", "B. The concert starts at 8:00 PM.", "C. He loves to travel—he’s been to every continent except Antarctica.", "D.  She loves to cook-and she’s very good at it."],
        "correct_option_id": 3,  # Index 3
        "explanation": "في الجملة  \"She loves to cook-and she’s very good at it.\",  تم استخدام الشرطة بشكل غير صحيح.  يجب استخدام فاصلة  بدلاً من الشرطة،  أو استخدام جملتين منفصلتين.   الخيار الصحيح هو: \"She loves to cook, and she’s very good at it.\"  أو \"She loves to cook. She’s very good at it.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a dash to summarize or restate a previous idea?",
        "options": ["A. He's a kind, generous, and thoughtful person—in other words, a great friend.", "B. He's a kind, generous, and thoughtful person, in other words, a great friend.", "C. He's a kind, generous, and thoughtful person; in other words, a great friend.", "D. He's a kind, generous, and thoughtful person in other words—a great friend."],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم الشرطة لتلخيص  أو إعادة صياغة فكرة سابقة.   الخيار  \"He's a kind, generous, and thoughtful person—in other words, a great friend.\"  هو الجملة الوحيدة التي تستخدم الشرطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a dash be placed in this sentence: 'Her favorite hobbies are reading, writing, and painting all creative pursuits'",
        "options": ["A. Her favorite hobbies are: reading, writing, and painting—all creative pursuits.", "B. Her favorite hobbies are—reading, writing, and painting—all creative pursuits.", "C. Her favorite hobbies are reading, writing, and painting all creative pursuits.", "D. Her favorite hobbies are reading, writing, and painting—all creative pursuits."],
        "correct_option_id": 3,  # Index 3
        "explanation": "في هذه الجملة،  تُستخدم الشرطة لفصل العبارة  \"all creative pursuits\"   التي تُلخّص الهوايات.  الخيار الصحيح هو:  \"Her favorite hobbies are reading, writing, and painting—all creative pursuits.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct dash usage:",
        "options": ["A.  She loves to dance—it's her passion.", "B. She loves to dance - it's her passion.", "C.  She loves to dance it's her passion.", "D. She loves to dance it's—her passion."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الخيار  \"She loves to dance - it's her passion.\"   هو الجملة الوحيدة التي تستخدم الشرطة بشكل صحيح  لإضافة معلومة إضافية  أو شرح.  "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a dash to indicate an interruption or hesitation?",
        "options": ["A. I was—well, I was a little surprised.", "B. I was well, I was a little surprised.", "C.  I was, well, I was a little surprised.", "D. I was well—I was a little surprised."],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم الشرطة للإشارة إلى توقف  أو تردد في الكلام.  الخيار  \"I was—well, I was a little surprised.\"  هو الجملة الوحيدة التي تستخدم الشرطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a dash be placed in this sentence: 'He had only one fear spiders'",
        "options": ["A. He had only one fear spiders.", "B. He had only one fear-spiders.", "C.  He had only one fear spiders-", "D. He had only one fear: spiders."],
        "correct_option_id": 1,  # Index 1
        "explanation": "في هذه الجملة،  تُستخدم الشرطة لفصل الكلمة  \"spiders\"   للتأكيد عليها.  الخيار الصحيح هو:  \"He had only one fear—spiders.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with incorrect dash usage:",
        "options": ["A.  The movie was—to put it mildly—terrible.", "B. She loves to sing—and she has a beautiful voice.", "C.  The store is having a sale—everything is 50% off!", "D.  The train arrived—right on time."],
        "correct_option_id": 1,  # Index 1
        "explanation": "في الجملة  \"She loves to sing—and she has a beautiful voice.\",   تم استخدام الشرطة بشكل غير صحيح.  يجب استخدام فاصلة  بدلاً من الشرطة،  أو استخدام جملتين منفصلتين.   الخيار الصحيح هو:  \"She loves to sing, and she has a beautiful voice.\"  أو \"She loves to sing. She has a beautiful voice.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a dash to set off an appositive that contains commas?",
        "options": ["A. My favorite cities—Paris, Rome, and London—are all in Europe.", "B. My favorite cities, Paris, Rome, and London, are all in Europe.", "C.  My favorite cities Paris, Rome, and London—are all in Europe.", "D. My favorite cities: Paris, Rome, and London are all in Europe."],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم الشرطة لإحاطة تعبير وصفي (appositive)  يحتوي على فواصل.  الخيار  \"My favorite cities—Paris, Rome, and London—are all in Europe.\"  هو الجملة الوحيدة التي تستخدم الشرطة بشكل صحيح."
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhere should a dash be placed in this sentence: 'He had three goals in life to be happy, to be successful, and to make a difference'",
        "options": ["A. He had three goals in life to be happy, to be successful, and to make a difference.", "B. He had three goals—in life to be happy, to be successful, and to make a difference.", "C. He had three goals in life—to be happy, to be successful, and to make a difference.", "D. He had three goals in life to be happy, to be successful, and to make—a difference."],
        "correct_option_id": 2,  # Index 2
        "explanation": "في هذه الجملة،  تُستخدم الشرطة لفصل قائمة الأهداف  للتأكيد عليها.  الخيار الصحيح هو: \"He had three goals in life—to be happy, to be successful, and to make a difference.\""
    },
    {
        "question": "اختر الإجابة الصحيحة:\nIdentify the sentence with correct dash usage:",
        "options": ["A. She has a lot of friends—she’s very outgoing.", "B.  She has a lot of friends - she’s very outgoing.", "C.  She has a lot of friends, she’s very outgoing.", "D. She has a lot of friends—she’s very—outgoing."],
        "correct_option_id": 1,  # Index 1
        "explanation": "الخيار  \"She has a lot of friends - she’s very outgoing.\"   هو الجملة الوحيدة التي تستخدم الشرطة بشكل صحيح  لإضافة معلومة إضافية  أو شرح. "
    },
    {
        "question": "اختر الإجابة الصحيحة:\nWhich sentence correctly uses a dash to indicate a sudden break in a sentence?",
        "options": ["A. I was going to tell her—but then I changed my mind.", "B. I was going to tell her but then I changed my mind.", "C.  I was going to tell her, but then I changed my mind.", "D.  I was going to tell her but then—I changed my mind."],
        "correct_option_id": 0,  # Index 0
        "explanation": "تُستخدم الشرطة للإشارة إلى توقف  أو فاصل مفاجئ في الجملة.  الخيار  \"I was going to tell her—but then I changed my mind.\"  هو الجملة الوحيدة التي تستخدم الشرطة بشكل صحيح."
    }
]

}
 
    
}
