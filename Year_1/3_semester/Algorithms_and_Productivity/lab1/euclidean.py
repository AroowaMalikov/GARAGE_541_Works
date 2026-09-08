import time
from random import randint

M = int(input('First input Num: '))
N = int(input('Second input Num: '))


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
    return (gcd ,milestone2 - milestone1, counter)


def gcd_rev_enum(M, N):
    milestone1 = time.time()
    gcd, num = 1, 1
    counter = 0
    while num > 0:
        counter += 1
        if M % num == 0 and N % num == 0:
            gcd = num
        num -= 1
    milestone2 = time.time()
    return (gcd ,milestone2 - milestone1, counter)


def gcd_euclidean(M, N):
    milestone1 = time.time()
    counter = 0
    if N >= M:
        counter += 1
        if M == 0:
            gcd = N
        gcd = gcd_euclidean(N % M, M)
    else:
        counter += 1
        if N == 0:
            gcd = M
        gcd = gcd_euclidean(N, M % N)
    milestone2 = time.time()
    return (gcd, milestone1 - milestone2, counter)

"""Research part"""

exp = int(input('Enter the amount of experiments: '))

u_border = 10 ** 5 #upper border of a random number
for _ in range(exp):
    N, M = randint(1, u_border), randint(1, u_border)
    