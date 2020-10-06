
def linearSearch(a,b):

    found = True
    
    for i in range(0, len(a), 1):
        if a[i] == b:
            found = True
            break
        else:
            found = False
        
    print(found)

a = [0,1,2,3,4,5,6,7,8,9]

linearSearch(a,120)

b = 4