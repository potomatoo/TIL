import sys
import itertools
sys.stdin = open('./input/input_10888.txt','r')

def find_min(store, tartget_y, tartget_x):
    min_distance = 0xffffff

    for y, x, d in store:
        distance = abs(y - tartget_y) + abs(x - tartget_x)
        min_distance = min(min_distance, distance)

    return min_distance

TC = int(input())

for tc in range(TC):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    chicken = []
    home = []
    for y in range(N):
        for x in range(N):
            if board[y][x] > 1:
                chicken.append((y, x, board[y][x]))
            if board[y][x] == 1:
                home.append((y, x))

    ans = 0xffffff
    for i in range(1, len(chicken)+1):
        store = list(itertools.combinations(chicken, i))
        print(store)
        for s in store:
            middle = 0
            for home_y, home_x in home:
                middle += find_min(s, home_y, home_x)
            for y, x, d in s:
                middle += d
            ans = min(ans, middle)
    print("#{} {}".format(tc+1, ans))

