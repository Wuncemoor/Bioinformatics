def rna2prot(rna):
    i=0
    codon2prot = { 
            'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
            'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
            'UUA':'L', 'CUA':'L', 'AUA':'I','GUA':'V',
            'UUG':'L', 'CUG':'L', 'AUG':'M','GUG':'V',
            'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
            'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
            'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
            'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
            'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
            'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
            'UAA':'stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
            'UAG':'stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
            'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
            'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
            'UGA':'stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
            'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'
            }

    proteinseq = ''
    while i < len(rna):
        
        codon = rna[i:i+3]
        protein = codon2prot.get(codon)
        proteinseq = proteinseq + protein
        i += 3
        
    return proteinseq
    
