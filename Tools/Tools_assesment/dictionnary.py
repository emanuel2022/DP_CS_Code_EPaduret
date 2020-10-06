from pprint import pprint #As to make the dictionary more readable when printed at the end of the function
#Presence of modules: High level language because high level of abstraction
'''
Description: This function finds all the prime numbers from a to b, which are two integers, and stores i) all the numbers 
inside a dictionary and ii) all the prime numbers in another dictionary
Parameters: A and B, which serve of range value, must be positive integers

Pre-Conditions: -
Post-Conditions: - 

'''
def primes(a,b):

    #Dictionaries are dynamic data structure, because their size can change
    d_all = {} #New dictionaries, which are empty, in order to store all the number or all the prime numbers only
    d_prime = {}

    for i in range(a,b+1,1): #b+1, in order to make it inclusive, with a increment of one
        if i > 1: #Prime number needs to be bigger than one
            for j in range(2,i): #Nested for loop
                if(i%j ==0): #Checks if i divided j has a rest. If it does, it's a prime number, as they can't be divided by any number (except one and itself)
                    #print(i, "is not a prime")
                    d_all[i] =  "is not a prime" #Stores the prime number i , which is the key, with the assigned value "is not a prime" in the dictionary
                    break #Important, as it make it faster (not so important but still, good manners)
            else:
                #print(i, "is a prime")
                d_all[i] =  "is a prime"
                d_prime[i] = "is a prime"
    pprint(d_all)
    pprint(d_prime)

#Testing

a = 1
b = 100

primes(a,b)