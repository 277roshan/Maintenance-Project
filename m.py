import itertools

def data_structure(length_of_module):
	tree = {}
	with open('input.txt') as f:
		while True:
			a = f.readline()
			a = a.split()
			if a[0] == '**':
				break
			if len(a[0]) > length_of_module or len(a[1]) > length_of_module:
				return False
			if a[0] not in tree.keys():
				tree[a[0]]=[a[1]]
			else:
				tree[a[0]].append(a[1])

	return tree

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

#test
tree = data_structure(3)
print get_transactions(tree)


