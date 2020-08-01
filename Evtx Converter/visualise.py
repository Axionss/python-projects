import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
import sys

#Time stamp function. Returns the time that the function was called at
def tstamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Open the log file
log = open(sys.argv[2], 'w')

filePath = sys.argv[1]
print("Setting file path: {0}".format(filePath))
listOfFiles = list()
txtFile = list()

#Get a list of the files
for (dirpath, dirnames, filenames) in os.walk(filePath):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

for i in listOfFiles:
    if "analyse_log" in i:
        filePath = i
        break

matchedEventIds = []
for i in open(filePath, "r"):
    if "MATCHED" in i:
        matchedEventIds.append(i)

filePath.strip("\n")

matchedEventsIdsInt = []
for i in matchedEventIds:
    print(i[18:])
    matchedEventsIdsInt.append(int(i[18:]))

uniqueIds = dict()
for i in matchedEventsIdsInt:
    uniqueIds[i] = uniqueIds.get(i, 1) + 1

yAxis = []
for key in uniqueIds:
    yAxis.append(uniqueIds[key])

xAxis = []
for i in uniqueIds:
    xAxis.append(i)

plt.barh(range(len(uniqueIds)), uniqueIds.values(), align='center')
plt.yticks(np.arange(len(uniqueIds)), uniqueIds)
plt.xlabel("Event Count")
plt.ylabel("Event ID Codes")
plt.title("Event IDs")
plt.show()
