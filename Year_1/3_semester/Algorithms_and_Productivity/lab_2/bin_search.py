def bin_search(arr, num):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Находим середину текущего диапазона
        mid = (left + right) // 2

        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            # Ищем в левой половине
            right = mid - 1
        else:
            # Ищем в правой половине
            left = mid + 1

    # Если элемент не найден
    return -1