#wap to create an integer list of 20 element increases the odd-valued elements by 5.

a=eval(input("Enter the 20 numbers:"))
b=list(a)
c=[]
for i in b:
    if i%2!=0:
        i=i+5
    c.append(i)

print(c)