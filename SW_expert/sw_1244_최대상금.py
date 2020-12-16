import sys
sys.stdin = open('./input/input_1244.txt','r')

def getMostMony(k):
    global ans
    if k == n:
        ans = max(int(''.join(arr)), ans)
        return
    for i in range(N-1):
        for j in range(i+1, N):
            arr[i], arr[j] = arr[j] , arr[i]
            middle = int(''.join(arr))
            if middle in visit[k+1]:
                continue
            visit[k+1].add(middle)
            getMostMony(k+1)
            arr[i], arr[j] = arr[j], arr[i]

TC = int(input())
for tc in range(TC):
    number, n = map(str,input().split())
    n = int(n)
    arr = []
    ans = 0
    for i in range(len(number)):
        arr.append(number[i])
    N = len(arr)
    visit = [set() for _ in range(n+1)]
    getMostMony(0)
    print('#{} {}'.format(tc+1, ans))