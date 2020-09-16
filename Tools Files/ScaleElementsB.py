def ScaleElementsB(a,b): #Pure Function
    #How can the postcondition of a should be to not change the array if
    #it has to multiply it
    #Solution, create a new Array?
    new_list = []
    for value in b:
        new_elem = a * value
        new_list.append(new_elem)
    return new_list

things = [2,5,9,31]
print(things)
things = ScaleElementsB(2, things)
print(things)