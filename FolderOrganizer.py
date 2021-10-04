import os
def organiser(path , file , format):
    os.chdir(path)
    i=1
    files = os.listdir(path)
    with open(file) as f :
        filelist = f.read().split("\n")

    for file in  files:
        if file not in filelist:
            os.rename(file , file.capitalize())

        if os.path.splitext(file)[1]== format:
            os.rename(file,f"{i}{format}")
            i +=1

ard = input("Enter the full path name: ")
filen= input("Enter file name which contains name of files not to alter: ")
ext = input("Enter .format : ")
organiser(ard, filen , ext)