def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    max  = 0
    k = 0
    while k<len(list_num):
        if max<list_num[k]:
            max = list_num[k]
        k+=1
    return max
    

v = main([12, 2, 5, 2, 7, 9, 1])
print(v)