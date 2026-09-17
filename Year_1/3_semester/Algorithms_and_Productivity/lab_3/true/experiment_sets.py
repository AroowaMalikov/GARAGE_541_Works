from time import perf_counter
from random import random, randrange, seed
from structures import SortedArraySet, UnsortedArraySet

# Размеры множеств для эксперимента
SIZES = [10**k for k in range(2, 6)]
CALLS = 2000  # количество запросов в каждой серии

# Доли операций (add, remove, contains) в серии — в сумме дают 1
MIXES = [
    (0.8, 0.1, 0.1),
    (0.4, 0.3, 0.3),
    (0.1, 0.1, 0.8),
    (0.34, 0.33, 0.33),
]


def weighted_query(rng_value: float, shares) -> str:
    """Выбирает вид запроса по случайному числу и заданным долям.

    Свой ГПСЧ-подход: одно равномерное число разбивает отрезок [0, 1)
    на части пропорционально долям операций.
    """
    border = 0.0
    for op, share in zip(("add", "remove", "contains"), shares):
        border += share
        if rng_value < border:
            return op
    return "contains"


def run_series(SetClass, n, shares):
    """Выполняет серию из CALLS запросов и возвращает время работы в секундах."""
    s = SetClass()
    # Предзаполняем половину множества, чтобы remove/contains что-то находили
    for _ in range(n // 2):
        s.add(randrange(-n, n))

    milestone1 = perf_counter()
    for _ in range(CALLS):
        op = weighted_query(random(), shares)
        value = randrange(-n, n)
        if op == "add":
            s.add(value)
        elif op == "remove":
            s.remove(value)
        else:
            s.contains(value)
    return perf_counter() - milestone1


def main():
    seed(42)  # одинаковые серии для обеих реализаций
    print(f"{'N':<8} | {'Доли add/remove/contains':<26} | {'Sorted (мс)':<12} | {'Unsorted (мс)':<12}")
    print("-" * 70)

    for n in SIZES:
        for shares in MIXES:
            # Одинаковая последовательность запросов для обеих структур
            seed(42)
            t_sorted = run_series(SortedArraySet, n, shares)
            seed(42)
            t_unsorted = run_series(UnsortedArraySet, n, shares)

            mix_str = "/".join(f"{s:.2f}" for s in shares)
            print(f"{n:<8} | {mix_str:<26} | {t_sorted*1000:<12.4f} | {t_unsorted*1000:<12.4f}")
        print("-" * 70)


if __name__ == "__main__":
    main()
