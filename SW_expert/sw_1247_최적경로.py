import sys
sys.stdin = open('./input/input_1247.txt', 'r')

def searchRoute(k, before, long):
    global ans
    if long >= ans:
        return
    if k == N:
        long += (abs(before[0] - home[0]) + abs(before[1] - home[1]))
        ans = min(ans, long)
        return

    for i in range(len(people)):
        if visit[i]: continue
        visit[i] = 1
        searchRoute(k+1, (people[i][0], people[i][1]), long+(abs(before[0] - people[i][0]) + abs(before[1] - people[i][1])))
        visit[i] = 0

TC = int(input())
for tc in range(TC):
    N = int(input())
    arr = list(map(int,input().split()))
    people = []
    samsung = (0, 0)
    home = (0, 0)

    for i in range(0, len(arr), 2):
        if i == 0:
            samsung = (arr[i], arr[i+1])
        if i == 2:
            home = (arr[i], arr[i+1])
        if i > 2:
            people.append((arr[i], arr[i+1]))
    ans = 0xfffffff
    middle = 0
    visit = [0] * N
    searchRoute(0,samsung,0)
    print('#{} {}'.format(tc+1, ans))



