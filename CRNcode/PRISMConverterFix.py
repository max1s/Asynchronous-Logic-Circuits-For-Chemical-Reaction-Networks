import sys
import re


inputfile = open(sys.argv[1])
outputfile = open(inputfile.name + "fixed", 'w')
print "working..."
for line in inputfile:
    if re.search("\[(.)*\]\strue", line):
    	match = re.search("\(.*\)", line)
        newline = line.replace("true", match.group(0) + " > 0", 1)
        outputfile.write(newline)
    else:
    	outputfile.write(line)
print "done"