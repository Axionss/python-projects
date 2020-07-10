import sys
import random
import os

def half(path):
    allFiles = []
    for root, dirs, files in os.walk(path):
        for filenames in files:
            file = os.path.join(root,filenames)
            absolutePath= os.path.abspath(file)
            allFiles.append(absolutePath)

    random.shuffle(allFiles)

    for i in range(len(allFiles)//2):
        os.remove(allFiles[i])

half(sys.argv[1])
