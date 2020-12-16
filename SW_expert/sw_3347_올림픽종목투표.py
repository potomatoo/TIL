import sys
sys.stdin = open('./input/input_3347.txt','r')

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    sports = list(map(int,input().split()))
    people = list(map(int,input().split()))
    ans = [0] * len(sports)
    for i in range(len(people)):
        for j in range(len(sports)):
            if people[i] >= sports[j]:
                ans[j] += 1
                break
    print('#{} {}'.format(tc+1, ans.index(max(ans))+1))
