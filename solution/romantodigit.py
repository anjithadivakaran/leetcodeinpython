
def romantodigit(s):
	result = 0
	previous = 0
	lookup = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

	for i in reversed(s):
		if lookup[i] >= previous:
			result += lookup[i]
		else:
			result -= lookup[i]
		previous = lookup[i]
	return result




s = input("Enter the string: ")
result = romantodigit(s)
print(result)