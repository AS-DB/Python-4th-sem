#1.wap to enter two different sets with string element combine both the set remove any dupliccate are present, printthe new set.
set1=eval(input("Enter the set elements:"))
set2=eval(input("Enter the set elements:"))

set3=set(set1)
set4=set(set2)

#print(set3)

set3.update(set4)
print(f"merge value of set is {set3}")

