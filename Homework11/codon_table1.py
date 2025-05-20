class codon_table:
    def __init__(self):
        self.table = {}

    def read(self,filename):
        f = open(filename)
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
        n = len(aa)
        for i in range(n):
            codon = b1[i] + b2[i] + b3[i]
            isInit = (st[i] == 'M')
            self.table[codon] = (aa[i],isInit)
            
    def amino_acid(self,codon):
        if codon in self.table:
            aa = self.table.get(codon)[0]
        else:
            aa = 'X'
        return aa

    def is_init(self,seq):
        codon = seq.seq[:3]
        if codon in self.table:
            init = self.table.get(codon)[1]
        else:
            init = False
        return init
            
    def get_ambig_aa(self,codon):
        if codon[0] != 'N':
            n1syms = codon[0]
        else:
            n1syms = 'ACGT'
        if codon[1] != 'N':
            n2syms = codon[1]
        else:
            n2syms = 'ACGT'
        if codon[2] != 'N':
            n3syms = codon[2]
        else:
            n3syms = 'ACGT'
        aas = set()
        for n1 in n1syms:
            for n2 in n2syms:
                for n3 in n3syms:
                    thecodon = n1+n2+n3
                    aas.add(amino_acid(self.table,thecodon))
        if len(aas) > 1:
            aa = 'X'
        else:
            aa = aas.pop()    
        return aa

    def translate(self,seq,frame):
        aalist = []
        for i in range(frame-1,len(seq.seq),3):
            codon = seq.seq[i:i+3]
            if 'N' in codon:
                aa = self.get_ambig_aa(codon)
            else:
                aa = self.amino_acid(codon)
            aalist.append(aa)
        aaseq = ''.join(aalist)
        return aaseq
    
    def rev_translate(self,seq,frame):
        aalist = []
        for i in range(frame-1,len(seq),3):
            codon = seq[i:i+3]
            if 'N' in codon:
                aa = self.get_ambig_aa(codon)
            else:
                aa = self.amino_acid(codon)
            aalist.append(aa)
        aaseq = ''.join(aalist)
        return aaseq

