def heapsort(arr):
    """
    Пирамидальная сортировка.
    """
    n = len(arr)
    comparisons = 0

    # Построение кучи
    for i in range(n // 2 - 1, -1, -1):
        while True:
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n:
                comparisons += 1
                if arr[l] > arr[largest]:
                    largest = l
            
            if r < n:
                comparisons += 1
                if arr[r] > arr[largest]:
                    largest = r

            if largest == i:
                break

            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest

    # Сортировка (извлечение элементов)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        i = 0

        while True:
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            # Аналогично считаем все попытки сравнения
            if l < n:
                comparisons += 1
                if arr[l] > arr[largest]:
                    largest = l
            
            if r < n:
                comparisons += 1
                if arr[r] > arr[largest]:
                    largest = r

            if largest == i:
                break

            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest

    return arr, comparisons