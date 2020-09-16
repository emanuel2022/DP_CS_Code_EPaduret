def ScaleElementsA(a, b): #Modifier
    for position in range(len(b)):
        b[position] = a * b[position]
        #Side-Effect

things = [2, 5, 9, 31]
print(things)
ScaleElementsA(2, things)
print(things)