import platform, os, subprocess, time, datetime, sys

# Function to create time stamp
def tstamp():
    return datetime.datetime.now().strftime("%I_%M%p_%B_%d_%Y")

#Create and open log file
f = open("converstion_log_"+tstamp()+".txt", "w+")

# Set variables
path = str(sys.argv[1])
fileCount = 0 
sTime = time.time()
sFile = 0
fFile = 0
os.system("rm evtx_logs -r -f")
os.system("cp evtx_logs_back evtx_logs -r")

f.write("Start Time: {0}".format(tstamp()))

# Get the list of all files in directory tree at given path
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(path):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

# Write to log file which files have been found
for file in listOfFiles:
    print("File Found: {0}".format(file))
    f.write("File Found: {0} \n".format(file))

# Get number of files found and write to log file
fileCount = len(listOfFiles)
print("Number of files found: {0} \n".format(fileCount))
f.write("Number of files found: {0} \n".format(fileCount))

# Convert files
for file in listOfFiles:
    try:
        os.system("evtx_dump.py {0} > {1}xml".format(file, file[:-4]))
        f.write("File Converted: {0} \n".format(file))
        sFile += 1
    except:
        f.write("[!] File could not be converted: {0} \n".format(file))
        fFile += 1

# Write number of files converted and number failed
print("Files converted: {0} \n".format(sFile))
f.write("Files converted: {0} \n".format(sFile))
print("Files failed to convert: {0} \n".format(fFile))
f.write("Files failed to convert: {0} \n".format(fFile))
# Calculate amount of time taken and write to log file
eTime = time.time()
dTime = eTime - sTime
print("Time Taken: {0} seconds".format(dTime))
f.write("Time Taken: {0} seconds".format(dTime))

# Close log file as script finishes
f.close()
