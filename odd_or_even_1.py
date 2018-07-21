def odd_or_even(number):
    """returns even if integer is even, odd if integer is odd"""
    if type(number) is not int:
        raise TypeError('Argument must be an integer.')
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'
