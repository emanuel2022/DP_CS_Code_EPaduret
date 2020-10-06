'''
Description: This function removes a character from a string at index n 
paramaters: a string and a number
return: a new string with all characters except the one from index n
pre-conditions: valid string, valid int
post-conditions: -
'''

def missing_char(str, n):
  new_str = ""
  
  for i in range(0, len(str), 1):
    if i != n: 
      new_str = new_str + str[i] #Adds every characters except the one at index n to the new string
      
  print(new_str)

missing_char("elephant", 2)