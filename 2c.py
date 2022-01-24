#WAP in python to find the highest prime number in a range.
def prime(x, y):
	prime_list = []
	for i in range(x, y):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				prime_list.append(i)
	return prime_list

starting_range = int(input("Starting range: "))
ending_range = int(input("Ending range: "))
lst = prime(starting_range, ending_range)
print("Maximum prime number is",max(lst))

