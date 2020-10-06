
def addStringsSmallLarge(a,b):

    if len(a) >= len(b):
        c = a + b
        return c
    else:
        d = b + a
        return d
    

print(addStringsSmallLarge("elephant", "tiger"))
print(addStringsSmallLarge("mouse", "blue"))
print(addStringsSmallLarge("one", "two"))