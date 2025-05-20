#input
import sys
if len(sys.argv) < 2:
    print("Please provide a codon file and DNA sequence file on the command line.")
    sys.exit(1)

codonfile = sys.argv[1]
seqfile = sys.argv[2]
seq = ''.join(open (seqfile).read().split())

f = open(codonfile)
data = {}
for l in f:
    sl = l.split()
    k = sl[0]
    v = sl [2]
    data[k] = v
f.close()

b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
codons = {}
n = len(aa)   

for i in range(0,n):
    codon = b1[i]+b2[i]+b3[i]
    codons[codon] = aa[i]


# defining function for translation frame
def codonn(codon):
    aa_d = {}
    if codon[2] == 'N':
        codon2 = codon[0:2]
        for nuc in 'ATGC':
            codon3 = nuc
            new_codon = codon2 + codon3
            aa_d[new_codon] = codons[new_codon]
        values = list(aa_d.values())
        if all(items == values[0] for items in values):
            codon_n = next(iter(aa_d))
        else:
            codon_n = codon
    return codon_n
               
def frame1 (seq):
    aaseq = ''
    for i in range(0,len(seq),3):
        seq_codon = seq[i:i+3]
        if len (seq_codon) >= 3 and seq_codon[2] == 'N':
            seq_codon = codonn(seq_codon)
        aaseq += codons.get(seq_codon,'X')
    return aaseq

def frame2(seq):
    aaseqf2 = ''
    for i in range(1,len(seq),3):
        seq_codon = seq[i:i+3]
        if len(seq_codon) >= 3 and seq_codon[2] == 'N':
            seq_codon = codonn(seq_codon)
        aaseqf2 += codons.get(seq_codon,'X')
    return aaseqf2

def frame3(seq): 
    aaseqf3 = ''
    for i in range(2,len(seq),3):
        seq_codon = seq[i:i+3]
        if len (seq_codon) >=3 and seq_codon == 'N':
            seq_codon = codonn(seq_codon)
        aaseqf3 += codons.get(seq_codon,'X')
    return aaseqf3

# reverse complement
comp = {'A':'T','T':'A','G':'C','C':'G'}
# sequence into list
reverse = (list (reversed (seq)))
reverse_comp = ''.join([comp.get(nuc,nuc) for nuc in reverse])

  

# output

print ("Seqquence:\n",seq)
print ("Farme 1 transaltion:\n",frame1(seq))
print ("Farme 2 transaltion:\n",frame2(seq))
print ("Farme 3 transaltion:\n",frame3(seq))
print ("Reverse complement", reverse_comp)
print ("Reverse complement Farme 1 transaltion:\n",frame1(reverse_comp))
print ("Reverse complement Farme 2 transaltion:\n",frame2(reverse_comp))
print ("Reverse complement Frame 3 transaltion:\n",frame3(reverse_comp))



