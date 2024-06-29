#to check whethere its leap year or not
a=int(input("Enter the year:"))

if a%4==0:
    print(f"{a} is leap year")
else:
    print(f"{a} is not leap year")