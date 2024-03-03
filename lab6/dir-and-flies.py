#1 - Write a Python program to list only directories, files and all directories, files in a specified path.(check again)
"""
import os

def listDirectories(path):
    print("Directories")
    for enter in os.scandir(path):
        if enter.is_dir():
            print(enter.name)

def listFiles(path):
    print("Files")
    for enter in os.scandir(path):
        if enter.is_file():
            print(enter.name)


print("All the directories and files:")
for dir in listDirectories(path):
    print(dir)
for file in listFiles(path):
    print(file)

    
path = input("Enter the path: ")
listDirectories(path)
listFiles(path)
"""

#2 - Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
"""
import os

path = input("Path: ")

if os.path.exists(path):
    print("Path exists")
    if os.access(path, os.R_OK):
        print("Readible")
    else:
        print("Not Readible")
    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not Writable")
    if os.access(path, os.X_OK):
        print("Executable")
    else:
        print("Not Executable")
else:
    print("Path does not exist")
"""

#3 - Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
"""
import os

path = input("Path: ")

if os.path.exists(path):
    print("Path exists")

    head, tail = os.path.split(path)
    print("Directory: ", head)
    print("Filename: ", tail)
    #or
    #print(os.path.dirname(path))
    #print(os.path.basename(path))
else:
    print("Path does not exists")
"""

#4 - Write a Python program to count the number of lines in a text file.
"""
import os

with open("something.txt", 'r') as file:
    length = len(file.readlines())
    print("number of lines: ", length)
"""

#5 - Write a Python program to write a list to a file.
"""
import os

with open("writelist.txt", 'w') as file:
    myList = []
    myList = input()
    file.write(myList)
    file.close()

with open("writelist.txt", 'r') as file:
    read = file.read()
    print(read)
"""

#6 - Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
"""
import os
import string

for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as file:
        file.writelines(letter)
"""

#7 - Write a Python program to copy the contents of a file to another file
"""
import os

with open("something.txt", "r") as file1, open("writelist.txt", "a") as file2:
    if os.stat("writelist.txt").st_size != 0:
        file2.write("\n")
    for line in file1:
        file2.write(line)
"""

#8 - Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
"""
import os

path = input()

if os.path.exists(path):
    os.remove(path)
    print("File is deleted")
else:
    print("File is not found")
"""