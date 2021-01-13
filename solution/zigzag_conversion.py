"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number 
of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR/" """



def sconversion(s, row):
	# initailize varibles

	cycle = 2*row -2 # shows how many letters can come in one row
	slen = len(s)
	results = ""

	# if the number of row we want to print is 1
	if row <= 1:
		return s

	# else 
	for i in range(0, row):
		for j in range(i, slen, cycle):
			results += s[j]
			secondj = (j-i) + cycle - i # index of next element

			if (secondj - j) % cycle != 0 and secondj <slen:
				results += s[secondj]
	return(results)




s = input("Enter the string: ")
nrow = input("Enter number of rows: ")
result = sconversion(s,int(nrow))
print(result)