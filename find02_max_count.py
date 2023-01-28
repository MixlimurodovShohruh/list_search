def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    mx=data[0]
    for i in data:
        if mx<i:
            mx=i
    return data.count(mx)
print(find_max_count([1, 8, 3, 8, 5]))
    