#prints whole line, module code, and number of sections of file entry
import csv

mfile = open("Python/modules.csv")
csvreader= csv.reader(mfile, dialect='excel')

for line in csvreader:
	print(line)
	print(line[1])
	print(len(line))

mfile.close

#prints only module title
import csv

mfile = open("Python/modules.csv")
csvreader= csv.reader(mfile, dialect='excel')

for line in csvreader:
	print(line[1])


mfile.close


#prints modules only offered in module one
import csv

mfile = open("Python/modules.csv")
csvreader= csv.reader(mfile, dialect='excel')

for line in csvreader:
	if line[3] == "This module is only offered in Semester 1":
		print(line[1])
	

mfile.close


#print files by specific person
import csv

mfile = open("Python/modules.csv")
csvreader= csv.reader(mfile, dialect='excel')

for line in csvreader:
	if line[2] == "Mr Neil Taylor":
		print(line[1])
	

mfile.close
