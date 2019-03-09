import time

#The algorithms here aim to solve the famous edit-distance (aka levenstein distance) problem.
#We have 2 strings :
x = "mosuzjmklfalkflkzeflhakjajazkjklfksfjklfsjsskjflklfaedflmkzeflhasfopkfsdlfsdksfdkkzkjklfksfjkqljdqdlskjdqksllqdslezjkzajazelkezalkzfsdjknqjbvsjbvsjbvsbsdjqkjlqdfsdjkfsdljdsfjksfjklfsjsskjflklfaesfopkfsdlfsdksfdkklkzfsdjknqjbvsjbvsjbvsbsdjqkjlqdfsdjkfsdllfsdjdmslkfsdmlkmdksfdklkdfssfkdslmdskssffdslfsdljdsfjlfsdjlfdslfsljsfiojslmosuzjmklfalkflkzeflhakjajazkjkfsdljdsfjlfsdjlmosuzjmklfalkflkzeflhakjajazkjklfksfjklfsjsskjflklfaesfopkfsdlfsdksfdkklkzfsdjkfsdljdsfjfdslfsljsfiojvjsknksvskljlfdlsfdjsfdkjfsjdsfldksfljdkjkkkdsqklqdskdqlqdkjqskhfsjqfhkjaoiozqskhfsjqfhkjaoioziuezkjnfsiuezkjnfsjsfdkjfdhfsd"
y = "lofmloxokfeklsfmaezpeoazpaesfopkfsdlfsdksfdklkdfsksdflmkzeflhakjajazkjklfksfjkqljdqdlskjdqksllqdslezjkzajazelkezajezalakezjaezjfsddbsvdbsksoqjlknvbsbvbfdmksfjklfsjsskjflklfaesfopkfsdlfsdksfdkklkzfsdjknqjbvsjbvsjbvsbsdjqkjlqdfsdjkfsdlslkfslkflkzeflhakjajazkjklfksfjklfsjskklkzfsdjkfsdjkfsdljdsfjlfsdmlkmsfkdslmdlfsdksfdklkdfsksdskssffdslfsdljdsfjlfsdjlfdslfsljsfiojskljlljsfiojskljlfdlsfdjsfdkjfsjdsfldksfljdkjkkkdsqklqdskdqlqdkjqskhfsjqfhkjaoioziuezkjnfsjsfdkjfdhfsdjksdfljlsfdlksfdkldfsklsdfjlksdfjsflmqdldmmmqsmldqdlqdqldpqslkksfmlfslmfsmkkfsmlsfmlkfsmklskfmanjznjeplqkqdohfibeeizbfifzf"


#And we have 3 operations allowed : insertion, deletion, replace.
#Each of those operations have a specific cost.
#We'll choose 
insertion_cost = 4 
deletion_cost = 1
replace_cost = 3
do_nothing_cost = 0
#We want to minimize the total cost of the operations needed to turn X into y


##########################################  Step 1 : subproblems
# Since our input are strings, we'll be able to represent subproblems by either using : suffix, preffix or substrings... Let's just try working with suffix (or preffix),
# and we'll see such approach works well (as the guesses only "attack" the first element of the input/parameter sequence).

########################################## Step 2 : possibilities/guess 
# The three operation allowed corresponds to the three possibilities which can happen each time a choice is made to move toward the problem's solution...
# Let's detail a bit :
# Let's focus on the first letter of x. 


# Replace :Suppose you use replace operation to transform x[0] ('m') into y[0] ('l').. Then the only thing you'll have to care from 
# now on are x[1:] and y[1:]


# Insertion : Suppose you use insert, you will add y[0] in front of x[0]. Now y[0]+x[0]+x[1]
#                                                                             y[0]+y[1]+y[2]
# we still have to deal with the matching of x and y[1:]

# Deletion : Suppose you use delete, you will delete x[0], so you end up with :
# x[1]+x[2]+x[3]
# y[0]+y[1]+[2]
# we need to match now x[1:] and y

# Last possibility we use none of those transformations.

######################################### Step 3 : finding the reccurence

#Exponentional reccurence O(4^n)
def edit_distance_simple_recursion(x,y):

	if len(x)==0 and len(y)==0 :
		return 0

	if len(x)==0:
		return len(y)*insertion_cost

	if len(y)==0:
		return len(x)*deletion_cost

	if  (x[0]==y[0]):
		return edit_distance_simple_recursion(x[1:],y[1:])


	values = [edit_distance_simple_recursion(x[1:],y[1:])+replace_cost,
		edit_distance_simple_recursion(x,y[1:])+insertion_cost,
		edit_distance_simple_recursion(x[1:],y)+deletion_cost]
	return min(values)






#########################################################

# bottom-up approach (topological order)

def bottom_up_approach_edit_distance_DP(x,y):
	subproblems_values = [ [1000000 for j in range(len(y)+1) ] for i in range(len(x)+1) ]

	#initialization 
	for k in range(len(y)+1):
		subproblems_values[-1][k]=insertion_cost*(len(y)-k)

	for k in range(len(x)+1):
		subproblems_values[k][-1]=deletion_cost*(len(x)-k)

	#print(subproblems_values)

	#using topological order to solve subproblems
	# beginning by loop i or by loop j doesn't matter. All the subproblems are solved anyway (without conflict).
	for i in range(len(x)-1,-1,-1):
		for j in range(len(y)-1,-1,-1):
			subproblems_values[i][j] = min(
				subproblems_values[i+1][j+1]+replace_cost,
				insertion_cost+subproblems_values[i][j+1],
				deletion_cost+subproblems_values[i+1][j],
				#adding the MANDATORY special case checker (works only thanks to it !!!)
				(do_nothing_cost + subproblems_values[i+1][j+1]) if  x[i]==y[j] else 1000000
				)
	return subproblems_values[0][0]
	



start = time.time()
print(f"result bottom up : {bottom_up_approach_edit_distance_DP(x,y)}")
end = time.time()
print(end - start)


###################################

# memoization/reccurence approach :
def memoization_approach_helper_edit_distance(x,y,index_x,index_y,subproblems_values):
	
	if subproblems_values[index_x][index_y] == -1 :
		subproblems_values[index_x][index_y] = min(
		memoization_approach_helper_edit_distance(x,y,index_x+1,index_y+1,subproblems_values)+replace_cost,
		insertion_cost+memoization_approach_helper_edit_distance(x,y,index_x,index_y+1,subproblems_values),
		deletion_cost+memoization_approach_helper_edit_distance(x,y,index_x+1,index_y,subproblems_values),
		memoization_approach_helper_edit_distance(x,y,index_x+1,index_y+1,subproblems_values) if x[index_x]==y[index_y] else 100000000000
		)
		return subproblems_values[index_x][index_y]
	else :
		return subproblems_values[index_x][index_y]

def memoization_approach_edit_distance(x,y):
	subproblems_values = [ [-1 for j in range(len(y)+1) ] for i in range(len(x)+1) ]
	#initialization 
	for k in range(len(y)+1):
		subproblems_values[-1][k]=insertion_cost*(len(y)-k)
	for k in range(len(x)+1):
		subproblems_values[k][-1]=deletion_cost*(len(x)-k)

	a = memoization_approach_helper_edit_distance(x,y,0,0,subproblems_values) 
	return a



start = time.time()
print(f"result memoization approach : {memoization_approach_edit_distance(x,y)}")
end = time.time()
print(end - start)