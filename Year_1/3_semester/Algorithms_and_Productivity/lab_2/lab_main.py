from bubblesort import bubblesort
from heapsort import heapsort
from insertion import insertion
from bin_search import bin_search
from time import time
from random import randint

n = 1000 # Размер массива
k_max = 1000 # Максимальное количество поисковых запросов

'''Заполнение массива'''
arr_original = []
arr_original = insertion(arr_original, n)

print(f"{'K':<6} | {'t_послед (мс)':<14} | {'t_кв (мс)':<14} | {'t_быстр (мс)':<14} | {'t_встр (мс)':<14}")
print("-" * 75)

for k in range(10, k_max + 1, 50):
    '''Последовательный поиск'''
    arr_seq = arr_original.copy()
    milestone1 = time()
    for _ in range(k):
        target = randint(-n, n)
        for item in arr_seq:
            if item == target:
                break
    milestone2 = time()
    t_послед = (milestone2 - milestone1) * 1000

    '''Квадратичная сортировка + K поисков'''
    arr_quad = arr_original.copy()
    milestone1 = time()
    sorted_arr_quad, _ = bubblesort(arr_quad)
    for _ in range(k):
        target = randint(-n, n)
        bin_search(sorted_arr_quad, target)
    milestone2 = time()
    t_кв = (milestone2 - milestone1) * 1000

    '''Быстрая сортировка + K поисков'''
    arr_quick = arr_original.copy()
    milestone1 = time()
    sorted_arr_quick, _ = heapsort(arr_quick)
    for _ in range(k):
        target = randint(-n, n)
        bin_search(sorted_arr_quick, target)
    milestone2 = time()
    t_быстр = (milestone2 - milestone1) * 1000

    '''Встроенная сортировка + K поисков'''
    arr_int = arr_original.copy()
    milestone1 = time()
    sorted_arr_int = sorted(arr_int)
    for _ in range(k):
        target = randint(-n, n)
        bin_search(sorted_arr_int, target)
    milestone2 = time()
    t_встр = (milestone2 - milestone1) * 1000

    print(f"{k:<6} | {t_послед:<14.4f} | {t_кв:<14.4f} | {t_быстр:<14.4f} | {t_встр:<14.4f}")