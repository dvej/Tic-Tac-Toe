
def tabla(mat):
	import string
	dim = len(mat)
	znak = [' ','X','O']
	print()
	for i in range(dim):
		print('{:2d}'.format(dim-i) + '  ',end='')
		for j in range(dim):
			print(f' {znak[mat[i][j]]} ',end='')
			if j != dim-1:
				print('|',end='')
		if i != dim-1:
			print('\n   ' + dim * ' ---')
	print('\n\n  ',end='')
	for j in range(dim):        
		print(f'   {string.ascii_uppercase[j]}',end='')
	print('\n')


def provera(mat):
	n = len(mat)
	for i in range(n):
		for j in range(n-2):
			for k in range(1,3):
				red,kol,di,sdi = 0,0,0,0
				for l in range(3):
					if mat[i][j+l] == k:    # by rows
						red += 1
					if mat[j+l][i] == k:    # by columns
						kol += 1
					if i < n-2:
						if mat[i+l][j+l] == k:  # po diagonals
							di += 1
						if mat[i-l+2][j+l] == k:    # by reverse diagonals
							sdi += 1
				if 3 in [red,kol,di,sdi]:
					return k
	return 0


def unos(mat):
	n = len(mat)
	tabla(mat)
	p1,p2,prazno = 1,2,1
	while prazno > 0:
		poz = input(f'Player {p1}: ')
		if poz == 'exit': exit() 
		red,kol = poz[1:],poz[:1]
		if red.isdecimal() and kol.isalpha():
			red = n-int(red)
			if kol.isupper():
				kol = ord(kol)-65
			else:
				kol = ord(kol)-97
		else:
			print('Wrong entry')
			continue
		if red in range(n) and kol in range(n):
			if mat[red][kol] == 0:
				mat[red][kol] = p1
				p1,p2 = p2,p1
				tabla(mat)
				ishod = provera(mat)
				if ishod in (1,2):
					return print(f'Player {ishod} has won!!')
				prazno = 0
				for lista in mat:
					for element in lista:
						if element == 0: prazno += 1
			else:
				print(f'Field {poz} is not empty')
		else:
			print('Field does not exist')
	print('Draw!')


dimenzija = int(input('Table dimensions: '))
if dimenzija < 3:
		print('Number must be greater then 2')
else:
	matrica = [[0 for j in range(dimenzija)] for i in range(dimenzija)]
	unos(matrica)
