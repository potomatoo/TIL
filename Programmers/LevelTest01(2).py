def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for y in range(len(board)):
            if board[y][move-1]:
                if stack:
                    if stack[-1] != board[y][move-1]:
                        stack.append(board[y][move-1])
                    else:
                        stack.pop()
                        answer += 2
                else:
                    stack.append(board[y][move - 1])
                board[y][move - 1] = 0
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
