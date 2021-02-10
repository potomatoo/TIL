from collections import deque

def solution(begin, target, words):
    def check_alpha(word1, word2):
        check = 0
        flag = True
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                check += 1
            if check == 2:
                flag = False
                break
        if not flag: return False
        return True

    answer = 0
    Q = deque()
    Q.append((begin, 0))
    visit = [0] * len(words)
    while Q:
        word, d = Q.popleft()
        if word == target:
            answer = d
            break
        for i in range(len(words)):
            if check_alpha(word, words[i]) and not visit[i]:
                visit[i] = 1
                td = d + 1
                Q.append((words[i], td))
    if answer:
        return answer
    return 0

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))