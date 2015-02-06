import sys

initial_array = range(10)
union_operations = sys.argv[1:]

print 'Initial array:', initial_array
print 'Union operations sequence', str(union_operations)

def union(p, q):
	p_id = initial_array[p]
	q_id = initial_array[q]
	for i, i_id in enumerate(initial_array):
		if i_id == p_id:
			initial_array[i] = q_id
	print p, ' ', q, ' ', p_id, ' ', q_id, ' ', initial_array

print 'p   q  pid qid  resulting_array'

for operation in union_operations:
	p, q = [int(i) for i in operation.split('-')]
	union(p, q)

print 'Resulting array:', initial_array
print 'Answer:', ' '.join(map(str, initial_array))