from numpy import minimum


def minimumSwaps(arr):
    arr = [a-1 for a in arr]
    swap = 0
    for i in range(len(arr)-1):
        while (arr[i] != i):
            temp = arr[i]
            arr[i], arr[temp] = arr[temp], arr[i]
            swap += 1
    return swap


arr = [7, 1, 3, 2, 4, 5, 6]

minimumSwaps(arr)
