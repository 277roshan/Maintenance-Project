'''Program to implement maintenace project.'''

import itertools

def data_structure(length_of_module, file_name):
	'''Create required data structure taking length_of_module as input'''
	tree = {}
	with open(file_name) as f:
		while True:
			a = f.readline()
			a = a.split()
			# print a
			if a[0] == '*':
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


	final = [ ' '.join(i) for i in final]
	required_paths = [' '.join(i) for i in required_paths]
	final = final + required_paths
	final = set(final)
	final = list(final)

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
				
				for i in reversed(tree[vertex]):
					if i not in visited:
						stack.append((i,space + 1))
					else:
						for k in xrange(space + 1):
							print ' ',
						s-=2
						print i,'*' 


def main():
	'''Main program to test the modules.'''
	data = data_structure(10, 'inp.txt')
	try:
		tree = data[0] #Get tree structure for the dataset
		print tree
		defect = data[1]  #Get the defective module
		transactions = get_transactions(tree) #Get all transactions in the tree structure

		#Find unique modules
		print
		for i in transactions:
			m = unique_modules(tree, i)
			print "Unique modules for transaction", i,":"
			for i in m:
				print i,
			print
			print "Number of unique modules is",len(m)
			print
		#Find unique modules

		#Find all paths from a transaction to given defective module
		print "Paths from the transaction to the given defective module"
		for i in transactions:
			print
			print i, "TO",defect
			ans = all_paths(tree, i, defect)
			for i in ans:
				for j in i:
					print j,
				print

		print
		#Find all paths from a transaction to given defective module

		# Find explosion of the above system for particular transactions
		print 'Explosion of the above system'
		print
		for i in transactions:
			print 'Explosion for transaction',i
			explosion(tree,i)
			print 
		# Find explosion of the above system for particular transactions

	except:
		print "Module Characters more than 10. Please correct!" # Error message in case module names are more than 10 characters


if __name__ == "__main__":
	'''Main Program.'''
	main()