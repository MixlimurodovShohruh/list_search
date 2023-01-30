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
    if len(d)==0:
        return -1
    mx=data[0]
    for d in d:
        if mx<d:
            mx=d

    return mx
print(find_max_even([1, 4, 3, 8, 5]))
