# Question 6
#WAP to enter a number and check whether it is palindrome or not.
a=input("enter the number:")
b=(a[::-1])

if (a==b):
    print("Its pallindrome")
else:
    print("Its not pallindrome")