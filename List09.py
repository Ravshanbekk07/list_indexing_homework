def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i = 1
    while i <len(list1):
        if list1[i] != list1[0]:
            return False
            



        i+=1
    return True
v = main(['x', 'x', 'y', 'y', 'z'])
print(v)