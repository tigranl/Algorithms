def search(values, target):
    values = sorted(values)
    min = 0
    max = len(values) - 1
    while min <= max:
        mid = (min + (max - min) * (target - values[min])) // \
                    (values[max] - values[min])
        if values[mid] == target:
            return mid
