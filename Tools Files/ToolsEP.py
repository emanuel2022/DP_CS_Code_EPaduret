'''
isEven takes a single integer paramater a >= 0 returning true if a is even 
and false if a is odd.
'''
def isEven (a):
    if a % 2 == 0:
        return True
    return False

#Test Code for isEven
print(isEven (0))
print(isEven (1))
print(isEven (2))

#Batch Test for isEven
for i in range (0, 100, 1):
    print(isEven(i))


def base2To10(str)