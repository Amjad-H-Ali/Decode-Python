print("Decode!")

# Uses recursion to evaluate the number of ways to decode data
# k represents the portion of the string currently being evaluated
def helper(data, k):
	# Exit code: for empty strings ("")
	if (k == 0):
		return 1;

	# Variable holding value of first index in current string
	s = data.length - k	

	# When string contains '0'; no way to decode
	if (data[s] == '0'):
		return 0;




# Takes in digits in the form of a string type as Argument
def num_of_ways(data):

	return helper(data, data.length)
