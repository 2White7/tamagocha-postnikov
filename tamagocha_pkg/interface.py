"""Консольний інтерфейс для взаємодії з тамагочі."""

MENU_TEXT = (
    "Добро пожаловать домой! Что вы хотите сделать, хозяин?\n"
    "Посмотреть статус - 1\n"
    "Покормить - 2\n"
    "Отправить в кровать - 3\n"
    "Навести порядки и покупать - 4\n"
    "Отправить на прогулку - 5\n"
    "Отправить в БДСМ клуб - 6\n"
    "Выйти - 7\n"
)

ACTIONS = {
    1: lambda pet: pet.status_text(),
    2: lambda pet: pet.feed(),
    3: lambda pet: pet.sleep(),
    4: lambda pet: pet.clean(),
    5: lambda pet: pet.socialize(),
    6: lambda pet: pet.bdsm_club(),
}


def run_turn(pet, choice):
    """Виконує одну дію меню та повертає текст-відповідь."""
    if choice == 7:
        return None
    action = ACTIONS.get(choice)
    if action is None:
        return "Я не понимаю, повторите еще раз."
    text = action(pet)
    death = pet.death_message()
    if death:
        text += "\n" + death
    return text


def read_choice(input_func=input):
    """Зчитує вибір користувача та перевіряє, що це число у діапазоні 1-7."""
    raw = input_func()
    try:
        choice = int(raw)
    except ValueError:
        return None
    if choice < 1 or choice > 7:
        return None
    return choice


def game_loop(pet, input_func=input, print_func=print):
    print_func(MENU_TEXT)
    while True:
        choice = read_choice(input_func)
        if choice is None:
            print_func("Некорректный ввод, введите число от 1 до 7.")
            continue
        result = run_turn(pet, choice)
        if choice == 7:
            break
        print_func(result)
    return pet
