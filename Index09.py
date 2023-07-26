def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    s=int(s)
    if s!=int(s):
        print('-1')
    return s
print(main(4))
print(main('k'))