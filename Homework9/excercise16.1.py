from myDNAstuff import*
from codon_table import*
import sys

if len(sys.argv)<3:
    print("Require codon table and DNA sequence on command-line.")
    sys.exit(1)
table = read_codons_from_file(sys.argv[1])
seq = read_seq_from_file(sys.argv[2])

      
if is_init(table,seq[:3]):
    print("Initial codon is a translation start codon")

for frame in [1,2,3]:
    print("Frame",frame,"forward",translate(table,seq,frame))
for frame in [1,2,3]:
    print("Frame",frame,"reverse",translate(table,revcomp(seq),frame))

