# uncomment lines 2, 16, and 32 to print execution time to console
# import time


def delete_nth(order, max_e):
    """
    Given a list lst and a number N, create a new list
    that contains each number of lst at most N times without
    reordering. For example if N = 2, and the input is
    [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next
    [1,2] since this would lead to 1 and 2 being in the
    result 3 times, and then take 3, which leads
    to [1,2,3,1,2,3].
    """
    if type(order) is list or type(order) is tuple:
        # starttime = time.time()
        d = {}
        out = []
        for i in order:
            if type(i) is not int:
                if type(i) is not float:
                    raise TypeError('Non integer or float.')
            if i in d:
                if d[i] < max_e:
                    d[i] = d[i] + 1
            else:
                d[i] = 1
        for j in order:
            if j in d and d[j] > 0:
                out.append(j)
                d[j] = d[j] - 1
        # print('execution time: {}'.format(time.time() - starttime))
        return out
    else:
        raise TypeError('Arument must be list or tuple of integers.')


