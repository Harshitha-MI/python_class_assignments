from DNAseq import *
from codon_table1 import *
import sys


if len(sys.argv) < 3:
    print("Require codon table and DNA sequence on command-line.")
    sys.exit(1)
#get the codon_table file and assign the codon_table class object
codons = codon_table()
codons.read(sys.argv[1])

# get the dna sequence file and assign the DNAseq class object
seq = DNAseq()
seq.read(sys.argv[2])

# initial start codon
if codons.is_init(seq):
    print("Initial codon is an initiation codon")

# translation in six frames
for frame in (1,2,3):
    print("Frame",frame,"(forward):",codons.translate(seq,frame))
    print("Frame",frame,"(reversed):",
          codons.rev_translate(seq.reversecomplement(),frame))

