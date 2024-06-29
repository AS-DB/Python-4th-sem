#4.wap to create a create a list containing the power of said number in bases raised to the corresponding number in the index using map.

list01=eval(input("Enter the list elment:"))
list1=list(list01)

list02=eval(input("Enter the list elment:"))
list2=list(list02)

result=list(map(lambda list1,list2:list1**list2,list1,list2))
print(list(result))

