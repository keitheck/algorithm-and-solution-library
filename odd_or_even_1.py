def odd_or_even(number):
    """returns even if number is even, odd if number is odd"""
    if type(number) is not int:
        raise TypeError('Argument must be an integer.')
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'
