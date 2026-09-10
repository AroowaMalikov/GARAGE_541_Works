import time
from math import sqrt
from random import randint

exp = int(input('Enter the amount of experiments:'))


def is_prime_enum(N):
    milestone1 = time.time()
    num = 2
    counter = 0
    while num < N:
        counter += 1
        if N % num == 0:
            milestone2 = time.time()
            return (False, milestone2 - milestone1, counter)
        num += 1
    milestone2 = time.time()
    return (True, milestone2 - milestone1, counter)

# result1 = is_prime_enum(N)

def is_prime_enum_odd(N):
    milestone1 = time.time()
    counter = 1
    if N != 2 and N % 2 == 0:
        milestone2 = time.time()
        return (False, milestone2 - milestone1, counter)
    
    num = 3
    while num < N:
        counter += 1
        if N % num == 0:
            milestone2 = time.time()
            return (False, milestone2 - milestone1, counter)
        num += 2
    
    milestone2 = time.time()
    return (True, milestone2 - milestone1, counter)

# result2 = is_prime_enum_odd(N)


def is_prime_enum_sqrt(N):
    milestone1 = time.time()
    num = 2
    counter = 0
    while num <= sqrt(N):
        counter += 1
        if N % num == 0:
            milestone2 = time.time()
            return (False, milestone2 - milestone1, counter)
        num += 1
    milestone2 = time.time()
    return (True, milestone2 - milestone1, counter)

# result3 = is_prime_enum_sqrt(N)


def is_prime_enum_sqrt_odd(N):
    milestone1 = time.time()

    counter = 1
    if N % 2 == 0:
        milestone2 = time.time()
        return (False, milestone2 - milestone1, 1)
    
    num = 3
    while num * num <= N:
        counter += 1
        if N % num == 0:
            milestone2 = time.time()
            return (False, milestone2 - milestone1, counter)
        num += 2
    
    milestone2 = time.time()
    return (True, milestone2 - milestone1, counter)

# result4 = is_prime_enum_sqrt_odd(N)

'''
Вывод для одного эксперимента:

# Заголовок таблицы
header = f"{'#':<3} {'Algorithm':<35} {'Result':<8} {'Time (s)':<12} {'Operations':<10}"
separator = "-" * len(header)

print(separator)
print(header)
print(separator)
print(f"{'1':<3} {'ENUMERATING':<35} {str(result1[0]):<8} {result1[1]:<12.6f} {result1[2]:<10}")
print(f"{'2':<3} {'ENUMERATING ONLY ODD':<35} {str(result2[0]):<8} {result2[1]:<12.6f} {result2[2]:<10}")
print(f"{'3':<3} {'ENUMERATING TILL SQRT':<35} {str(result3[0]):<8} {result3[1]:<12.6f} {result3[2]:<10}")
print(f"{'4':<3} {'ENUMERATING ONLY ODD TILL SQRT':<35} {str(result4[0]):<8} {result4[1]:<12.6f} {result4[2]:<10}")
print(separator)
'''

results = []

u_border = 10 ** 5
for _ in range(exp):
    N = randint(1, u_border)
    result1 = is_prime_enum(N)
    result2 = is_prime_enum_odd(N)
    result3 = is_prime_enum_sqrt(N)
    result4 = is_prime_enum_sqrt_odd(N)
    results.append((N, result1, result2, result3, result4))


'''ВЫВОД РЕЗУЛЬАТОВ'''

# Сортируем по N для наглядности зависимости
results.sort(key=lambda x: x[0])

# Заголовок
header = (
    f"{'N':>10} | "
    f"{'ENUM time':>10} {'ENUM ops':>8} | "
    f"{'ODD time':>10} {'ODD ops':>8} | "
    f"{'SQRT time':>10} {'SQRT ops':>8} | "
    f"{'SQRT_ODD time':>12} {'SQRT_ODD ops':>10}"
)
separator = "-" * len(header)

print(separator)
print(header)
print(separator)

for N, r1, r2, r3, r4 in results:
    print(
        f"{N:>10} | "
        f"{r1[1]:>10.6f} {r1[2]:>8} | "
        f"{r2[1]:>10.6f} {r2[2]:>8} | "
        f"{r3[1]:>10.6f} {r3[2]:>8} | "
        f"{r4[1]:>12.6f} {r4[2]:>10}"
    )

print(separator)


'''Анализ и средние значения:'''


# Вычисляем средние значения для каждого алгоритма
avg_time1 = sum(r1[1] for _, r1, _, _, _ in results) / exp
avg_ops1  = sum(r1[2] for _, r1, _, _, _ in results) / exp

avg_time2 = sum(r2[1] for _, _, r2, _, _ in results) / exp
avg_ops2  = sum(r2[2] for _, _, r2, _, _ in results) / exp

avg_time3 = sum(r3[1] for _, _, _, r3, _ in results) / exp
avg_ops3  = sum(r3[2] for _, _, _, r3, _ in results) / exp

avg_time4 = sum(r4[1] for _, _, _, _, r4 in results) / exp
avg_ops4  = sum(r4[2] for _, _, _, _, r4 in results) / exp

# Формируем таблицу средних значений
print("\n" + "=" * 65)
print(f"       СВОДНАЯ ТАБЛИЦА (Средние значения по {exp} эксп.):")
print("=" * 65)

header = (
    f"{'Algorithm':<33} | "
    f"{'Avg Time (s)':>12} | "
    f"{'Avg Operations':>14}"
)
separator = "-" * len(header)

print(separator)
print(header)
print(separator)
print(f"{'1. ENUMERATING':<33} | {avg_time1:>12.6f} | {avg_ops1:>14.2f}")
print(f"{'2. ENUMERATING ONLY ODD':<33} | {avg_time2:>12.6f} | {avg_ops2:>14.2f}")
print(f"{'3. ENUMERATING TILL SQRT':<33} | {avg_time3:>12.6f} | {avg_ops3:>14.2f}")
print(f"{'4. ENUMERATING ONLY ODD TILL SQRT':<33} | {avg_time4:>12.6f} | {avg_ops4:>14.2f}")
print(separator)