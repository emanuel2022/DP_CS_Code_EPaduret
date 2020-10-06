'''
Description: This function gives the sum of all the digits of a list of doubles
Parameters: List of doubles, data

Pre-conditions: Data has to be a list of doubles, but it can any positive real number
post-conditions: -
'''
def modSum4(data): #Data is passed in the function as a reference type, but is not modified.

    total = 0 #Assignment statement, assigns the value of 0 to itself

    for i in range(0, len(data), 1): # For loop, goes through the length of data and incrementing by 1

        a = data[i] #Number at the n'th iteration
        a = str(a) #Makes the doubles into a strings as to remove the period, casting
        a = a.replace(".", "") #Removes the period and shows abstraction (high-level)

        for j in range(0, len(a), 1): #for loop again, but goes through the 

            v = a[j]
            v = int(v) #Makes the doubles from a string to integers in order to be able to add them together
            total = total + v
        
    print(total)

#Testing
a = [1.2,3.14,7.89,] #Reference type
modSum4(a)