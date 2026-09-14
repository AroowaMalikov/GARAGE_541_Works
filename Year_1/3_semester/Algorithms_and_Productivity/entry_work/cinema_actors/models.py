"""
Описание классов программы «Киноактеры».

Actor        -- один актер (4 свойства).
ListOfActors -- список актеров с ограничением N_MAX.
"""

# Максимальное количество элементов в списке
N_MAX = 12


class Actor:
    """Актер: фамилия, имя, количество фильмов, гонорар (млн долл.)."""

    def __init__(self, surname: str, name: str,
                 films_amount: int, sum_fee: float) -> None:
        self.surname = surname
        self.name = name
        self.films_amount = films_amount
        self.sum_fee = sum_fee

    def check(self) -> None:
        """Печать информации об актере одной строкой (без шапки таблицы)."""
        print(f'{self.surname:<20} | '
              f'{self.name:<15} | '
              f'{self.films_amount:>5} | '
              f'{self.sum_fee:>10.2f}')


class ListOfActors:
    """Список актеров, хранит не более N_MAX элементов."""

    def __init__(self) -> None:
        self.actors: list[Actor] = []

    def insert(self, actor: Actor) -> bool:
        """Добавить актера в конец списка.

        Возвращает True, если добавление прошло успешно,
        False -- если список уже заполнен.
        """
        if len(self.actors) >= N_MAX:
            print(f'Невозможно добавить элемент: '
                  f'достигнут лимит N_MAX = {N_MAX}.')
            return False
        self.actors.append(actor)
        return True

    def delete(self, number: int) -> bool:
        """Удалить актера по его номеру в списке (нумерация с 1).

        Возвращает True, если удаление прошло успешно,
        False -- если список пуст или номер неверный.
        """
        if not self.actors:
            print('Невозможно удалить элемент: список пуст.')
            return False
        if not 1 <= number <= len(self.actors):
            print(f'Невозможно удалить элемент: '
                  f'номер должен быть от 1 до {len(self.actors)}.')
            return False
        removed = self.actors.pop(number - 1)
        print(f'Удален актер: {removed.surname} {removed.name}.')
        return True