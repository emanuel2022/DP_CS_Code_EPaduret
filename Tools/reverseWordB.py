
'''
Description: This function reverses a list of strings and creates a new list composed of the reversed strings
paramaters: a list of strings
return: a new string composed of the reversed strings
pre-conditions: lst has to be a list of strings
post-conditions: -
'''

def reverseWordB(lst):

    new_list = [] #New list where reversed elements will be stored

    for i in range(0 , len(lst), 1):
        a = lst[i]
        new_c = a[::-1] #Reverses the order of the word at index i
        new_list.append(new_c) #Appends the reversed word to a list
    
    new_str = ""
    new_str = new_str.join(new_list) #Creates a new string composed of all the elements from the new list

    print(new_str)
        
#testing
l = ["cat", "doggo", "elephant", "anna", ""]
reverseWordB(l)
