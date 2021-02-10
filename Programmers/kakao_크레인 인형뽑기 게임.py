def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []
    for x in moves:
        x = x-1
        for y in range(N):
            if board[y][x] != 0:
                if not stack:
                    stack.append(board[y][x])
                else:
                    if stack[-1] == board[y][x]:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(board[y][x])
                board[y][x] = 0
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))