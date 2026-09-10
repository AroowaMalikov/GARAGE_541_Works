# Описание класса


class Actor:
    def __init__(self, surname, name, films_amount, sum_fee) -> None:
        # Конструктор класса.
        self.surname = surname
        self.name = name
        self.films_amount = films_amount
        self.sum_fee = sum_fee
        pass


    def create() -> None:
        pass


    def read() -> None:
        pass


    def update() -> None:
        pass


    def delete() -> None:
        pass


    def check(self) -> None:
        """
        Вывод информации об актере
        """
        print(f'{self.surname:<20} | '
              f'{self.name:<15} | '
              f'{self.films_amount:>5} | '
              f'{self.sum_fee:>10.2f}')