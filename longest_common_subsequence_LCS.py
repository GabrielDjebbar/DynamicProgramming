import numpy

# Example 1 :
x0 = 'abcad'
y0 ='bcca'
# we expect a LCS of length 3, such as 'bca'

# Example 2:
x = 'abcbdab'
y = 'bdcaba'
# we expect a LCS of length 4. 'bdab' is one of them.


def display_solution(parent_pointers,x,y):
	solution = ''
	index_y = 0
	for i in range(len(x)):
		if index_y < len(y) :
			if parent_pointers[i][index_y][0] == 1 :
				solution += x[i]
				index_y = parent_pointers[i][index_y][1]
	return solution

################ BOTTOM-UP approach

def find_occurence(element_to_search,sequence,index_beginning_the_search):
	for i in range(index_beginning_the_search,len(sequence)) :
		if sequence[i] == element_to_search :
			return i
	return -1


#using topological order
def LCS_bottom_up_approach(x,y):
	LCS_subproblems_array = [[-1 for i in range(len(y)+1)] for i in range(len(x)+1)]
	parent_pointers = [[-1 for i in range(len(y)+1)] for i in range(len(x)+1)]

	# initializing base case subproblems
	for i in range(len(x)+1):
		LCS_subproblems_array[i][-1] = 0
	for j in range(len(y)+1) :
		LCS_subproblems_array[-1][j] = 0
	for i in range(len(x)-1,-1,-1):
		for j in range(len(y)-1,-1,-1):
			take_xi = (1+LCS_subproblems_array[i+1][find_occurence(x[i],y,j)+1] if find_occurence(x[i],y,j)!=-1 else 0)
			not_take_xi = LCS_subproblems_array[i+1][j]
			LCS_subproblems_array[i][j] = max(take_xi,not_take_xi)
			parent_pointers[i][j] = (numpy.argmax([not_take_xi,take_xi]),j if numpy.argmax([not_take_xi,take_xi])==0 else find_occurence(x[i],y,j)+1)

# 		LCS_subproblems_array[i][j] = max((1+LCS_subproblems_array[i+1][find_occurence(x[i],y,j)] if find_occurence(x[i],y,j)!=-1 else 0) # we choose to take x[i] element
# ,LCS_subproblems_array[i+1][j]  # we choose not to take x[i]
# )

	print(display_solution(parent_pointers, x, y))
	return LCS_subproblems_array[0][0]


print(LCS_bottom_up_approach(x0,y0))
print(LCS_bottom_up_approach(x,y))








############## memoization approach (recursive)

def LCS_helper(x,i,y,j,subproblems_array):
	if i>=len(x):
		return 0
	elif j >= len(y):
		return 0
	if subproblems_array[i][j] != -1 :
		return subproblems_array[i][j]
	else :
		subproblems_array[i][j] = max(LCS_helper(x,i+1,y,j,subproblems_array),(1+LCS_helper(x,i+1,y,find_occurence(x[i],y,j)+1,subproblems_array) if find_occurence(x[i],y,j) != -1 else 0 ) )
		return subproblems_array[i][j]


def LCS_memoized_approach(x,y):
	LCS_subproblems_array = [[-1 for i in range(len(x)+1)] for i in range(len(y)+1)]
	return LCS_helper(x,0,y,0,LCS_subproblems_array)



#print(LCS_memoized_approach(x,y))