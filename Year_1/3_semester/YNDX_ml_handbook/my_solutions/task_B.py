import numpy as np

def most_frequent(nums):
    """
    Find the most frequent value in an array
    :param nums: array of ints
    :return: the most frequent value
    """
    # Используем bincount для подсчета частоты каждого элемента
    counts = np.bincount(nums)
    # Находим индекс наиболее часто встречающегося элемента
    most_index = np.argmax(counts)
    return most_index
