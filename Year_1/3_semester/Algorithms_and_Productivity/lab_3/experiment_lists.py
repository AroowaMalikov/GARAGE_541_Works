from time import perf_counter
from random import randrange
from structures import ArrayList, DLinkedList

# Размеры структур для эксперимента
SIZES = [10**k for k in range(2, 7)]
CALLS = 10  # количество вызовов для усреднения


def fill(structure, n):
    """Заполняет структуру n случайными числами."""
    for _ in range(n):
        structure.append(randrange(-n, n))


def measure(func, *args) -> float:
    """Возвращает среднее время CALLS вызовов функции func."""
    total = 0.0
    for _ in range(CALLS):
        milestone1 = perf_counter()
        func(*args)
        total += perf_counter() - milestone1
    return total / CALLS


def run_builtins(n):
    """Замеряет встроенные аналоги: list (ArrayList) и deque (LinkedList)."""
    from collections import deque
    arr = list(range(n))
    deq = deque(range(n))
    middle = n // 2

    for name, structure in (("list (встр. ArrayList)", arr), ("deque (встр. LinkedList)", deq)):
        milestone1 = perf_counter()
        structure.append(n)
        t_append = perf_counter() - milestone1

        milestone1 = perf_counter()
        structure.insert(middle, n)
        t_insert = perf_counter() - milestone1

        milestone1 = perf_counter()
        _ = structure[middle]
        t_get = perf_counter() - milestone1

        milestone1 = perf_counter()
        del structure[middle]
        t_remove = perf_counter() - milestone1

        print(f"{n:<9} | {name:<24} | {t_append*1000:<10.5f} | {t_insert*1000:<10.5f} | "
              f"{t_get*1000:<10.7f} | {t_remove*1000:<10.5f}")


def main():
    print(f"{'N':<9} | {'Структура':<24} | {'append (мс)':<12} | {'insert (мс)':<12} | "
          f"{'get (мс)':<12} | {'remove (мс)':<12}")
    print("-" * 105)

    for n in SIZES:
        # Самописные структуры одинакового содержания
        array_list = ArrayList()
        linked_list = DLinkedList()
        fill(array_list, n)
        fill(linked_list, n)
        middle = n // 2

        for name, structure in (("ArrayList (свой)", array_list), ("DLinkedList (свой)", linked_list)):
            t_append = measure(structure.append, n)
            t_insert = measure(structure.insert, middle, n)
            t_get = measure(structure.get, middle)
            t_remove = measure(structure.remove, middle)

            print(f"{n:<9} | {name:<24} | {t_append*1000:<10.5f} | {t_insert*1000:<10.5f} | "
                  f"{t_get*1000:<10.7f} | {t_remove*1000:<10.5f}")

        run_builtins(n)
        print("-" * 105)


if __name__ == "__main__":
    main()
