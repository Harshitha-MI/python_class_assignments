#imprt Entrez and SeqIO from Biopython
from Bio import Entrez, SeqIO

# provide email
Entrez.email = 'shm68@georgetown.edu'

# creating a handle for the esearch
handle = Entrez.esearch(db="protein",
         term="Homo sapiens[Organism] AND BRCA2[Gene Name] AND REFSEQ")
result = Entrez.read(handle)
idlist = ','.join (result['IdList'])

# efetch to get the sequence of the protein ids
handle = Entrez.efetch(db="protein", 
                       id=idlist,
                       rettype="gb")
save_file = open("human-BRCA-proteins.fasta", "w")
for r in SeqIO.parse(handle, "genbank"):
# saving the sequence of each protein id in a single fasta file    
    save_file.write(r.id)
    save_file.write(r.description)
    save_file.write(str (r.seq))

save_file.close()





    


    
        
        








    












