# Question 9
#WAP to enter a string and print it in reverse also print the number of vowels and consonant in it.
count1=0
count2=0

a=input("Enter the String:")
print(a[::-1])

b=["a","e","i","o","u"]

for i in a:
    if i in b:
        count1= count1+1
    else:
        count2= count2+1

print("Number vowels in it:",count1,"Consonent:",count2)