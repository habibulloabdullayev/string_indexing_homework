def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    x = s[0] + s[-1]
    return x
print(main('good'))
print(main('uz'))