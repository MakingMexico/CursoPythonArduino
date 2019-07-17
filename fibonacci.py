def fibonnacci(n):
	n1 = 1
	n2 = 1
	count = 1
	if n == 1 or n == 2:
		return 1
	elif n <= 0:
		return 0
	else:
		while count < n-1:
			answer = n1 + n2
			n1 = n2
			n2 = answer
			count += 1
	return answer

n = int(input('Enter a number: '))
print(fibonnacci(n))
