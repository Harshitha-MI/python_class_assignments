#input primer sequences

primer = "CAGCACATGACGGAGGTTGT"
#primer = "TTGAGTAGACGCGTCTACTCAA"
#primer = "TTGAGTAGACGTCGTCTACTCAA"
#primer = "ATATATATATATATAT"
#primer = "ATCTATATATATGTAT"

#assiging function

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

# determining reverse complement palindrome

chunk_primer = len (primer)//2

if len (primer)== chunk_primer*2:
    first_part = primer[ :chunk_primer]
    second_part = primer[chunk_primer:]
else:
    first_part = primer[ :chunk_primer]
    second_part = primer[chunk_primer+1:]
    
if reverse_comp (second_part) == first_part:
    print("The primer is a reverse complement palindrome")
else:
    print("The primer is not a reverse complement palindrome")

#output
print ("Length of primer:",len (primer),"Chunk length:", chunk_primer)
print ("First part of primer:",first_part,"Second part of primer:",second_part)
print ("Reverse complement of second part is:",reverse_comp(second_part))

