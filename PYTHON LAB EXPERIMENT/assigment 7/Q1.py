#WAP to read last n lines of files.
n=int(input("Enter a number:"))
f=open("File.txt",'r')
data=f.readlines()
q=data[-1:-n:-1]
for i in q:
 print(i)
f.close()
