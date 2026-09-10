from random import randint


def insertion(arr, amount):
    for _ in range(amount):
        arr.append(randint(-amount, amount))
    return arr