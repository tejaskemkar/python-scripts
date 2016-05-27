import re


def print_array_before(arr, i):
    n = len(arr)
    arr = re.sub(r'\[|\]|\s', '', str(arr))
    print [n, i]
    print arr
    print(((2 * n) - (2 * (n - i))) * ' ') + '^'


a=[i for i in xrange(10)]

for x in xrange(1,10):
	print_array_before(a, x)