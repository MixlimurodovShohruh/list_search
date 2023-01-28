def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    f=[]
    for i in data:
        if i%2==1:
            f.append(i)
    min=f[0]
    for g in f:
        if min>g:
            min=g

    return min
print(find_min_odd([7, 8, 4, 3, 5]))

