#wap to print factorial of a number
'''
import math

a=int(input("enter the number:"))
b=math.factorial(a)

print(b)
'''

def fact(a):
    if a==1:
        print(a)
    elif a==0:
        print(a)
    else:
        fact=1
        for i in range(a,0,-1):
            fact=fact*i
        print(f"factorial of {a} is:{fact}")

num1=int(input("Enter the number:"))
fact(num1)                