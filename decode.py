print("Decode!")

# Uses recursion to evaluate the number of ways to decode data
# k represents the portion of the string currently being evaluated
def helper(data, k):
	# Exit code: for empty strings ("")
	if (k == 0):
		return 1;

	# Variable holding value of first index of char in current string
	s = len(data) - k	

	# When string contains char '0'; no way to decode
	if (data[s] == '0'):
		return 0;

	# Ex: helper("12345") = helper("2345") + helper("345")
	result = helper(data, k - 1)

	# Add helper("345") only if digit less than 27
	if (k >= 2  and int(data[s:s+2]) <= 26):
		result += helper(data, k - 2)

	return result	
 	




# Takes in digits in the form of a string type as Argument
def num_of_ways(data):

	return helper(data, len(data))

print(num_of_ways("123")) # 3
print(num_of_ways("023")) # 0
print(num_of_ways("1203")) # 1
print(num_of_ways("")) # 1
print(num_of_ways("2723")) # 2
print(num_of_ways("12")) # 2
