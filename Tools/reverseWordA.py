
'''
Description: This function reverses a string
Parameters: s, a string 
return: a new string composed of the reversed string

pre-conditions: s has to be a string
post-conditions: -
'''

#Method A
def reverseWordA(s):

    new_lst = []
    i = len(s) #I for index
    
    while i > 0: #Index 
        i = i - 1
        new_lst.append(s[i]) #Appends the letter to a list in an inverted order

    new_str = ""
    new_str = new_str.join(new_lst) #Creates a string out of the list

    print(new_str)

reverseWordA("catto")

#Method B
def reverseWordB(s): #Reverses the word
    word = s[::-1]
    print(word)

reverseWordB("cat")

#Method C
def reverseWordC(s):
    new_str= "".join(reversed(s)) #Uses the built-in function reversed to create a new string composed of the reversed string
    print(new_str)

reverseWordC("cat")