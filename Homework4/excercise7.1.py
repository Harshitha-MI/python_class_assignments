# defining a function
def complement(nuc):
    comp = ''
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

#input sequence
import sys
file = sys.argv[1]
input_seq = open(file).read().strip().split('\n')

#output
for c in input_seq:
    c_list = (c.split(' ')) 
    print (reverse_comp(c_list[0]), reverse_comp(c_list[1]))

    

    
    
    
