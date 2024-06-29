# Question 3
# WAP to enter three sides of a tringle. Find out the area of the tringle.

a=int(input("Enter the first side:"))

b=int(input("Enter the second side:"))

c=int(input("Enter the third side:"))
s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print(area)