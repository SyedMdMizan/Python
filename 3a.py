#WAP in python to create a list and perform following methods:-
# 1.insert()
# 2.remove()
# 3.append()
# 4.len()
# 5.pop()
# 6.clear()

lst=[1,2,3,4,5]
print("Original list: ",lst)
lst.insert(1,20)#insert func to insert a element at certain index
print("List after using insert function to insert 20 at index 1: ",lst)
lst.remove(5)#remove func to remove a certain element
print("List after using remove function to remove 5: ",lst)
lst.append(10)#append func to add an element at the end of list
print("List after using append function to append 10 in the list: ",lst)
print("No. of elements in list using len function: ",len(lst))
lst.pop()
print("List after using pop function: ",lst)
lst.clear()
print("List after using clear function: ",lst)


