#input
import sys
if len(sys.argv) < 2:
    print("Please provide a DNA sequence file on the command line.")
    sys.exit(1)
file = sys.argv[1]
seq = ''.join(open(file).read().split())

freq = {}
for nuc in seq:
    num = seq.count(nuc)
    freq[nuc] = num
sort = (sorted (freq.items(), key= lambda v: v[1]))
sort = list (reversed(sort))

#output
print ('Frequencies of nucleotides in most occurance to least occurance:\n',sort)

