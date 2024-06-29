#wap to print second largest and smallest element in a list of 10 integer without using the sort function.

a=eval(input("Enter the list integer elements:"))
b=list(set(a))
print(b)

minimum=min(b)
maximum=max(b)

print(b)

b.remove(minimum)
b.remove(maximum)

new_minimum=min(b)
new_maximum=max(b)

print(f"second largest number is:{new_minimum} and second smallest number is:{new_maximum}")