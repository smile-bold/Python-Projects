#!/usr/bin/python3
f = open('inputFile.txt', 'r') # opens file with only read permissions
passFile = open('PassFile.txt', 'w') #opens file with write permissions
failFile = open('FailFile.txt', 'w') # opens file with write permissions 
for line in f: # loops through line element of total line array 
    line_split = line.split() 
    if line_split[2] == 'P': # conditional - if array is split after second word equaling P 
        passFile.write(line)
    else:
        failFile.write(line)
    

f.close()
passFile.close()
failFile.close()
