# generate random values and create a guess game. 
import random
num=random.randint(0, 100)
print(num)
r = True
print("------------------------------------Welcome to the number guessing game!-----------------------------------------")
print("I am thinking of the number between 0 and 100.") 
guess = int(input("Guess a number between 0 and 100: "))
attempt=0

while (r) :
    if guess in range(num-10,num+10) and guess!=num :
        print("You are Close.....!!!!")
    if guess < num:
        print("Think a Little Higher")
        guess = int(input("Guess a number between 0 and 100: "))
        attempt=attempt+1
    elif guess > num:
        print("Think a little Lower")
        guess = int(input("Guess a number between 0 and 100: "))
        attempt=attempt+1
    else:
        attempt=attempt+1
        print(f"\n\nYou got the Right number in {attempt} attempts........ Congratulations")
        r = False


