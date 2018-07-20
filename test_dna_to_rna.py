from dna_to_rna import DNAtoRNA
import pytest


def test_arg_is_string():
    """Confirms Exception thrown if arg is not string"""
    with pytest.raises(TypeError):
        DNAtoRNA(['A', 'T', 'G', 'A', 'C'])


def test_validate_nucleotides():
    """Confirms Exception thrown if nucleotide string is corrupt"""
    with pytest.raises(TypeError):
        DNAtoRNA('ATGCTGGAATCCCVTGCA')


def test_lowercase_handled_correctly():
    assert DNAtoRNA('ATGCatgc') == 'AUGCAUGC'


def test_mode_exeption_handling():
    """Confirms exception thrown if dna or rna are not used"""
    with pytest.raises(TypeError):
        DNAtoRNA('TGCATCGA', 'rma')


def test_short_dna():
    """Confirms dna converted correctly"""
    assert DNAtoRNA('TGTCA') == 'UGUCA'


def test_long_dna():
    """Confirms dna of 10,000 nucleotides converted correctly"""
    assert DNAtoRNA(
        'tgaacaaagactaccccactctccgtgcgccgctcatactggttcgtaggtacggtagatcactgagatggcttccagggtgatttcgctaattagactggtcccaatgcgtggaagttgtgctcaggagctgagggtatccgcagggtgtagtttaatgtgacggcgcctaaaacgtaaaaactcgaacttgagcatttataccgaaagtccgaagctcctctcaccgtataccggtgacctcatagtagtttcctggatcgcgggtgagtgattctgaaattaaatgaagtagtctcgacggggcaggctcgccaatcgcacaatccatctggacgtttatcgcatttgagctccaggctccgcattagagtagtctcctccattggacccgatcgatacaactaagtgactcgtgatgctagctatactacagttgccggacgttctatgaactattccgttggtgcgcaccattagcggagtgcccacttcatttcagacctgtaagctccggccgagaatgcaattttttaaagttccacgtggcgcccaatcgaccctgataacaagggcctccagactagcttcttgaccgaagatggccgtgcgccacgaccgagccgactaaacggcttatgtattaaccgtccccgaattacgtggtgttcacagcaaatacccgatcaagactgactagaccacgcacactcgtcatatggcagtgtgcctaggctacgggtgagcacctacgtgtgtatggtaaggtccgagcggtaataacgagctctccccggggaaaaactgagcgccaagaatccgcccgcaagcattggtaccacgttgctaggagtgaaacggtgaaggtagctagggccagaatcaggttctacgtcaactgaggctaatcgctagcgccaggtagagacggctgttagaactaatggatcgggcggacccaatggttcgaagcagaagtccgagatctcatttcaggagcttcaacacgaccaacacctatcggtggtagcccgtccatagtaacgttaggaccgcgcacatgcttaatggtttcattaagtcagtcataatcttcccgttcgttccctgtggacatccctctgcgttctagggttgaactgatggcttccctgaacagataagttaacatgagcaggaggtacctcttcgcaacaggtctaggtcagccttgtctttatgggaagacagataggtattattttcacattgtgaactgctcgcaggtgatccggtaacctcgtcaatcgttacctagttccgccgtgcaccagtaaacctcatcctgtaacatcgactttcggaaggccctgccgttagtggggctaaagagcttccgttggaatatagtaggtcacagtgtgataccaggaccgtgtgcgatttgatcgggtccggctgttaccgatagtggtctgatacatcgtgagcagtcatgccgccaagggctccgataacccggatgatcgacatgggcagagagtacagaagtttagccttctgagagacagcaggggaggttggtacaccggtgatctgtcgaatgcttgagaccctcgccaatatactcaatcctatcgggcggttatctgactgattgctgtaactctgacgatggtccctgatagcgggcgcttcggcccttccaaacactcgccttttccgaacgggcgcttaggggcggctagtagatccaagtgactggtgccagagggcgttacccctcgctggtctaccgatatggacttaggatcaaaccgtgctttagttaaagccgactccagtggtgtgcccgagataacctgcgataatatccagtctggtcaacgctccgggcacttcactggttctcctttgcagtaatatgacaacaaaagactgcatgattcaccagggaagcttgaagtcaatattgatgcggccactgtgagggcccctactggatcttcaagcattctttacaagcatcggaactcgatgttacaattgtgtcactataacgtggaactactctacgtccttaagaataactgaaatgagaacgtggtacatatgagagtgacaaacgaccagcgttcctcgccggttcatccataggatgcctaagttaatgatagagcgtccgcctaacactgcgccaatgatcgcctctgagaatcaaagttccggggcttggatactgtcacaacgaatgtcgtacccctggccggttaaataaccgtgacgttgacgctgtgatacaagttggcggaattaccgaacgtacgacactccgcatcggtctaatataaacgaccgaaagcaccatttacacggcgcgaatacgcactcgcctctcgggtgttatggttatgattcccgacttccaattaagcaatgtaaggttcgtggggtccgttgtggttgggctctcaagggacatagcacgctgacccgttctttattgtcgtagtaatcgccctgggcgctaattacacgttcgttcgcctgtagatcccgacgaggcgtatcctagcttctgccccataccataaaagaatcaattgatgcgtatacatggagcagtttttctccggctacacatctatgcgcgcgctgatcaccatggggtcggaaaacagcttctcggggatagacggtgaggccttatgcaattacggttggttggtcagatccccctattccacgcacctatgtctgctagtccaacgcccgtgattaaactgcgctatcgcgggggagagctcccgtcgtggcagcgcgcaccgtcacgctgatctgccggcttcgagttttctcagtcaagctactgatcttcaagcttggtggcgccctggcaactgtgatttaccaggcaggttgtcagttcgtttttatcactggcacatgcataatctgttctacatattgagttgtgtggcgctagtgacactcccatgacgtccttagattggactctccaagttttacaggcaccatgcgcctgttagtccttcgtcgtaaaccgaggatatgactgttcctcgggggttatgcgttagtgttacccttctattaatgtcgccgtcctgcgatcgctacaacaggcattgggtgcttagtacagagtcatacaaagtaagggcgtccggggtcatatgacagtatgttttcatcctccctaactacccccctctatgggtggtgactaatcagcgccgtgagcttaattagcatggtattacctcaaattccggtagtgggcggcctcgctgactctgctacagttccaatctggagcggtgatccgtacgtcgcaggtcgaagttagcacttcctaacagtgtcaggtagtcatgccaagagccttgacccgtccgcctgcgtgtacaaacatgtactgtccgcctccctgtcagaaataaatcgatgagacatttagatgtcagcccacaggattcattccggcgggagtgacgtttgacgtgaggggcgagtcagaaagattgcatggtcacagcgcaagaattgctccgatcacatcccaagtccaagagcaacttcgtgacgagtcgagggtcccaccgcgcggcagtttcctaaacctcgcagcgcgaaagtgagacttttgtgtgtatcatccagcgtacccccttccttgatcttcattattggattgagctaagggggtaataatgtatcactgggttataattcgtttcccaaggcgtgttgggctgaagccgccataagccacggaggaaagcaaggttgcggacctacgaagaagccaaactcacacacactcagagtgggtgagattggtctgactactacgcgaagtagtctctccgccggtcctcccaagcccacgctcataggttccgatgttgggattctgcagcattcccaattggctgatccctcaggcataacattacacgttctcagcatggggcctttcggtcaatactagaaaccgattaagacggggcatccagggactagagagatggggtggtcccgtgcgttcgaaatggtcgcatgccgccccttagatttggtggtcgatctccgcggtccttacgtagactcgtggattggaatgccgcactatgacgaataggactcgccagtagcacggaccaagccaacaagccatcaggctgagtacgggcagcaatctgctgtcgagccggtcctgtggggtggcacattcagcaaatcttgtatcgttgctactattcgggtaggcgccaaatatgatgtaccatctcctccctacccatcgacgcattgcgcaagtccagtaaaaaacaacccctattggaactgtccgctcaatctggtcttgctgcggaagcccactgaaacttggttcgtcgtccttctaaactggtaaggagtatcccttcctcttgaggtgtctgtctgccgtaatgcccctagtgcttctaatttcgcacttccgtaaggacatcccccccacatatgttccgtgattaacaaagatatgggatgagccatacgcatgcaactacaatatcccaaagcattactaaaagcgagcagcttctggtgctcccatcggttgactgatgggggggctcaggattaggtaagctagtaagacagcttttatggacgatacgtacgagggagtagctggccctacctcaaaaggaacggccactcttctgccggtttataagccagtaaggtgtattacctttcctacgccagtgagttactatatcgacacatcttaaatgttagggtggacgagcagaattcctccgagaccatgttgcgttatacgagttggccaatgatttgcatttagatgatctgtatatatccatgaaggcgtggagggcttacaccactaccgatatttatcggctagactcaggcgggggcgtgtaggggattaacgccacttaagcttaacatctaagaacggagaggaccgaagtgtctagacatataaaaccctacgtttcgagaatcgtcggttaaaaccaggaaaaaccagttcattgtgcccagtattaagcgagatagattgctagcgttagaaacgcgcctttgacagtctagttcgtggggaggatgttgagtgcacttatgcccacgtccgatccgccgtatcgcactttaacctgtttacgtcaagtataaactgactcatcatgcacgtgtacaggtaccttgaagaacactaaccttcgcctggaatactaggtcacctacggcgtgaaattgctgagggcccttaaaactcgacaacctgtccactagagattctagtgtggcagccgactgctacatgtttttcaaaaatggtatctatctgaccttctggtatttccgcagtagctacgacgtaactgtcccctgtagtccgtcgacacgtggggtgtggcggccgcacggatttggatccttcccaatggatatctagtaggctagccagttcctcccaacaataaatagcttctagataattaagtcattccatgttgtaggcttacctaagaatggaaggattttgcaccggacttgctgaccgcgcgcgtattagggggccgaacgacacgttaataccaggctcaggacgttatctaacttatcttatccgccgtttcgtatagttaggctggcctggtacaaccgtcaacccgggcccctgctcattaggagagtctcctataactctcctctatgaagcacaaagatttgacatcagtcccttcataacttctggctaatgtctagcttactaacaaataagtgcacagcaacaggcgggttaaggctgggaacatcagccttggttcaaggtccccatcgatgataaagtcgctagtcatatcatatgacagaagttatgatttgtggaatgtgggagtgttacttgctcgagcatttgctgtcttagcaatgcgagacgtggaggagagccagattggcgccttactttcttatttcatgtaaaacgtgcatcggttaccgatgcgcgatcatgttcgcctttatttgaaaagtcctacacgacatggctagcagctttttggctgtcgtcctctgtacacccacatcagaccatagtcagaggaggagtagtggactcgtttcaagattggttttatgcactggttttgactgaaatatctagatgatatcgagaagacgtcaggagagcgcttctcctcggcactggcatcccaagctatgacaatatttactttacaccttgtggatggctgggctcaacctctttctatttcaggtaccacccggttgtaacacgctgttgacccaatgttcctggacagtaattcgcgggacaatctcagcaacggatggttggcgttcacaaggccaatattcgattaccatcaaacggcaccaaatggttgctatcagaacgtagacagcgacagtgagagaggacaaaaacacatgacttttcataactctttcgacgccgattagacaggctcgtcctcggtaacctggtaagcgatatcgcggtaaatacattgcttgaggcacctgactctagtggcatcagtctgccgttttgtatcggcgtgctgccgtctggctgtgcacactaatcgaacgatgatcgtcgatccaaattacaggataacccgatgtaaggacgctcagcgccacgccatcgtcagaggccatgatggtcggaaaggtcatcacaacttgggggtaaaagtatttgcgttattcgagaagacgtgtgtgataacacctcgcgcgccctgcgggagttgagaggaactgtttagtacacgggagttgattcattactctgaactcttatgagcaatttgtcttacacgtaaacgtgaaatttgctcttctcccatacctatgcgtgaaaggcgtcgccgatggacaagtagaagttcatgcccaggtgaaacgtgttagttaggcagttccacgacgaatacctgtggttcgtcgctccgtccccattgagccagcacttaattacgtgagatgccgtgagatcatctaacgtcaggtccatatgcgccttagctcgacctaatgcgtactagtccaatatcgacaatcctacttgcttactgttctgaaatcattaatatctgttcagtgattgctgtgcgaagattgttattggagtctattccataaatgggcttatagggcggaaaccattcaactaggtaagaggtctagtgagagacagtgcagtgcgcatcttggtatatatctattctataagacactacggatcgtacgtttaccggccacgacaataacaattctgctcctcagcgacgggaggagattattccggtcatgatctgtttatcttatacgcgtggtcggcgcccgacttccttatatacagtccctttggtgcattcgatggcgggctaaagggagatttttccccggataccgggtgcattcaacgagcaaagcgggccgagaataggctagaggcacttcacacgcgttccacccgctcggatgctagcgcatgcggtcaggctagacgcaggtaatcgcctaagggaagtagcaggatgatcgcctcgtaaactgatcgacttcgataactaacccaagcaacatcagaagataaatcttaggcactaattgtaaaactggtggaaccgtaagcatcgtatcttagtgaggcgtgttgaggctggtttacgcgactaccgcgcgcaacaagtgcctcgacgtggttcccacctacgaccgcaattactttggccgatcgtgttcgcctctcctaagcggcggaggagggcatgacagttgctattgcccattagttaatctcagcgccaaccaatatgagaatgtaatcatgaccggcgacccaaaaatgcctacattggaactcgtattttctgctccacattcgtacactgcgacccagtggggactgtaaggacatctcacatagcctatgcgatcggccgttctttaaagccgtcccctcattcacttagcctacccgaatcagggtttgtgaagggacacagatcgtatgtcccacggttaagtctaccgggaatatacgagtgagtgcccataggagcataccaatacgtttcgctgtggaaccaaggcaaagcaagtacgctagcagggtaggaccaactcctccttttcagcaccaaagtttagcacagcatcatctagtagtatagaagcagtggcgtagctccatcaagtagccgactactctttaagaaatgctctccacggtttggggcggatcattcattaaatcgaactctctgcatgaaaaaatgatatgttccgttgcaaggcgttcgacttggccgataagtatcttgtgcatgactattgcgcaagggttatccggaagagggctcaaagagtaataagtgcagataaaacggctaagcctttgcccgtatccataattggctagtcgtcgtggtaattcggggtcagattgctgcgcccgaaagtgtcggggccggggtgatgactattcgctgtcataagacacagtgtgccgaaaatgtgtacgctacataagggagacgtaggtgatcacattcgtcatgatagacaatgatatgccgcacgcgagccagacgaataatgtcgtctatttcaggtcggagtcaatggtgaggcagaacaccgcagcttatgagattcttaattggtggattccccatacgtccattttgcgcaggttctggaaaatttatcttactcactacagatctaaggcccggcacctaattactaagctaaacgaaggataattgatgttgctacctcataggagctatagtccgggccaggggtgcagtcgcgatttttaactatccaaccggctcccgggtagacctagtcttcgaatctcccgcgattcaaaagactgaaggtcggattttcgaatctaatcatacattgggcacagctacggagagagagaagaacgtcagttccgctaggagaattgcccttgtcatgctgaacggcgtgctgtgcctgctcgtggtgtttattcagcgagcgttataacaaacagggttgcgaagaattcactgtagagttaaagtcaggggggtgacgccttgtttgtctcgttgcctgacgctacctggacggcgtccattattgccaccttcttttcgcggcgatcgaccgagttttgttatatgccaatattcgctcacaaccacattgaatgacggagatgtggcgtcctattcgcagtattaataatgctatccaacctggctcctacggtcgctacatgtgagttatcattatcgtagcctcggcaacagaggggattcttgcttaaataatcagtttgctgtaaccgacgcaattagtgtgtatttattacgaaggtgtgggtgtttcgtaatggaggccggtctacctgtagttctccccaggcagaattgtttaattggtatcggacatctagcaccgagctgacggcggattcttatcagcgcattagcgttggtatgcgcgcgagcaacatgtaacgcgaaagttacaatctttcttgtctctctattttggtcggagggttgttgtgactaccaggtaccgaacactagtcagcctagttcctgaattctgaagagccggctttttcggggaccataaaacctactacacattcttcagctattaggcgatcagcacattctgcgcgcgtctgaagcgtgttttaggctagtaagaggcagacagtccggcaaattgacatgtctttattagtgctcatgtaatggagtcgaacttgaatagaacaccttgagtgtcatggcctatagtccggaggaataggaataactgcagacaagcgcattttcgaatagtcttgcagttgacctaaagccacagtttaaagatactttctcagcgtatatgtcttctggcggactacatcagagaacgt'
        ) == 'UGAACAAAGACUACCCCACUCUCCGUGCGCCGCUCAUACUGGUUCGUAGGUACGGUAGAUCACUGAGAUGGCUUCCAGGGUGAUUUCGCUAAUUAGACUGGUCCCAAUGCGUGGAAGUUGUGCUCAGGAGCUGAGGGUAUCCGCAGGGUGUAGUUUAAUGUGACGGCGCCUAAAACGUAAAAACUCGAACUUGAGCAUUUAUACCGAAAGUCCGAAGCUCCUCUCACCGUAUACCGGUGACCUCAUAGUAGUUUCCUGGAUCGCGGGUGAGUGAUUCUGAAAUUAAAUGAAGUAGUCUCGACGGGGCAGGCUCGCCAAUCGCACAAUCCAUCUGGACGUUUAUCGCAUUUGAGCUCCAGGCUCCGCAUUAGAGUAGUCUCCUCCAUUGGACCCGAUCGAUACAACUAAGUGACUCGUGAUGCUAGCUAUACUACAGUUGCCGGACGUUCUAUGAACUAUUCCGUUGGUGCGCACCAUUAGCGGAGUGCCCACUUCAUUUCAGACCUGUAAGCUCCGGCCGAGAAUGCAAUUUUUUAAAGUUCCACGUGGCGCCCAAUCGACCCUGAUAACAAGGGCCUCCAGACUAGCUUCUUGACCGAAGAUGGCCGUGCGCCACGACCGAGCCGACUAAACGGCUUAUGUAUUAACCGUCCCCGAAUUACGUGGUGUUCACAGCAAAUACCCGAUCAAGACUGACUAGACCACGCACACUCGUCAUAUGGCAGUGUGCCUAGGCUACGGGUGAGCACCUACGUGUGUAUGGUAAGGUCCGAGCGGUAAUAACGAGCUCUCCCCGGGGAAAAACUGAGCGCCAAGAAUCCGCCCGCAAGCAUUGGUACCACGUUGCUAGGAGUGAAACGGUGAAGGUAGCUAGGGCCAGAAUCAGGUUCUACGUCAACUGAGGCUAAUCGCUAGCGCCAGGUAGAGACGGCUGUUAGAACUAAUGGAUCGGGCGGACCCAAUGGUUCGAAGCAGAAGUCCGAGAUCUCAUUUCAGGAGCUUCAACACGACCAACACCUAUCGGUGGUAGCCCGUCCAUAGUAACGUUAGGACCGCGCACAUGCUUAAUGGUUUCAUUAAGUCAGUCAUAAUCUUCCCGUUCGUUCCCUGUGGACAUCCCUCUGCGUUCUAGGGUUGAACUGAUGGCUUCCCUGAACAGAUAAGUUAACAUGAGCAGGAGGUACCUCUUCGCAACAGGUCUAGGUCAGCCUUGUCUUUAUGGGAAGACAGAUAGGUAUUAUUUUCACAUUGUGAACUGCUCGCAGGUGAUCCGGUAACCUCGUCAAUCGUUACCUAGUUCCGCCGUGCACCAGUAAACCUCAUCCUGUAACAUCGACUUUCGGAAGGCCCUGCCGUUAGUGGGGCUAAAGAGCUUCCGUUGGAAUAUAGUAGGUCACAGUGUGAUACCAGGACCGUGUGCGAUUUGAUCGGGUCCGGCUGUUACCGAUAGUGGUCUGAUACAUCGUGAGCAGUCAUGCCGCCAAGGGCUCCGAUAACCCGGAUGAUCGACAUGGGCAGAGAGUACAGAAGUUUAGCCUUCUGAGAGACAGCAGGGGAGGUUGGUACACCGGUGAUCUGUCGAAUGCUUGAGACCCUCGCCAAUAUACUCAAUCCUAUCGGGCGGUUAUCUGACUGAUUGCUGUAACUCUGACGAUGGUCCCUGAUAGCGGGCGCUUCGGCCCUUCCAAACACUCGCCUUUUCCGAACGGGCGCUUAGGGGCGGCUAGUAGAUCCAAGUGACUGGUGCCAGAGGGCGUUACCCCUCGCUGGUCUACCGAUAUGGACUUAGGAUCAAACCGUGCUUUAGUUAAAGCCGACUCCAGUGGUGUGCCCGAGAUAACCUGCGAUAAUAUCCAGUCUGGUCAACGCUCCGGGCACUUCACUGGUUCUCCUUUGCAGUAAUAUGACAACAAAAGACUGCAUGAUUCACCAGGGAAGCUUGAAGUCAAUAUUGAUGCGGCCACUGUGAGGGCCCCUACUGGAUCUUCAAGCAUUCUUUACAAGCAUCGGAACUCGAUGUUACAAUUGUGUCACUAUAACGUGGAACUACUCUACGUCCUUAAGAAUAACUGAAAUGAGAACGUGGUACAUAUGAGAGUGACAAACGACCAGCGUUCCUCGCCGGUUCAUCCAUAGGAUGCCUAAGUUAAUGAUAGAGCGUCCGCCUAACACUGCGCCAAUGAUCGCCUCUGAGAAUCAAAGUUCCGGGGCUUGGAUACUGUCACAACGAAUGUCGUACCCCUGGCCGGUUAAAUAACCGUGACGUUGACGCUGUGAUACAAGUUGGCGGAAUUACCGAACGUACGACACUCCGCAUCGGUCUAAUAUAAACGACCGAAAGCACCAUUUACACGGCGCGAAUACGCACUCGCCUCUCGGGUGUUAUGGUUAUGAUUCCCGACUUCCAAUUAAGCAAUGUAAGGUUCGUGGGGUCCGUUGUGGUUGGGCUCUCAAGGGACAUAGCACGCUGACCCGUUCUUUAUUGUCGUAGUAAUCGCCCUGGGCGCUAAUUACACGUUCGUUCGCCUGUAGAUCCCGACGAGGCGUAUCCUAGCUUCUGCCCCAUACCAUAAAAGAAUCAAUUGAUGCGUAUACAUGGAGCAGUUUUUCUCCGGCUACACAUCUAUGCGCGCGCUGAUCACCAUGGGGUCGGAAAACAGCUUCUCGGGGAUAGACGGUGAGGCCUUAUGCAAUUACGGUUGGUUGGUCAGAUCCCCCUAUUCCACGCACCUAUGUCUGCUAGUCCAACGCCCGUGAUUAAACUGCGCUAUCGCGGGGGAGAGCUCCCGUCGUGGCAGCGCGCACCGUCACGCUGAUCUGCCGGCUUCGAGUUUUCUCAGUCAAGCUACUGAUCUUCAAGCUUGGUGGCGCCCUGGCAACUGUGAUUUACCAGGCAGGUUGUCAGUUCGUUUUUAUCACUGGCACAUGCAUAAUCUGUUCUACAUAUUGAGUUGUGUGGCGCUAGUGACACUCCCAUGACGUCCUUAGAUUGGACUCUCCAAGUUUUACAGGCACCAUGCGCCUGUUAGUCCUUCGUCGUAAACCGAGGAUAUGACUGUUCCUCGGGGGUUAUGCGUUAGUGUUACCCUUCUAUUAAUGUCGCCGUCCUGCGAUCGCUACAACAGGCAUUGGGUGCUUAGUACAGAGUCAUACAAAGUAAGGGCGUCCGGGGUCAUAUGACAGUAUGUUUUCAUCCUCCCUAACUACCCCCCUCUAUGGGUGGUGACUAAUCAGCGCCGUGAGCUUAAUUAGCAUGGUAUUACCUCAAAUUCCGGUAGUGGGCGGCCUCGCUGACUCUGCUACAGUUCCAAUCUGGAGCGGUGAUCCGUACGUCGCAGGUCGAAGUUAGCACUUCCUAACAGUGUCAGGUAGUCAUGCCAAGAGCCUUGACCCGUCCGCCUGCGUGUACAAACAUGUACUGUCCGCCUCCCUGUCAGAAAUAAAUCGAUGAGACAUUUAGAUGUCAGCCCACAGGAUUCAUUCCGGCGGGAGUGACGUUUGACGUGAGGGGCGAGUCAGAAAGAUUGCAUGGUCACAGCGCAAGAAUUGCUCCGAUCACAUCCCAAGUCCAAGAGCAACUUCGUGACGAGUCGAGGGUCCCACCGCGCGGCAGUUUCCUAAACCUCGCAGCGCGAAAGUGAGACUUUUGUGUGUAUCAUCCAGCGUACCCCCUUCCUUGAUCUUCAUUAUUGGAUUGAGCUAAGGGGGUAAUAAUGUAUCACUGGGUUAUAAUUCGUUUCCCAAGGCGUGUUGGGCUGAAGCCGCCAUAAGCCACGGAGGAAAGCAAGGUUGCGGACCUACGAAGAAGCCAAACUCACACACACUCAGAGUGGGUGAGAUUGGUCUGACUACUACGCGAAGUAGUCUCUCCGCCGGUCCUCCCAAGCCCACGCUCAUAGGUUCCGAUGUUGGGAUUCUGCAGCAUUCCCAAUUGGCUGAUCCCUCAGGCAUAACAUUACACGUUCUCAGCAUGGGGCCUUUCGGUCAAUACUAGAAACCGAUUAAGACGGGGCAUCCAGGGACUAGAGAGAUGGGGUGGUCCCGUGCGUUCGAAAUGGUCGCAUGCCGCCCCUUAGAUUUGGUGGUCGAUCUCCGCGGUCCUUACGUAGACUCGUGGAUUGGAAUGCCGCACUAUGACGAAUAGGACUCGCCAGUAGCACGGACCAAGCCAACAAGCCAUCAGGCUGAGUACGGGCAGCAAUCUGCUGUCGAGCCGGUCCUGUGGGGUGGCACAUUCAGCAAAUCUUGUAUCGUUGCUACUAUUCGGGUAGGCGCCAAAUAUGAUGUACCAUCUCCUCCCUACCCAUCGACGCAUUGCGCAAGUCCAGUAAAAAACAACCCCUAUUGGAACUGUCCGCUCAAUCUGGUCUUGCUGCGGAAGCCCACUGAAACUUGGUUCGUCGUCCUUCUAAACUGGUAAGGAGUAUCCCUUCCUCUUGAGGUGUCUGUCUGCCGUAAUGCCCCUAGUGCUUCUAAUUUCGCACUUCCGUAAGGACAUCCCCCCCACAUAUGUUCCGUGAUUAACAAAGAUAUGGGAUGAGCCAUACGCAUGCAACUACAAUAUCCCAAAGCAUUACUAAAAGCGAGCAGCUUCUGGUGCUCCCAUCGGUUGACUGAUGGGGGGGCUCAGGAUUAGGUAAGCUAGUAAGACAGCUUUUAUGGACGAUACGUACGAGGGAGUAGCUGGCCCUACCUCAAAAGGAACGGCCACUCUUCUGCCGGUUUAUAAGCCAGUAAGGUGUAUUACCUUUCCUACGCCAGUGAGUUACUAUAUCGACACAUCUUAAAUGUUAGGGUGGACGAGCAGAAUUCCUCCGAGACCAUGUUGCGUUAUACGAGUUGGCCAAUGAUUUGCAUUUAGAUGAUCUGUAUAUAUCCAUGAAGGCGUGGAGGGCUUACACCACUACCGAUAUUUAUCGGCUAGACUCAGGCGGGGGCGUGUAGGGGAUUAACGCCACUUAAGCUUAACAUCUAAGAACGGAGAGGACCGAAGUGUCUAGACAUAUAAAACCCUACGUUUCGAGAAUCGUCGGUUAAAACCAGGAAAAACCAGUUCAUUGUGCCCAGUAUUAAGCGAGAUAGAUUGCUAGCGUUAGAAACGCGCCUUUGACAGUCUAGUUCGUGGGGAGGAUGUUGAGUGCACUUAUGCCCACGUCCGAUCCGCCGUAUCGCACUUUAACCUGUUUACGUCAAGUAUAAACUGACUCAUCAUGCACGUGUACAGGUACCUUGAAGAACACUAACCUUCGCCUGGAAUACUAGGUCACCUACGGCGUGAAAUUGCUGAGGGCCCUUAAAACUCGACAACCUGUCCACUAGAGAUUCUAGUGUGGCAGCCGACUGCUACAUGUUUUUCAAAAAUGGUAUCUAUCUGACCUUCUGGUAUUUCCGCAGUAGCUACGACGUAACUGUCCCCUGUAGUCCGUCGACACGUGGGGUGUGGCGGCCGCACGGAUUUGGAUCCUUCCCAAUGGAUAUCUAGUAGGCUAGCCAGUUCCUCCCAACAAUAAAUAGCUUCUAGAUAAUUAAGUCAUUCCAUGUUGUAGGCUUACCUAAGAAUGGAAGGAUUUUGCACCGGACUUGCUGACCGCGCGCGUAUUAGGGGGCCGAACGACACGUUAAUACCAGGCUCAGGACGUUAUCUAACUUAUCUUAUCCGCCGUUUCGUAUAGUUAGGCUGGCCUGGUACAACCGUCAACCCGGGCCCCUGCUCAUUAGGAGAGUCUCCUAUAACUCUCCUCUAUGAAGCACAAAGAUUUGACAUCAGUCCCUUCAUAACUUCUGGCUAAUGUCUAGCUUACUAACAAAUAAGUGCACAGCAACAGGCGGGUUAAGGCUGGGAACAUCAGCCUUGGUUCAAGGUCCCCAUCGAUGAUAAAGUCGCUAGUCAUAUCAUAUGACAGAAGUUAUGAUUUGUGGAAUGUGGGAGUGUUACUUGCUCGAGCAUUUGCUGUCUUAGCAAUGCGAGACGUGGAGGAGAGCCAGAUUGGCGCCUUACUUUCUUAUUUCAUGUAAAACGUGCAUCGGUUACCGAUGCGCGAUCAUGUUCGCCUUUAUUUGAAAAGUCCUACACGACAUGGCUAGCAGCUUUUUGGCUGUCGUCCUCUGUACACCCACAUCAGACCAUAGUCAGAGGAGGAGUAGUGGACUCGUUUCAAGAUUGGUUUUAUGCACUGGUUUUGACUGAAAUAUCUAGAUGAUAUCGAGAAGACGUCAGGAGAGCGCUUCUCCUCGGCACUGGCAUCCCAAGCUAUGACAAUAUUUACUUUACACCUUGUGGAUGGCUGGGCUCAACCUCUUUCUAUUUCAGGUACCACCCGGUUGUAACACGCUGUUGACCCAAUGUUCCUGGACAGUAAUUCGCGGGACAAUCUCAGCAACGGAUGGUUGGCGUUCACAAGGCCAAUAUUCGAUUACCAUCAAACGGCACCAAAUGGUUGCUAUCAGAACGUAGACAGCGACAGUGAGAGAGGACAAAAACACAUGACUUUUCAUAACUCUUUCGACGCCGAUUAGACAGGCUCGUCCUCGGUAACCUGGUAAGCGAUAUCGCGGUAAAUACAUUGCUUGAGGCACCUGACUCUAGUGGCAUCAGUCUGCCGUUUUGUAUCGGCGUGCUGCCGUCUGGCUGUGCACACUAAUCGAACGAUGAUCGUCGAUCCAAAUUACAGGAUAACCCGAUGUAAGGACGCUCAGCGCCACGCCAUCGUCAGAGGCCAUGAUGGUCGGAAAGGUCAUCACAACUUGGGGGUAAAAGUAUUUGCGUUAUUCGAGAAGACGUGUGUGAUAACACCUCGCGCGCCCUGCGGGAGUUGAGAGGAACUGUUUAGUACACGGGAGUUGAUUCAUUACUCUGAACUCUUAUGAGCAAUUUGUCUUACACGUAAACGUGAAAUUUGCUCUUCUCCCAUACCUAUGCGUGAAAGGCGUCGCCGAUGGACAAGUAGAAGUUCAUGCCCAGGUGAAACGUGUUAGUUAGGCAGUUCCACGACGAAUACCUGUGGUUCGUCGCUCCGUCCCCAUUGAGCCAGCACUUAAUUACGUGAGAUGCCGUGAGAUCAUCUAACGUCAGGUCCAUAUGCGCCUUAGCUCGACCUAAUGCGUACUAGUCCAAUAUCGACAAUCCUACUUGCUUACUGUUCUGAAAUCAUUAAUAUCUGUUCAGUGAUUGCUGUGCGAAGAUUGUUAUUGGAGUCUAUUCCAUAAAUGGGCUUAUAGGGCGGAAACCAUUCAACUAGGUAAGAGGUCUAGUGAGAGACAGUGCAGUGCGCAUCUUGGUAUAUAUCUAUUCUAUAAGACACUACGGAUCGUACGUUUACCGGCCACGACAAUAACAAUUCUGCUCCUCAGCGACGGGAGGAGAUUAUUCCGGUCAUGAUCUGUUUAUCUUAUACGCGUGGUCGGCGCCCGACUUCCUUAUAUACAGUCCCUUUGGUGCAUUCGAUGGCGGGCUAAAGGGAGAUUUUUCCCCGGAUACCGGGUGCAUUCAACGAGCAAAGCGGGCCGAGAAUAGGCUAGAGGCACUUCACACGCGUUCCACCCGCUCGGAUGCUAGCGCAUGCGGUCAGGCUAGACGCAGGUAAUCGCCUAAGGGAAGUAGCAGGAUGAUCGCCUCGUAAACUGAUCGACUUCGAUAACUAACCCAAGCAACAUCAGAAGAUAAAUCUUAGGCACUAAUUGUAAAACUGGUGGAACCGUAAGCAUCGUAUCUUAGUGAGGCGUGUUGAGGCUGGUUUACGCGACUACCGCGCGCAACAAGUGCCUCGACGUGGUUCCCACCUACGACCGCAAUUACUUUGGCCGAUCGUGUUCGCCUCUCCUAAGCGGCGGAGGAGGGCAUGACAGUUGCUAUUGCCCAUUAGUUAAUCUCAGCGCCAACCAAUAUGAGAAUGUAAUCAUGACCGGCGACCCAAAAAUGCCUACAUUGGAACUCGUAUUUUCUGCUCCACAUUCGUACACUGCGACCCAGUGGGGACUGUAAGGACAUCUCACAUAGCCUAUGCGAUCGGCCGUUCUUUAAAGCCGUCCCCUCAUUCACUUAGCCUACCCGAAUCAGGGUUUGUGAAGGGACACAGAUCGUAUGUCCCACGGUUAAGUCUACCGGGAAUAUACGAGUGAGUGCCCAUAGGAGCAUACCAAUACGUUUCGCUGUGGAACCAAGGCAAAGCAAGUACGCUAGCAGGGUAGGACCAACUCCUCCUUUUCAGCACCAAAGUUUAGCACAGCAUCAUCUAGUAGUAUAGAAGCAGUGGCGUAGCUCCAUCAAGUAGCCGACUACUCUUUAAGAAAUGCUCUCCACGGUUUGGGGCGGAUCAUUCAUUAAAUCGAACUCUCUGCAUGAAAAAAUGAUAUGUUCCGUUGCAAGGCGUUCGACUUGGCCGAUAAGUAUCUUGUGCAUGACUAUUGCGCAAGGGUUAUCCGGAAGAGGGCUCAAAGAGUAAUAAGUGCAGAUAAAACGGCUAAGCCUUUGCCCGUAUCCAUAAUUGGCUAGUCGUCGUGGUAAUUCGGGGUCAGAUUGCUGCGCCCGAAAGUGUCGGGGCCGGGGUGAUGACUAUUCGCUGUCAUAAGACACAGUGUGCCGAAAAUGUGUACGCUACAUAAGGGAGACGUAGGUGAUCACAUUCGUCAUGAUAGACAAUGAUAUGCCGCACGCGAGCCAGACGAAUAAUGUCGUCUAUUUCAGGUCGGAGUCAAUGGUGAGGCAGAACACCGCAGCUUAUGAGAUUCUUAAUUGGUGGAUUCCCCAUACGUCCAUUUUGCGCAGGUUCUGGAAAAUUUAUCUUACUCACUACAGAUCUAAGGCCCGGCACCUAAUUACUAAGCUAAACGAAGGAUAAUUGAUGUUGCUACCUCAUAGGAGCUAUAGUCCGGGCCAGGGGUGCAGUCGCGAUUUUUAACUAUCCAACCGGCUCCCGGGUAGACCUAGUCUUCGAAUCUCCCGCGAUUCAAAAGACUGAAGGUCGGAUUUUCGAAUCUAAUCAUACAUUGGGCACAGCUACGGAGAGAGAGAAGAACGUCAGUUCCGCUAGGAGAAUUGCCCUUGUCAUGCUGAACGGCGUGCUGUGCCUGCUCGUGGUGUUUAUUCAGCGAGCGUUAUAACAAACAGGGUUGCGAAGAAUUCACUGUAGAGUUAAAGUCAGGGGGGUGACGCCUUGUUUGUCUCGUUGCCUGACGCUACCUGGACGGCGUCCAUUAUUGCCACCUUCUUUUCGCGGCGAUCGACCGAGUUUUGUUAUAUGCCAAUAUUCGCUCACAACCACAUUGAAUGACGGAGAUGUGGCGUCCUAUUCGCAGUAUUAAUAAUGCUAUCCAACCUGGCUCCUACGGUCGCUACAUGUGAGUUAUCAUUAUCGUAGCCUCGGCAACAGAGGGGAUUCUUGCUUAAAUAAUCAGUUUGCUGUAACCGACGCAAUUAGUGUGUAUUUAUUACGAAGGUGUGGGUGUUUCGUAAUGGAGGCCGGUCUACCUGUAGUUCUCCCCAGGCAGAAUUGUUUAAUUGGUAUCGGACAUCUAGCACCGAGCUGACGGCGGAUUCUUAUCAGCGCAUUAGCGUUGGUAUGCGCGCGAGCAACAUGUAACGCGAAAGUUACAAUCUUUCUUGUCUCUCUAUUUUGGUCGGAGGGUUGUUGUGACUACCAGGUACCGAACACUAGUCAGCCUAGUUCCUGAAUUCUGAAGAGCCGGCUUUUUCGGGGACCAUAAAACCUACUACACAUUCUUCAGCUAUUAGGCGAUCAGCACAUUCUGCGCGCGUCUGAAGCGUGUUUUAGGCUAGUAAGAGGCAGACAGUCCGGCAAAUUGACAUGUCUUUAUUAGUGCUCAUGUAAUGGAGUCGAACUUGAAUAGAACACCUUGAGUGUCAUGGCCUAUAGUCCGGAGGAAUAGGAAUAACUGCAGACAAGCGCAUUUUCGAAUAGUCUUGCAGUUGACCUAAAGCCACAGUUUAAAGAUACUUUCUCAGCGUAUAUGUCUUCUGGCGGACUACAUCAGAGAACGU'


def test_short_rna():
    """Confirms rna converted correctly"""
    assert DNAtoRNA('UGCAUCGA', 'rna') == 'TGCATCGA' 