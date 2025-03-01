import random

# Список слогов
syllables = [
    "га", "гу", "го", "гы", "ге", "ги", "ла", "лу", "ло", "лы", "ле", "ли",
    "ра", "ру", "ро", "ры", "ре", "ри", "на", "ну", "но", "ны", "не", "ни",
    "ма", "му", "мо", "мы", "ме", "ми", "ба", "бу", "бо", "бы", "бе", "би",
    "да", "ду", "до", "ды", "де", "ди", "за", "зу", "зо", "зы", "зе", "зи",
    "ва", "ву", "во", "вы", "ве", "ви", "та", "ту", "то", "ты", "те", "ти",
    "па", "пу", "по", "пы", "пе", "пи", "ка", "ку", "ко", "кы", "ке", "ки",
    "са", "су", "со", "сы", "се", "си", "а", "у", "о", "ы", "е", "и", "я", "ю",
    "тра", "тро", "тру", "дро", "дру", "гра", "гро", "гру", "бра", "бро", "бру",
    "пра", "про", "пру", "кра", "кро", "кру", "вра", "вро", "вру",
    "сла", "сло", "слу", "сма", "смо", "сму",
    # Слоги перед окончанием
    "габ", "губ", "гоб", "гыб", "геб", "гиб",
    "лав", "лув", "лов", "лыв", "лев", "лив",
    "раг", "руг", "рог", "рыг", "рег", "риг",
    "над", "нуд", "нод", "ныд", "нед", "нид",
    "баз", "буз", "боз", "быз", "без", "биз",
    "зак", "зук", "зок", "зык", "зек", "зик",
    "вал", "вул", "вол", "выл", "вел", "вил",
    "там", "тум", "том", "тым", "тем", "тим",
    "пан", "пун", "пон", "пын", "пен", "пин",
    "кар", "кур", "кор", "кыр", "кер", "кир",
    "сас", "сус", "сос", "сыс", "сес", "сис",
    "тат", "тут", "тот", "тыт", "тет", "тит"
]

# Окончания и их вероятности
endings_with_probabilities = {
    "ус": 0.15,
    "ар": 0.11,
    "ыр": 0.12,
    "ур": 0.05,
    "ик": 0.05,
    "ык": 0.04,
    "ис": 0.05,
    "ыс": 0.04,
    "ан": 0.04,
    "ит": 0.05,
    "ад": 0.12,
    "ак": 0.05,
    "рс": 0.05,
    "а": 0.03
}

# Вероятности длины основной части
length_probabilities = {
    4: 0.20,
    5: 0.35,
    6: 0.35,
    7: 0.10
}

# Гласные буквы
vowels = "ауоыеияю"

# Согласные буквы (кроме ч, ш, щ, ц, х, ж, й, ф)
consonants = "бвгдклмнпрстз"

# Все возможные сочетания из двух гласных подряд
forbidden_vowel_pairs = [v1 + v2 for v1 in vowels for v2 in vowels]

# Запрещенные буквосочетания
forbidden_consonant_pairs = [
    "бг", "вг", "дг", "зг", "кг", "лг", "мг", "нг", "пг", "рг", "сг", "тг",
    "бд", "вд", "гд", "зд", "кд", "лд", "мд", "нд", "пд", "рд", "сд", "тд",
    "бп", "вп", "гп", "дп", "зп", "кп", "лп", "мп", "нп", "рп", "сп", "тп",
    "кы", "зы", 
    "вб", "гб", "дб", "зб", "кб", "мб", "нб", "пб", "сб", "тб",
    "бз", "вз", "гз", "дз", "кз", "мз", "нз", "пз", "сз", "тз",
    "бк", "вк", "гк", "дк", "зк", "мк", "нк", "пк", "тк"
]

def generate_main_part():
    # Выбираем длину основной части на основе вероятностей
    length = random.choices(list(length_probabilities.keys()), weights=length_probabilities.values())[0]
    
    main_part = []
    for _ in range(length - 1):  # Генерируем все слоги, кроме последнего
        syllable = random.choice(syllables)
        main_part.append(syllable)
    
    # Последний слог должен заканчиваться на согласную
    consonant_ending_syllables = [s for s in syllables if s[-1] not in vowels]
    last_syllable = random.choice(consonant_ending_syllables)
    main_part.append(last_syllable)
    
    return "".join(main_part)

def choose_ending():
    # Выбираем случайное окончание на основе вероятностей
    endings = list(endings_with_probabilities.keys())
    probabilities = list(endings_with_probabilities.values())
    return random.choices(endings, weights=probabilities)[0]

def is_valid_word(word):
    # Проверка на подряд идущие одинаковые буквы
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return False
    
    # Проверка на наличие запрещенных сочетаний гласных
    for pair in forbidden_vowel_pairs:
        if pair in word:
            return False
    
    # Проверка на три подряд идущих согласных
    consonant_count = 0
    for letter in word:
        if letter in consonants:
            consonant_count += 1
            if consonant_count >= 3:
                return False
        else:
            consonant_count = 0
    
    # Проверка на общую длину слова
    if len(word) > 15:
        return False
    
    # Проверка на запрещенные буквосочетания
    for pair in forbidden_consonant_pairs:
        if pair in word:
            return False
    
    return True

def generate_word():
    max_attempts = 1000  # Максимальное количество попыток
    attempt = 0
    
    while attempt < max_attempts:
        main_part = generate_main_part()
        ending = choose_ending()
        word = main_part + ending
        
        if is_valid_word(word):
            return word
        
        attempt += 1
    
    # Если не удалось сгенерировать слово за max_attempts попыток
    return "Не удалось сгенерировать псевдомонгольское название"

# Генерация и вывод 10 псевдомонгольских слов
for _ in range(10):
    print(generate_word())