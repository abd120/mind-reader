#These lines will import needed modules from the Tkinter library.
from tkinter import *
from tkinter import messagebox

#This line will initiate and create the frame that will contain our gui.
root = Tk()
#This line adds a title in the title bar of our window.
root.title("MindReader")
#Add an icon to the titlebar
root.iconbitmap(r'C:\Users\Abdulrahman\Desktop\mind-reader\tkinter\icon.ico')

#An empty array to store the magical parasites.
arr = []

#Bunch of fuctions for buttons and bindings.
def num_is(event=None):
    messagebox.showinfo(
            "Amazeballs.",
            str(sum(arr))
        )

def clr_arr(event=None):
    arr.clear()

def abt_msg(event=None):
    messagebox.showinfo(
            "About",
            "Coded by code virtuoso, Abdulrahman Tabaza. Twitter: @ruiningcomedy."
        )

def bind_button1(event=None):
    arr.append(1)

def bind_button2(event=None):
    arr.append(2)

def bind_button3(event=None):
    arr.append(4)

def bind_button4(event=None):
    arr.append(8)

def bind_button5(event=None):
    arr.append(16)

def bind_button6(event=None):
    arr.append(32)

#All widgets for the GUI are below, grid is for positioning
greeting1 = Label(root, text="Hello human. Today, I'll be reading your mind.")
greeting1.grid(row=0, column=1, padx=4, pady=4, sticky=W)

greeting2 = Label(root, text="Choose a number between 1 and 63, and I'll guess it. Click the reset button after each try.")
greeting2.grid(row=1, column=1, padx=4, pady=4, sticky=W)

greeting3 = Label(root, text="Below are six sets of numbers, look for your number in each and follow the instructions.")
greeting3.grid(row=2, column=1, padx=4, pady=4, sticky=W)

about_button = Button(root, text="Click to read things.", command=abt_msg)
about_button.grid(row=0, column=2, padx=4, pady=4)

magic_button = Button(root, text="Click to see your number.", command=num_is)
magic_button.grid(row=1, column=2, padx=4, pady=4)

clear_button = Button(root, text="Click to start over.", command=clr_arr)
clear_button.grid(row=2, column=2, padx=4, pady=4)

setone1 = Label(root, text="This is the first set, if you see the number you chose in it, check the box below it.")
setone1.grid(row=4, column=1, padx=4, pady=4, sticky=W)

setone2 = Label(root, text="1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63.")
setone2.grid(row=5, column=1, padx=4, pady=4, sticky=W)

setone3 = Checkbutton(root, text="I see my number.")
setone3.bind("<Button-1>", bind_button1)
setone3.grid(row=5,  column=2, padx=4, pady=4)

settwo1 = Label(root, text="This is the second set, if you see the number you chose in it, check the box below it.")
settwo1.grid(row=8,  column=1, padx=4, pady=4, sticky=W)

settwo2 = Label(root, text="2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, 47, 50, 51, 54, 55, 58, 59, 62, 63.  ")
settwo2.grid(row=9, column=1, padx=4, pady=4, sticky=W)

settwo3 = Checkbutton(root, text="I see my number.")
settwo3.bind("<Button-1>", bind_button2)
settwo3.grid(row=9, column=2, padx=4, pady=4)

setthree1 = Label(root, text="This is the third set, if you see the number you chose in it, check the box below it.")
setthree1.grid(row=12,  column=1, padx=4, pady=4, sticky=W)

setthree2 = Label(root, text="4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, 47, 52, 53, 54, 55, 60, 61, 62, 63.")
setthree2.grid(row=13,  column=1, padx=4, pady=4, sticky=W)

setthree3 = Checkbutton(root, text="I see my number.")
setthree3.bind("<Button-1>", bind_button3)
setthree3.grid(row=13,  column=2, padx=4, pady=4)

setfour1 = Label(root, text="This is the fourth set, if you see the number you chose in it, check the box below it.")
setfour1.grid(row=15,  column=1, padx=4, pady=4, sticky=W)

setfour2 = Label(root, text="8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61, 62, 63.  ")
setfour2.grid(row=16,  column=1, padx=4, pady=4, sticky=W)

setfour3 = Checkbutton(root, text="I see my number.")
setfour3.bind("<Button-1>", bind_button4)
setfour3.grid(row=16,  column=2, padx=4, pady=4)

setfive1 = Label(root, text="This is the fifth set, if you see the number you chose in it, check the box below it.")
setfive1.grid(row=19,  column=1, padx=4, pady=4, sticky=W)

setfive2 = Label(root, text="16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63.")
setfive2.grid(row=20,  column=1, padx=4, pady=4, sticky=W)

setfive3 = Checkbutton(root, text="I see my number.")
setfive3.bind("<Button-1>", bind_button5)
setfive3.grid(row=20,  column=2, padx=4, pady=4)

setsix1 = Label(root, text="This is the sixth set, if you see the number you chose in it, check the box below it.")
setsix1.grid(row=23,  column=1, padx=4, pady=4, sticky=W)

setsix2 = Label(root, text="32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63.  ")
setsix2.grid(row=24,  column=1, padx=4, pady=4, sticky=W)

setsix3 = Checkbutton(root, text="I see my number.")
setsix3.bind("<Button-1>", bind_button6)
setsix3.grid(row=24,  column=2, padx=4, pady=4)

#To keep the hamsters rolling the wheel so the gui works.
root.mainloop()
