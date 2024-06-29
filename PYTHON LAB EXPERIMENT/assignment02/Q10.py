# Question 10
#WAP to enter a 3 digit number and print all the prime factors of the number.

a=int(input("Enter the number:"))

for i in range(2,a+1):
    c=0
    if a%i==0:
        for j in range(2,i):
            if i%j==0:
                c=c+1
        if c==0:
            print(i)        
            
