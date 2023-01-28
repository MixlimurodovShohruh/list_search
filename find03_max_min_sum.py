def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i=0
    mx=data[0]
    mn=data[0]
    while i<len(data):
        if mx<data[i]:
            mx=data[i]
        if mn>data[i]:
            mn=data[i]
        i+=1
    return mx+mn 
print(find_max_min_sum([1, 2, 3, 4, 5]))

