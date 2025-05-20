#dictionary for comp

comp = {'A':'T','T':'A','G':'C','C':'G'}
# sequence into list
import sys
if len(sys.argv) < 2:
    print("Please provide a DNA sequence file on the command line.")
    sys.exit(1)
file= sys.argv[1]
inputseq = list(''.join(open(file).read().split()))
reverse = (list (reversed (inputseq)))
print (''.join([comp.get(nuc,nuc) for nuc in reverse]))



