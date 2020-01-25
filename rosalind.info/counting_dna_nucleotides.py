#Look at each nucleotide in dna string, increase appropriate counter by 1
def count_nucleotides(dna):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    
    for i in dna:
        if i == 'A':
            a_count += 1
        elif i == 'C':
            c_count += 1
        elif i == 'G':
            g_count += 1
        elif i == 'T':
            t_count += 1
    
    print(a_count, c_count, g_count, t_count)
    
