A, B = map(int, input().split())
N, M = map(int, input().split())
robot = []
for _ in range(N):
    x, y, d = input().split()
    robot.append([B-int(y), int(x)-1, d])

order = []
for _ in range(M):
    robot_n, robot_o, order_n = input().split()
    order.append([int(robot_n)-1, robot_o, int(order_n)])

d_dict = {
    'E': [0, 0, 1],
    'S': [1, 1, 0],
    'W': [2, 0, -1],
    'N': [3, -1, 0],
}

break_answer = 'OK'
flag = True

for robot_n, robot_o, order_n in order:
    if robot_o == 'R':
        if not ((d_dict[robot[robot_n][2]][0] + order_n) % 4):
            robot[robot_n][2] = 'E'
        elif (d_dict[robot[robot_n][2]][0] + order_n) % 4 == 1:
            robot[robot_n][2] = 'S'
        elif (d_dict[robot[robot_n][2]][0] + order_n) % 4 == 2:
            robot[robot_n][2] = 'W'
        else:
            robot[robot_n][2] = 'N'

    elif robot_o == 'L':
        if robot[robot_n][2] == 'E' or robot[robot_n][2] == 'W':
            if not ((d_dict[robot[robot_n][2]][0] + order_n) % 4):
                robot[robot_n][2] = 'E'
            elif (d_dict[robot[robot_n][2]][0] + order_n) % 4 == 1:
                robot[robot_n][2] = 'N'
            elif (d_dict[robot[robot_n][2]][0] + order_n) % 4 == 2:
                robot[robot_n][2] = 'W'
            else:
                robot[robot_n][2] = 'S'
        else:
            if not ((d_dict[robot[robot_n][2]][0] + order_n) % 4):
                robot[robot_n][2] = 'W'
            elif (d_dict[robot[robot_n][2]][0] + order_n) % 4 == 1:
                robot[robot_n][2] = 'S'
            elif (d_dict[robot[robot_n][2]][0] + order_n) % 4 == 2:
                robot[robot_n][2] = 'E'
            else:
                robot[robot_n][2] = 'N'

    else:
        y = robot[robot_n][0]
        x = robot[robot_n][1]
        d = robot[robot_n][2]
        flag2 = True
        while order_n:
            y = y + d_dict[d][1]
            x = x + d_dict[d][2]
            if y < 0 or y > B-1 or x < 0 or x > A-1:
                break_answer = 'Robot {} crashes into the wall'.format(robot_n+1)
                flag2 = False
                break
            for i in range(len(robot)):
                if i == robot_n:
                    continue
                if [robot[i][0], robot[i][1]] == [y, x]:
                    break_answer = 'Robot {} crashes into robot {}'.format(robot_n + 1, i+1)
                    flag2 = False
                    break
            if not flag2:
                flag = False
                break
            order_n -= 1

        robot[robot_n] = [y, x, d]

        if not flag2:
            flag = False
            break

    if not flag:
        break

print(break_answer)