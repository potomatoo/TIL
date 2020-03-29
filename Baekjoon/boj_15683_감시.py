def permutation(k):
    if k == len(camera):
        for z in range(len(order)):
            print(order[z])

    else:
        for i in range(len(camera)):
            if visit[i]: continue
            visit[i] = 1
            order.append(camera[i])
            permutation(k+1)
            visit[i] = 0
            order.pop()

N, M = map(int, input().split())
place = []
for _ in range(N):
    place.append(list(map(int,input().split())))

one = [[(-1, 0)], [(0, 1)], [(1, 0)], [(-1, 0)]]
two = [[(0, 1), (0, -1)], [(-1, 0), (1, 0)], [(0, 1), (0, -1)], [(-1, 0), (1, 0)]]
three = [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]]
four = [[(0, -1), (1, 0), (0, 1)], [(1, 0), (0, 1), (-1, 0)], [(-1, 0), (0, -1), (0, 1)], [(-1, 0), (0, -1), (1, 0)]]
five = [[(1, 0), (-1, 0), (0, 1), (0, -1)],[(1, 0), (-1, 0), (0, 1), (0, -1)], [(1, 0), (-1, 0), (0, 1), (0, -1)],[(1, 0), (-1, 0), (0, 1), (0, -1)]]

camera = []
w_camera = []
for y in range(N):
    for x in range(M):
        if place[y][x] == 0 or place[y][x] == 6:
            continue
        if place[y][x] == 1:
            camera.append(one)
        if place[y][x] == 2:
            camera.append(two)
        if place[y][x] == 3:
            camera.append(three)
        if place[y][x] == 4:
            camera.append(four)
        if place[y][x] == 5:
            camera.append(five)
order = []
visit = [0] * len(camera)
permutation(0)