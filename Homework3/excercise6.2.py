#Input and manipulation command on command line

import sys
input_seq = sys.stdin.read()
command = sys.argv[1]

#To handle lower case

input_seq = input_seq.upper()

#assiging function

def complement(nuc):
    comp = ""
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

# Manipulation commands   

if command == "complement":
    newseq = ''
    for nuc in input_seq:
        newseq = newseq + complement(nuc)
    print ("Complement of sequence:", newseq)
    
if command == "reverse":
    newseq = ""
    for nuc in input_seq:
        newseq = nuc + newseq
    print ("Reverse of sequence:", newseq)
    
if command == "reversecomplement":
    print ("Reverse complement of sequence:", reverse_comp(input_seq))
    
print("DNA sequence:", input_seq)
