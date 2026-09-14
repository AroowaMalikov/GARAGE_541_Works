from structures import *
from collections import deque
from generator import generator
import time
import random

MIN_LEN = 100 # минимальный размер массива
MAX_LEN = 10 ** 7 # максимальный размер массива
sizes = [10**k for k in range(MIN_LEN, MAX_LEN + 1)]

results = {}  # (n, имя структуры, операция) -> среднее время


import random
import time


def measure(func, n) -> float:
    """Возвращает среднее время CALLS вызовов функции func."""
    CALLS = 10  # количество вызовов для усреднения

    def choice() -> int:
        """Случайный индекс элемента"""
        return random.randrange(n)

    total = 0.0
    for _ in range(CALLS):
        milestone1 = time.perf_counter()
        i = choice()
        func(i)
        total += time.perf_counter() - milestone1
    return total / CALLS


for n in sizes:
    array_list, linked_list = generator(n)  # одинаковые по содержанию структуры размера n
    middle = n // 2

    for name, structure in (("ArrayList", array_list), ("DLinkedList", linked_list)):
        results[(n, name, "append")] = measure(structure.append, n)
        results[(n, name, "insert")] = measure(structure.insert, middle, n)
        results[(n, name, "get")] = measure(structure.get, middle)
        results[(n, name, "remove")] = measure(structure.remove, middle)