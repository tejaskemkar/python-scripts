[N, m]=[int(x) for x in raw_input().split()]
C=[int(x) for x in raw_input().split()]

sol=[[-1 for x in range(m)] for x in range(N + 1)]

def change(N, m, C):
	# print sol
	# print [N, m, C]
	if (N == 0):
		return 1
	if N < 0:
		return 0
	if m == 0 and N > 0:
		return 0
	if (sol[N][m-1] == -1):
		sol[N][m-1] = change(N-C[m-1], m, C) + change(N, m-1, C)
	return sol[N][m-1]

print str(change(N, m, C))
