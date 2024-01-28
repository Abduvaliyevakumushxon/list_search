def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    s=[]
    for i in data:
        if i%2==1:
            s.append(i)
    if len(s)==0:
        return -1
    mn=s[0]
    for a in s:
        if mn>a:
            mn=a
    
    return mn
print(find_min_odd( [1, 8, 2, 8, 5]))

