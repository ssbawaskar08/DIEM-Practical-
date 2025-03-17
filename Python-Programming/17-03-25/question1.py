# practical date: 17-03-25
# Aim: Take input of grade from user and check for the following condition- 1) 90-100 => A grade 2) 70-90 => B grade 3) 40-70 => C grade 4) less than 40 => Fail. 
n = 1 
while(n):
    grade = int(input("Please enter your Grade: "))
    if(grade<100 and grade>=90):
        print("A grade")
    elif(grade<90 and grade>=70):
        print("B grade")
    elif(grade<70 and grade>=40):
        print("C grade")
    elif (grade<40 and grade>=0):
        print("Fail !!")
    elif(grade==-1):
        n=0
    print("enter -1 to exit")
