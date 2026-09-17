from structures import ArrayList, DLinkedList
from random import randint

def generator(n: int):
    """Создаёт ArrayList и DLinkedList одинакового содержания"""
    array_list = ArrayList()
    linked_list = DLinkedList()
    for _ in range(n):
        num = randint(-n, n)
        array_list.append(num)
        linked_list.append(num)
    return array_list, linked_list