arr = [9, 5, 7, 6, 1, 2, 3, 8, 3]
N = len(arr)

def getMin(lo, hi):  # arr[]에서 최소값을 찾아서 반환

    if lo == hi: return arr[lo]

    ret = getMin(lo, hi-1)
    return min(ret, arr[hi])

# print(getMin(0, N-1))

def getMin2(lo, hi):
    print(lo,hi)
    if lo == hi: return arr[lo]

    mid = (lo+hi) >> 1
    l = getMin2(lo, mid)
    r = getMin2(mid + 1, hi)
    return min(l,r)

print(getMin2(0, N-1))
