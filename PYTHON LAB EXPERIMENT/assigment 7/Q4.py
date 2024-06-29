#.WAP to copy the content of a file to another file.
with open("File.txt", "r") as f:
 file_contents = f.read()
with open("Copy.txt", "w") as q:
 q.write(file_contents)
with open("Copy.txt", "r") as r:
 print(r.read())
