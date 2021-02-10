def solution(key, lock):
    answer = True
    def rotate(board):
        rotate_key = [[0 for _ in range(len(key))] for _ in range(len(key))]
        for y in range(len(key)):
            for x in range(len(key)):
                rotate_key[x][y] = board[-y-1][x]
        return rotate_key

    for z in range(len(key)):
        print(key[z])
    print()
    key = rotate(key)
    for z in range(len(key)):
        print(key[z])


    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))