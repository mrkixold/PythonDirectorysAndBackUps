import os
import shutil
import directory
def singleRenameMenu(paths):
    print("")    
    print("Directory: " + paths)
    print("What do you want to do?:")
    print("")
    print("Option 1: Rename files and folders inside the directory")
    print("Option 2: Rename only files inside the directory")
    print("Option 3: Rename only folders inside the directory")
    print("")
    menuresult = input("Please select your option: ")
    if(menuresult == "1"):
        print("something")
    elif(menuresult == "2"):
        print("another thing")
    elif(menuresult == "3"):
        print("another thing 2")
    else: 
        print("error in the input, please introduce your input again")
        singleRenameMenu(paths)    
def singleBackUpMenu(paths):
    print("")    
    print("Directory: " + paths)
    print("What do you want to do?:")
    print("")
    print("Option 1: Rename files and folders inside the directory")
    print("Option 2: Rename only files inside the directory")
    print("Option 3: Rename only folders inside the directory")
    print("")
    menuresult = input("Please select your option: ")
    if(menuresult == "1"):
        print("something")
    elif(menuresult == "2"):
        print("another thing")
    elif(menuresult == "3"):
        print("another thing 2")
    else: 
        print("error in the input, please introduce your input again")
        singleBackUpMenu(paths)  
def chooseOptionsOne(paths):
    print("")    
    print("Directory: " + paths)
    print("What do you want to do?:")
    print("")
    print("Option 1: Rename files and folders")
    print("Option 2: Create a BackUp")
    print("")
    menuresult = input("Please select your option: ")
    if(menuresult == "1"):
        print("something")
        singleRenameMenu(paths)
    elif(menuresult == "2"):
        print("another thing")
        singleBackUpMenu(paths)
    else: 
        print("error in the input, please introduce your input again")
        chooseOptionsOne(paths)

def fileMenu():
    print("You're on file menu")

def writeMenu():
    path = input("Please introduce the path of the folder: ")
    try:
        os.listdir(path)
    except:
        print("Directory not found")
        writeMenu()
    else: 
        chooseOptionsOne(path)

def firstMenu():
    print("Please, select how do you want to select your directory:")
    print("")
    print("Option 1: Take the input from the listdir.txt file")
    print("Option 2: Write the path of the directory manually")
    print("")
    menuresult = input("Please select your option: ")
    if(menuresult == "1"):
        print("something")
        fileMenu()
    elif(menuresult == "2"):
        print("another thing")
        writeMenu()
    else: 
        print("error in the input, please introduce your input again")
        firstMenu()
firstMenu()