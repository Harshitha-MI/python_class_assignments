
# Variable

dna_seq = "gcatcacgttatgtcgactctgtgtggcgtctgctggg"

code = "atg"

#processing

location = dna_seq.find(code)

Trans_frame =((location+1)%3)

#output

print ("Position of the codon is", location + 1)
print("The translation frame of the codon is",Trans_frame)






