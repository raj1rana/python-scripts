import glob, os
directory = input("Enter directory to list all files it contains: ")
os.chdir(directory)
for folder in glob.glob("*.*"):
    print(folder)
