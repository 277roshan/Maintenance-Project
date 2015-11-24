'''Program to implement maintenace project.'''
import itertools

def data_structure(length_of_module):
	'''Create required data structure taking length_of_module as input'''
	tree = {}
	with open('input.txt') as f:
		while True:
			a = f.readline()
			a = a.split()
			if a[0] == '**':
				defective = f.readline()
				defective = defective.split()
				break
			if len(a[0]) > length_of_module or len(a[1]) > length_of_module:
				return False
			if a[0] not in tree.keys():
				tree[a[0]]=[a[1]]
			else:
				tree[a[0]].append(a[1])
	return (tree,defective[0])

def get_transactions(tree):
	'''Get all available transactions.'''
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
	'''Find and return all unique modules for a transaction.'''
	visited = []
	queue = [transaction]

	while True:
		if len(queue) == 0:
			return visited[1:]
		value = queue.pop()
		if value not in visited:
			visited.append(value)
		if value in tree.keys(): 
			for i in tree[value]:
				if i not in visited:
					queue = [i] + queue


def all_paths(tree, transaction, defective):
	'''Find all paths to a defective module from a given transaction by breadth first search.'''
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
	check_point = []
	final = []
	for i in rest:
		for j in required_paths:
			if i[-1] == j[1]:
				final.append(i + j[2:])

	return final


def explosion(tree, transaction):
	'''Show the explosion for a transaction by depth first search.'''

	visited = []
	stack = [(transaction,0)]
	s = 0

	while stack:
		vertex, space = stack.pop()
		for i in xrange(space):
			print ' ',
		print vertex
		
		if vertex not in visited:
			visited = visited + [vertex]
			if vertex in tree.keys():
				s += 1
				for i in reversed(tree[vertex]):
					if i not in visited:
						stack.append((i,s))
					else:
						for k in xrange(space + 1):
							print ' ',
						s-=2
						print i,'*' 


def main():
	#test
	data = data_structure(10)
	try:
		tree = data[0]

		# print tree
		defect = data[1] 
		transactions = get_transactions(tree)


		print
		for i in transactions:
			m = unique_modules(tree, i)
			print "Unique modules for transaction", i,":"
			for i in m:
				print i,
			print
			print "Number of unique modules is",len(m)
			print

		print "Paths from the transaction to the given defective module"
		for i in transactions:
			print
			print "Path from",i,"to",defect
			print i, "TO",defect
			ans = all_paths(tree, i, defect)
			for i in ans:
				for j in i:
					print j,
				print

		print
		print 'Explosion of the above system'
		print
		for i in transactions:
			print 'Explosion for transaction',i
			explosion(tree,i)
			print 

	except:
		print "Module Characters more than 10. Please correct!" 


if __name__ == "__main__":
	main()