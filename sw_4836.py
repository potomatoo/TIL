import sys
sys.stdin = open('input_4836.txt', 'r')

TC = int(input())
for tc in range(TC):
    n = int(input())
    c_map = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        if color == 1:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    if c_map[y][x] == 2:
                        cnt += 1
                        c_map[y][x] = 1
                    else:
                        c_map[y][x] = 1

        else:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    if c_map[y][x] == 1:
                        cnt += 1
                        c_map[y][x] = 2
                    else:
                        c_map[y][x] = 2
    print('#{} {}'.format(tc+1, cnt))

