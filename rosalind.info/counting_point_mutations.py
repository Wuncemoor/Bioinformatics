def get_hamming_distance(string1, string2):
    ham_count = 0
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            pass
        else:
            ham_count += 1
    
    return ham_count
    

    