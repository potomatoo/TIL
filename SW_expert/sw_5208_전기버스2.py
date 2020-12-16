import sys
sys.stdin = open('./input/input_5208.txt', 'r')

def backtrack(idx, remain, cnt):
    global N, ans
    remain -= 1
    if idx == N:
        ans = min(ans, cnt)
        return
    if cnt > ans:
        return

    # 배터리를 교환하고 다음 정류장으로 진행
    backtrack(idx+1, arr[idx], cnt+1)
    # 배터리를 교환하지 않고 다음 정류장으로 진행
    if remain > 0:
        backtrack(idx+1, remain, cnt)

TC = int(input())
for tc in range(TC):
    arr = list(map(int, input().split()))
    N = arr[0]
    order = []
    visit = [0] * N
    ans = 0xffffff
    backtrack(2, arr[1], 0)
    print(f'#{tc+1} {ans}')

