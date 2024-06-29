#wap to create two lists first list containing 5 integer and a second list containg 5 string.print both list one element from each list combined at a time.

a=eval(input("Enter the list integer elements:"))
b=list(a)

c=eval(input("Enter the list integer elements:"))
d=list(c)

e=[]
for i in range(len(b)):
    e.append((b[i],d[i]))

print(e)