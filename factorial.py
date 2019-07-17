def factorial(n):
    answer = 1
    count = 0
    if n == 0:
        return 0
    else:
        while count < n:
            answer *= (count + 1)
            count += 1
    return answer

def recur_factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

n = int(input('Enter a number: '))
print(factorial(n))
print(recur_factorial(n))
