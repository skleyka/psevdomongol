import random

# Слоги для генерации слов (без "ц", "ф", "ш", "щ", "ь", "ъ", "х", "й")
# Слоги состоят из одной гласной, сочетания "согласная + гласная" или благозвучных сочетаний из трех букв
syllables = [
    "га", "гу", "го", "гы", "ге", "ги", "ла", "лу", "ло", "лы", "ле", "ли",
    "ра", "ру", "ро", "ры", "ре", "ри", "на", "ну", "но", "ны", "не", "ни",
    "ма", "му", "мо", "мы", "ме", "ми", "ба", "бу", "бо", "бы", "бе", "би",
    "да", "ду", "до", "ды", "де", "ди", "за", "зу", "зо", "зы", "зе", "зи",
    "ва", "ву", "во", "вы", "ве", "ви", "та", "ту", "то", "ты", "те", "ти",
    "па", "пу", "по", "пы", "пе", "пи", "ка", "ку", "ко", "кы", "ке", "ки",
    "са", "су", "со", "сы", "се", "си", "а", "у", "о", "ы", "е", "и", "я", "ю", "ё",
    # Благозвучные слоги с двумя согласными (не длиннее трех букв)
    "тра", "тро", "тру", "дро", "дру", "гра", "гро", "гру", "бра", "бро", "бру",
    "пра", "про", "пру", "кра", "кро", "кру", "вра", "вро", "вру",
    "сла", "сло", "слу", "сма", "смо", "сму"
]

# Гласные буквы
vowels = "ауоыэяиюёе"

# Окончания и их вероятности (без дефисов)
endings = {
    "ус": 0.15,
    "ар": 0.10,
    "ыр": 0.10,
    "ур": 0.05,
    "ик": 0.05,
    "ык": 0.04,
    "ис": 0.05,
    "ыс": 0.04,
    "ан": 0.04,
    "ит": 0.05,
    "са": 0.05,
    "ад": 0.10,
    "ак": 0.05,
    "ан": 0.05,
    "рс": 0.05,
    "а": 0.03
}

# Функция для проверки, что в слове нет подряд идущих одинаковых букв
def has_no_double_letters(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return False
    return True

# Функция для проверки, что слово не заканчивается на гласную, кроме "а"
def ends_with_valid_letter(word):
    last_char = word[-1]
    return last_char == "а" or last_char not in vowels

# Функция для проверки, что в слове нет двух гласных подряд
def has_no_double_vowels(word):
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i + 1] in vowels:
            return False
    return True

# Функция для проверки, что в слове нет двух подряд идущих одинаковых слогов
def has_no_double_syllables(word, syllables):
    for i in range(len(word) - 1):
        # Проверяем все возможные слоги
        for syllable in syllables:
            if word[i:i+len(syllable)] == syllable and word[i+len(syllable):i+2*len(syllable)] == syllable:
                return False
    return True

# Функция для выбора окончания на основе вероятностей (альтернатива random.choices)
def choose_ending():
    # Создаем список окончаний и их весов
    endings_list = list(endings.keys())
    weights = list(endings.values())
    
    # Нормализуем веса (сумма должна быть равна 1)
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    
    # Генерируем случайное число и выбираем окончание
    rand = random.random()
    cumulative_weight = 0.0
    for ending, weight in zip(endings_list, normalized_weights):
        cumulative_weight += weight
        if rand < cumulative_weight:
            return ending
    return endings_list[-1]  # На случай, если что-то пошло не так

# Функция для генерации слова
def generate_word():
    while True:
        # Выбираем случайное количество слогов для основной части слова (от 5 до 7)
        # Чтобы общее количество слогов с окончанием не превышало 8
        num_syllables = random.randint(5, 7)
        word = ""
        
        # Генерируем основную часть слова из случайных слогов
        for _ in range(num_syllables):
            syllable = random.choice(syllables)
            word += syllable
        
        # Добавляем окончание
        ending = choose_ending()
        word += ending
        
        # Проверяем:
        # 1. Нет подряд идущих одинаковых букв
        # 2. Нет двух гласных подряд
        # 3. Слово не заканчивается на гласную, кроме "а"
        # 4. Нет двух подряд идущих одинаковых слогов
        # 5. Общее количество слогов (основная часть + окончание) не превышает 8
        if (
            has_no_double_letters(word)
            and has_no_double_vowels(word)
            and ends_with_valid_letter(word)
            and has_no_double_syllables(word, syllables)
            and (num_syllables + 1) <= 8  # Окончание добавляет 1 слог
        ):
            return word

# Генерация и вывод 10 примеров слов
for _ in range(10):
    print(generate_word())