import sys
sys.stdin = open('./input/input_1486.txt','r')

def permutation(k):
    global result
    global min_result
    global flag
    if flag:
        if result > min_result:
            return
        if result == B:
            min_result = 0
            flag = False
        if result > B:
            min_result = min(result, min_result)
            return
        before = -1
        for i in range(N):
            if visit[i] == 1 or before == person[i]:
                continue
            visit[i] = 1
            before = person[i]
            result += person[i]
            permutation(k+1)
            visit[i] = 0
            result -= person[i]

TC = int(input())
for tc in range(TC):
    N, B = map(int,input().split())
    person = list(map(int,input().split()))
    visit = [0] * N
    order = []
    min_result = 0xffffffff
    result = 0
    flag = True
    permutation(0)
    print('#{} {}'.format(tc+1,min_result-B))
