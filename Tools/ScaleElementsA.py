

'''
Description: This function scales a pre-existing list and scales it according to a parameter
paramaters: a, the scaling parameter and b the list
return: a new list composed of the old list but with scaled elements.
pre-conditions: a has to be a positive integer.
post-conditions: -
'''

def ScaleElementsA(a, b): #Modifier
    for i in range(0, len(b), 1):
        b[i] = a * b[i]
        #Side-Effect
    return

things = [2, 5, 9, 31]
print(things)
ScaleElementsA(2, things)
print(things)