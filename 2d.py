#WAP in python to write 5 or more digit number in words.

num=int(input("Enter a number: "))
length=len(num)
while(num!=0):
        dig=num%10
        if(dig==0):
                print("Zero",end=" ")
        elif(dig==1):
                print("One",end=" ")
        elif(dig==2):
                print("Two",end=" ")
        elif(dig==3):
                print("Three",end=" ")
        elif(dig==4):
                print("Four",end=" ")
        elif(dig==5):
                print("Five",end=" ")
        elif(dig==6):
                print("Six",end=" ")
        elif(dig==7):
                print("Seven",end=" ")
        elif(dig==8):
                print("Eight",end=" ")
        elif(dig==9):
                print("Nine",end=" ")
        num=num//10
