# 1
# 9
# -2 1 -3 4 -1 2 1 -5 4
def max_subarray(A):
	max_ending_here = max_contiguous = max_non_contiguous = 0
	max_subseq_here = max_subseq = []
	if(len([x for x in A if x >= 0]) == 0):
		max_contiguous = max_non_contiguous = max(A)
		max_subseq.append(max(A))
		max_subseq_here.append(max(A))
	else:
		for x in A:
			if (max_ending_here + x > 0):
				max_ending_here = max_ending_here + x
				max_subseq_here.append(x)
			else:
				max_ending_here = 0
				max_subseq_here = []
			# max_ending_here = max(0, max_ending_here + x)
			if (max_ending_here > max_contiguous):
				max_contiguous = max_ending_here
				max_subseq = list(max_subseq_here)
			# max_contiguous = max(max_contiguous, max_ending_here)
			if(x > 0):
				max_non_contiguous = max_non_contiguous + x
	print str(max_contiguous) + ' ' + str(max_non_contiguous)
	# print str(max_subseq)

# max_subarray([int(x) for x in "-2 1 -3 4 -1 2 1 -5 4".split()])
t = int(raw_input().strip())
for i in range(0,t):
	n = int(raw_input().strip())
	A = [int(x) for x in raw_input().split(' ')]
	max_subarray(A)
