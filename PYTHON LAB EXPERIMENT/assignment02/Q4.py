# Question 4
#WAP to find the minimum number from three different numbers using ternary operator.
a,b,c=10,25,6
min=a if a<b and a<c else b if b<a and b<c else c
print("Minimun number=",min)