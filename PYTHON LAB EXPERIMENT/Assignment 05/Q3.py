#3.wap to enter a set and copy the content of the set into a new set one element at a time.

input_set = {1, 2, 3, 4, 5}  
new_set = set()  

for item in input_set:
    new_set.add(item)  

print("Original Set:", input_set)
print("Copied Set:", new_set)

