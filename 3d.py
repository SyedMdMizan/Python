#WAP of function in pyhton that takes two list and return True if they are equal otherwise false
def equality(x,y):
    if sorted(x)==sorted(y):
        return True
    else:
        return False

lst1=[]
lst2=[]
n1=int(input("Enter the elements you want to input in list 1: "))
for i in range(n1):
    x=int(input())
    lst1.append(x)
n2=int(input("Enter the elements you want to input in list 2: "))
for i in range(n2):
    x=int(input())
    lst2.append(x)
print("list 1:",lst1)
print("List 2:",lst2)
print(equality(lst1,lst2))
