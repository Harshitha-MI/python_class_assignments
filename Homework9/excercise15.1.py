import pandas as pd
import numpy as np

df = pd.read_csv('proteomics.summary.tsv',sep = '\t')

minexpress = (df.min()>=2)
print("Number of genes with at least two distinct peptides in all samples:",
      sum(minexpress), sep = '\n')
maxexpress = (df.max()>=2)
print("Number of genes with at least two distinct peptides in at least one sample",
       sum(maxexpress), sep='\n')
