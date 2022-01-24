#WAP to create a menu with fpollowing options:-
# 1. To perform Addition
# 2. To perform Subtraction
# 3. To perform Multiplication
# 4. To perform Division
#Accepts user input and perform the operation accordingly.
#Use functions with arguments.
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
i=1
while(i==1):
    n1=int(input("Enetr a number: "))
    n2=int(input("Enetr another number: "))
    print("1. Add( + )\n2. Sub( - )\n3. Mul( X )\n4. Div( / )")
    op=int(input("Enetr the operation no.: "))
    if op==1:
        print(add(n1,n2))
    elif op==2:
        print(sub(n1,n2))
    elif op==3:
        print(mul(n1,n2))
    elif op==4:
        print(div(n1,n2))
    else:
        print("Input out of range!!")
    i=int(input("Do you want to perform again(1/0): "))
