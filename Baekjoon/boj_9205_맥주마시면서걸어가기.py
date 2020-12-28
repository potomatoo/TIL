from _collections import deque

def bfs():
    Q = deque()
    check = []
    Q.append((home_x, home_y))
    check.append([home_x, home_y])
    while Q:
        x, y = Q.popleft()
        if x == goal_x and y == goal_y:
            print("happy")
            return
        for nx, ny in beer_charge:
            if [nx, ny] not in check:
                dist = abs(nx-x) + abs(ny-y)
                if dist <= 1000:
                    Q.append((nx, ny))
                    check.append([nx, ny])
    print("sad")
    return

TC = int(input())

for _ in range(TC):
    n = int(input())
    beer_charge = []
    home_x, home_y = map(int, input().split())

    for _ in range(n):
        beer_charge.append(list(map(int, input().split())))
    goal_x, goal_y = map(int, input().split())
    beer_charge.append((goal_x, goal_y))
    bfs()



