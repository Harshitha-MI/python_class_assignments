f = open ('codon.txt')
#f = open ('anthraxcodon.txt')
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
start = data['Starts']
codons = {}
init = {}
n = len(aa)
for i in range(0,n):
    codon = b1[i]+b2[i]+b3[i]
    codons[codon] = aa[i]
    init[codon] = start[i]
#print(init)
#print(codons)

import sys
seqfile = sys.argv[1]
seq = ''.join(open (seqfile).read().split())
print ("Sequence:")
print (seq)

aaseq = ''
for i in range(0,len(seq),3):
    seq_codon = seq[i:i+3]
    aaseq += codons[seq_codon]
print ("Amino acid sequence:")
print(aaseq)

if (init[seq[0:3]]== 'M'):
        print("Sequence has a valid translation start site")
else:
        print("Sequence does not have a valid transaltion start site")

        
    

    


    
    
    
