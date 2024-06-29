#WAP to print given length of a string
a=input("Enter the string:")
count=0

for i in a:
    if i!=" " and i!="\t":
        count=count+1   
print(count)