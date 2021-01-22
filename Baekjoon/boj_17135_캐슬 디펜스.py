from itertools import combinations
from copy import deepcopy

def move_enemy():
    after_move = []
    for ey, ex in enemies:
        if (ey, ex) in after_attack:
            continue
        if ey+1 == N-1:
            continue
        after_move.append((ey+1, ex))
    return after_move

def attak(attacker):
    kill = set()
    for x in attacker:
        can_kill = []
        for ey, ex in enemies:
            if abs(ey-(N-1)) + abs(ex-x) <= D:
                can_kill.append((ey, ex, abs(ey-(N-1)) + abs(ex-x)))
        if can_kill:
            can_kill.sort(key=lambda x:[x[2], x[1]])
            kill.add((can_kill[0][0], can_kill[0][1]))
    return list(kill)

def check_enemy():
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                start_enemies.append((y, x))

N, M, D = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
board.append([2] * M)
N += 1

attackers = list(combinations([x for x in range(M)], 3))

start_enemies = []
check_enemy()

answer = 0
for attacker in attackers:
    mid_answer = 0
    enemies = deepcopy(start_enemies)
    while True:
        after_attack = attak(attacker)
        mid_answer += len(after_attack)
        after_move = move_enemy()
        if not after_move:
            break
        enemies = after_move

    answer = max(answer, mid_answer)
print(answer)


