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
        total = total + a % 10 #access the ones digit
        a = a//10

    return total
