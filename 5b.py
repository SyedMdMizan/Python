#WAP in python to print try, except and finally block statement

try:
    n1=int(input("Enter a number: "))
    n2=int(input("Enetr another number: "))
    div=n1//n2

except ZeroDivisionError:
    print("Division by Zero")

else:
    print(n1,"//",n2,"=",div)

finally:
    print("Program terminated")
