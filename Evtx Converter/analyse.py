import os
from bs4 import BeautifulSoup as bs
import datetime
import sys

def tstamp():
    return datetime.datetime.now().strftime("%I_%M%p_%B_%d_%Y")

path = sys.argv[1]

eventIds = open(str(sys.argv[2]),"w")
xmlCount = 0
eventIdsCount = 0
matchEventIdsCount = 0

# ------------------------------ Get a list of xml files  -----------------------------
# Get list of files in path, second loop removes any files that are not xml files
# Get list of files in path
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(path):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
# Create list of xml files
listOfXml = []
for file in listOfFiles:
    if ".xml" in file:
        listOfXml.append(file)
xmlCount = len(listOfXml)
# ----------------------- Get xml information and write to file -----------------------
for file in listOfXml:
    print(file)

checkEvents = [1102,4611,4624,4634,4648,4661,4662,4663,4672,4673,4688,4698,4699,4702,4703,4719,4732,4728,4742,4776,4798,4799,4985,5136,5140,5142,5156,5158]

for file in listOfXml:
    print("Opening: {0}".format(file))
    f  = open(file,"r")
    soup = bs(f,'xml')
    events = soup.findAll("EventID")
    for event in events:
        if int(event.get_text()) in checkEvents:
            eventIds.write("MATCHED Event ID: {0}\n".format(event.get_text()))
            eventIdsCount += 1
            matchEventIdsCount += 1
        else:
            eventIds.write("NO MATCH for Event ID: {0}\n".format(event.get_text()))
            eventIdsCount += 1

eventIds.write("Number of XMl files found: {}\n".format(xmlCount))
eventIds.write("Event ID Count: {}\n".format(eventIdsCount))
eventIds.write("Matched Event IDs: {}\n".format(matchEventIdsCount))

eventIds.close()
