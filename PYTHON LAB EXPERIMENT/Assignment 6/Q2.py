#2.wap to triple all numbers in a given list of integers. use map()

def triple(a):
    return 3*a

list01=eval(input("Enter the list elment:"))
list1=list(list01)

result=map(triple,list1)
print(list(result))

