'''
    S = passed string parameter only containing hex characters
    HEX = ["0", "1", "2", ..., "E", "F"]
    BIN = ["0000", ... "1111"]

    RESULT = ""
    Loop through S from end to start

    Loop N from S.length - 1 to 0:
        Loop I from 0 to len(HEX) - 1
            if HEX[I] == N
                RESULT = BIN[I] + result
            end if
        end loop
    end loop

    return result

'''

'''
Commenting for understanding:

Description: This function takes a string containing HEX characters 
adn returns the base2 conversion as a string

Parameters: String S
Return: S
precondition: s contains only hex characters
post-condition: if you pass a list as a parameter

'''
'''
Commenting for learning: 

'''


def hexToBase2(s):
    HEX = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    BIN = ["0000",
           "0001", 
           "0010", 
           "0011", 
           "0100", 
           "0101", 
           "0110", 
           "0111",
           "1000", 
           "1001",
           "1010",
           "1011",
           "1100",
           "1101",
           "1110",
           "1111"]

    Result = ""

    for n in range(len(s) -1, -1, -1):
        for i in range(0, len(HEX), 1):
            if HEX[i] == s[n]:
                Result = BIN[i] + Result

    return Result

print(hexToBase2("A12"))
print(hexToBase2("F"))

