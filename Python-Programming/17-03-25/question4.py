# 3 membership option 1) Gold 2)Silver 3)Regular 
# condition1: if gold membership and 
#                 purchase more than 1000 then disccount 30%
#                 purchase more than 500 then 20%
#                 purchase more than 100 then 10%
# condition2: if silver membership and 
#                 purchase more than 1000 then disccount 20%
#                 purchase more than 500 then 15%
#                 purchase more than 100 then 5%
# condition1: if regular membership and 
#                 purchase more than 1000 then disccount 10%
#                 purchase more than 500 then 5%
n = 1
while(n):
    print("Chose the Index from the menu:\n\t 1. Gold\n\t 2. Silver\n\t 3. Regular\n\t 4. Exit")
    member = int(input("Enter your membership index: "))
    match(member):
        case 1 :
            spend = int(input("Enter your Spending amount: "))
            if(spend > 1000):
                print(f'Your Discount Amount is : {spend*0.3}')
            elif(spend in range(500,1001)):
                print(f'Your Discount Amount is : {spend*0.2}')
            elif(spend in range(100,501)):
                print(f'Your Discount Amount is : {spend*0.1}')
            elif(spend in range(0,101)):
                print("OOPSSS!!!! No discount Applicable")
            else:
                print("Enter amount above 0 RS .")
        case 2 :
            spend = int(input("Enter your Spending amount: "))
            if(spend > 1000):
                print(f'Your Discount Amount is : {spend*0.2}')
            elif(spend in range(500,1001)):
                print(f'Your Discount Amount is : {spend*0.15}')
            elif(spend in range(100,501)):
                print(f'Your Discount Amount is : {spend*0.05}')
            elif(spend in range(0,101)):
                print("OOPSSS!!!! No discount Applicable")
            else:
                print("Enter amount above 0 RS .")
        case 3 :
            spend = int(input("Enter your Spending amount: "))
            if(spend > 1000):
                print(f'Your Discount Amount is : {spend*0.1}')
            elif(spend in range(500,1001)):
                print(f'Your Discount Amount is : {spend*0.05}')
            elif(spend in range(0,501)):
                print("OOPSSS!!!! No discount Applicable")
            else:
                print("Enter amount above 0 RS .")
        case 4:
            print("Exitting...........! Have A good day")
            n=0
        case _:
            print("Please enter choice between 1 and 3. ")