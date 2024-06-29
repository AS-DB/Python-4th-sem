# Question 4
# WAP to enter the coefficients of a quadratic equation and findout the roots of the equivalent
a=int(input("Enter the coefficient of x^2:"))
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the constant:"))
d=(b**2-(4*a*c))**0.5
if(d>0):
    r1=(-b+d)/(2*a)
    r2=(-b-d)/(2*a)
    print("Root 1=",r1)
    print("Root 2=",r2)
elif(d==0):
    r1=(-b+d)/(2*a)
    print("Root1=Root2=",r1)
else:
    print("No real roots.")
