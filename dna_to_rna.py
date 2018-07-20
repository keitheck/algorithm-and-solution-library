def DNAtoRNA(dna):
    if type(dna) is str:
        rna = ''
        for nucleotide in dna:
            if nucleotide is not 'A' or nucleotide is not 'C', or nucleotide is not 'G', or nucleotide is not 'T':
                raise TypeError('DNA must only be A, C, T, G.')
            if nucleotide == 'T':
                rna = rna + 'U'
            else:
                rna = rna + nucleotide
        return rna
    else:
        raise TypeError('Argument must be a string')