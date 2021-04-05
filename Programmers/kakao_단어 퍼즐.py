# 효율성 bad!

from collections import deque

def solution(strs, t):
    Q = deque()

    for str in strs:
        if str[0] == t[0]:
            Q.append((1, str))

    while Q:
        cnt, now = Q.popleft()
        if now == t:
            return cnt
        for i in range(len(strs)):
            if now + strs[i] == t[:len(now)+len(strs[i])]:
                Q.append((cnt+1, now+strs[i]))

    return -1

print(solution(["ba","na","n","a"], "banana"))
print(solution(["app","ap","p","l","e","ple","pp"], "apple"))
print(solution(["ba","an","nan","ban","n"], "banana"))
