def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    mn=data[0]
    for i in data:
        if mn>i:
            mn=i
    return data.count(mn) 
print(find_min_count(data=[1, 8, 3, 8, 5]))
