def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """

    mn=data[0]
    for m in data:
        if mn>m:
            mn=m
    return mn
print(find_min(data=[1,2,-3,4,5]))