import tkinter as tk

def process(*args):

    val = ent_value.get()
    print(val)

    #Check to ensure string of 1's and 0's (by checking if the number of 1's and 0's is equal to the number of characters)
    check = check01(val)
    print (check)

    if (check == True):
        val = remove0(val)
        result = base2to10(val)
        lab_results.config(text = str(val) + " --> " + str(result))

    else:
        lab_results.config(text = "Error: This is not a binary number")

    ent_value.delete(0,tk.END)

def base2to10(str):
    n = 0 
    total = 0 

    for i in range(len(str) - 1, -1, -1):
        total = total + int(str[i])*2**n
        n = n + 1
    return total

def remove0(str):

    for i in range(0, len(str),1):
        if (str[i] == "1"):
            return str[i:]

    return str

def check01(str):
    num_0 = str.count("0")
    num_1 = str.count("1")

    if num_0 + num_1 == len(str):
        return True
    return False

root = tk.Tk()

#Construct the widgets
lab_instruction = tk.Label(root, text = "Enter Binary")
ent_value = tk.Entry(root)
lab_results = tk.Label(root, text = "--")

#Configure the widgets

#Add the widgets to the window
lab_instruction.pack()
ent_value.pack()
lab_results.pack()


root.bind("<Return>", process)
root.mainloop()