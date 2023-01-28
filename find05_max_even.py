def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    d=[]
    for i in data:
        if i%2==0:
            d.append(i)
    mx=d[0]
    for d in d:
        if mx<d:
            mx=d

    return mx
print(find_max_even([7, 6, 3, 4, 9]))
