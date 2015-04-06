import random

def conflict((r1, c1), (r2, c2)):
	""" Verifies if there is a conflict with given values.
		@r1 param: row to verify if there is a conflic
		@r2 param: row to verify if there is a conflic
		@c1 param: column to verify if there is a conflic
		@c2 param: column to verify if there is a conflic
	"""
	if(r1 == r2):	return True
	if(c1 == c2):	return True
	if(r1 / 3 == r2 / 3 and c1 / 3 == c2 / 3 and (not (r1 == r2 and c1 == c2))):	return True
	return False

def setminus(lst1, lst2):
	""" Looks for a value in Lst1 that is not in Lst2 and returns it.
	"""
	return [x for x in lst1 if x not in lst2]

def nextcell((i, j)):
	""" Finds next cell to fill
	"""
	if(j == 8):
		if(i == 8):	return (0, 0)
		return (i + 1, 0)
	return (i, j + 1)

def solve(sudoku):
	""" Function to solve the given sudoku.
	This fuction solves a sudoku verifying the possible candidates per position (i,j). 
    A solved sudoku is returned, just it sudoku has a valid result. If sudoku is not 
    resolvable an empty list is returned.
	"""
	empty = [[0] * 9] * 9
	def satisfy(pos, sudoku):
		def getAllowedValues():
			""" Get allowed values, reviewing cells randomly
			"""
			conflicts = set([(r, c) for r in range(9) for c in range(9) if((r, c) != pos and conflict(pos, (r, c)))])
			notallowed = set([sudoku[r][c] for (r, c) in conflicts if sudoku[r][c] != 0])
			s = setminus(range(1, 10), notallowed)
			# print s
			random.shuffle(s)
			return s
		if(sudoku[pos[0]][pos[1]] != 0):
			if(pos != (8, 8)):	return satisfy(nextcell(pos), sudoku)
			else:	return sudoku

		values = getAllowedValues()
		if(values == empty): return empty
		new = [r[:] for r in sudoku]
		for value in values:
			new[pos[0]][pos[1]] = value
			filled = satisfy(nextcell(pos), new)
			if(filled != empty):	return filled
		return empty
	return satisfy((0, 0), sudoku)

def printSudoku(sudoku):
	""" Function to print a sudoku like a matrix
	"""
	print '-------------------------'
	for i in range(9):
		for j in range(9):
			if(j == 8):	print sudoku[i][j]
			elif(j%3 == 2):	print str(sudoku[i][j]) + '|',
			else: print str(sudoku[i][j]) + ' ',
		if(i%3 == 2):
			print '-------------------------'
	print