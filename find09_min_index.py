def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    min=data[0]
    for i in data:
        if min>i:
            min=i
    return data.index(min)
print(find_min_index([12, 2, 5, 2, 7, 9, 1]))