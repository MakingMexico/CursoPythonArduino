def recur_fibo(n):
    if n <= 2:
       return 1
    else:
       return recur_fibo(n-1) + recur_fibo(n-2)

n = int(input('Enter a number: '))
print(recur_fibo(n))
