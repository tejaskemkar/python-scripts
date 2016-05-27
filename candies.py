N=int(raw_input())
scores=[]
for i in xrange(N):
	scores.insert(i, int(raw_input()))

candies=[]
for i in xrange(N):
	if (i == 0):
		candies.insert(i, 1)
	else:
		if(scores[i] > scores[i - 1]):
			candies.insert(i, candies[i - 1] + 1)
		else:
			candies.insert(i, 1)

# print candies
for i in xrange(N - 2, -1, -1):
	if (scores[i] > scores[i + 1]):
		nval=candies[i + 1] + 1
		oval=candies[i]
		candies.pop(i)
		candies.insert(i, max(nval, oval))
	# print candies

# print candies
print sum(candies)