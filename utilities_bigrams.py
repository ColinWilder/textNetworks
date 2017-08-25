# -*- coding: utf-8 -*-
# Subcreated first on Sunday, September 22, 2013, with improvements periodically from 2013 to 2017. 
# @author: Colin F. Wilder
# Intellectual Property statement: This code is based on lots of other freely available code on the internet, especially lessons from the Programming Historian by Adam Crymble and William Turkel. The utilities to make bigrams are, I believe, fairly original to me, though not rocket science anyway.  Parts of them were inspired by code written by Duncan Buell in his CSCE 500; Programming for Humanists course at the University of South Carolina in Autumn 2013. This module is therefore released under a CC-BY license i.e. Creative Commons Attribution 2.0 Generic license, which is explained at https://creativecommons.org/licenses/by/2.0/.#

def makeSpreadBigrams(textString, wordDistance): # arguments: the string and the number of words in the n-grams
    # takes string and returns list of bigrams in it
    textAsList=textString.split() # make string into list by tokenizing
    # vet errors created by underlength lists
    # print "Length of text as list is %s." % (len(textAsList))
    if len(textAsList)<=wordDistance: # e.g. cannot make 3-grams from a string with 3 or fewer words
        print "\terror: text string has too few words"        
    # need for loop to get from 1 to wordDistance
    firstAndMiddlePairings=[]
    for i in range(0,len(textAsList)-wordDistance-1):
        for j in range(i+1,i+wordDistance+1):
            if i>=j:
                continue
            else:
                firstAndMiddlePairings.append(sorted([textAsList[i], textAsList[j]]))
    # here is for the last elements; this also works
    lastPairings=[]
    for i in range(len(textAsList)-wordDistance-1,len(textAsList)-1):
        for j in range(i+1,len(textAsList)):
            if i>=j:
                continue
            else:
                lastPairings.append(sorted([textAsList[i], textAsList[j]]))
    firstAndMiddlePairings.extend(lastPairings)
    # This works. 
    outputBigramList=[]    
    for pair in firstAndMiddlePairings:
        if pair[0]==pair[1]:
            continue
        else:
            outputBigramList.append(pair)
    return outputBigramList
    


def countNgram(ngram, ngramDictionary):
# takes a list of bigrams as argument
# returns a dictionary with bigrams as keys, their frequencies as values
    pairTuple=ngram[0], ngram[1]
    if pairTuple in ngramDictionary.keys():
        ngramDictionary[pairTuple]=ngramDictionary[pairTuple]+1
    else:
        ngramDictionary[pairTuple]=1
    return ngramDictionary

def countTokens(token, tokenDictionary): # takes as arguments a token and a token dictionary
# use this while making ngrams, in the middle of the process, to also make a frequency dictionary of the tokens themselves
    if token in tokenDictionary.keys():
        tokenDictionary[token]=tokenDictionary[token]+1
    else:
        tokenDictionary[token]=1
    return tokenDictionary # a dictionary









def mostFrequentBigrams(bigramsFreqsDict, numberToShow):
# Takes bigram frequency dictionary. Returns sorted list of most frequent bigrams
# First loop over the dictionary to find the highest value (frequency). 
    highestFreqValue=0    
    for key in bigramsFreqsDict:
        if bigramsFreqsDict[key]>highestFreqValue:
            highestFreqValue=bigramsFreqsDict[key]
# Then loop through and for each key whose value is that high value, print key and value. Then go down one unit to next lowest value and print all those keys and values. Do this until you reach the number of frequencies requested to be shown. 
    counter=0
    for i in range(highestFreqValue,0,-1):
        for key in bigramsFreqsDict:
            if bigramsFreqsDict[key]==i:
                print key,":",bigramsFreqsDict[key],"occurence(s)"
                counter +=1
            if counter==numberToShow: 
                break
        if counter==numberToShow: 
                break

#==============================================================================
# ## from Duncan - an alternative way to sort a frequency dictionary
# ## create a list of [value key] pairs instead of [key, value]
# ## pairs so we can sort on the frequencies (which are the 'value'
# ## entries in the dictionary)
# flipped = []
# for key, value in freqs.items():
#     flipped.append([value, key])
# flipped.sort()
#==============================================================================

#==============================================================================
# the following just runs this on the Genesis1 sample text. 
# sb=makeSpreadBigrams("Genesis1.txt",2)
# csb=countBigrams(sb)
# print csb
# mostFrequentBigrams(csb,10)
#==============================================================================

def sampleBigramsRun(textFile):
    sbrb=makeSpreadBigrams(textFile,4)
    print len(sbrb),"bigrams in total including duplicates"
    csbrb=countBigrams(sbrb)
    print len(csbrb),"unique bigrams"
    mostFrequentBigrams(csbrb,100)
    # cyphernomicon of 161k words took 2 hours to run on this function
    # to do: find common collocations and eliminate doubles e.g. 'use, use'.
    return csbrb
