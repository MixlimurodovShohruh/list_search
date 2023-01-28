def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    g=[]
    mx=0
    for i in data:
        if i%2==1:
            g.append(i)
    for c in g:
        if mx<c:
            mx=c
    return mx
print(find_max_odd([11, 7, 5, 4, 9]))