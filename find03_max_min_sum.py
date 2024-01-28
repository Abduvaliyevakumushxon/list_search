def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    a=0
    max3=data[0]
    while a<len(data):
        if max3<data[a]:
            max3=data[a]
        a+=1
    

    mn=data[0]
    for m in data:
        if mn>m:
            mn=m
    return mn+max3
print(find_max_min_sum(data=[1, 2, 3, 4, 5]))
