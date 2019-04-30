#Converts given DNA sequence "dna" into amino acid sequence "proteinseq" 
dna = 'ATGACTAGCTAGCTAGCACTCGATCGATCGATCGATCTCGATGCATCGATCGATCATGCTAGCTACGTACGACGATCGATCGATCGATCGTGA'
dnasplit = []
extracodonjunk = []
proteinseq = []
i = 0
codon2prot = {
	r'TTT':'F', r'TTC':'F', r'TTA':'L', r'TTG':'L',
	r'TCT':'S', r'TCC':'S', r'TCA':'S', r'TCG':'S',
	r'TAT':'Y', r'TAC':'Y', r'TAA':'stop',r'TAG':'stop',
	r'TGT':'C', r'TGC':'C', r'TGA':'stop',r'TGG':'W',
	r'CTT':'L', r'CTC':'L', r'CTA':'L', r'CTG':'L',
	r'CCT':'P', r'CCC':'P', r'CCA':'P', r'CCG':'P',
	r'CAT':'H', r'CAC':'H', r'CAA':'Q', r'CAG':'Q',
	r'CGT':'R', r'CGC':'R', r'CGA':'R', r'CGG':'R',
	r'ATT':'I', r'ATC':'I', r'ATA':'I', r'ATG':'M',
	r'ACT':'T', r'ACC':'T', r'ACA':'T', r'ACG':'T',
	r'AAT':'N', r'AAC':'N', r'AAA':'K', r'AAG':'K',
	r'AGT':'S', r'AGC':'S', r'AGA':'R', r'AGG':'R',
	r'GTT':'V', r'GTC':'V', r'GTA':'V', r'GTG':'V',
	r'GCT':'A', r'GCC':'A', r'GCA':'A', r'GCG':'A',
	r'GAT':'D', r'GAC':'D', r'GAA':'E', r'GAG':'E',
	r'GGT':'G', r'GGC':'G', r'GGA':'G', r'GGG':'G'
}
for codons in dna:
	codon = dna[i:i+3]
	if len(codon) == 3:
		protein = codon2prot.get(codon)
		dnasplit.append(codon)
		proteinseq.append(protein)
		i = i+3
	else:
		extracodonjunk.append(codon)
		break
print(dnasplit)
print(extracodonjunk)
print(proteinseq)