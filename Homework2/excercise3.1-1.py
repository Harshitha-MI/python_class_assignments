# assiging variables
sasp = "TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG"
sasp = sasp.lower().replace('t','u')

# To find if sasp gene starts with met codon

if sasp.startswith ('aug'):
    print ("The SASP gene starts with met codon")
else :
    print ("The SASP gene does not stat with met codon")
# finding if met codon is in frame 1

loc_met = sasp.find('aug')
frame = (loc_met % 3)+1
print ("The position of met codon is:", loc_met + 1)
print ("The frame of met codon is:",frame)

if frame == 1:
   print (" Yes, The SASP gene has frame 1 met codon")
else:
    print ("No, The SASP gene does not have frame 1 met codon.It has frame", frame)
# Number of nucleotides in SASP gene

total_nuc = len(sasp)
print ("The number of nucleotides in the SASP gene:", total_nuc)

# Number of amino acids
total_aa = total_nuc/3
print ("The number of amino acids in sasp protein:", int(total_aa))
#print ("The number of amino acids in sasp protein:", total_nuc/3)

# percentage of g

num_g = sasp.count('g')
percent_g = num_g/total_nuc * 100
print ("Percentage of 'G' in SASP gene:", percent_g)

# percentage of c

num_c = sasp.count('c')
percent_c = num_c/total_nuc * 100
print ("Percentage of 'c' in SASP gene:", percent_c)






