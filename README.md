# Text_networks: The project

"Text networks" is my unimaginative name for a set of python modules I have written for computational text analysis. The modules were developed for courses I teach on digital history at the University of South Carolina. Feel free to email me for more information about me, the code, or the classes.

# Ambiguity of project name

There is an unintended resemblance between the title “textNetworks” and recent scholarship by a colleague of mine at the University of South Carolina. See Michael Gavin, "Historical Text Networks: The Sociology of Early English Criticism," Eighteenth-Century Studies 50, no. 1 (2016). It is possible that the name for the software occurred to me in conversations with him, although I do not *believe* that there is much similarity between the methods and tools in this software repository and the analysis undertaken in his work.

# what the code does

The code takes a string of text of any given length, removes (English) stop words from it, then creates a dictionary of the frequencies of all bigrams in the text. It then creates node and edge files suitable for graphing in the network vizualization program Gephi from this dictionary. You the user must yourself operate Gephi, since at this stage I don't know how to operate Gephi automatically from inside a Python interpreter (if that can even be done). The resulting Gephi graph will be a network diagram showing how all words in the text relate to one another in terms of proximity. That is, it will depict words as nodes and show an edge between two words if those two words appear next to one another in the text. You can change the graphing parameters in Gephi to do things like make the edge or node size vary with the frequency those words or edges appear and so forth. 

The code also has a logging function built into it. This generates a simple text log file in a folder every time the main program (the multi-string main program that is) is run. The log file contains the output from that run. This is so you can have a handy record of all you'ev accomplished. Any and all output folders can be deleted at anytime. The output function does however require a folder (called output) inside the directory where the code is. So if your code is in a folder called text_networks, then create text_networks/output. In text_networks, create a file called index.txt and write a number in it, say 1. That's all: text_networks/output/index.txt containing a number. 

# IP stuff

This code is mostly based on modules at The Programming Historian. See header comments of the files here for more information. 

# about this effort

I am a noob in GitHub. This repository will be my first real effort to put some code out in the world for others to see. 
