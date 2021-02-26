def find_block(n, m, map):
    remove = set()
    for y in range(n):
        for x in range(m):
            if map[y][x] == '^':
                continue
            flag = True
            check = [(y, x)]
            for i in range(3):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or ty > n-1 or tx < 0 or tx > m-1:
                    flag = False
                    break
                if map[ty][tx] != map[y][x]:
                    flag = False
                    break
                check.append((ty, tx))
            if flag:
                for yy, xx in check:
                    remove.add((yy, xx))
    return remove

def go_down(n, m, map):
    new_map = []
    return_map = [['' for _ in range(m)] for _ in range(n)]
    for x in range(m):
        check = []
        for y in range(n):
            check.append(map[y][x])
        new_check = []
        for i in range(len(check)):
            if check[i] == '^':
                continue
            new_check.append(check[i])
        while len(new_check) != n:
            new_check = ['^'] + new_check
        new_map.append(new_check)

    for y in range(m):
        for x in range(n):
            return_map[x][y] = new_map[y][x]
    return return_map

dy = [0, 1, 1]
dx = [1, 0, 1]
def solution(m, n, board):
    answer = 0
    n, m = m, n
    map = []
    for y in range(n):
        one = ','.join(board[y])
        map.append(one.split(','))

    while True:
        remove = find_block(n, m, map)
        if not remove:
            break
        for remove_y, remove_x in remove:
            map[remove_y][remove_x] = '^'
        new_map = go_down(n, m, map)
        map = new_map

    for y in range(n):
        for x in range(m):
            if map[y][x] == '^':
                answer += 1
    return answer

print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))

