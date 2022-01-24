#WAP in python to create a tuple and apply following methods:-
# 1. Add items
# 2. len()
# 3. check for item in tuple
# 4. access items

tup=(1,2,3,4,5)
print("Original tuple:",tup)
print("Length of tuple:",len(tup))
n=int(input("Enetr the number you want to find in tuple: "))
if n in tup:
    print("Item present in tuple")
else:
    print("Item not present in tuple")
print("Item at index 3:",tup[3])

