# print 1 to 50 and print 'first_name' if the number is divisible by 3 and print 'last_name' if the number is divisible by 5 and print "first_name" and "last_name if divisible by both"
firstName = "Shreyas"
lastName = "Bawaskar"
for i in range(1, 51):
    if i%3==0 and i%5 == 0 :
        print(firstName+" "+lastName)
    elif i%5 == 0 :
        print(lastName)
    elif i%3 == 0 :
        print(firstName)
    else:
        print(i)
