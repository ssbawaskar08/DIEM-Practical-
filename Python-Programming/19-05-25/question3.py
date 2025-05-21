import random
choices = ["rock", "paper", "scissors","exit"]
while(True):
    userChoice = input("Enter rock, paper, scissors or exit: ").lower()
    if userChoice not in choices:
        print("Invalid choice! Please enter rock, paper, scissors or exit")
    elif userChoice == "exit":
        exit()
    else:
        computerChoice = random.choice(choices)
        print(f"Computer chose: {computerChoice}")
        if userChoice == computerChoice:
            print("It's a tie!")
        elif (userChoice == "rock" and computerChoice == "scissors") or \
            (userChoice == "paper" and computerChoice == "rock") or \
            (userChoice == "scissors" and computerChoice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")