def valid_parentheses(string):
    """
    Write a function called that takes a string of parentheses,
    and determines if the order of the parentheses is valid.
    The function should return true if the string is valid, and false
    if it's invalid.
    """
    if type(string) is str:
        count = 0
        for i in string:
            if i == "(":
                count += 1
            if i == ")":
                count -= 1
            if count < 0:
                print(string)
                return False
        return count == 0
    else:
        raise TypeError('Argument must be a string')

