# These are utilities for making a running log. Uses a text file called index to keep track of what the current generation is. 

import os, datetime

def sendToOutput(outputString):
    # set basePath for output
    cwd=os.getcwd() # when you run the program the cwd reverts back to the default
    print "cwd: \t\t" + cwd
    outputDir="output"
    basePath=os.path.join(cwd,outputDir)
    print "basePath: \t" + basePath

    # set specific path of index file
    indexPath=basePath+'\index.txt'
    print "indexPath: \t" + indexPath
    
    # find the index of the most recent output
    currentIndex=findCurrentOutputIndex(indexPath)
    print "currentIndex: \t\t" + str(currentIndex)
    
    # increment index for next time
    currentIndex+=1
    
    # write new index back into file for next time
    f = open(indexPath, "w")
    f.write(str(currentIndex)) # print to output ######################
    f.close
    
    # make new folder and put a log file stub in there
    newFolderName="output"+str(currentIndex) 
    folderPath=basePath+'\\'+newFolderName
    print folderPath
    if not os.path.exists(folderPath): # make sure it exists
        os.makedirs(folderPath)
        
    # open log file for writin; this will stay open until end of session a while from now
    logFilePath=folderPath+'\\'+'logFile.txt'
    f = open(logFilePath,"w")
    
    # write stuff
    f.write("logFile "+str(currentIndex) + "\n")
    now = datetime.datetime.today().strftime("This log file was created on %m/%d/%Y, %H:%M:%S"+"\n")
    f.write(now)
    f.write(outputString)
    f.close
    
def findCurrentOutputIndex(indexPath): # returns the index of the current output folder based on the index file
    # foundation
    #read and increment the index file
    f = open(indexPath, "r")
    currentIndex =  int(f.readline())
    f.close()
    return currentIndex # should return an integer = current output index
    
