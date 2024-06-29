#Question 5
#WAP to enter a five digit number and print the digits present at odd locations.
a=int(input("Enter the number"))
digits = str(a)
length = len(digits)
for i in range(0,length+1,2):
    if i % 2 == 0:  
        print(digits[i])