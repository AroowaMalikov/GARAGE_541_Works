import time

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
    return (gcd ,milestone2 - milestone1)


def gcd_rev_enum(M, N):
    milestone1 = time.time()
    gcd, num = 1, 
    counter = 0
    while num > 0:
        counter += 1
        if M % num == 0 and N % num == 0:
            gcd = num
        num -= 1
    milestone2 = time.time()
    return (gcd ,milestone2 - milestone1)