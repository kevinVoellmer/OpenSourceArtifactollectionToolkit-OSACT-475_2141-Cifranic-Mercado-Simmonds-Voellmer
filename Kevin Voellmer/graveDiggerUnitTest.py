##Unit testing for graveDigger

import graveDigger

##Open text file for writing output
text_file = open("Output.txt", "w+")

##Write the output of wordwheelQuery to the output text file
text_file.write(graveDigger.wordWheelQuery())

##Write the output of lastVisitedMRU to the output text file
text_file.write(graveDigger.lastVisitedMRU())

##Write the output of runMRU to the output text file
text_file.write(graveDigger.runMRU())

##close output text file
text_file.close()
