#wap to remove all duplicates value from given string

a=(input("Enter the string:"))
b=[]
for i in a:
    b.append(i)
b.sort()    
c=list((set(b)))
for t in c:
    print(t)