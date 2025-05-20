class p_digest:
    def __init__(self,seq):
        self.seq =''.join(seq.split()) 

    def length (self):
        return len (self.seq)
    def cutsite(self):
        cutsite = [0]
        try:
            value, omit = self.cleavage()
        except ValueError:
            value = self.cleavage()
        if isinstance (self,lys_n):
            for i in range (0,self.length()-1):
                if self.seq[i] in value:
                    cutsite.append(i)
        if value:
            for i in range (0,self.length()-1):
                if self.seq[i] in value:
                    cutsite.append(i+1)
        elif value and omit:
            for i in range (0,self.length()-1):
                if self.seq[i] in value and self.seq[i+1] not in omit:
                    cutsite.append(i+1)
            
        if cutsite[-1]!= self.length():
            cutsite.append(self.length())
        return cutsite
    def m_cleavage(self, miss_cleavage):
        peptide_info_list = []
        cutsite = self.cutsite()
        if miss_cleavage == 0:                   
            for j in range (0,len(cutsite)-1):
                start = cutsite[j]
                end = cutsite[j+1]
                peptide= self.seq[start:end]
                left_aa = self.seq[start-1]if start >0 else None
                right_aa = self.seq[end] if end < self.length() else None
                peptide_info_list.append({'peptide': peptide,
                                         'left': left_aa,
                                         'right': right_aa})
                
            
        elif miss_cleavage == 1:
            for j in range(0, len(cutsite)-2):
                start1 = cutsite[j]
                end1 = cutsite[j+1]
                peptide1 = self.seq[start1:end1]
                left_aa1 = self.seq[start1-1]if start1 >0 else None
                right_aa1 = self.seq[end1] if end1 < self.length() else None
                peptide_info_list.append({'peptide': peptide1,
                                         'left': left_aa1,
                                         'right': right_aa1})
                start2 = cutsite[j]
                end2 = cutsite[j+2]
                peptide2 = self.seq[start2:end2]
                left_aa2 = self.seq[start2-1]if start2 >0 else None
                right_aa2 = self.seq[end2] if end2 < self.length() else None
                peptide_info_list.append({'peptide': peptide2,
                                         'left': left_aa2,
                                         'right': right_aa2})
            last_start = cutsite[-2]
            last_end = cutsite[-1]       
            peptide_info_list.append({'peptide': self.seq[last_start:last_end],
                                      'left': self.seq[last_start-1]if last_start >0 else None,
                                      'right': self.seq[last_end] if last_end <self.length() else None})

        elif miss_cleavage == 2:
            for j in range (0, len(cutsite)-3):
                start1 = cutsite[j]
                end1 = cutsite[j+1]
                start1 = cutsite[j]
                end1 = cutsite[j+1]
                peptide1 = self.seq[start1:end1]
                left_aa1 = self.seq[start1-1]if start1 >0 else None
                right_aa1 = self.seq[end1] if end1 < self.length() else None
                peptide_info_list.append({'peptide': peptide1,
                                         'left': left_aa1,
                                         'right': right_aa1})
                start2 = cutsite[j]
                end2 = cutsite[j+2]
                peptide2 = self.seq[start2:end2]
                left_aa2 = self.seq[start2-1]if start2 >0 else None
                right_aa2 = self.seq[end2] if end2 < self.length() else None
                peptide_info_list.append({'peptide': peptide2,
                                         'left': left_aa2,
                                         'right': right_aa2})
                start3 = cutsite[j]
                end3 = cutsite[j+3]
                peptide3 = self.seq[start3:end3]
                left_aa3 = self.seq[start3-1]if start3 >0 else None
                right_aa3 = self.seq[end3] if end3 < self.length() else None
                peptide_info_list.append({'peptide': peptide3,
                                         'left': left_aa3,
                                         'right': right_aa3})
            last1_start = cutsite[-3]
            last1_end = cutsite[-2]       
            peptide_info_list.append({'peptide': self.seq[last1_start:last1_end],
                                      'left': self.seq[last1_start-1]if last1_start >0 else None,
                                      'right': self.seq[last1_end] if last1_end <self.length() else None})
            last2_start = cutsite[-3]
            last2_end = cutsite[-1]       
            peptide_info_list.append({'peptide': self.seq[last2_start:last2_end],
                                      'left': self.seq[last2_start-1]if last2_start >0 else None,
                                      'right': self.seq[last2_end] if last2_end <self.length() else None})  
            last3_start = cutsite[-2]
            last3_end = cutsite[-1]       
            peptide_info_list.append({'peptide': self.seq[last3_start:last3_end],
                                      'left': self.seq[last3_start-1]if last3_start >0 else None,
                                      'right': self.seq[last3_end] if last3_end <self.length() else None})
        return peptide_info_list
    
    mw = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
          'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
          'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
          'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06 }
    def mol_wt(self,peptide):
        return sum(map(self.mw.get,list(peptide)))
    def peptide_len(self,peptide):
        return len(peptide)
        
    
    def filter(self,miss_cleavage,minlen, maxlen, minwt, maxwt):
        chunk = []
        peptides_info = self.m_cleavage(miss_cleavage)
        for peptide_info in peptides_info:
            peptide = peptide_info.get('peptide')
            left = peptide_info.get('left')
            right = peptide_info.get('right')
            mol_wt= self.mol_wt(peptide)
            mol_wt = int(round(mol_wt))
            length = self.peptide_len(peptide)
            if minwt <= mol_wt <= maxwt and minlen<= length <=maxlen:
                chunk_info = [peptide,mol_wt,length,miss_cleavage,left,right]
                chunk.append(chunk_info)
            sort_chunk = sorted (chunk, key=lambda x: (x[2],x[1]),reverse=True)
        return sort_chunk
            
             
class trypsin(p_digest):
    def cleavage (self):
        value = ['K','R']
        omit = ['P']
        return value, omit   
            
class lys_c(p_digest):
    def cleavage(self):
        value = ['K']
        return value

class lys_n(p_digest):
    def cleavage(self):
        value = ['K']
        return value

class glu_c_bicarb (p_digest):
    def cleavage(self):
        value = ['E']
        omit = ['P','E']
        return value, omit
class glu_c_phos(p_digest):
    def cleavage(self):
        value = ['D','E']
        omit = ['P','E']
        return value,omit

