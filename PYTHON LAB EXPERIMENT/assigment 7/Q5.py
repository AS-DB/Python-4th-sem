#WAP that takes a text file as input and returns the number of words of a given text file.
f=open("File.txt",'r')
d=f.read()
a=d.split()
y=len(a)
print("The total num,ber of words present in the list is :",y)
f.close()
