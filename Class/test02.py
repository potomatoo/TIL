import sys
from copy import deepcopy
sys.stdin = open('./input/input_test02.txt', 'r')

# 사탕을 나누어주는 것을 dfs로 구현한다.
def give_candy(k):
    global ans
    # 기저사례
    if k == M:
        c_kids = deepcopy(kids)
        for index in range(N):
            # 사탕의 종류보다 어린이의 숫자가 작으면 그만나누어 준다.
            if index > len(order)-1:
                break
            # 순서대로 순열의 사탕을 어린이에게 나누어준다.
            c_kids[index].add(order[index])
        # 어린이마다 가지고 있는 사탕의 종류를 더한다.
        kindOfCandy = 0
        for c_kid in c_kids:
            kindOfCandy += len(c_kid)
        # 계속해서 사탕종류의 최댓값을 갱신한다.
        ans = max(ans, kindOfCandy)
        return
    for i in range(M):
        if visit[i]: continue
        visit[i] = 1
        # order는 전체 사탕종류로 만들 수 있는 순열을 저장하고 있는 배열이다.
        order.append(plus_candy[i])
        # 재귀를 사용하여 순열을 생성한다.
        give_candy(k+1)
        visit[i] = 0
        order.pop()

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    # 어린이 배열을 set()을 사용하여 중복이 되도 종류는 늘어나지 않도록 해준다.
    kids = [set() for _ in range(N)]
    for i in range(N):
        arr = list(map(int,input().split()))
        for j in range(1, len(arr)):
            kids[i].add(arr[j])

    # 사탕의 종류를 1부터 배열을 만든다.
    plus_candy = [x for x in range(1, M+1)]
    order = []
    visit = [0] * M
    ans = 0
    give_candy(0)
    print('#{} {}'.format(tc+1, ans))