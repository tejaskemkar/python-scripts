def get_path_count(loc, dim, m, n):
    count = 0
    next_locs = set()
    if m == 0:
        return 1
    elif str(loc) in pcount.keys() and m in pcount[str(loc)].keys():
        return pcount[str(loc)][m]
    else:
        pcount[str(loc)] = {}
        for i in xrange(n):
            if loc[i] + 1 <= dim[i] and loc[i] + 1 > 0:
                loc[i]+=1
                count += get_path_count(loc, dim, m - 1, n)
                loc[i]-=1
            if loc[i] - 1 <= dim[i] and loc[i] - 1 > 0:
                loc[i]-=1
                count += get_path_count(loc, dim, m - 1, n)
                loc[i]+=1
        pcount[str(loc)][m] = count
    return count


for x in xrange(int(raw_input())):
    pcount = {}
    [n, m] = [int(x) for x in raw_input().split()]
    loc = [int(x) for x in raw_input().split()]
    dim = [int(x) for x in raw_input().split()]
    print get_path_count(loc, dim, m, n)
