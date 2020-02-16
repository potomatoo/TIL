import sys
sys.stdin = open('./input/input_1267.txt','r')

for tc in range(10):
    V, E = map(int,input().split())
    G = [[] for _ in range(V+1)]
    visit = [0] * (V+1)
    S = []
    roads = list(map(int,input().split()))
    road = [[roads[i], roads[i+1]] for i in range(0,len(roads)-1,2)]
    front = [road[i][0] for i in range(len(road))]
    back = [road[i][1] for i in range(len(road))]

    for i in range(len(road)):
        if road[i][0] not in back:
            road[0], road[i] = road[i], road[0]

    for i in range(len(road)):
        for j in range(len(road)):
            if road[i][1] == road[j][0]:
                road[i], road[j] = road[j], road[i]

    result = []
    for i in range(len(road)):
        if road[i][0] not in result:
            result.append(road[i][0])
        if road[i][1] not in result:
            result.append(road[i][1])
    print('#{}'.format(tc+1),end=' ')
    for i in range(len(result)):
        if i == len(result)-1:
            print(result[i])
        else:
            print(result[i], end=' ')

        


