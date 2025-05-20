#Input
seq = "TTCAGGACCTACAGAAAGGCT"
#seq = "aggagcaggacttcgacac"
#seq = "gagcccacaagccacgggtc"
seq = seq.upper()
print ("Sequence:",seq)

#Method 1

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
print ("Method 1 Reverse complement:", reverse_comp(seq))

#Method 2

comp_d = {'A':'T','T':'A','G':'C','C':'G'}
l = []
for nuc in reversed(seq):
    comp = comp_d[nuc]
    l.append(comp)
    reverse_seq = ''.join(l)
print ("Method 2 Reverse complement:",reverse_seq)

#Method 3

comp = []
for nuc in reversed (seq):
    if nuc == 'A':
        comp.append('T')
    elif nuc == 'T':
        comp.append('A')
    elif nuc == 'G':
        comp.append('C')
    elif nuc == 'C':
        comp.append('G')
        
print("Method 3 Reverse complement:",''.join(comp))


#Method 4

def r_comp(seq):
    newseq = ''
    for nuc in seq:
        newnuc = nuc.replace('A','t').replace('G','c').replace('T','a').replace('C','g')
        newseq = newnuc + newseq
        newseq = newseq.upper()
    return newseq

print ("Method 4 Reverse complement:", r_comp(seq))
    
    
