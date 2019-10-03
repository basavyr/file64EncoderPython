import os
import shutil

filename="./inputFiles/file1.txt"
filename2="./inputFiles/file2.txt"
file1=open(filename)
file2=open(filename2)

newFile="./encodedFiles/test.txt"

shutil.copy2(filename,newFile)
