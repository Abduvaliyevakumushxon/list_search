def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    mx=data[0]
    for i in data:
        if mx<i:
            mx=i

    return data.index(mx)
print(find_max_even(data=[1,2,3,4,5]))
