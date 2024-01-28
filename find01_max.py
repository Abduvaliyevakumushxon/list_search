def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    a=0
    max3=data[0]
    while a<len(data):
        if max3<data[a]:
            max3=data[a]
        a+=1
    return max3
print(find_max(data=[1,2,3,4,5]))

    