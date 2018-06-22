def sort_insert(array):
    """
    A fuction that takes an array of
    strings, sorts it alphabetically and
    returns the first value with three *
    between each character in the string. 
    """
    # if type(array) is list or type(array) is tuple
    if type(array) is tuple or type(array) is list:
        if type(array) is tuple:
            array = sorted(array)
        array.sort()
        list(array)
        return '***'.join(list(array[0]))
    else:
        raise TypeError('Argument must be list or tuple')
    