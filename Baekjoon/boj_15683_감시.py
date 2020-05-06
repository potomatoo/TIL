def permutation(k):
    if k == len(camera):
        for z in range(len(order)):
            print(order[z])
        print()

    else:
        for i in range(len(camera)):
            if visit[i]: continue
            visit[i] = 1
            order.append(camera[i])
            permutation(k+1)
            visit[i] = 0
            order.pop()

N, M = map(int,input().split())
field = []
for _ in range(N):
    field.append(list(map(int,input().split())))

one = [[(1, 0)], [(-1, 0)], [(0, 1)], [(0, -1)]]
two = [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]]
three = [[(1, 0), (0, 1)], [(1, 0), (0, -1)], [(0, 1), (-1, 0)], [(0, -1), (-1, 0)]]
four = [[(0, -1), (1, 0), (0, 1)], [(0, -1), (-1, 0), (0, 1)]]
five = [[(-1, 0), (1, 0), (0, -1), (0, 1)]]

camera = []
for y in range(N):
    for x in range(M):
       if field[y][x] == 1:
           camera.append(one)
       if field[y][x] == 2:
           camera.append(two)
       if field[y][x] == 3:
           camera.append(three)
       if field[y][x] == 4:
           camera.append(four)
       if field[y][x] == 5:
           camera.append(five)

visit = [0] * len(camera)
order = []
permutation(0)

