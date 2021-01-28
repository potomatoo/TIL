from collections import deque

def binary(n):
    if n == 1:
        return '0001'
    answer = ''
    while n // 2 >= 1:
        remain = n % 2
        n = n // 2
        answer = str(remain) + answer
        if n < 2:
            answer = str(n) + answer
    while len(answer) < 4:
        answer = '0' + answer
    return answer

def is_range(y, x):
    if y < 0 or y > N-1 or x < 0 or x > M-1:
        return False
    return True

def bfs(y, x):
    now_room_size = 0
    def find_room(y, x):
        for k in range(4):
            if board[y][x][k] == '0':
                ty = y + dy[k]
                tx = x + dx[k]
                if is_range(ty, tx) and not visit[ty][tx]:
                    visit[ty][tx] = room_cnt
                    Q.append((ty, tx))
    Q = deque()
    Q.append((y, x))
    visit[y][x] = room_cnt
    while Q:
        yy, xx = Q.popleft()
        find_room(yy, xx)
        now_room_size += 1
    return now_room_size

def break_wall(n, y, x):
    Q = deque()
    Q.append((y, x))
    visit2 = [[0 for _ in range(M)] for _ in range(N)]
    visit2[y][x] = 1
    near_room = set()
    while Q:
        yy, xx = Q.popleft()
        for i in range(4):
            ty = yy + dy[i]
            tx = xx + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                continue
            if visit[ty][tx] != n:
                near_room.add(visit[ty][tx])
            if visit[ty][tx] == n and not visit2[ty][tx]:
                visit2[ty][tx] = 1
                Q.append((ty, tx))

    return list(near_room)

M, N = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for y in range(N):
    for x in range(M):
        board[y][x] = binary(board[y][x])

visit = [[0 for _ in range(M)] for _ in range(N)]

room_cnt = 0
room_size = 0
room_info = dict()
enter_room = []
for y in range(N):
    for x in range(M):
        if not visit[y][x]:
            room_cnt += 1
            enter_room.append((room_cnt, y, x))
            now_room_size = bfs(y, x)
            room_info[room_cnt] = now_room_size
            room_size = max(room_size, now_room_size)



break_wall_size = 0
for room_number, y, x in enter_room:
    near_room = break_wall(room_number, y, x)
    for near_number in near_room:
        break_wall_size = max(break_wall_size, room_info[room_number] + room_info[near_number])

print(room_cnt)
print(room_size)
print(break_wall_size)