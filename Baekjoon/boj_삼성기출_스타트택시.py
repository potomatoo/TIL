from _collections import deque

def fit_y_x(str):
    result = int(str) - 1
    return result

def bfs(cnt):
    global fuel, before_fuel, taxi_y, taxi_x, now, flag

    visit = [[0 for _ in range(N)] for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    Q = deque()
    Q.append((taxi_y, taxi_x, 0))
    visit[taxi_y][taxi_x] = 1

    while Q:
        y, x, d = Q.popleft()
        if cnt % 2 == 1 and 0 < road[y][x] < 200:
            # print(Q)
            # print(y, x, d)
            min_y = 0xffffff
            result = []
            for one in Q:
                if one[2] != d:
                    break
                if road[one[0]][one[1]] != 0 and one[0] <= y:
                    if one[0] < min_y:
                        min_y = one[0]
            for two in Q:
                if two[2] != d:
                    break
                if road[two[0]][two[1]] != 0 and two[0] == min_y:
                    result.append(two)

            if len(result) == 1:
                y, x, d = result[0][0], result[0][1], result[0][2]

            if len(result) > 1:
                sorted(result, key=lambda x: x[1])
                y, x, d = result[0][0], result[0][1], result[0][2]

            taxi_y = y
            taxi_x = x
            now = road[y][x]
            road[y][x] = 0
            fuel -= d
            if fuel < 0 or before_fuel == fuel:
                flag = False
                return
            before_fuel = fuel
            break
        if cnt % 2 == 0 and road[y][x] == now * 100:
            taxi_y = y
            taxi_x = x
            road[y][x] = 0
            fuel -= d
            if fuel < 0 or before_fuel == fuel:
                flag = False
                return
            fuel += (d * 2)
            before_fuel = fuel
            break
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or tx < 0 or ty > N - 1 or tx > N - 1:
                continue
            if road[ty][tx] != 1 and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                Q.append((ty, tx, d + 1))

N, M, fuel = map(int,input().split())
road = []
for _ in range(N):
    line = list(map(int,input().split()))
    road.append(line)
taxi_y, taxi_x = map(int,input().split())
taxi_y = taxi_y - 1
taxi_x = taxi_x - 1
passenger = []
k = 2
for _ in range(M):
    one_passenger = list(map(fit_y_x,input().split()))
    road[one_passenger[0]][one_passenger[1]] = k
    road[one_passenger[2]][one_passenger[3]] = k * 100
    k += 1
    passenger.append(one_passenger)

now = 0
before_fuel = fuel
flag = True

for cnt in range(1, len(passenger)*2+1):
    bfs(cnt)
    # print('fuel: ', fuel)
    # print('before_fuel: ', before_fuel)
    # for z in range(N):
    #     print(road[z])
    # print('======================================')

    if not flag:
        break

if not flag:
    print(-1)
else:
    print(fuel)
