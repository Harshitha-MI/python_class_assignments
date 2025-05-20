from model import *
import sys

#get the organism name from the command line

try:
    org_name = sys.argv[1]
except IndexError:
    print("Need an organism name argument", file=sys.stderr)
    sys.exit(1)

hs = Name.selectBy(name = org_name)
for n in hs:
    print('Scientific name of the organism',org_name,'is',n.taxonomy.scientific_name)
    tid= n.taxonomy.taxid
    print('Taxid of the organism is',tid,'rank:', n.taxonomy.rank)
    t = Taxonomy.byTaxid(tid)
    print('Taxonomic lineage')
    print('Organism',n.taxonomy.scientific_name, 'has parent',
          t.parent.scientific_name,t.rank, t.parent.taxid)
    for c in t.children:
        print("Organism",t.scientific_name,"has child",c.scientific_name,
              c.rank, c.taxid,)
    print()
    print()    





