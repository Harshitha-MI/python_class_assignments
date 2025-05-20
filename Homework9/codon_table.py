#function to read the codon file
def read_codons_from_file(codonfile):
    f = open(codonfile)
    data = {}
    for l in f:
        sl = l.split()
        key = sl[0]
        value = sl[2]
        data[key] = value    
    f.close()

    b1 = data['Base1']
    b2 = data['Base2']
    b3 = data['Base3']
    aa = data['AAs']
    st = data['Starts']
    codon_dict = {}
    init = {}
    n = len(aa)
    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        codon_dict[codon] = (aa[i])
        init[codon]=(st[i]=='M')
    return codon_dict

# function to check for vaild translation start codon
def is_init(table,codon):
    aa={}
    aa[codon] = (table.get(codon)=='M')
    return aa

# function to get the protein sequence  
def translate(table,seq,frame):
    seq=seq[frame-1:]
    aalist = []
    for i in range(0,len(seq),3):
        codon = seq[i:i+3]
        aa = table.get(codon,'X')
        aalist.append(aa)
        aaseq = "".join(aalist)
    return aaseq


