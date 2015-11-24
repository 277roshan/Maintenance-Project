import itertools

def data_structure(length_of_module):
	tree = {}
	with open('input.txt') as f:
		while True:
			a = f.readline()
			a = a.split()
			if a[0] == '**':
				defective = f.readline()
				break
			if len(a[0]) > length_of_module or len(a[1]) > length_of_module:
				return False
			if a[0] not in tree.keys():
				tree[a[0]]=[a[1]]
			else:
				tree[a[0]].append(a[1])
	
	return tree, defective

def get_transactions(tree):
	a = tree.keys()
	b = tree.values()
	b = list(itertools.chain(*b))
	b = set(b)
	b = list(b)
	transactions = []
	for i in a:
		if i not in b:
			transactions.append(i)
	return transactions

def unique_modules(tree, transaction):
	visited = []
	queue = [transaction]

	while True:
		if len(queue) == 0:
			return visited[1:]
		value = queue.pop()
		if value not in visited:
			# print value
			visited.append(value)
		if value in tree.keys(): 
			for i in tree[value]:
				# print tree[value]
				# print i
				# print visited
				if i not in visited:
					queue = [i] + queue


def all_paths(tree, transaction, defective):
	queue = [[transaction]]
	required_paths = []
	rest = []
	while queue:
		a = queue.pop()
		if a[-1] in tree.keys():
			for i in tree[a[-1]]:
				if i not in a:
					new = a + [i]
					queue = [new] + queue
					if i == defective:
						required_paths.append(new)
					else:
						rest.append(new)

	# print required_paths
	check_point = []

	final = []
	for i in rest:
		for j in required_paths:
			if i[-1] == j[1]:
				final.append(i + j[2:])

	return final
				
		

		
		

		
		

		

	# print required_paths

#test
tree,defective = data_structure(3)
x = get_transactions(tree)
# for i in x:
# 	m = unique_modules(tree, i)
# 	print "Unique modules for", i
# 	print m
# 	print "Number of unique modules:",len(m)

print all_paths(tree,'A','F')
# print tree