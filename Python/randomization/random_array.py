from random import randint


def rand(arr):
    for i in range(len(arr)):
        j = randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
