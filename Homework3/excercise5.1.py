#Input
#TP53 primers
#primer set1
primer1 = "CAGCACATGACGGAGGTTGT"
primer2 = "TCATCCAAATACTCCACACGC"
#primer set2
#primer1 = "GAGGTTGGCTCTGACTGTACC"
#primer2 = "TCCGTCCCAGTAGATTACCAC"
#primer set3
#primer1 = "ACAGCTTTGAGGTGCGTGTTT"
#primer2 = "CCCTTTCTTGCGGAGATTCTCT"

#Code to handle lower and upper cases

primer1 = primer1.upper()
primer2 = primer2.upper()

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
    
#output

#print (reverse_comp(primer1),reverse_comp(primer2))
print("The reverse complement of forward primer:",reverse_comp(primer1))
print("The reverse complement of reverse primer:",reverse_comp(primer2))
      
