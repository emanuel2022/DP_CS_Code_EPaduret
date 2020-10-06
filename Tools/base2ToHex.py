
'''
Description: This function takes a string s consisting of 1 and 0's and converts it to HEX
Parameter: String s

pre-condition: -
post-condition: -

'''


def base2ToHex(s):


    HEX = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    

    #Assignment Statement: Declares result and initializes it to ""
    #This line stores the resulting HEx value that is returned
    result = ""


    #This line adds the appropriate amount of zeros to make the length of s divisible by 4
    #Python specific: 2 * string = stringstring
    s = (4- (len(s))%4) * "0" + s


    #Counted Loop: Looping through s and incrementing by 4
    for i in range (0, len(s), 4):

        '''
        10111111
        i = 0 [0: 0 + 4] = [0:4] --> 1011
        i = 4 [4: 4 + 4] = [4:8] --> 1111 
        '''

        #Using substring string to access 4 characters and store the result in v
        v = s[i: i +4]

        #Accesses each index of v and multiples it by the corresponding power of 2
        #to generate base 2 value of the 4 digits
        # 1011 --> 8 + 2 + 1 = 11
        # 1111 --> 8 + 4 + 2 + 1 = 15
        # Casting: We are casting the strings to integer values. Casting is the process of changing types
        index = int(v[0])*8 + int(v[1])*4 + int(v[2])*2 + int(v[3])*1 
        # By converting the 4 digit base 2 number into base 10, we can use that as the index of HEX to get the value
        result = result + HEX[index]

    # Return result 
    return result

BIN = ["0000","0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001","1010","1011","1100","1101","1110","1111"]

for i in range (0, len(BIN), 1):
    print(base2ToHex(BIN[i]))

print (base2ToHex("10111110101")) # 2F5
print (base2ToHex( "1110111110110")) #1DF6