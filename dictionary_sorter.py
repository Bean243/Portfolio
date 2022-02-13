import os
#open file of the words taken from the wordle source code
my_file = open("list.txt", "r")
words = my_file.read()
#split them up
word_list = words.split('","')
my_file.close()
#open a new empty file
textfile = open("words.txt", "w")
#write them all on a seperate line in a new file
for element in word_list:
	textfile.write(element + "\n")
textfile.close()
#open a new empty file
sortedwords = open("sortedwords.txt", "w")
with open("words.txt", "r") as r:
	for line in sorted(r):
		sortedwords.write(line)
		print(line,end='')
os.remove("words.txt")