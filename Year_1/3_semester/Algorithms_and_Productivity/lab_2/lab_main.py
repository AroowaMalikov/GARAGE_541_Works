from bubblesort import bubblesort
from heapsort import heapsort
from insertion import insertion
from bin_search import bin_search
from time import time
from random import randint

# --- Исходные параметры ---
n = 10
k_max = 50

'''Заполнение массива'''
arr_original = []
arr_original = insertion(arr_original, n)

# --- Экспериментальная часть ---

print(f"{'K (запросы)':<10} | {'t_послед (мс)':<15} | {'t_кв (мс)':<15} | {'t_быстр (мс)':<15} | {'t_встр (мс)':<15}")
print("-" * 85)

for k in range(10, k_max + 1, 50):
    # 1. Последовательный поиск (без сортировки)
    arr_seq = arr_original.copy()
    start = time()
    for _ in range(k):
        target = randint(-n, n)
        # Простой линейный поиск
        found = False
        for item in arr_seq:
            if item == target:
                found = True
                break
    t_seq = (time() - start) * 1000

    # 2. Квадратичная сортировка + K двоичных поисков
    arr_quad = arr_original.copy()
    start = time()
    sorted_arr_quad, _ = bubblesort(arr_quad) # Получаем отсортированный массив
    for _ in range(k):
        target = randint(-n, n)
        bin_search(sorted_arr_quad, target)
    t_quad = (time() - start) * 1000

    # 3. Быстрая (пирамидальная) сортировка + K двоичных поисков
    arr_quick = arr_original.copy()
    start = time()
    sorted_arr_quick, _ = heapsort(arr_quick)
    for _ in range(k):
        target = randint(-n, n)
        bin_search(sorted_arr_quick, target)
    t_quick = (time() - start) * 1000

    # 4. Встроенная сортировка + K двоичных поисков
    arr_int = arr_original.copy()
    start = time()
    sorted_arr_int = sorted(arr_int)
    for _ in range(k):
        target = randint(-n, n)
        bin_search(sorted_arr_int, target)
    t_integrated = (time() - start) * 1000

    print(f"{k:<10} | {t_seq:<15.4f} | {t_quad:<15.4f} | {t_quick:<15.4f} | {t_integrated:<15.4f}")
