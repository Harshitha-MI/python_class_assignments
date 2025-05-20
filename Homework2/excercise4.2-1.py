#input 

seq = "AAAAAAAAAAAAAAAA"
#seq = "CACACACACACACACA"
#seq = "ATTCGATTCGATTCG"
#seq = "GTAGTAGTAGTAGTA"
#seq = "TCAGTCACTCACTCAG"

# identifying tandem

codon = seq [0:1]
#codon = seq [0:2]
#codon = seq [0:5]
#codon = seq [0:3]
#codon = seq [0:4]

tandem = seq.count(codon)

#processing

seq_len = len (seq)
codon_len = len (codon)
if seq_len == codon_len * tandem:
    print ("The sequence", seq, "has perfect or integer number of tandem repeats")
else:
    print ("The sequence",seq,"does not have integer number of tandem repeats")



#output

print ("The tandem repeat in the sequence",seq,"is:",codon)
print ("The number of tandem repeats in the sequence is:",tandem)




