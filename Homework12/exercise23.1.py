import sys
import sqlite3

name = sys.argv[1]

conn = sqlite3.connect('taxa.db3')
params = [name]
c = conn.cursor()
c.execute("""
   select * from name
   where name = ?;
""",params)
# get the tax id of the name provided
for row in c:
    tax_id = row[1]
    param = [tax_id]
    c.execute("""select * from taxonomy
             where tax_id = ?;
             """,param)
    # to get the scientific name of the tax id 
    for r in c:
        print(r[1])







