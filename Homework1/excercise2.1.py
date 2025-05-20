# variable

code = "ATG"

# Processing

first_nuc = code[-1]
second_nuc = code[1]
third_nuc = code[0]
code_backwards = (first_nuc + second_nuc + third_nuc).lower()
#code_backwards_lower = code_backwards.lower()

# output

print (code_backwards)
