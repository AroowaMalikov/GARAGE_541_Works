# Описание классов


class Actor:
    def __init__(self, surname, name, films_amount, sum_fee) -> None:
        # Конструктор класса.
        self.surname = surname
        self.name = name
        self.films_amount = films_amount
        self.sum_fee = sum_fee


    def enter(self):
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        films_amount = input('Введите количество фильмов: ')
        sum_fee = input('Введите суммарный гонорар: ')
        self.surname = surname
        self.name = name
        self.films_amount = films_amount
        self.sum_fee = sum_fee


    def check(self) -> None:
        """
        Вывод информации об актере
        """
        print(f'{self.surname:<20} | '
              f'{self.name:<15} | '
              f'{self.films_amount:>5} | '
              f'{self.sum_fee:>10.2f}')


class ListOfActors:
    """
    Список актеров
    """
    N_MAX = 12
    def __init__(self, actors=set()):
        self.actors = actors


    def insert(self, actor):
        if len(self.actors) == self.N_MAX:
            return 'Невозможно добавить 13-ый элемент'
        else:
            self.actors.append(actor)


    def delete(self, name=None):
        if name == None:
            input('Введите имя удаляемого актера: ')
        for act in self.actors:
            if name == act[0]:
                
