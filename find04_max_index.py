def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    mx=0
    for i in data:
        if mx<i:
            mx=i

    return data.index(mx)
print(find_max_index([6, 8, 7, 4, 0]))
