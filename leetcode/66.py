# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

var = [2,8,8,2]

num = 0 
for i in range(len(var)):
	num += var[i] * pow(10,len(var) - 1-i)
ans = [int(j) for j in str(num+1)]
print(ans)