"""Створіть разважальний чат-бот на Python. Даний бот може рекомендувати фільми, музику,
ігри за жанрами, анекдоти, цікаві історії, а також надати можливість пограти в гру.
За бажанням можете додати додаткові можливості. """

import random
from colorama import Fore, Back, Style, init
from pyjokes import get_joke
from art import tprint
from translate import Translator
import emoji

films = {
    "фантастика": ["Дюна", "Матриця", "Зоряні війни"],
    "комедія": ["Один вдома", "Маска", "Брюс Всемогутній"],
    "жахи": ["Сяйво", "Екзорцист", "Воно"],
    "драма": ["Втеча з Шоушенка", "Зелена миля", "Список Шиндлера"],
    "бойовик": ["Міцний горішок", "Термінатор 2", "Матриця"]
}

music = {
    "поп": ["Taylor Swift", "Ed Sheeran", "Madonna"],
    "рок": ["Queen", "Nirvana", "Metallica"],
    "хіп-хоп": ["2Pac", "Eminem", "Drake"],
    "електронна": ["David Guetta", "Martin Garrix", "Alan Walker"],
    "джаз": ["Louis Armstrong", "Duke Ellington", "Frank Sinatra"]
}

games = {
    "рольові": ["The Witcher 3", "The Elder Scrolls V: Skyrim", "Cyberpunk 2077"],
    "шутери": ["Counter-Strike 2", "Apex Legends", "Call of Duty"],
    "симулятори": ["The Sims 4", "Stardew Valley", "Cities: Skylines"],
    "пригоди": ["The Last of Us Part I", "The Legend of Zelda", "Red Dead Redemption 2"],
    "стратегії": ["StarCraft II", "Civilization VI", "Age of Empires II"]
}

stories = [
    "Назва мови походить не від змії. Автор Python, Гвідо ван Россум,\n"
    "назвав її на честь улюбленого комедійного серіалу BBC — \n"
    "«Літаючий цирк Монті Пайтона» (Monty Python's Flying Circus).",
    "Простота написання. Python розробляли з акцентом на читабельність\n"
    "і простий синтаксис. Завдяки цьому він дозволяє писати код у 3-5 \n"
    "разів швидше, ніж на інших мовах, наприклад C++ або Java.",
    "Програмісти часто використовують гумову качечку для налагодження\n"
    "коду. Цей метод називається \"методом гумової качечки\". Ідея\n"
    "полягає в тому, щоб пояснити кожен рядок коду неживому предмету\n"
    "(наприклад, гумовій качечці). Сам процес пояснення допомагає \n"
    "виявити логічні помилки, які інакше було б важко знайти.",
    "Програмісти називають помилки \"багами\" через реального жука.\n"
    "У 1947 році програмісти Гарвардського університету знайшли в \n"
    "обчислювальній машині Mark II Aiken Relay Calculator жука (англ. bug),\n"
    "який застряг у реле, спричинивши збій. Це був перший\n"
    "задокументований \"комп'ютерний баг\".",
    "Програмісти дуже цінують якісний сон. Багато програмістів\n"
    "вважають, що найкращі ідеї для вирішення складних проблем\n"
    "приходять уві сні або після гарного відпочинку. Коли мозок не\n"
    "перевантажений, він може знайти неочевидні рішення.",
    "Багато сучасних програмістів — самоуки. Хоча вища освіта є\n"
    "великим плюсом, багато успішних програмістів отримали свої\n"
    "знання самостійно, користуючись онлайн-курсами, книгами та\n"
    "відкритими ресурсами. Постійне самовдосконалення є важливою\n"
    "частиною цієї професії."
]


def game_rock_paper():
    """Гра Камінь-ножиці-папір"""
    init(autoreset=True)
    options = ["камінь", "ножиці", "папір"]

    while True:
        game_choose = input("Оберіть камінь, ножиці або папір: ").lower()
        if game_choose in options:
            break
        print(f"{Fore.RED}Невірний вибір!{Style.RESET_ALL}")

    random_choose = random.choice(options)
    print(f"Комп'ютер обрав: {Fore.YELLOW}{random_choose}{Style.RESET_ALL}")
    result = (game_choose, random_choose)
    match result:
        case (choice, computer_choice) if choice == computer_choice:
            print(f"{Back.YELLOW}{Fore.BLACK}Нічия!{Style.RESET_ALL}")
        case ('камінь', 'ножиці') | ('ножиці', 'папір') | ('папір', 'камінь'):
            print(f"{Back.GREEN}{Fore.BLACK}Ви виграли!{Style.RESET_ALL}")
        case _:
            print(f"{Back.RED}{Fore.BLACK}Ви програли!{Style.RESET_ALL}")


def guess_number():
    """Гра вгадай число"""
    init(autoreset=True)
    attempts = 0
    guessed = False
    your_range = int(input("Введіть до якого числа будемо вгадувати: "))
    guessed_number = random.randint(1, your_range)
    print(f"{Fore.BLUE}Загадано число від 1 до {your_range}. Спробуйте вгадати!{Style.RESET_ALL}")
    while not guessed:
        your_attempt = input("Ваша спроба: ")
        if your_attempt.isdigit():
            your_attempt = int(your_attempt)
        else:
            print(f"{Fore.RED} Будь ласка, введіть ціле число! {Style.RESET_ALL}")
            continue
        attempts += 1
        if your_attempt < guessed_number:
            print("Загадане число більше!")
        elif your_attempt > guessed_number:
            print("Загадане число менше!")
        else:
            guessed = True
            print(f"{Fore.GREEN}Ви вгадали! {Style.RESET_ALL}\nЗагадане число було: "
                  f"{Fore.GREEN}{guessed_number}{Style.RESET_ALL}. Кількість ваших спроб: "
                  f"{Fore.GREEN}{attempts}{Style.RESET_ALL}")


def pole_chudes():
    """Гра Поле Чудес"""
    init(autoreset=True)

    text_dict = {
        "програмування": "Галузь знань, що вивчає створення комп'ютерних програм.",
        "комп'ютер": "Електронний пристрій для обробки інформації.",
        "алгоритм": "Послідовність дій для розв'язання задачі.",
        "клавіатура": "Пристрій для введення інформації у комп'ютер.",
        "проєкт": "Задуманий і розроблений план роботи.",
        "термінал": "Програмне вікно, що імітує інтерфейс командного рядка.",
        "компілятор": "Програма, що перетворює вихідний код в машинний.",
        "бібліотека": "Набір готових функцій та інструментів для використання в коді.",
        "репозиторій": "Місце для зберігання і спільного керування версіями коду.",
        "синтаксис": "Набір правил, що визначає структуру програми.",
        "дебагінг": "Процес пошуку та виправлення помилок у коді.",
        "фреймворк": "Каркас, що спрощує розробку програмних додатків.",
        "функція": "Іменований блок коду, який виконує певну дію.",
        "змінна": "Місце в пам'яті для зберігання даних.",
        "інтерфейс": "Точка взаємодії між користувачем і програмою.",
        "коментар": "Текст у коді, який ігнорується компілятором і призначений для людей.",
        "об'єкт": "Екземпляр класу в об'єктно-орієнтованому програмуванні.",
        "сценарій": "Файл з кодом, що виконується інтерпретатором послідовно.",
        "цикл": "Конструкція, що повторює виконання коду кілька разів.",
        "збірка": "Процес перетворення програмного коду на готовий продукт."
    }

    random_choice, description = random.choice(list(text_dict.items()))
    print(f"{Fore.GREEN}{description}")
    board_with_word_list = ['_'] * len(random_choice)
    guessed_letters = []
    while '_' in board_with_word_list:
        print(f"\nСлово: {Fore.BLUE}{' '.join(board_with_word_list)}")
        user_input = input("Введіть букву або ціле слово: ").lower()
        if not user_input.isalpha() and not "'" in user_input:
            print(f"{Fore.RED}Некоректний ввід. Будь ласка, введіть букву або слово.")
            continue
        if user_input == random_choice:
            print(f"{Fore.GREEN}Вітаю! Ви вгадали ціле слово і це справді "
                  f"{Fore.BLUE}{random_choice}!")
            break
        elif len(user_input) == 1:
            if user_input in guessed_letters:
                print(f"{Fore.YELLOW}Цю літеру '{user_input}' ви вже вводили. Спробуйте іншу.")
                continue
            guessed_letters.append(user_input)
            if user_input in random_choice:
                print(f"{Fore.CYAN}Так, літера '{user_input}' є в слові!")
                for position, letter in enumerate(random_choice):
                    if letter == user_input:
                        board_with_word_list[position] = user_input
            else:
                print(f"{Fore.RED}На жаль, літери '{user_input}' у слові немає.")
        else:
            print(f"{Fore.RED}Неправильне слово. Спробуйте ще раз.")
    else:
        print(f"{Fore.GREEN}Вітаю! Ви відгадали слово: {random_choice}!")
    print("Гру завершено!")


def get_joke_and_translate():
    """Беремо жарт з pyjokes і перекладаємо його українською"""
    translator = Translator(to_lang="uk")
    text_en = get_joke()
    print(f"{Fore.YELLOW} {text_en} {Style.RESET_ALL}")
    translation = translator.translate(text_en)
    text_uk = translation
    print(f"{Fore.BLUE} {text_uk} {Style.RESET_ALL}")


def show_menu():
    """Показуємо меню"""
    tprint("chat bot!")
    print(emoji.emojize(
        "\nПривіт! :hand_with_fingers_splayed: Я твій розважальний бот. "
        "Чим я можу допомогти:red_question_mark: "))
    print(emoji.emojize("1. Порадь фільм :film_frames:"))
    print(emoji.emojize("2. Порадь музику :musical_score:"))
    print(emoji.emojize("3. Порадь гру :video_game:"))
    print(emoji.emojize("4. Розвесели мене анекдотом :face_with_tears_of_joy:"))
    print(emoji.emojize("5. Розкажи цікаву історію :books:"))
    print(emoji.emojize("6. Пограймо в гру 'Вгадай число' :game_die:"))
    print(emoji.emojize("7. Пограймо в гру 'Камінь-ножиці-папір' "
                        ":rock: :scissors: :newspaper:"))
    print(emoji.emojize("8. Пограймо в гру 'Поле-чудес' :stop_button::stop_button:"
                        ":stop_button::stop_button:"))
    print(emoji.emojize("9. Вийти :door:"))


def main():
    """Головна функція"""
    while True:
        show_menu()
        choice = input("Твій вибір: ")

        match choice:
            case '1':
                category_films = input("Вибери жанр фільму "
                                       "(Фантастика/Комедія/Жахи/Драма/Бойовик): ").lower()
                if category_films in films:
                    print(f"Рекомендую подивитися: {Fore.BLUE}"
                          f"{random.choice(films[category_films])}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Вибач, такого жанру немає.{Style.RESET_ALL}")
            case '2':
                category_music = input("Вибери жанр музики "
                                       "(Поп/Рок/Хіп-хоп/Електронна/Джаз): ").lower()
                if category_music in music:
                    print(
                        f"Рекомендую послухати виконавця: {Fore.BLUE}"
                        f"{random.choice(music[category_music])}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Вибач, такого жанру немає.{Style.RESET_ALL}")
            case '3':
                category_games = input("Вибери жанр гри "
                                       "(Рольові/Шутери/Симулятори/Пригоди/Стратегії): ").lower()
                if category_games in games:
                    print(f"Рекомендую пограти: "
                          f"{Fore.BLUE}{random.choice(games[category_games])}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED} Вибач, такого жанру немає.{Style.RESET_ALL}")
            case '4':
                get_joke_and_translate()
            case '5':
                print("Цікавий факт:")
                print(f"{Fore.LIGHTGREEN_EX} {random.choice(stories)} {Style.RESET_ALL}")
            case '6':
                guess_number()
            case '7':
                game_rock_paper()
            case '8':
                pole_chudes()
            case '9':
                print(emoji.emojize(f"{Fore.GREEN} До зустрічі! "
                                    f":hand_with_fingers_splayed:{Style.RESET_ALL}"))
                break
            case _:
                print("Неправильний вибір, спробуй ще раз.")


main()
