

def findModSum1(data):
    total = 0

    for i in range(0, len(data), 1):
        if data[i] % 3 == 0:
            total = total + data[i]
            
    print (total)

a = [0,1,2,3,4,5,6,7,8,9,10] #18
b = [0,3,6,9,12,15,18,21] 
c = [0,53525,12512,342341,21321235,1232252]

findModSum1 (c)


