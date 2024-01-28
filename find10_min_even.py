def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    a=[]
    for i in data:
        if i%2==0:
            a.append(i)
    if len(a)==0:
        return -1
    mn=a[0]
    for s in a:
        if mn>s:
            mn=s
    return mn 
print(find_min_even(data=[1, 8, 2, 8, 5]))

