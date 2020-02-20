import sys
sys.stdin = open('./input/input_4880.txt','r')

def win(i, j):
    if fight[i] == '1' and fight[j] == '2': return j
    elif fight[i] == '1' and fight[j] == '3': return i
    elif fight[i] == '2' and fight[j] == '1': return i
    elif fight[i] == '2' and fight[j] == '3': return j
    elif fight[i] == '3' and fight[j] == '1': return j
    elif fight[i] == '3' and fight[j] == '2': return i
    else:
        if i < j:
            return i
        else:
            return j

def getwin(lo, hi):
    if lo == hi: return lo
    mid = (lo+hi) >> 1
    l = getwin(lo, mid)
    r = getwin(mid + 1, hi)
    return win(int(l), int(r))


TC = int(input())
for tc in range(TC):
    N = int(input())
    fight = input().split()

    print('#{} {}'.format(tc+1,getwin(0, N-1)+1))

