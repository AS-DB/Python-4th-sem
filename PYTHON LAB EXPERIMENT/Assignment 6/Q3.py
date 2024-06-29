#3.wap to add three given list using python map and lambda

#list,eval,input
list01=eval(input("Enter the list elment:"))
list1=list(list01)
list02=eval(input("Enter the list elment:"))
list2=list(list02)
list03=eval(input("Enter the list elment:"))
list3=list(list03)

res=list(map(lambda list1,list2,list3:list1+list2+list3,list1,list2,list3))
print(res)
