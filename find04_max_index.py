def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    mx=data[0]
    for i in data:
        if mx<i:
            mx=i

    return data.index(mx)
print(find_max_index(data=[1,2,3,4,5]))
