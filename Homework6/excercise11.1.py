import csv
import sys
import statistics

# check for the command line argument
if len(sys.argv)<3:
    print ("Please provide the sequence file name:", file = sys.stderr)
    sys.exit(1)
    
# get the inputs from command line argument 
filename = sys.argv[1]
gene_name = sys.argv[2]
#read csv file 
f = open(filename,'r')
rows = csv.DictReader(f)
value = []
for r in rows:
    value.append(float(r[gene_name]))
#output
print ("means of expression values:\n",statistics.mean(value))
print ("standard deviation of expression values:\n",statistics.stdev(value))
f.close()

