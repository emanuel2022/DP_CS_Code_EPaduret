
def findModSum2(data, a, b):
    total = 0
    for i in range(0, len(data), 1):
        if data[i] > a and i < b or i < a and i >b:
            total = total + data[i]
    print (total)

a = [2,3,10,9,14,25,3,100]
findModSum2(a,5,25)

#figure out which one is bigger before the for loop