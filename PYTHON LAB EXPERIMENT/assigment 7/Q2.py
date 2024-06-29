#WAP to read a file line by line and store in into a list.
s=[]
f=open("File.txt",'r')
d=f.readlines()
s.extend(d)
print(d)
f.close()

