#Question 5
# WAP to enter an integer number and find out its binary, octal and hexadecimal equivalents.

a=int(input("Enter the value of a:"))
b=bin(a)
c=hex(a)
d=oct(a)

print(f"binary:{b},hexadecimal:{c} and octal:{d}")