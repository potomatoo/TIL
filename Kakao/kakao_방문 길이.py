def solution(dirs):
    answer = 0
    road = dict()
    now = (0, 0)
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            if now[0] - 1 < -5:
                continue
            if (now[0], now[1], now[0]-1, now[1]) not in road:
                road[(now[0], now[1], now[0]-1, now[1])] = 1
                road[(now[0] - 1, now[1], now[0], now[1])] = 1
                now = (now[0]-1, now[1])
                answer += 1
            else:
                now = (now[0] - 1, now[1])
        elif dirs[i] == 'D':
            if now[0]+1 > 5:
                continue
            if (now[0], now[1], now[0]+1, now[1]) not in road:
                road[(now[0], now[1], now[0]+1, now[1])] = 1
                road[(now[0] + 1, now[1], now[0], now[1])] = 1
                now = (now[0]+1, now[1])
                answer += 1
            else:
                now = (now[0] + 1, now[1])
        elif dirs[i] == 'L':
            if now[1]-1 < -5:
                continue
            if (now[0], now[1], now[0], now[1]-1) not in road:
                road[(now[0], now[1], now[0], now[1]-1)] = 1
                road[(now[0], now[1] - 1, now[0], now[1])] = 1
                now = (now[0], now[1]-1)
                answer += 1
            else:
                now = (now[0], now[1] - 1)
        elif dirs[i] == 'R':
            if now[1]+1 > 5:
                continue
            if (now[0], now[1], now[0], now[1]+1) not in road:
                road[(now[0], now[1], now[0], now[1]+1)] = 1
                road[(now[0], now[1] + 1, now[0], now[1])] = 1
                now = (now[0], now[1]+1)
                answer += 1
            else:
                now = (now[0], now[1]+1)

    return answer

print(solution('LRLRL'))
print(solution('LULLLLLLU'))