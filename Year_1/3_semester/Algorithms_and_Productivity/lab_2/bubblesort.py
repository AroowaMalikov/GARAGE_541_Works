def bubblesort(arr):
    n = len(arr)
    counter = 0
    for i in range(n):
        for j in range(0, n-i-1):
            counter += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, counter