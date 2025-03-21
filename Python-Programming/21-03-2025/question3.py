# even number count and odd number count between 1 - 100
even_count = 0
odd_count = 0
for i in range(1,101):
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
else:
    print("Even number count between 1-100 is: ", even_count)
    print("Odd Number count between 1-100 is: ", odd_count)