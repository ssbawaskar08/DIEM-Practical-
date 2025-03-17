# practical date: 17-03-25 Question2
# Aim: Take input of grade from user and check for the following condition- 1) if the input lies between 0-100 then calculate according to 5rs per unit 2) if the input lies between 101-200 the calculate according to 7rs per unit 3) if input is greater than 200 then calculate according to 10rs per unit.
n=1
while(n):
    unit = int(input("Please enter your Units: "))
    if(unit in range(0,101)):
        print(f"Your Bill is {unit * 5}" )
    elif(unit in range(101,200)):
        print(unit*7)
    elif(unit > 200):
        print(unit*10)
    elif(unit== -1):
        n = 0 
        print("Exitting........!")
    print("for Exit input -1")
 