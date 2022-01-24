#WAP in python to create a dictionary and apply following methods:-
# 1. Print the dictionary items
# 2. access items
# 3. use get()
# 4. change values
# 5. use len()

dic={1:'Apple',2:'Orange',3:'Grapes',4:'Banana',5:'Date'}
print("Original dictionary:",dic)
print("Accesssing items from the dictionary:",dic[3])
print("Accessing items using get function:",dic.get(2))
dic[2]='Strawberry'
print("Dictionary after changing the value:",dic)
print("No. of elements in dictionary using len function:",len(dic))
