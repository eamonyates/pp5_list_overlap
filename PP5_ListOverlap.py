import random


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
d = random.sample(range(100), 11)
e = random.sample(range(100), 13)


def merge_lists(list1,list2):
	c = []
	for number in list1:
		if number in c:
			continue
		elif number in list2:
			c.append(number)
		else:
			continue
	print (list1)
	print (list2)
	print (c)


if __name__ == "__main__":
	merge_lists(d,e)
