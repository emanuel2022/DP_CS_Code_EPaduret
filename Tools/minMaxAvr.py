

def minMaxAvr1(a):
    a.sort()
    maximum = a[-1]
    minimum = a[0]
    
    total1 = 0
    total2 = len(a)

    for i in range(0, len(a), 1):
        total1 = total1 + a[i]
    
    average = total1/total2
    
    print(maximum)
    print(minimum)
    print(average)

a = [1,2,3,4,5,6,7,8,9,10]
minMaxAvr1(a)

def minMaxAvr2(a):
    maximum = 0
    minimum = maximum

    for i in range(0 , len(a), 1):
        if a[i] > maximum:
            maximum = a[i]
    
    for i in range(0, len(a), 1):
        if a[i] < minimum:
            minimum = a[i]

    total1 = 0
    total2 = len(a)

    for i in range(0, len(a), 1):
        total1 = total1 + a[i]
    
    average = total1/total2
    
    print(maximum)
    print(minimum)
    print(average)

a = [1,2,3,4,5,6,7,8,9,10]
minMaxAvr2(a)
