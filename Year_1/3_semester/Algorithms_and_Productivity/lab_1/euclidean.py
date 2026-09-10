import time
from random import randint


def gcd_enum(M, N):
    milestone1 = time.time()
    gcd, num = 1, 1
    counter = 0
    while num <= min(M, N):
        counter += 1
        if M % num == 0 and N % num == 0:
            gcd = num
        num += 1
    milestone2 = time.time()
    return (gcd, milestone2 - milestone1, counter)


def gcd_rev_enum(M, N):
    milestone1 = time.time()
    gcd, num = 1, min(M, N)
    counter = 0
    while num > 0:
        counter += 1
        if M % num == 0 and N % num == 0:
            gcd = num
            break
        num -= 1
    milestone2 = time.time()
    return (gcd ,milestone2 - milestone1, counter)


def gcd_euclidean(M, N):
    milestone1 = time.time()
    counter = 0
    a, b = M, N
    while b != 0:
        counter += 1
        a, b = b, a % b
    milestone2 = time.time()
    return (a, milestone2 - milestone1, counter)


"""Research part"""

exp = int(input('Enter the amount of experiments: '))

# Один список вместо девяти — удобнее
results = []

u_border = 10 ** 5
for _ in range(exp):
    N, M = randint(1, u_border), randint(1, u_border)
    
    r1 = gcd_enum(M, N)
    r2 = gcd_rev_enum(M, N)
    r3 = gcd_euclidean(M, N)
    
    results.append((M, N, r1, r2, r3))


# ============================================================
# ТАБЛИЦА 1: Детальный вывод по каждому эксперименту
# ============================================================

print("\n" + "=" * 100)
print(f"{'ДЕТАЛЬНЫЕ РЕЗУЛЬТАТЫ ЭКСПЕРИМЕНТОВ':^100}")
print("=" * 100)

header = (
    f"{'#':>3} | {'M':>6} {'N':>6} | "
    f"{'ENUM gcd':>8} {'time':>10} {'ops':>5} | "
    f"{'REV gcd':>8} {'time':>10} {'ops':>5} | "
    f"{'EUC gcd':>8} {'time':>10} {'ops':>5}"
)
separator = "-" * len(header)

print(header)
print(separator)

for i, (M, N, r1, r2, r3) in enumerate(results, 1):
    print(
        f"{i:>3} | {M:>6} {N:>6} | "
        f"{r1[0]:>8} {r1[1]:>10.6f} {r1[2]:>5} | "
        f"{r2[0]:>8} {r2[1]:>10.6f} {r2[2]:>5} | "
        f"{r3[0]:>8} {r3[1]:>10.6f} {r3[2]:>5}"
    )

print(separator)


# ============================================================
# ТАБЛИЦА 2: Средние значения
# ============================================================

avg_time1 = sum(r[2][1] for r in results) / exp
avg_ops1  = sum(r[2][2] for r in results) / exp

avg_time2 = sum(r[3][1] for r in results) / exp
avg_ops2  = sum(r[3][2] for r in results) / exp

avg_time3 = sum(r[4][1] for r in results) / exp
avg_ops3  = sum(r[4][2] for r in results) / exp

print("\n" + "=" * 70)
print(f"{'СВОДНАЯ ТАБЛИЦА (Средние значения по ' + str(exp) + ' эксп.)':^70}")
print("=" * 70)

header2 = (
    f"{'Algorithm':<25} | "
    f"{'Avg Time (s)':>12} | "
    f"{'Avg Ops':>10}"
)
separator2 = "-" * len(header2)

print(separator2)
print(header2)
print(separator2)
print(f"{'1. ENUM (1 to min)':<25} | {avg_time1:>12.6f} | {avg_ops1:>10.2f}")
print(f"{'2. REV ENUM (min to 1)':<25} | {avg_time2:>12.6f} | {avg_ops2:>10.2f}")
print(f"{'3. EUCLIDEAN':<25} | {avg_time3:>12.6f} | {avg_ops3:>10.2f}")
print(separator2)