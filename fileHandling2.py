import os

def takeFolderFile(path):
    path=r"{}".format(path)
    foldersList = []
    filesList = []
    try:
        all_ = os.listdir(path)
        for i in all_:
            filePath = os.path.join(path,i)
            if os.path.isdir(filePath):
                foldersList.append(filePath)
            else:
                size = os.stat(filePath).st_size
                tup = (i, size)
                filesList.append(tup)
    except:
        foldersList = []
        filesList = []
    return foldersList, filesList

path = input('Path: ')
path = r"{}".format(path)

foldersList, filesList = takeFolderFile(path)

while len(foldersList) != 0:
    # Take folders and files in folder (in folder list)
    for i in foldersList:
        folders, files = takeFolderFile(i)

        for file in files:
            filesList.append(file)

        foldersList.remove(i)
        for folder in folders:
            foldersList.append(folder)
            
print(filesList)