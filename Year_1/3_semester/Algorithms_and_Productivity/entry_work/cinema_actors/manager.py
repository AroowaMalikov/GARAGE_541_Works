"""
Сортировка, фильтрация и преобразование гонорара для «Киноактеров».
"""

# Курс: 1 доллар = EURO_RATE евро
EURO_RATE = 0.93

# Поля, по которым возможна сортировка: (номер, название, атрибут)
SORT_FIELDS = [
    (1, 'Фамилия', 'surname'),
    (2, 'Имя', 'name'),
    (3, 'Количество фильмов', 'films_amount'),
    (4, 'Гонорар', 'sum_fee'),
]


def sort_actors(actor_list, field_number: int) -> None:
    """Отсортировать список актеров по выбранному полю (на месте).

    field_number -- номер поля из SORT_FIELDS (1..4).
    """
    for num, title, attr in SORT_FIELDS:
        if num == field_number:
            actor_list.actors.sort(key=lambda actor: getattr(actor, attr))
            print(f'Список отсортирован по полю «{title}».')
            return
    print('Невозможно отсортировать: выбрано неверное поле.')


def filter_by_fee(actor_list, min_fee: float) -> None:
    """Вывести актеров, чей гонорар не менее min_fee."""
    selected = [actor for actor in actor_list.actors
                if actor.sum_fee >= min_fee]
    if not selected:
        print(f'Нет актеров с гонораром не менее {min_fee:.2f} млн долл.')
        return
    print(f'Актеры с гонораром не менее {min_fee:.2f} млн долл.:')
    print_table_header()
    for actor in selected:
        actor.check()


def print_fees_in_euro(actor_list) -> None:
    """Вывести гонорары всех актеров в Евро (список не меняется)."""
    if not actor_list.actors:
        print('Список пуст: выводить гонорары не в чем.')
        return
    print('Гонорары актеров в Евро:')
    print(f'{"Фамилия":<20} | {"Имя":<15} | '
          f'{"Гонорар, млн евро":>17}')
    print('-' * 60)
    for actor in actor_list.actors:
        fee_euro = actor.sum_fee * EURO_RATE
        print(f'{actor.surname:<20} | {actor.name:<15} | '
              f'{fee_euro:>17.2f}')


def print_table_header() -> None:
    """Печать шапки основной таблицы."""
    print(f'{"Фамилия":<20} | {"Имя":<15} | '
          f'{"Фильмов":>7} | {"Гонорар, млн$":>13}')
    print('-' * 66)