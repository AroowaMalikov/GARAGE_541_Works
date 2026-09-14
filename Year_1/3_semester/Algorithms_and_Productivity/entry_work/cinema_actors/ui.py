"""
Консольный интерфейс программы «Киноактеры»: меню и ввод данных.
"""

from models import Actor
from manager import (SORT_FIELDS, sort_actors, filter_by_fee,
                     print_fees_in_euro, print_table_header)

MENU = """
================ Меню ================
1. Вывести всех актеров (таблица)
2. Выход
3. Добавить нового актера
4. Удалить актера (по номеру)
5. Сортировка по выбранному свойству
6. Фильтр: гонорар не менее указанного
7. Вывести гонорары всех актеров в Евро
=======================================
"""


def input_int(prompt: str):
    """Ввод целого числа. При ошибке возвращает None."""
    try:
        return int(input(prompt))
    except ValueError:
        print('Ошибка: нужно ввести целое число.')
        return None


def input_float(prompt: str):
    """Ввод вещественного числа. При ошибке возвращает None."""
    try:
        return float(input(prompt))
    except ValueError:
        print('Ошибка: нужно ввести число (например 12.5).')
        return None


def show_all(actor_list) -> None:
    """Пункт 1: вывод всех актеров в виде таблицы."""
    if not actor_list.actors:
        print('Список пуст.')
        return
    print(f'Всего актеров: {len(actor_list.actors)}.')
    print_table_header()
    for number, actor in enumerate(actor_list.actors, start=1):
        print(f'{number:>2}. ', end='')
        actor.check()


def add_actor(actor_list) -> None:
    """Пункт 3: добавление нового актера (данные вводит пользователь)."""
    surname = input('Введите фамилию: ').strip()
    name = input('Введите имя: ').strip()
    if not surname or not name:
        print('Ошибка: фамилия и имя не могут быть пустыми.')
        return
    films_amount = input_int('Введите количество фильмов: ')
    if films_amount is None:
        return
    if films_amount < 0:
        print('Ошибка: количество фильмов не может быть отрицательным.')
        return
    sum_fee = input_float('Введите суммарный гонорар (млн долл.): ')
    if sum_fee is None:
        return
    if sum_fee < 0:
        print('Ошибка: гонорар не может быть отрицательным.')
        return
    if actor_list.insert(Actor(surname, name, films_amount, sum_fee)):
        print(f'Актер {surname} {name} добавлен.')


def delete_actor(actor_list) -> None:
    """Пункт 4: удаление актера по его номеру в таблице."""
    if not actor_list.actors:
        print('Невозможно удалить элемент: список пуст.')
        return
    show_all(actor_list)
    number = input_int('Введите номер удаляемого актера: ')
    if number is None:
        return
    actor_list.delete(number)


def sort_menu(actor_list) -> None:
    """Пункт 5: сортировка по выбранному пользователем свойству."""
    print('По какому свойству отсортировать?')
    for num, title, _attr in SORT_FIELDS:
        print(f'  {num}. {title}')
    number = input_int('Введите номер свойства: ')
    if number is None:
        return
    sort_actors(actor_list, number)


def filter_menu(actor_list) -> None:
    """Пункт 6: фильтр по минимальному гонорару."""
    min_fee = input_float('Введите минимальный гонорар (млн долл.): ')
    if min_fee is None:
        return
    filter_by_fee(actor_list, min_fee)


def run(actor_list) -> None:
    """Главный цикл меню."""
    actions = {
        1: show_all,
        3: add_actor,
        4: delete_actor,
        5: sort_menu,
        6: filter_menu,
        7: print_fees_in_euro,
    }
    while True:
        print(MENU)
        choice = input_int('Выберите пункт меню: ')
        if choice is None:
            continue
        if choice == 2:
            print('Выход из программы. До свидания!')
            break
        action = actions.get(choice)
        if action is None:
            print(f'Пункта меню №{choice} не существует, повторите ввод.')
        else:
            action(actor_list)
