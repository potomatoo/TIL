import sys
sys.stdin = open('./input/input_test03.txt', 'r')
from _collections import deque

# 현재지점에 대하여 상, 하, 좌, 우, 현재지점을 판단하기 위한 deltaY, deltaX 배열 생성
dy = [-1, 1, 0, 0, 0]
dx = [0, 0, -1, 1, 0]

def find_start(k):
    global ans
    # 기저사례 : 출발 할 수 있는 두 지점에서 동시에 시작
    if k == 2:
        # 최소시간를 찾기 위하여 deque 사용
        Q = deque()
        D = [[(0, 0) for _ in range(N)] for _ in range(N)]
        for index in range(len(order)):
            # 출발 지점에서 동시에 시작하기 위하여 deque에 두 지점 추가
            # deque에 해당 y좌표, x좌표, 현재 거리, 1플레이어인지 2플레이어인지 저장
            if index == 0:
                Q.append((order[index][0], order[index][1], 0, 1))
            if index == 1:
                Q.append((order[index][0], order[index][1], 0, 2))

        while Q:
            y, x, d, k = Q.popleft()
            # 기저 사례
            # deque에서 꺼낸 요소가 이미 상대 플레이어가 다녀간 방이면 break
            if D[y][x][0] != 0 and D[y][x][1] != k:
                # 최소시간을 갱신해준다.
                ans = min(ans, D[y][x][0])
                break
            # 다섯개의 방향을 기준으로 탐색 시작
            for index in range(5):
                ty = y + dy[index]
                tx = x + dx[index]
                if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                    continue
                if (maze[ty][tx] == 0 or maze[ty][tx] == 2):
                    Q.append((ty, tx, d+1, k))
                    D[ty][tx] = (D[y][x][0] + 1, k)
        return
    for i in range(len(can_start)):
        if find_start_visit[i]: continue
        # 출발지점 중에 중복을 피하기 위한 작업을 수행한다.
        if len(order) > 0:
            if order[-1] > can_start[i]:
                continue
        find_start_visit[i] = 1
        order.append(can_start[i])
        # 재귀를 통하여 출발지점 2곳을 재귀로 만들어준다.
        find_start(k+1)
        find_start_visit[i] = 0
        order.pop()

N = int(input())
maze = []
for _ in range(N):
    maze.append(list(map(int,input().split())))
can_start = []
# 시작할 수 있는 좌표를 저장
for y in range(N):
    for x in range(N):
        if maze[y][x] == 2:
            can_start.append((y, x))

order = []
find_start_visit = [0] * len(can_start)
ans = 0xfffffff
find_start(0)
# 결과 출력
print(ans)
