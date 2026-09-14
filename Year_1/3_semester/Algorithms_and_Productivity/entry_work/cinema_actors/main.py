"""
Точка входа в программу «Киноактеры» (вариант 10).

При запуске список уже содержит 5 демо-актеров (hard-code).
"""

from models import Actor, ListOfActors
from ui import run

# 5 демонстрационных актеров: (фамилия, имя, кол-во фильмов, гонорар млн$)
DEMO_ACTORS = [
    ('Нортон', 'Эдвард', 42, 80.5),
    ('Дефо', 'Уиллем', 110, 40.0),
    ('Джоли', 'Анджелина', 65, 120.0),
    ('Уиллис', 'Брюс', 100, 250.0),
    ('Робертс', 'Джулия', 55, 200.0),
]


def create_demo_list() -> ListOfActors:
    """Создать список актеров и наполнить его демо-данными."""
    actor_list = ListOfActors()
    for surname, name, films, fee in DEMO_ACTORS:
        actor_list.insert(Actor(surname, name, films, fee))
    return actor_list


def main() -> None:
    """Запуск программы."""
    actor_list = create_demo_list()
    run(actor_list)


if __name__ == '__main__':
    main()
