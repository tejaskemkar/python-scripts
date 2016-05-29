from helpers import print_array_before
for x in xrange(int(raw_input())):
    n = int(raw_input())
    p = [int(i) for i in raw_input().split()]
    s = pr = max_sofar = 0
    a = [0 for i in xrange(n)]
    # print [len(p), len(a)]
    for i in xrange(n - 1, -1, -1):
        # print [i, max_sofar]
        # print_array_before(p, i)
        if p[i] <= max_sofar:
            a.pop(i)
            a.insert(i, -1)
        elif p[i] > max_sofar:
            a.pop(i)
            a.insert(i, 1)
            max_sofar = p[i]
        # print_array_before(a, i)

    for i in xrange(n):
        # print_array_before(p, i)
        # print_array_before(a, i)
        if a[i] == -1:
            s += 1
            pr += p[i] * a[i]
        elif a[i] == 1:
            pr += p[i] * s
            s = 0

    print (pr)
