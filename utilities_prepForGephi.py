# Subcreated first on Wednesday, June 7, 2017
# @author: Colin F. Wilder
# Intellectual Property statement: This code is based on lots of other freely available code on the internet, but the synthesis is mine. This relates to my broader metaphysics of creation and subcreation. I have gained a lot from Stack Overflow. The basic ngrams stuff I think is my own, but may also come from lessons from the Programming Historian by Adam Crymble and William Turkel. Parts of them were inspired by code written by Duncan Buell in his *CSCE 500: Programming for Humanists* course at the University of South Carolina in Autumn 2013. This module is therefore released under a CC-BY license i.e. Creative Commons Attribution 2.0 Generic license, which is explained at https://creativecommons.org/licenses/by/2.0/.#

# this is a set of utilities that takes an ngram frequency dictionary and
# produces a node list and an edge list suitable for graphing in Gephi

# get required modules
import csv

###################################
# make list of edges (in CSV form)
###################################

def makeEdgeListForGephi(ngramsFrequencyDictionary):
    
    # make list of triples (i.e. list of 3-item lists)
    outputList=[]
    outputList.append(["Source","Target","Type","Weight"]) # this adds column titles
    for key in ngramsFrequencyDictionary:
        outputList.append([key[0],key[1],"Undirected",ngramsFrequencyDictionary[key]]) # adds information for each ngram
    
    # write the new output list into the new file and close it
    csvEdgeFileObject=open("text_networks_output_edges.csv", 'wb')
    w=csv.writer(csvEdgeFileObject)
    # alt # path=os.path.join(os.getcwd(),"edges-CSV.csv") # and tell the writer to open path
    w.writerows(outputList)

    print "edge list has been generated"


###################################
# make list of nodes (in CSV form)
###################################
# we need this because to graph a network, you need label names

def makeNodeListForGephi(tokensFrequencyDictionary):
    
    # transform the token dictionary into a list of triples
    outputList=[]
    outputList.append(["Id","Label","Weight"]) # Id and Label are same (improve this later)
    for key in tokensFrequencyDictionary:
        outputList.append([key,key,tokensFrequencyDictionary[key]])
    
    # write the new output list into the new file and close it
    csvNodeFileObject=open("text_networks_output_nodes.csv", 'wb')
    w2=csv.writer(csvNodeFileObject)
    w2.writerows(outputList)
    
    print "node list has been generated"
    
