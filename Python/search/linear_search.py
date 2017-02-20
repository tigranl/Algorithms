def search(values, target):
    for item in values:
        if item == target:
            return values.index(item)
        if item > target:
            return
