# Subcreated first on Wednesday, June 7, 2017
# @author: Colin F. Wilder
# Intellectual Property statement: This code is based on lots of other freely available code on the internet, but the synthesis is mine. This relates to my broader metaphysics of creation and subcreation. I have gained a lot from Stack Overflow. The basic ngrams stuff I think is my own,but may also come from lessons from the Programming Historian by Adam Crymble and William Turkel. Parts of them were inspired by code written by Duncan Buell in his CSCE 500; Programming for Humanists course at the University of South Carolina in Autumn 2013. This module is therefore released under a CC-BY license i.e. Creative Commons Attribution 2.0 Generic license, which is explained at https://creativecommons.org/licenses/by/2.0/.#

# perform text analysis separately on multiple strings in a CSV file

# get required modules
from utilities_bigrams import *
from utilities_prepForGephi import *
from utilities_logging import *

# declare global variables
fileName="stringSample.txt"
desiredWordDistance=1 # 1 means that ngrams are contructed only of adjacent words 
allNgrams=[] # this is where all the ngrams from all lines of the file will be stored together
allTokens=[]
ngramsDict={} # the frequency dictionary for the ngrams
tokenDict={} # the frequency dictionary for the tokens
output="" # this is what we will send to the output file at the end

# open, read, and process the file with the multiple string lines
with open(fileName,'r+') as f:
    lines = f.readlines()
    for i in range(0,len(lines)):
        line=lines[i].lower()
        #print len(line)
        if len(line)==1: # something weird but I think it is counting the carriage return as a character
            print "processing empty line"
            continue
        elif len(line)<=20:
            print "processing line: " + line[0:-1]
        else:
            print "processing line: " + line[0:20]
        # here we insert a flow of control statement to address cases of varying number of tokens
        lineSplit=lines[i].lower().split()
        # case 1: nothing there: continue.
        if len(lineSplit) == 0:
            print "empty line"
            continue
        # case 2: # tokens < desiredWordDistance: count tokens but do not make ngrams
        elif len(lineSplit) < desiredWordDistance:
            for token in lineSplit:
                allTokens.append(token)
                tokenDict=countTokens(token, tokenDict) # count each token into the token dictionary
        # case 3: # tokens >= desiredWordDistance: count tokens and make ngrams
        else:
            allNgrams.extend(makeSpreadBigrams(line,desiredWordDistance)) # makes ngrams; add to allNgrams list
            for token in lineSplit:
                allTokens.append(token)
                tokenDict=countTokens(token, tokenDict) # count each token into the token dictionary

# put all ngrams into the ngram frequency dictionary
for ngram in allNgrams:
    ngramsDict=countNgram(ngram, ngramsDict)

# print all ngrams
print "\nNgrams:"
output += "\n\nNgrams:"
print len(allNgrams)
output += "\n"+ str(len(allNgrams))
for ngram in allNgrams:
    print ngram
    output += "\n"+ str(ngram)
    
#print all tokens
print "\nTokens:"
output += "\n\nTokens:"
print len(allTokens)
output += "\n"+ str(len(allTokens))
print allTokens
output += "\n"+ str(allTokens)

# print ngrams dictionary
print "\nNgram frequency dictionary:"
output += "\n\nNgram frequency dictionary:"
print ngramsDict
output += "\n"+ str(ngramsDict)

# print token dictionary
print "\nToken frequency dictionary:"
output += "\n\nToken frequency dictionary:"
print tokenDict
output += "\n"+ str(tokenDict)

# make the CSV files for graphing in Gephi
makeEdgeListForGephi(ngramsDict)
makeNodeListForGephi(tokenDict)

# print to output and log file
sendToOutput(output)