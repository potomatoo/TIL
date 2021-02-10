import itertools

n = 10
def solution(n):
    board = [1, 2, 4]
    idx = 1
    check = 0
    while True:
        if check >= n:
            middle = list(itertools.product(board, repeat=idx-1))
            middle_check = -(check - n + 1)
            break
        cnt = 3 ** idx
        check += cnt
        idx += 1

    answer = ""
    for num in middle[middle_check]:
        answer += str(num)
    return answer

print(solution(n))