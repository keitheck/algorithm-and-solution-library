# uncomment lines 2, 18, 36, 41-42 to print execution time to console
# import time


def insert_missing_letters(st):
    """
    This function takes in a string and outputs the same
    string processed in a particular way.

    The function should insert only after the first occurence
    of each character of the input string, all the alphabet letters that:

        -are NOT in the original string
        -come after the letter of the string you are processing

    Each added letter should be in uppercase, the letters of the
    original string will always be in lowercase.
    """
    # starttime = time.time()
    if type(st) is not str:
        raise TypeError('Argument must be a string.')
    st = st.lower()
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    out = ''
    used = set()
    for letter in st:
        try:
            out = out + letter
            if letter not in used:
                used.add(letter)
                indx = alph.index(letter.upper())
                for char in alph[indx + 1:]:
                    if char.lower() not in st:
                        out = out + char    
        except:
            raise TypeError('String characters must be alpha.')
    # print('execution time: {}'.format(time.time() - starttime))
    return out


# if __name__ == '__main__':
#     insert_missing_letters('qwertyuiop')