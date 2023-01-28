def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    min=data[0]
    for i in data:
        if min>i:
            min=i
    return data.count(min)
print(find_min_count([0, -4, 3, 9, -2, -4]))