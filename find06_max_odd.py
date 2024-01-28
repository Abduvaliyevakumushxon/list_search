def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    a=[]
    for i in data:
        if i%2==1:
            a.append(i)
    if len(a)==0:
        return -1
    mx=a[0]
    for d in a:
        if mx<d:
            mx=d
    
    return mx
print(find_max_odd([11, 8, 3, 8, 5]))