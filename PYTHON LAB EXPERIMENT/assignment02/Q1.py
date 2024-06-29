# Question 1
#WAP to enter a percentage and display the gradation system (100-90 = O,89-80 = A,79-70 = C)
a=int(input("Enter the percent:"))

if(a>0 and a<101):
    
    if a in range(90,101):
        print("A")
    elif a in range(80,90):
        print("B")
    elif a in range(60,80):
        print("C")
    elif a in range(40,60):
        print("D")
    elif a in range(32,40):
        print("F")
    else:
        print("Fail")
    '''
    if a>89:
        print("A")
    elif a>80:
        print("b")
    else:
        print("fail")
        '''
else:
    print("Wrong input")
