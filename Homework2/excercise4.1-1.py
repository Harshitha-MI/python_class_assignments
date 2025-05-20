# defining function

def complement (nuc):
    if nuc == 'a':
        comp = 't'
    elif nuc == 't':
        comp = 'a'
    elif nuc == 'u':
        comp = 'a'
    elif nuc == 'g':
        comp = 'c'
    elif nuc == 'c':
        comp = 'g'
    elif nuc == 'A':
        comp = 'T'
    elif nuc == 'T':
        comp = 'A'
    elif nuc == 'U':
        comp = "A"
    elif nuc == 'G':
        comp = 'C'
    elif nuc == 'C':
        comp = 'G'
    else:
        comp = nuc
    return comp

# creating a variable

#codon = 'atg'
#codon = 'ATG'
#codon = 'HEY'
#codon = 'AUG'
codon = 'uua'
first = codon[0]
second = codon[1]
third = codon [-1]

reverse = complement (third) + complement (second) + complement(first)

    
#output

print("The reverse complement of codon", codon, " is", reverse)
     
