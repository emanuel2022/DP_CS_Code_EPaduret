'''
Description: This function write to File writes to file
paramaters: name of the file and the list that will be written in the file
return: nothing
pre-conditions: name has to be valid
post-conditions: file has to be modified
'''

def writeToFile1 (name,lst): 				#Name of the function and paramaters. name is name of the file and lst is the list that will get written in the file.
	file = open(name, "w") 					#w means write (in the file)
	for i in range (0, len(lst), 1): 		#for loop to write every element from the list.
		file.write(str(lst[i]) + "\n") 		#file.write is what's writing in the file
	file.close() 							#close the file in order to save any modification


#Testing
a = [0,1,2,3,4,5,6,7,8,9] 
b = [1,2,8,2,9,10,523,40]
c = ["17", "12", "142"]
writeToFile1 ("test.txt", a)


def writeToFile2 (name,lst):
	file = open(name, "w")
	lst.sort()

	for i in range (0, len(lst), 1):
		file.write(str(lst[i]) + "\n")
	file.close()

writeToFile2("test1.txt", c)

""" 
Pseudocode:
NAME = passed string
LST = passed list
FILE = open file for writing
loop I from 0 to len(LST)-1
	FILE.write(LST[I])
end loop
"""


