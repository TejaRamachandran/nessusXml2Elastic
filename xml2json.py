import xml.etree.ElementTree as etree
import json
from io import StringIO
from tqdm import tqdm
from pandas import json_normalize
import sys

#print ("Input File Name: " % sys.argv[0])
#print ("Output File Name: " % sys.argv[1])

InputFilePath = str(input("Input File Name: "))
OutputFilePath = str(input("Output File Name: "))

fp = InputFilePath

tree = etree.parse(fp)
root = tree.getroot()
op_file = OutputFilePath
op = open(op_file,"w")
c = 0

for ip in root[1].iter(tag="ReportHost"):
    data = {}
    data["ip"] = ip.attrib["name"]
    for hostproperty in tqdm(ip.iter(tag="HostProperties")):
        for tag in hostproperty:
            tag_attrib = tag.attrib["name"]
            data[tag_attrib] = tag.text
        for reportitem in ip.iter(tag="ReportItem"):
            vulnerabilty = {}
            vulnerabilty.update(reportitem.attrib)
            for child in reportitem:
                vulnerabilty[child.tag] = child.text
                data["vulnerabilty"] = vulnerabilty
            #print(data)
            c += 1
            json.dump(data, op)
            op.write('\n')
print(c)
op.close()

