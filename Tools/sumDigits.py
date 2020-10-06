
'''
Description: This function returns the sum of the digits of a integer type value
paramaters: an integer a
return: sum
pre-conditions: a has to be an integer
post-conditions: -
'''

def sumDigitsA(a):
    a = str(a) #Casting: the process of changing types of data
    total = 0
    
    #Bread and Butter Algorithm
    for i in range (0, len(a),1):
        total = total + int(a[i])
       
    return total 

print(sumDigitsA(123))


def sumDigitsB(a):
    total = 0

    while (a>0):
        total = total + a % 10 #access the ones digit with mod
        a = a//10 #Get rid of unnecessary digits with floor div

    return total
