
def mergeStrings(a,b):
    l1 = a.copy()
    l2 = b.copy()fo
    #l3 = [i + j for  i,j in zip(l1,l2)]
    while len(l1) > len(l2):
        l2.append("")
    while len(l2) > len(l1):
        l1.append("")

    l3 = [ "".join(z) for z in zip(l1,l2)]
    print(l3)
    print(a,b)

    

a = ["one", "two", "three", "four"]
b = ["one", "two", "three","four", "five"]

mergeStrings(a,b)