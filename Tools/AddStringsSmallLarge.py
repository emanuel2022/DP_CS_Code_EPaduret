def addStringsSmallLarge(a,b):
    
    if len(b) > len(a):
        c = b + a
    else:
        c = a + b

    return c

name1 = "Elephant"
name2 = "Mouse"
adjective1 = "red"
adjective2 = "orange"

print(name2, adjective2)
new_char1 = addStringsSmallLarge(name2, adjective2)
print(new_char1)
print(name1,adjective1)
new_char2 = addStringsSmallLarge(name1, adjective1)
print(new_char2)

