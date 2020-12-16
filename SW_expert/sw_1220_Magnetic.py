import sys
sys.stdin = open('./input/input_1220.txt','r')

for tc in range(10):
    N = int(input())
    m_map = []
    for _ in range(N):
        m_map.append(list(map(int,input().split())))

    result = []
    for x in range(N):
        cnt = 0
        S = ''
        for y in range(N):
            if m_map[y][x] != 0:
                S += str(m_map[y][x])
        result.append(S)

    cnt = 0
    for i in range(len(result)):
        cnt += result[i].count('12')
    print('#{} {}'.format(tc+1, cnt))