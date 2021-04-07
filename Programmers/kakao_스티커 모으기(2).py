def solution(sticker):
    def check_visit(idx):
        if idx == 0:
            visit[-1] = 1
            visit[idx+1] = 1
            visit[idx] = 1
        elif idx == len(sticker) - 1:
            visit[idx-1] = 1
            visit[idx] = 1
            visit[0] = 1
        else:
            visit[idx - 1] = 1
            visit[idx] = 1
            visit[idx+1] = 1

    def find_max(idx, visit):
        mid_answer = 0
        mid_answer += sticker[idx]
        check_visit(idx)
        while True:
            if sum(visit) == len(sticker):
                break
            max_number = 0
            for i in range(len(sticker)):
                if visit[i]: continue
                max_number = max(sticker[i], max_number)
            now_max = sticker.index(max_number)
            check_visit(now_max)
            mid_answer += sticker[now_max]
        return mid_answer

    answer = 0
    for i in range(len(sticker)):
        visit = [0] * len(sticker)
        answer = max(answer, find_max(i, visit))
    return answer

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))