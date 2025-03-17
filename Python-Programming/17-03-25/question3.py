# variable name balance = 1000/- 2nd variable is amount(for withdrawal):
#  condition1 if amount grater than balance then display insuffiecient balance
#  condition2 amount should be the multiples of 100
#  condition3 if the balance - amount after successful transaction and display current balance 
balance = 1000
amount = int(input("Enter the Amount you wish to withdraw: "))
if(amount < balance):
    if(amount %10 != 0):
        print("Please enter the withdrawal ammount in multiples of 10")
    elif(amount %10 == 0):
        print(f'Your Current balance is {balance-amount}')
else:
    print("Insufficient Balance ")