
#Method 1
def base10ToBase2(a):

    if a > 1:
        base10ToBase2(a // 2)
    print(a % 2, end = '')

base10ToBase2(5)
print()

#Method 2
def base10Tobase2(b):
    b = bin(b)
    print(b)

base10Tobase2(6)