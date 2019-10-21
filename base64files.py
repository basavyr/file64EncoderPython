import os
import shutil
import base64
from os.path import isfile, join

folderPath = os.getcwd()
newFolderName = 'encodedFiles'
newFolderPath = newFolderName+'/'


def makeFolder(newFolderName):
    try:
        os.mkdir(newFolderName)
    except FileExistsError:
        print(f'Cannot create the {newFolderName} directory.')


fileArray = []

script = os.path.basename(__file__)


class fileSystem:
    def __init__(self, fileName, fileExtension):
        self.fileName = fileName
        self.fileExtenstion = fileExtension

    def copyFile(self, filePath, src):
        dst = self.fileName+'.'+self.fileExtenstion
        dst = filePath+dst
        print(dst)
        shutil.copy2(src, dst)


def copyFile(filePath, src, name, ext):
    dst = name+'.'+ext
    dst = filePath+dst
    #print(f'{src} : {dst}')
    shutil.copy2(src, dst)


makeFolder(newFolderName)


def showFolderContent(folderPath):
    files = os.listdir(folderPath)
    for file, x in zip(files, range(0, len(files))):
        if(isfile(file)):
            dotfile = str(file)
            if(dotfile[0][:1] == '.' or dotfile == script):
                pass
            else:
                #print(f'File no{x+1} name is {file}')
                item1 = dotfile
                name = item1.split(".")[0]
                ext = item1.split(".")[1]
                newFileTitle = base64.b64encode(bytearray(name, 'utf-8'))
                newFileTitleDecoded = newFileTitle.decode('utf-8')
                #print(f'{newFileTitle} : {newFileTitleDecoded} \n')
                fileArray.append(newFileTitleDecoded)
                copyFile(newFolderPath, item1, newFileTitleDecoded, ext)
        else:
            pass


showFolderContent(folderPath)
print(f'The script {script} run succesfully')
# print(fileArray)

""" encoded = base64.b64encode(b'data to be encoded')
print(encoded)
list=["rob3","rob2","rob1"]
print(base64.b64encode(bytearray(list[0],'utf-8'))) """

# encodedTitle=base64.encodestring(fileArray[0])
# print(encodedTitle)
# for x in fileArray:


# os.mkdir(newFolderPath)


# print(os.getcwd())
# print(os.path.dirname(os.path.abspath(__file__)))

""" 
filename="./inputFiles/file1.txt"
filename2="./inputFiles/file2.txt"
file1=open(filename)
file2=open(filename2)

newFile="./encodedFiles/test.txt"

shutil.copy2(filename,newFile)
 """
