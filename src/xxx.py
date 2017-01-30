
import xml.etree.ElementTree as ET
from lxml.etree import fromstring
import urllib2
from lxml import etree

tree = ET.parse('xs.xml')
root = tree.getroot()
print root.tag
for elem in tree.iter(tag='sub-branch'):
   print elem.tag, elem.attrib
   
tree = ET.parse('xs1.xml')
root = tree.getroot()

for child in root:
   #  print(child)
     for child1 in child:
         #print(child1)
         for child2 in child1:
            # print(child2)
             for child3 in child2:
                for child4 in child3:
                   print child4.tag, child4.text