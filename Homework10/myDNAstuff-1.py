#read the sequence file
def read_seq_from_file(seqfile):
    seq = "".join(open(seqfile).read().split())
    seq = seq.upper()
    return seq

#function to get reverse complement
comp = {'A':'T','G':'C','T':'A','C':'G','N':'N'}
def revcomp (seq):
    rc = []
    for nuc in reversed(seq):
        rc.append(comp.get(nuc,'x'))
        rc_seq = "".join(rc)
    return rc_seq
#function to calculate gc content

def gc_content(seq):
    total_nucs = len(seq)
    gc = seq.count('G')+seq.count('C')
    gc_percent = gc/total_nucs*100
    return round (gc_percent,2)
