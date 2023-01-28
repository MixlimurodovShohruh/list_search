def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    min=data[0]
    for i in data:
        if min>i:
            min=i
    return min
print(find_min( [1, 2, -3, 4, 5]))