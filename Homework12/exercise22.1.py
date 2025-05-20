# import NCBIXML from Bio.Blast
from Bio.Blast import NCBIXML

# creating a file handel fo rthe xml file
result_handle = open('results.xml')
blast_list = []
blast_dict = {}
#parsing the xml file
for blast_result in NCBIXML.parse(result_handle):
    query = blast_result.query
    for alignment in blast_result.alignments: 
        for hsp in alignment.hsps:
            if hsp.expect < 1e-5:
               print ('********** query *********')
               print(query)
               print('****Alignment****')
               print('sequence:',alignment.title)
               print('length:', alignment.length)
               print('e value:', hsp.expect)
               print('score', hsp.score)
##               print('query:',hsp.query[0:75]+ '...')
##               print('match:',hsp.match[0:75] + '...')
##               print('subj:',hsp.sbjct[0:75] + '...')
               #filtering the reads further 
               e_value = hsp.expect
               if e_value == 0.0:
                   blast_list.append([query,alignment.title,hsp.expect,hsp.score])
                   blast_dict[alignment.title] = query
# creating a dictionary with aloignment title as key and max score as value
max_scores_dict = {}
for blist in blast_list:
    alignment_title = blist[1]
    score = blist[3]
    if alignment_title not in max_scores_dict or score > max_scores_dict[alignment_title]:
        max_scores_dict[alignment_title] = score
# getting the corresponidng query, alignment and score
for k,v in blast_dict.items():
    score = max_scores_dict.get(k)
    print('query:',v,'alignment:',k, 'e value:',0.0,'score:',score)
    print()
    print()



        

                    
                   
       
                
                  
          

        
        


    
                   
                   
                 

                   
                    

