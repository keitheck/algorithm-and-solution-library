def divisors(integer):
    """
    Create a function that takes an integer n > 1 and returns an array
    with all of the integer's divisors(except for 1 and the number itself),
    from smallest to largest. If the number is prime return the
    string '(integer) is prime'.
    """
    if type(integer) is not int:
        raise TypeError
    arr = list(range(2, integer))
    out = []
    for i in arr:
        if integer % i == 0:
            out.append(i)
    if out == []:
        return "{} is prime".format(integer)
    else:
        return out
