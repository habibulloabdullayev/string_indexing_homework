def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x=s.count('*')
    if x==0:
        print('false')
        return ' '
    return x
print(main('4*34'))
print(main('good'))