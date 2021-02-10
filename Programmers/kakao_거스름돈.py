from itertools import combinations

def solution(n, money):
    answer = set()
    new_money = []
    for i in range(len(money)):
        cnt = n // money[i]
        for _ in range(cnt):
            new_money.append(money[i])
    for k in range(1, len(new_money)+1):
        com = combinations(new_money, k)
        for one in com:
            if sum(one) == n:
                answer.add(one)
    return len(answer) % 1000000007

print(solution(5, [1,2,5]))