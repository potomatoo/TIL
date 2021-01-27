import sys
sys.stdin = open('./input/input_1208.txt', 'r')

for tc in range(10):
    k = int(input())
    sand = list(map(int, input().split()))
    sand.sort()
    for _ in range(k):
        max_sand = sand.pop(sand.index(max(sand)))
        min_sand = sand.pop(sand.index(min(sand)))
        sand.append(max_sand - 1)
        sand.append(min_sand + 1)
        if max_sand == min_sand:
            break

    print('#{} {}'.format(tc+1, max(sand) - min(sand)))
