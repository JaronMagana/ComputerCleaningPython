import sys
import datetime
import os
import shutil

##This is a script to clean up my desktop

#This code is to plot the files 

#import plotly as px
#import matplotlib.pyplot as plt; plt.rcdefaults()
#import numpy as np
#import matplotlib.pyplot as plt
#import importlib

##This is the desktop by finding it
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

#This file makes a list that is of your favorite directories to clean, 
#such as desktop and downloads

pythonScriptDirectory = os.getcwd()
print(pythonScriptDirectory)
fileConditonalOption = os.path.exists("%s/options.txt" % pythonScriptDirectory)

fileConditonalLog = os.path.exists("%s/log.txt" % pythonScriptDirectory)

def printList(hotList):
    x = 1
    for i in hotList:
        print("%s: %s" % (x,i))
        x = x + 1

#Edit favorite directiories 
def editList(hotList):
    edit = "no"
    while edit != "yes":
        printList(hotList)
        decision = input("Do you want add, replace, or are you finished?\n")
        if decision == "add":
            addValue = input("What would you like to add?\n")
            hotList.append(addValue)
        elif decision == "replace":
            number = input("What number would you like to replace?\n") 
            number = int(number) - 1
            replaceValue = input("What would you like replace it with?\n")
            hotList[number] = replaceValue
        else:
            edit = input("Are you sure you're finish editing?\n")
            if edit == "yes":
                print("ok! Exiting edit function....")
                saveList(hotList)
            else:
                print("ok!")
    
#Create a list of your favorite directories
def createList(rangeHigh):
    rangeHigh = rangeHigh + 1
    hotList = []
    for i in range(1,rangeHigh):
            x = input("What would you like to have for your hotlist directories?\n")
            hotList.append(x)
    return hotList

#Save a file of your favorite directories as a txt file for permancy
def saveList(hotList):
    f= open("options.txt","w+")
    p = 1
    for i in hotList:
        total = len(hotList)
        if p == total:
            f.write("%s" % i)
        else: 
            #print(i)
            f.write("%s," % i)
            p = p + 1
    f.close()
    
def openList():
    f= open("options.txt","r")
    contents = f.read()
    hotList = contents.split(",")
    return hotList

#Commandlist for creating, editing, and saving files based of user responses
if fileConditonalOption:
    print("You have a file with your favorite directories currently")
    f= open("options.txt","r")
    contents = f.read()
    hotList = contents.split(",")
    seeList = input("Would you like to see your list?\n")
    if seeList == "yes":
        printList(hotList)
        edit = input("Would you like to edit your list?\n")
        if edit == "yes":
            hotList = editList(hotList)
        else:
            print("ok! Starting sorting function")
    else:
        seeList = input("Would you like to edit your list?\n")
    
else:
    y = input("You currently don't have a hotlist directory\nWould you like to make one?\n")
    if y == "yes" :
        lengthOfList = input("how many items would you like in your list?\n")
        lengthOfList = int(lengthOfList)
        hotList = createList(lengthOfList)
        #print(hotList)
    else:
        print("Ok!")

#If nothing happens the list is automatically save 
if fileConditonalOption == False:
    saveList(hotList)

#This opens the files for reading and manipulation
if fileConditonalLog:
    f = open("log.txt","w+")
    








##This is the directory you want to clean
try:
    y = input("What file do you want to clean from? Is it in your list?\n")
    if y == "yes":
        list2 = openList()
        printList(list2)
        z = int(input("Type in your number\n"))
        try :
            x = list2[z-1]
            print("You have chosen %s, now cleaning..." % x)
        
        except:
            print("This directory doesn't exist")
            x = input("What file do you want to clean from? (Make sure it is competeley correct with letters and capitalization)\n")
    else:
        print("What file do you want to clean from? (Make sure it is competeley correct with letters and capitalization)")
        x = input()
except ValueError:
    print("That is not a working directory.")    
    
currentDirectory = os.path.join(os.path.join(os.path.expanduser('~')), x)
x = os.listdir("%s" % currentDirectory)

#This is the directory you want to put your files into
#might add an option to place it somewhere else by user standards
#might add the option of asking whether to print the files that are moved.
moveDirectory = ("%s/extensions folder" % desktop)
#print(x)
       
# version 2
extensionList = []
noDirectoryList = []
for i in x:
    #print(i)
    if os.path.isdir("/Users/jaronmagana/Desktop/%s" % i):
        #print("%s this is a directory" % i)
        u = 0
    else:
        noDirectoryList.append(i)
        extensionRaw = i.split('.')
        #print(extensionRaw)
        #creates a boolean function to make sure that the list is larger than 2
        y = len(extensionRaw)
        if y  >= 2:
            extension = extensionRaw[-1]
            #print(extension)
            extensionList.append(extension)
            #print(extensionList)
#      elif y > 2:
#          print("something went wrong")
        else:
            #print("This does not have an extension")
            u = 1
counter = 0
unedittedExtentionsList = extensionList
extensionList = list(dict.fromkeys(extensionList))
numberOfExtensionsList = []
def numberOfExtensions(list1, list2):
    for i in list1:
        x = 0
        for j in list2:
            if j == i:
                x += 1
        numberOfExtensionsList.append(x)
    return numberOfExtensionsList
yValues = numberOfExtensions(extensionList,unedittedExtentionsList)

for i in noDirectoryList:
    for j in extensionList:
        if os.path.isdir("%s/%s folder" % (moveDirectory, j)) == False:
           counter += 1
           print("there is no directory listed here:%s" % counter)
           os.makedirs("%s/%s folder" % (moveDirectory, j))
        elif i.endswith(".%s" % j):
            if os.path.isdir("%s/%s folder" % (moveDirectory, j)) == True:
                shutil.move("%s/%s" % (currentDirectory,i), "%s/%s folder/%s" % (moveDirectory,j, i))
                print("moving %s to %s folder" % (i,j))
                noDirectoryList = noDirectoryList[1:]
            else:
                print("something went wrong")

print("cleaned")
extensionList.append("Total")

#This is to create a plot of the files that were moves

#total = sum(yValues)
#yValues.append(total)
#plt.bar(extensionList, yValues, align='center', alpha=0.5)
##plt.xticks(extensionList, objects)
#plt.ylabel('Number of files moved')
#plt.title('Extension of file')
#plt.show()


        
