from collections import deque
import sys

sys.stdin = open('./input/input_1486.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = deque()
    Q.append((0, 0))  # arr 요소, 키의 합
    ans = 0xfffffff
    while Q:
        k, s = Q.popleft()  # k번 요소, s: 선택된 요소들의 합
        if B <= s < ans:
            ans = s
            if ans == B:
                break
            continue
        if k == N:
            continue
        # k번 요소를 선택
        if s + arr[k] < ans:
            Q.append((k + 1, s + arr[k]))
        # 선택하지 않는 경우
        Q.append((k + 1, s))

    print('#{} {}'.format(tc, ans - B))