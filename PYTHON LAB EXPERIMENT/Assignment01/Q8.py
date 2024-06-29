# Question 8
# WAP to enter time in minutes and print it in hour and minute format.

a=int(input("Enter the seconds:"))
hours= a//3600
minutes=(a%3600)//60
seconds=a%60

print(f"{hours}:{minutes}:{seconds}")