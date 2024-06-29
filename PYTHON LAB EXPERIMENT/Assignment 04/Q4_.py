#wap to create a function thtat prints the first 15 terms of the fibonacchi series without using recursion.

a=int(input("Enter the number:"))
b=[0,1]
if a==0 or a==1:
    print("1")
else:
    print("0\n1")
    for i in range(2,a+1):
        term=b[i-1]+b[i-2]
        b.append(term)
        print(term)