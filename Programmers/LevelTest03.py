from collections import deque
def solution(begin, target, words):
    Q = deque()
    Q.append((begin, 0))
    visit = [0] * len(words)
    flag = False
    while Q:
        now, cnt = Q.popleft()
        if now == target:
            flag = True
            break
        for i in range(len(words)):
            if visit[i]:
                continue
            check = 0
            for j in range(len(words[i])):
                if words[i][j] == now[j]:
                    check += 1
            if check == len(now) - 1:
                visit[i] = 1
                Q.append((words[i], cnt + 1))
    if flag:
        return cnt
    else:
        return 0
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))