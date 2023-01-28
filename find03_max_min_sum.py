def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    mx=data[0]
    for i in data:
        if mx<i:
            mx=i
    min=data[0]
    for v in data:
        if min>=i:
            min=v
    return mx+min
print(find_max_min_sum([2, 7, 3, 4, 9]))

