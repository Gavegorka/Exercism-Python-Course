complement = {'G':'C', 'C':'G', 'T':'A', 'A':'U'} 


def to_rna(dna_strand):
    rna = ''
    for nuc in dna_strand:
        rna += complement[nuc]
    return rna
        
        
