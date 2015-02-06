import sys

id_array = range(10)
size = [1] * 10
union_operations = sys.argv[1:]

print 'Initial array:', id_array
print 'Union operations sequence', str(union_operations)

def root(i):
	while i != id_array[i]:
		i = id_array[i]
	return i


def union(p, q):
	i = root(p)
	j = root(q)
	if size[i] < size[j]:
		id_array[i] = j
		size[j] += size[i]
	else:
		id_array[j] = i
		size[i] += size[j]
	print p, ' ', q, ' ', i, ' ', j, ' ', id_array


print 'p   q   i   j   resulting_array'

for operation in union_operations:
	p, q = [int(i) for i in operation.split('-')]
	union(p, q)

print 'Resulting array:', id_array
print 'Answer:', ' '.join(map(str, id_array))
