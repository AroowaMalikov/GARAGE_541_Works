from bubblesort import bubblesort
from heapsort import heapsort
from insertion import insertion
from bin_search import bin_search
from time import time
from random import randint

n = 10 # Размер массива
k = 100 # Количество поисковых запросов

'''Заполнение массива'''
arr = []
arr = insertion(arr, n)
arr_ = arr

'''Квадратичная сортировка'''
milestone1 = time()
bubblesort(arr)
milestone2 = time()
t_quad = milestone2 - milestone1

'''Быстрая сортировка'''
arr = arr_
milestone1 = time()
heapsort(arr)
milestone2 = time()
t_quick = milestone2 - milestone1

'''Встроенная сортировка Python'''
arr = arr_
milestone1 = time()
arr = sorted(arr)
milestone2 = time()
t_integrated = milestone2 - milestone1

'''Запросы'''
results = []

for _ in range(1, k, 10):
    results.append(bin_search(arr, randint(-n, n)))

'''Результаты'''