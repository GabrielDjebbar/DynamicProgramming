__author__ = "Gabriel Djebbar"
__credits__ = ["Erik Demaine","MIT opencourseware"]

#The algorithms here solve the famous Knapsack problem.
#I used two approach to solve it : first a bottom-up approach, then a memoization approach

sack_capacity = 30 
objects = [(5,3),(10,13),(20,15),(29,22),(20,8),(4,17)] #(weight,value)=(si,vi)



###################################### Just getting a feel for the problem.

#Step 1 : Subproblem representation 
#The input of our initial problem is a set of objects, which can be represented as a sequence ... thus we "know" that we can use the suffix/preffix approach to define the subproblems, plus we need to use 
#the current remaining capacity to fully define the subproblems (aka subproblem states)


#Step 3 : find the knapsack reccurence
def knapsack(index_of_the_current_viewed_object,remaining_capacity) :
	if remaining_capacity<0:
		return -1000000000000000000000000
	#Step 2 : enumerating the guesses/possiblities 
	#The possibilities consist of a binary choice : do i take or not the first element of the suffix; that is, do i take or not the first object of the list ?
	return max(
		knapsack(index_of_the_current_viewed_object+1,remaining_capacity),
		knapsack(index_of_the_current_viewed_object+1,remaining_capacity - objects[index_of_the_current_viewed_object][0])+objects[index_of_the_current_viewed_object][1]
		)



##################################



##### bottom-up approach (using topological order) :
#the topological order tells us both what what subproblems we can directly initialize, and in what order the remaining subproblems must be visited

def bottom_up_approach_knapsack(objects,sack_max_capacity):
	subproblems_values = [[-1 for j in range(0,sack_max_capacity+1)] for i in range(1,len(objects)+1)] 


	#we need to do an intialization to do our bottom-up approach
	# initialize first column : case where sack_capacity = 0
	for index_object in range(len(objects)):
		subproblems_values[index_object][0] = 0

	# initialize last line : case where only the one last element remaining
	for capacity in range(1,sack_max_capacity+1):
		subproblems_values[len(objects)-1][capacity] = objects[len(objects)-1][1] if objects[len(objects)-1][0] <= capacity else 0


    #from biggest to smallests
	for i in range(len(objects)-2,-1,-1): #we don't care about the last line
		
		#from smallest to biggest capacity
		for c in range(1,sack_max_capacity+1): #we don't care about the last column
			subproblems_values[i][c] = max(
				subproblems_values[i+1][c],
				(subproblems_values[i+1][c-objects[i][0]] if c-objects[i][0]>=0 else -100000) + objects[i][1]
				)
		

	return subproblems_values[0][sack_max_capacity]


print(bottom_up_approach_knapsack(objects,sack_capacity))





##### memoization / reccurence approach :

def knapsack_reccurence_helper(objects,index,capacity,subproblems_values):
	if subproblems_values[index][capacity] != -1 :
		return subproblems_values[index][capacity]
	else  :
		return max(
			knapsack_reccurence_helper(objects,index+1,capacity,subproblems_values),
			knapsack_reccurence_helper(objects,index+1,capacity - objects[index][0],subproblems_values) + objects[index][1] if capacity - objects[index][0] >= 0 else -1000000
			)

def reccurence_approach_knapsack(objects,sack_max_capacity):
	subproblems_values = [[-1 for j in range(0,sack_max_capacity+1)] for i in range(1,len(objects)+1)] 

	for index_object in range(len(objects)):
		subproblems_values[index_object][0] = 0

	# initialize last line : case where only the one last element remaining
	for capacity in range(1,sack_max_capacity+1):
		subproblems_values[len(objects)-1][capacity] = objects[len(objects)-1][1] if objects[len(objects)-1][0] <= capacity else 0

	return knapsack_reccurence_helper(objects,0,capacity,subproblems_values)



print(reccurence_approach_knapsack(objects,sack_capacity))




	




