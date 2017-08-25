# Text_networks: The project

Text networks is the unimaginative name for a set of python modules I have written for computational text analysis. The modules were developed for courses I teach on digital history at the University of South Carolina. Feel free to email me for more information about me, the code, or the classes. 

# what the code does

The code takes a string of text of any given length, removes (English) stop words from it, then creates a dictionary of the frequencies of all bigrams in the text. It then creates node and edge files suitable for graphing in the network vizualization program Gephi from this dictionary. You the user must yourself operate Gephi, since at this stage I don't know how to operate Gephi automatically from inside a Python interpreter (if that can even be done). The resulting Gephi graph will be a network diagram showing how all words in the text relate to one another in terms of proximity. That is, it will depict words as nodes and show an edge between two words if those two words appear next to one another in the text. You can change the graphing parameters in Gephi to do things like make the edge or node size vary with the frequency those words or edges appear and so forth. 

# IP stuff

This code is mostly based on modules at The Programming Historian. See header comments of the files here for more information. 

# about this effort

I am a noob in GitHub. This repository will be my first real effort to put some code out in the world for others to see. 

God knows whether this will work. 