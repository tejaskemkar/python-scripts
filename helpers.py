import re


def print_array_before(arr, i):
    n = len(arr)
    arr = re.sub(r'\[|\]|\s', '', str(arr))
    # print [n, i]
    print arr
    print(((2 * n) - (2 * (n - i))) * ' ') + '^'


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


# a = [5, 4, 4, 4, 6, 6, 6, 7, 8, 2, 5, 6, 3]

# for x in xrange(len(a)):
#     print_array_before(a, x)
#     print local_minima(a, x)
#     print local_maxima(a, x)
