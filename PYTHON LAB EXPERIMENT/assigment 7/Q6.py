#WAP to combine each line from first file with the corresponding line in second file.
with open("File.txt",'a+') as e:
 c=e.readlines()
with open("File1.txt",'a+') as f:
 d=f.readlines()
b=min(len(d),len(c))
comline=[]
for i in range(b):
 comline.append(d[i].strip()+c[i])
with open("Result.txt",'a+') as f1:
 f1.write("".join(comline))
with open("Result.txt", "a+") as f2:
 print(f2.read())
