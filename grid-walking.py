from helpers import print_array_before
pcount = {}


def get_path_count(loc, dim, m, n):
    count = 0
    next_locs = set()
    print
    print
    # print str(pcount) + 'top'
    # print[tuple(loc), m]
    if tuple(loc) in pcount.keys() and m in pcount[tuple(loc)].keys():
        print str(pcount) + 'hit'
        return pcount[tuple(loc)][m]
    else:
        pcount[tuple(loc)] = {}
        for i in xrange(n):
            tmp = [loc[x] + 1 if x == i else loc[x] for x in range (n)]
            if tmp[i] <= dim[i] and tmp[i] > 0:
                next_locs.add(tuple(tmp))
            tmp = [loc[x] - 1 if x == i else loc[x] for x in range (n)]
            if tmp[i] <= dim[i] and tmp[i] > 0:
                next_locs.add(tuple(tmp))
            # print loc
        print 'next for ' + str(loc) + ' and ' + str(m) + ' steps' + ' : ' + str(len(next_locs)) + ' - ' + str(next_locs)
        count = len(next_locs)
        if m == 1:
            pcount[tuple(loc)][m] = count
        else:
            for l in next_locs:
                l_cnt = get_path_count(list(l), dim, m - 1, n)
                count += l_cnt
                print 'cur loc : ' + str(loc) + ' next_locs_len: '+str(len(next_locs))+' next loc: '+ str(l) + ' m: '+str(m-1)+' count:' + str(l_cnt)
            pcount[tuple(loc)][m] = count
            # print[tuple(loc), m]
    # print str(pcount) + 'bottom'
    return count


for x in xrange(int(raw_input())):
    [n, m] = [int(x) for x in raw_input().split()]
    loc = [int(x) for x in raw_input().split()]
    dim = [int(x) for x in raw_input().split()]
    print get_path_count(loc, dim, m, n)
