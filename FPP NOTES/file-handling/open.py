a="hello\ni\nam\aditya"

file=open("OPEN","w+")
file.writelines(a)
print(file.readlines())
file.close()

f=open("OPEN","r")
g=f.readlines()
print(*g)
f.close()
