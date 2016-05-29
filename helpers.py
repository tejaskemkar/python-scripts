import re


def print_array_before(arr, i):
    s = 0
    n = len(arr)
    for j in xrange(n):
        if(j < i):
            s += len(str(arr[j]))
    s+=i
    # print s
    arrstr = re.sub(r'^\[|\]$|\s', '', str(arr))
    # print [n, i]
    print arrstr
    print(s * ' ') + '^'


def local_minima(arr, i):
    if(i == 0):
        if arr[i] <= arr[i + 1]:
            return True
    elif(i == (len(arr) - 1)):
        if (arr[i] <= arr[i - 1]):
            return True
    elif((arr[i] <= arr[i + 1]) and (arr[i] <= arr[i - 1])):
        return True
    return False


def local_maxima(arr, i):
    if(i == 0):
        if arr[i] >= arr[i + 1]:
            return True
    elif(i == (len(arr) - 1)):
        if (arr[i] >= arr[i - 1]):
            return True
    elif((arr[i] >= arr[i + 1]) and (arr[i] >= arr[i - 1])):
        return True
    return False


# a = [5, -1, 4, 4, 4, -50, 6, 6, 6, 25, 7, 8, 2, 5, 6, 100, 3]

# for x in xrange(len(a)):
#     print_array_before(a, x)
#     print local_minima(a, x)
#     print local_maxima(a, x)
