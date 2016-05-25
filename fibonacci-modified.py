[a,b,n] = [int(x) for x in raw_input().split()]

def fibo(n):
	if (n == 1):
		return a
	if (n == 2):
		return b
	return fibo(n-1)**2 + fibo(n-2)

print fibo(n)
