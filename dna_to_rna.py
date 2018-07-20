def DNAtoRNA(data, mode='dna'):
    """
    Enter a string of nucleotides and this fuction will return the rna 
    equivalent or the dna equivelent.
    """
    mode.lower()
    modetypes = ['dna', 'rna']
    if mode not in modetypes:
        raise TypeError('mode only accepts \'dna\' or \'rna\'')
    if type(data) is str:
        data.upper()
        rna = ''
        ntides = ['A', 'C', 'T', 'G', 'U']
        for nucleotide in data:
            if nucleotide not in ntides:
                raise TypeError('DNA must only be A, C, T, G.')
            if nucleotide == 'T':
                rna = rna + 'U'
            else:
                rna = rna + nucleotide
        return rna
    else:
        raise TypeError('Argument must be a string')
