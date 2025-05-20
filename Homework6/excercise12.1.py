# importing modules
import Bio.SeqIO
import sys
import gzip
import statistics
from collections import Counter

# check for the command line argument
if len(sys.argv)<3:
    print ("Please provide the sequence file name:", file = sys.stderr)
    sys.exit(1)
# getting the file from cammand line argument
seqfilenamef = sys.argv[1]
seqfilenames = sys.argv[2]
# open gzip file
seqfile_f = gzip.open(seqfilenamef, mode ='rt')
aa_count = Counter()
total_aa = 0
for seq_record in Bio.SeqIO.parse(seqfile_f, 'fasta'):
    aaseq = seq_record.seq
    aa_count.update(aaseq)
    total_aa += len (aaseq)
#print (aa_count)
aa_percent = {aa:round((count/total_aa) *100,4) for aa,count in aa_count.items()}
max_aa = max(aa_percent.items(), key=lambda x:x[1])
min_aa = min(aa_percent.items(), key=lambda x:x[1])
print ("Most frequent amino acid in RefSeq proteome:\n", max_aa)
print ("least frequent amino acid in RefSeq proteome:\n", min_aa)
seqfile_f.close()

# open swiss prot gzip file
seqfile_s = gzip.open(seqfilenames)

aa_count_s = Counter()
total_aa_s = 0
for seq_record in Bio.SeqIO.parse(seqfile_s, 'uniprot-xml'):
    aaseq_s = seq_record.seq
    aa_count_s.update(aaseq_s)
    total_aa_s += len (aaseq_s)
#print (aa_count)
aa_percent_s = {aa:round((count/total_aa_s) *100,4)for aa,count in aa_count_s.items()}
aa_max_s = max(aa_percent_s.items(), key=lambda x:x[1])
aa_min_s = min(aa_percent_s.items(), key=lambda x:x[1])
print("Most frequent amino acid in SwissProt proteome:\n", aa_max_s)
print("Least frequent amino acid in SwissProt proteome:\n", aa_min_s)

#comparison
diff_dict = {}
diff_value = []
for key in aa_percent and aa_percent_s:
    if key in aa_percent and aa_percent_s:
            diff = abs(aa_percent.get(key)- aa_percent_s.get(key))
            diff_dict[key] = diff
            diff_value.append(diff_dict[key])
diff_mean = statistics.mean(diff_value)
stndev = statistics.stdev(diff_value)
print (diff_dict)
for key in diff_dict:
    if diff_dict[key] > diff_mean+ stndev:
       print ("The biggest difference is found with",key+
              " difference in frequency:",diff_dict[key])
        
seqfile_s.close()

