import xml.etree.ElementTree as ET
import urllib.request

thefile = urllib.request.urlopen('http://www.uniprot.org/uniprot/Q9H400.xml')

##for event, ele in ET.iterparse(thefile):
##    print(ele.tag,ele.attrib,ele.text)

document = ET.parse(thefile)
root = document.getroot()

ns = '{http://uniprot.org/uniprot}'
entry = root.find(ns+'entry')
#print (entry.attrib,entry.text)
references = entry.findall(ns+'reference')
for reference in references:
    print(reference.attrib['key'], end= " ")
    c= reference.find(ns+'citation')
    alist = c.find(ns+'authorList')
    for ele in alist.findall(ns+'person') or alist.findall(ns+'consortium'):
        print(ele.attrib.get('name',''), end = " ")
    title= c.find(ns+'title')
    if title is None:
        print('title not available', end=" ")
    else:
        print(title.text,end = " ")
    print(c.attrib.get('type',''),c.attrib.get('date',''),c.attrib.get('name',''),end = " ")
    print(c.attrib.get('volume',''),c.attrib.get('first',''),c.attrib.get('last',''),end = "")
    print(c.attrib.get('db',''),end = "")
    dbref = c.findall(ns+'dbReference')
    for eledb in dbref:
        print(eledb.attrib.get('type',''),eledb.attrib.get('id',''),end=" ")
    scope = reference.findall(ns+'scope')
    print("scope:",end="")
    for scope_ele in scope:
        print(scope_ele.text, end=" ")
    source = reference.find(ns+'source')
    if source is not None:
        print("tissue source:",end=" ")
        for tissue_ele in source.findall(ns+'tissue'):
            print(tissue_ele.text)
    print()
    print()
    
                      

        




