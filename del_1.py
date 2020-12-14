# du kan definere flere hjelpefunksjoner om du trenger dem


def complement(dna_in): # ikke endre den linjen
    # din kode her
    output = ''
    
    for letter in (dna_in):
        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'

    return(output[::-1])
    
    
# ikke endre noe nedenfor
if __name__ == "__main__":
    in_1 = "ATAGCAGT"
    out_1 = complement(in_1)
    
    print(f"The complement of {in_1} is {out_1}")
    if out_1 == "ACTGCTAT":
        print('That is correct!')

    check = complement(complement(in_1))
    if in_1 == check:
        print('Good! Applying complement twice returns the original')
    else:
        print('Hmm. This does not work.')
