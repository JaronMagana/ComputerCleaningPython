##This is a script to clean up my desktop
import os
import shutil

##This finds the location of your desktop from root
## wid == where is desktop
##def wid():
##    os.chdir("/")
##    cwd = os.getcwd()
##    print(cwd)


##This is your location of your main folder for storing all of your files
##This is on my desktop you can make it for any location you want
##os.chdir("/Users/jaronmagana/Desktop")


##This is the desktop
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

##This is the directory you want ot clean
try:
    print("What file do you want to clean from? (Make sure it is competeley correct with letters and capitalization)")
    x = input()
except ValueError:
    print("That is not a working directory.")    
    
currentDirectory = os.path.join(os.path.join(os.path.expanduser('~')), x)
x = os.listdir("%s" % currentDirectory)

#This is the directory you want to put your files into
moveDirectory = ("%s/extensions folder" % desktop)
print(x)

##This searches if a directory exist then if it does exist then nothing happens.
##If the directory does not exist then it creates a directory.
def search(moveDirectory):
    if os.path.isdir("%s" % moveDirectory) == False:
        print("there is no directory listed here:0")
        os.makedirs("%s" % moveDirectory)
        
    if os.path.isdir("%s/exe folder" % moveDirectory) == False:
        print("there is no directory listed here:1")
        os.makedirs("%s/exe folder" % moveDirectory)
        
    if os.path.isdir("%s/pdf folder" % moveDirectory) ==  False:
        print("there is no directory listed here:2")
        os.makedirs("%s/pdf folder" % moveDirectory)
        
    if os.path.isdir("%s/microsoft document folder" % moveDirectory) == False:
        print("there is no directory listed here:3")
        os.makedirs("%s/microsoft document folder" % moveDirectory)
        
    if os.path.isdir("%s/xlsx folder" % moveDirectory) == False:
        print("there is no directory listed here:4")
        os.makedirs("%s/xlsx folder" % moveDirectory)
        
    if os.path.isdir("%s/pages folder" % moveDirectory) == False:
        print("there is no directory listed here:5")
        os.makedirs("%s/pages folder" % moveDirectory)
                
    if os.path.isdir("%s/image folder" % moveDirectory) == False:
        print("there is no directory listed here:7")
        os.makedirs("%s/image folder"% moveDirectory)
        
    if os.path.isdir("%s/pptx folder" % moveDirectory) == False:
        print("there is no directory listed here:8")
        os.makedirs("%s/pptx folder" % moveDirectory)
        
    if os.path.isdir("%s/rtf folder" % moveDirectory) == False:
        print("there is no directory listed here:9")
        os.makedirs("%s/rtf folder" % moveDirectory)
        
    if os.path.isdir("%s/swift folder" % moveDirectory) == False:
        print("there is no directory listed here:9")
        os.makedirs("%s/swift folder" % moveDirectory)

    if os.path.isdir("%s/text folder" % moveDirectory) == False:
        print("there is no directory listed here:10")
        os.makedirs("%s/text folder" % moveDirectory)
    
    if os.path.isdir("%s/tex folder" % moveDirectory) == False:
        print("there is no directory listed here:11")
        os.makedirs("%s/tex folder" % moveDirectory)

    if os.path.isdir("%s/subdirectories" % moveDirectory) == False:
        print("there is no directory listed here:12")
        os.makedirs("%s/subdirectories" % moveDirectory)

    if os.path.isdir("%s/mobi folder" % moveDirectory) == False:
        print("there is no directory listed here:13")
        os.makedirs("%s/mobi folder" % moveDirectory)

    if os.path.isdir("%s/epub folder" % moveDirectory) == False:
        print("there is no directory listed here:14")
        os.makedirs("%s/epub folder" % moveDirectory)
        
    if os.path.isdir("%s/C# folder" % moveDirectory) == False:
        print("there is no directory listed here:15")
        os.makedirs("%s/C# folder" % moveDirectory)
        
    if os.path.isdir("%s/dmg folder" % moveDirectory) == False:
        print("there is no directory listed here:16")
        os.makedirs("%s/dmg folder" % moveDirectory)
        
    if os.path.isdir("%s/rar folder" % moveDirectory) == False:
        print("there is no directory listed here:17")
        os.makedirs("%s/rar folder" % moveDirectory)
        
    if os.path.isdir("%s/zip folder" % moveDirectory) == False:
        print("there is no directory listed here:18")
        os.makedirs("%s/zip folder" % moveDirectory)
        
    if os.path.isdir("%s/bin folder" % moveDirectory) == False:
        print("there is no directory listed here:19")
        os.makedirs("%s/bin folder" % moveDirectory)
        
    if os.path.isdir("%s/3ds junk folder" % moveDirectory) == False:
        print("there is no directory listed here:20")
        os.makedirs("%s/3ds junk folder" % moveDirectory)
        
    if os.path.isdir("%s/iso folder" % moveDirectory) == False:
        print("there is no directory listed here:21")
        os.makedirs("%s/iso folder" % moveDirectory)
        
    if os.path.isdir("%s/logger pro folder" % moveDirectory) == False:
        print("there is no directory listed here:22")
        os.makedirs("%s/logger pro folder" % moveDirectory)

    if os.path.isdir("%s/video folder" % moveDirectory) == False:
        print("there is no directory listed here:23")
        os.makedirs("%s/video folder" % moveDirectory)
        
    if os.path.isdir("%s/jar folder" % moveDirectory) == False:
        print("there is no directory listed here:24")
        os.makedirs("%s/jar folder" % moveDirectory)
        
    if os.path.isdir("%s/3d printer folder" % moveDirectory) == False:
        print("there is no directory listed here:25")
        os.makedirs("%s/3d printer folder" % moveDirectory)      
    else:
        print("All directories exist")

search(moveDirectory)


##This is to move all of your files to the right directories
for i in x:
    if i.endswith(".exe"):
        print("moving file %s to exe directory...." % i)
        shutil.move("%s/%s" % (currentDirectory,i), "%s/exe folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i == "extensions folder":
        print("can't move this directory")
    elif i.endswith(".pdf"):
        print("moving file %s to pdf directory...." % i)
        shutil.move("%s/%s" % (currentDirectory,i), "%s/pdf folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".docx") or i.endswith(".doc"):
        print("moving file %s to microsoft document directory...." % i)
        shutil.move("%s/%s" % (currentDirectory,i), "%s/microsoft document folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".xlsx"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/xlsx folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".pages"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/pages folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".jpeg") or i.endswith(".img") or i.endswith(".png") or i.endswith(".tiff") or i.endswith(".jpg") or i.endswith(".jp2") or i.endswith(".heif"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/image folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".rtf"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/rtf folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".swift"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/swift folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".pptx") or i.endswith(".ppt"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/pptx folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".tex") or i.endswith(".aux"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/tex folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".txt"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/text folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i == os.path.isdir("/Users/jaronmagana/Desktop/%s" % i):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/subdirectories/%s" % (moveDirectory,i))
        print("folder moved.")
    elif i.endswith(".mobi"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/mobi folder/%s" %  (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".epub") or i.endswith(".EPUB"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/epub folder/%s" %  (moveDirectory,i))
        print("file moved.")
    elif os.path.isdir("%s/%s" % (currentDirectory,i)):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/subdirectories/%s" % (moveDirectory,i))
    elif i.endswith(".cs"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/cs folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".dmg"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/dmg folder/%s" %  (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".rar"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/rar folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".3dsx") or i.endswith(".cia") or i.endswith(".skprx") or i.endswith(".sed") or i.endswith(".p7s") or i.endswith(".cur"):
        shutil.move("%s/%s" % (currentDirectory,i),  "%s/3ds junk folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".jar"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/jar folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".cmbl"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/logger pro folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".stl") or i.endswith(".gcode") or i.endswith(".h"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/3d printer folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".zip"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/zip folder/%s" %  (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".mpg") or i.endswith(".mp4") or i.endswith(".mov"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/video folder/%s" %  (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".bin"):
        shutil.move("%s/%s" % (currentDirectory,i), "%sy/bin folder/%s" % (moveDirectory,i))
        print("file moved.")
    elif i.endswith(".iso"):
        shutil.move("%s/%s" % (currentDirectory,i), "%s/iso folder/%s" % (moveDirectory,i))
        print("file moved.")
    else:
        print("This file %s does not have a directory" % i)
        

