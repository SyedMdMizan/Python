#WAP in python to find the factorial of a given number using function.

def fact(n):
    if n==0:
        return 0
    else:
        fac=1
        for i in range(n,0,-1):
            fac*=i
        return fac

num=int(input("Enter a number for which you want factorial: "))
print(fact(num))
