def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    d=[]

    for i in data:
        if i%2==0:
            d.append(i)
    min=d[0]
    for c in d:
        if min>c:
            min=c
    return min
print(find_min_even([1, 8, 2, 8, 5]))

