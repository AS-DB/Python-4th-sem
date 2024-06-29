# Question 2
#WAP to enter a 5 digit number and print the digits present at odd locations using while loop

a = int(input("Enter a 5-digit number: "))
digits = str(a)
length = len(digits)
i = 0
while i < length:
    if i % 2 == 0:  
        print(digits[i])
    i += 1
