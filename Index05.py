def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x=0
    if s[0].isdigit==true:
        x=x+1
    if s[1].isdigit==true:
        x=x+1
    if s[2].isdigit==true:
        x=x+1
    if s[3].isdigit==true:
        x=x+1
    if s[4].isdigit==true:
        x=x+1
    return x
print(main('12345'))