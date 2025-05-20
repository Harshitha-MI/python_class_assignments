from myDNAstuff import*
from codon_tablemine import*
import sys

try:
    table = read_codons_from_file(sys.argv[1])
    seq = read_seq_from_file(sys.argv[2])
    if is_init(table,seq[:3]):
        print("Initial codon is a translation start codon")
    for frame in [1,2,3]:
        print("Frame",frame,"forward",translate(table,seq,frame))
    for frame in [1,2,3]:
        print("Frame",frame,"reverse",translate(table,revcomp(seq),frame))
except IndexError:
    print('provide the codon and sequence file name', end=' ')
    print('on the command line')
except IOError:
    print("can't find the file")




