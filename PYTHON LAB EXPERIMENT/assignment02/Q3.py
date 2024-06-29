# Question 3
#WAP to find the second largest no in a list containing integers.

a=[1,2,5,6,6,3,0]
max2=a[0]
max1=max(a)
for i in range (0,len(a)):
    if (max2<a[i]) and (a[i]!=max1):
        max2=a[i]
print("2nd largest element in the list:",max2)