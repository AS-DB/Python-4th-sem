#5.wap to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence.use map() function.

def upper01(a):
    return a.upper()


def lower01(a):
    return a.lower()

a=int(input("ENter the number of characters:"))
b=[]
for i in range(1,a+1):
    l=input("Enter the character:")
    b.append(l)
    

result=map(upper01,b)
print(list(result))


result2=map(lower01,b)
print(list(result2))
