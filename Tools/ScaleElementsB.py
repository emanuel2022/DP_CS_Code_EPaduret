
'''
Description: This function scales a pre-existing list and scales it according to a parameter
paramaters: a, the scaling parameter and b the list
return: a new list composed of the old list but with scaled elements.
pre-conditions: a has to be a positive integer.
post-conditions: list can not change after it gets passed
'''
def ScaleElementsB(a,b): 
    
    #Pure Function
    #How can the postcondition of a should be to not change the array if
    #it has to multiply it
    #Solution, create a new Array?

    new_list = [] #New list for scaled elements
    for value in b:
        new_elem = a * value
        new_list.append(new_elem)
    return new_list

things = [2,5,9,31]
print(things) #List in unchanged
things = ScaleElementsB(2, things)
print(things) #List is changed