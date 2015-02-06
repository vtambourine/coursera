import sys
import math

resulting_array = [int(i) for i in sys.argv[1:][0].split(' ')]
# resulting_array = [int(i) for i in sys.argv[1:]]

# print 'Resulting array:', resulting_array

size = [1] * 10
for n in range(10):
	i = n
	c = 0
	while i != resulting_array[i] and c < 100:
		i = resulting_array[i]
		size[i] += 1
		c += 1

# print 'Sizes at nodes:', size

def check_sizes(id_array):
	for n in range(10):
		if n != id_array[n] and size[n] > size[id_array[n]] / 2:
			return False
	return True

def check_height_and_cycles(id_array):
	length = len(id_array)
	possible_heigth = math.log(len(id_array), 2)
	for n in id_array:
		cylce = 0
		depth = 1
		i = n
		while i != id_array[i]:
			if cylce > length:
				return False
			i = id_array[i]
			cylce += 1
			depth += 1
		if depth > possible_heigth:
			return False
	return True

def check_height(id_array):
	possible_heigth = math.log(len(id_array), 2)
	for n in id_array:
		h = 0
		i = n
		while i != id_array[i]:
			i = id_array[i]
			h += 1

	return True


could_be = check_sizes(resulting_array) and check_height_and_cycles(resulting_array)

# print 'Could be the result of running the weighted quick union algorithm?'
print resulting_array, could_be