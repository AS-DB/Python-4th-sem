#1.wap to input two dicitionary an dprints the value by merging the two dictionaries.
dict1=dict2={}

a=int(input("ENter the number of keys occurence for dict1:"))

for i in range(1,a+1):
    key=int(input("Enter the key value:"))
    item=int(input("Enter the item value:"))
    dict1[key]=item

print(f"dict1 value:{dict1}")


b=int(input("ENter the number of keys occurence for dict1:"))

for i in range(1,b+1):
    key=int(input("Enter the key value:"))
    item=int(input("Enter the item value:"))
    dict2[key]=item

print(f"dict1 value:{dict2}")

for i in dict2:
    dict1.update(dict2)

print(dict1)

