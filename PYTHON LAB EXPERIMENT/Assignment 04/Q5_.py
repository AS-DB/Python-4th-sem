#wap to create a function that takes the list as an argument and returns the even value of thre list. print the new list even values

def list_even(b):
    c=[]
    for i in b:
        if i%2==0:
            c.append(i)
    print(c)


a=eval(input("Enter the numbers list:"))
b=list(a)

list_even(b)