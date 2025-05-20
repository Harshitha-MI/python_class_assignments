class DNAseq:
    def __init__(self):
            self.seq = ''
            self.name = ''
    def read(self,filename):
        self.seq = ''.join(open(filename).read().split())  
    def reverse(self):
        return self.seq[::-1]
    def complement(self):
        comp = {'A':'T','T':'A','G':'C','C':'G'}
        return ''.join(map(comp.get,self.seq))
    def reversecomplement(self):
        return ''.join(reversed(self.complement()))
    def length(self):
        return len (self.seq)
    def freq(self,nuc):
        return self.seq.count(nuc)
    def percentgc(self):
        gccount = self.freq('G')+self.freq('G')
        return 100*float(gccount)/ self.length()
    def __str__(self):
        asstr = '>'+self.name+'\n'+self.seq
        return asstr


        
                       
