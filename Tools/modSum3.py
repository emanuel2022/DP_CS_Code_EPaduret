'''
Description: This function gives the sum of all the multiples of two ints from a set function
paramaters: a list of data, two integers
return: sum of all multiples from the list
pre-conditions: lst has to be a list of integers
post-conditions: -
'''
def modSum3(data, a, b):

    total = 0

    for i in range(0, len(data), 1):
        if data[i] % a  == 0 and data[i] % b == 0:
            total = total + data[i]

    print(total)

lst = [21,30,10,99,14,2,100]
modSum3(lst, 2, 1)