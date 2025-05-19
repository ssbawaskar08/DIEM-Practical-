import random

ticketNum = random.sample(range(0,10),4)
finalTicket = "".join(str(n) for n in ticketNum)
r=True
print(finalTicket)
guess = (input("Enter Your Lottery number: "))
attempt = 0
while r:
    if guess < finalTicket:
        print("Wrong Choice ,Think a Little Higher")
        guess = (input("Enter Your Lottery number: "))
        attempt=attempt+1
    elif guess > finalTicket:
        print("Wrong Choice, Think a little Lower")
        guess = (input("Enter Your Lottery number: "))
        attempt=attempt+1
    else:
        attempt=attempt+1
        print(f"\n\nYou got the Lottery!!!! {attempt} attempts........ Congratulations")
        r = False
    