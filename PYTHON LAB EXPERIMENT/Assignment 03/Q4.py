#wap to check whether the string is pallindrome
a=input("Eneter the string:")
b=a[::-1]

if a==b:
    print(f"{a} is pallindrome in nature")
else:
    print(f"{a} is not pallindrome in nature")