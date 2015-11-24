

def data_structure():
	tree = {}
	with open('input.txt') as f:
		while True:
			a = f.readline()
			a = a.split()
			if a[0] == '*':
				break
			tree[a[0]]=[a[1]]
			
	return tree


print data_structure()

