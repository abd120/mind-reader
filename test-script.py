import os
from time import sleep

print("Hello human. Today, I'll be reading your mind.")
sleep(5)
print("Choose a number between 1 and 63. I'll wait.")
sleep(5)
os.system('clear')

print("I will show you six sets of numbers.")
sleep(3)
print("Each set has 32 numbers on it, one of them might be yours, tell me when you see it.")
sleep(3)
print("If you have chosen a number, and we're ready to roll.")
sleep(3)
os.system('clear')

arr = []

print("This is the first set.")
sleep(2)
print(1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63)
print("If you see your number, enter: Yes.")
card_one = str(raw_input("Do you see it?"))
if card_one == "Yes":
    arr.append(1)
os.system('clear')

print("This is the second card.")
sleep(2)
print(2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31,34,35,38,39,42,43,46,47,50,51,54,55,58,59,62,63)
print("If you see your number, enter: Yes.")
card_two = str(raw_input("Do you see it?"))
if card_two == "Yes":
    arr.append(2)
os.system('clear')

print("This is the third card.")
sleep(2)
print(4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31,36,37,38,39,44,45,46,47,52,53,54,55,60,61,62,63)
print("If you see your number, enter: Yes.")
card_three = str(raw_input("Do you see it?"))
if card_three == "Yes":
    arr.append(4)
os.system('clear')

print("This is the fourth card.")
sleep(2)
print(8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31,40,41,42,43,44,45,46,47,56,57,58,59,60,61,62,63)
print("If you see your number, enter: Yes.")
card_four = str(raw_input("Do you see it?"))
if card_four == "Yes":
    arr.append(8)
os.system('clear')

print("This is the fifth card.")
sleep(2)
print(16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63)
print("If you see your number, enter: Yes.")
card_five = str(raw_input("Do you see it?"))
if card_five == "Yes":
    arr.append(16)
os.system('clear')

print("This is the sixth card.")
sleep(2)
print(32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63)
print("If you see your number, enter: Yes.")
card_six = str(raw_input("Do you see it?"))
if card_six == "Yes":
    arr.append(32)
os.system('clear')

print("Allow me to blow your socks off!")
sleep(2)
print ("The number you chose is:")
print sum(arr)
sleep(2)
print("Yes I know, It's very impressive. Well, that's how I roll.")

sleep(10)
