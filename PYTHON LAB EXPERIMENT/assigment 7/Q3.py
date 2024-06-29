#3.WAP to count the frequency of word in a file.
x=input("Enter the substring:")
f=open("File.txt",'r')
d=f.readlines()
print(d.count(x))
f.close()
