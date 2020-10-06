from pprint import pprint


'''
Description: This function reads from a pre-exisisting file
paramaters: - 
return: a list composed of the elements from the file
pre-conditions: - 
post-conditions: -
'''

new_list = []

def readFilestoList():

    f = open("/Users/emanuel.paduret/Documents/SL:HL Computer Science/TERM 1/Git_Hub_Repo_EPaduret/name.txt", "r") #I wasn't able to get an universal directory
    new_list = f.readlines() #Append the elements of the file in the list
   
     
    
    pprint (new_list)

readFilestoList()
#print (new_list)


    