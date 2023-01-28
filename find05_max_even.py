def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    d=[]
    mx=0
    for i in data:
        if i%2==0:
            d.append(i)
    for d in d:
        if mx<d:
            mx=d

    return mx
print(find_max_even([7, 6, 3, 4, 9]))
