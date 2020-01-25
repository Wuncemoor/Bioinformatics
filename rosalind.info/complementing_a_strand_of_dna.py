def reverse_complement(dna):
    
    complementary_nucleotide = { 'A':'T', 'C':'G', 'G':'C', 'T':'A' }
    complementary_dna = []
    
    #for each nucleotide in dna 
    for i in dna:
        #look at dictionary, put complement in list
        comp =  complementary_nucleotide[i]
        complementary_dna.append(comp)
    #reverse the list    
    complementary_dna.reverse()
    #stick it all together
    print(''.join(complementary_dna))
    


