import os
import subprocess
import json
import xmltodict
from sys import argv
import ast


portAndServiceList = []
formattedList = []
fJson = open("list.json","w")
productList = []
versionList = []
global jsonDictConverted

jsonDictConverted = {}

def runAndLog(c):
        #print("Running command: {}".format(c))
        os.system(c)

def runScan():
        #print("Scanning: {}".format(argv[1]))
        runAndLog("nmap -sC -sV {} -oX nmap_output.xml > /dev/null".format(argv[1]))

def convertFromUnicode(serviceEntryToConvert):
        for i in serviceEntryToConvert:
                value = serviceEntryToConvert[i].encode("ascii","ignore")
                jsonDictConverted[i.encode("ascii","ignore")] = value

def formatNmap():
        f = open("nmap_output.xml")
        xml_content = f.read()
        f.close()
        json_output = json.dumps(xmltodict.parse(xml_content), indent=4, sort_keys=True)
        fo = open("json_out","w")
        fo.write("json_output")

        jsonDict = json.loads(json_output)
        for i in jsonDict["nmaprun"]["host"]["ports"]["port"]:
                print(i)
                serviceEntryToConvert = i["service"]
#JSON data loaded as  type unicode so data could not be looked up for next setion. Three lines below build new
#dictionary with type string (ascii) for key and value pair)
                convertFromUnicode(serviceEntryToConvert)

        for i in jsonDictConverted:
                productList.append(jsonDictConverted["@product"])
                print(i)

formatNmap()
'''
for i in jsonDictConverted:
        print("I: {} \ Type: {} --- Value: {} \ Type: {}".format(i, type(i), jsonDictConverted[i], type(jsonDictConv$'''

#runScan()
