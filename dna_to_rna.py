def DNAtoRNA(data, mode='dna'):
    """
    Enter a string of nucleotides and this fuction will return the rna 
    equivalent or the dna equivelent.  To convert rna back to dna use
    the optional \'rna\' argument.
    """
    mode.lower()
    modetypes = ['dna', 'rna']
    if mode not in modetypes:
        raise TypeError('mode only accepts \'dna\' or \'rna\'')
    if type(data) is str:
        data = data.upper()
        print(data)
        out = ''
        ntides = ['A', 'C', 'T', 'G', 'U']
        for nucleotide in data:
            if nucleotide not in ntides:
                raise TypeError('DNA must only be A, C, T, G.')
            if mode == 'dna':
                if nucleotide == 'T':
                    out = out + 'U'
                else:
                    out = out + nucleotide
            if mode == 'rna':
                if nucleotide == 'U':
                    out = out + 'T'
                else:
                    out = out + nucleotide
        return out
    else:
        raise TypeError('Argument must be a string')
