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

    codon_table = {}
    n = len(aa)
    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        isInit = (st[i] == 'M')
        codon_table[codon] = (aa[i],isInit)
    return codon_table

def amino_acid(table,codon):
    if codon in table:
        aa = table.get(codon)[0]
    else:
        aa = 'X'
    return aa
# function to check for vaild translation start codon
def is_init(table,codon):
    try:
        init = table.get(codon)[1]
    except KeyError:
        init = print('Invalid transaltion start codon')
    except TypeError:
        init= print('codon not found in codon table')
    return init
   
# function to get the protein sequence  
def translate(table,seq,frame):
    seq=seq[frame-1:]
    aalist = []
    for i in range(0,len(seq),3):
        codon = seq[i:i+3]
        aa = amino_acid(table,codon)
        aalist.append(aa)
        aaseq = "".join(aalist)
    return aaseq


