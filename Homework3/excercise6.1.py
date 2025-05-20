#Input using command line

import sys
primer1 = sys.argv[1]
primer2 = sys.argv[2]

#To handle lower case sequences

primer1 = primer1.upper()
primer2 = primer2.upper()

#Assigning function

def complement(nuc):
    if nuc == 'A':
        comp ='T'
    elif nuc =='T':
          comp = 'A'
    elif nuc == 'G':
          comp = 'C'
    elif nuc == 'C':
          comp = 'G'
    return comp

def reverse_comp (seq):
    newseq = ''
    for nuc in seq:
        newseq = complement(nuc)+newseq
    return newseq

#output

#print (reverse_comp(primer1),reverse_comp(primer2))
print("The reverse complement of primer1:",reverse_comp(primer1))
print("The reverse complement of primer2:",reverse_comp(primer2))
