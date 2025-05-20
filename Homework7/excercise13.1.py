import pysam
bf = pysam.Samfile('10_Normal_Chr21.bam')

# For every position in the reference
max_value = 0
position=''
allele=''
for pileup in bf.pileup('21'):
    counts = {}
    # ...examine every aligned read
    for pileupread in pileup.pileups:
        # ...and get the read-base
        if pileupread.indel:
            continue
        if pileupread.is_del:
           continue
        al = pileupread.alignment
        if al.is_unmapped:
            continue
        if al.is_secondary:
            continue
        if int(al.opt('NM')) > 1:
          continue
        if int(al.opt('NH')) > 1:
           continue

        if not pileupread.query_position:
            continue
        readbase = pileupread.alignment.seq[pileupread.query_position]
        # Count the number of each base
        if readbase not in counts:
             counts[readbase] = 0
        counts[readbase] += 1
    # If there is no variation, move on
    if len(counts) < 2:
         continue
    # filter the reads for heterozygosity
    if max(counts.values()) >10:
        thr = 5/100 * max(counts.values())
        if sorted (counts.values()) [-2] >= max(counts.values()) - thr:
            # get the read with high coverage
            if(max_value < pileup.n):
                max_value=pileup.n
                listvalue=list(counts.values())
                listkey= list(counts.keys())
            position = pileup.pos
print("Locus",position, "reads",max_value, end="")
for r in range(len(listvalue)):
    allele = allele+' '+ listkey[r]+' '+ str(listvalue[r])
print(allele)


