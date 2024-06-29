# Question 9
# WAP to enter two numbers nd swap them using bitwise operators.

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))

c=a^b
a1=a^c
b1=b^c

print(f"before swapping a and b are {a} and {b} respectivily \n after swapping a and b are {a1} and {b1} respectively")
