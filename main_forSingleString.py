# Subcreated on Wednesday, March 22, 2017
# @author: Colin F. Wilder
# Intellectual Property statement: This code is to my knowledge mostly my creation. But the active power of forgetting, as Nietzsche called it, may have helped me forget where parts of it came from. There are probably elements from the Programming Historian by Adam Crymble and William Turkel. It is therefore released under a CC-BY license i.e. Creative Commons Attribution 2.0 Generic license, which is explained at https://creativecommons.org/licenses/by/2.0/.#

import utilities_preprocessing, utilities_bigrams, urllib2, re, sys, time, os, csv
from collections import defaultdict

# open the file and read it into a string
textString="In the beginning God created the heaven and the earth. And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light. And God saw the light, that it was good: and God divided the light from the darkness. And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day. And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters. And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so. And God called the firmament Heaven. And the evening and the morning were the second day. And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear: and it was so. And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good. And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth: and it was so. And the earth brought forth grass, and herb yielding seed after his kind, and the tree yielding fruit, whose seed was in itself, after his kind: and God saw that it was good. And the evening and the morning were the third day. And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years: and let them be for lights in the firmament of the heaven to give light upon the earth: and it was so. And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also. And God set them in the firmament of the heaven to give light upon the earth, and to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good. And the evening and the morning were the fourth day. And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven. And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that it was good. And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth. And the evening and the morning were the fifth day. And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so. And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that it was good. And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth. So God created man in his own image, in the image of God created he him; male and female created he them. And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth. And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat. And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat: and it was so. And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day."

# preprocess to simplify text
textString=utilities_preprocessing.removeSingletons(textString)
textString=textString.lower()
textString=utilities_preprocessing.stripTags(textString)
textString=utilities_preprocessing.removePunctuation(textString)
textString=utilities_preprocessing.removeNumbers(textString)
textString=utilities_preprocessing.removeExtraWhiteSpace(textString)
textString=utilities_preprocessing.removeStopWords(textString)
textString=utilities_preprocessing.removeSingletons(textString) # I don't remember why I do this a second time here. 

# make bigrams
bigramsList=utilities_bigrams.makeSpreadBigrams(textString, 2)
# note that a bigram is a 2-gram
# but the makeSpreadBigrams utility with an argument of 2 lets words that are 2 units from each other (i.e. separated by a word in the middle) be considered a bigram. 

# make frequency distribution out of this
freqDist=utilities_bigrams.countBigrams(bigramsList)

# make list of edges (in CSV form)

####### first, using the frequency distribution, make a list of triples (i.e. list of 3-item lists)
outputList=[]
outputList.append(["Source","Target","Weight"]) # this adds first triple
for key in freqDist:
    sublist=[key[0],key[1],freqDist[key]]
    outputList.append(sublist) # adds a subsequent triple

####### second, write the new output list into the new file and close it
csvEdgeFileObject=open("text_networks_output_edges.csv", 'wb')
w=csv.writer(csvEdgeFileObject)
# alt # path=os.path.join(os.getcwd(),"edges-CSV.csv") # and tell the writer to open path
w.writerows(outputList)

# make list of nodes (in CSV form)
# we need this because to graph a network, you need label names

####### first, make an (initially empty) target list where we will put all the node names
listOfNodesFromFreqDist=[]

####### second, add every key pair in the freqDist dictionary into that target list
for keyPair in freqDist.keys():
    # take each key in it
    # put each of the two elements in the key into the target list
    listOfNodesFromFreqDist.append(keyPair[0])
    listOfNodesFromFreqDist.append(keyPair[1])

####### third, remove duplicates
# an easy way to do this is to make it a set then make it a list again
listOfNodesFromFreqDist=list(set(listOfNodesFromFreqDist))

####### fourth, write the target node list into the new file with the right CSV columns
outputList=[]
outputList.append(["Id","Label"])
for nodeItem in listOfNodesFromFreqDist:
    sublist=[nodeItem,nodeItem]
    outputList.append(sublist)

####### fifth, write the new output list into the new file and close it
csvNodeFileObject=open("text_networks_output_nodes.csv", 'wb')
w2=csv.writer(csvNodeFileObject)
w2.writerows(outputList)

# you now have a node list and an edge list, ready for Gephi