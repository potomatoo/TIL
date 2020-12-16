import itertools

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    people = [1 for _ in range(n+1)]
    for i in lost:
        people[i] = 0
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            
    for i in reserve:
        if i - 1 >= 1 and not people[i-1]:
            if i - 2 >= 1 and not people[i-2]:
                people[i-1] = 1
                continue
        if i + 1 <= n and not people[i+1]:
            if i+2 <= n and not people[i+2]:
                people[i+1] = 1
                continue
        if i-1 >= 1 and not people[i-1]:
            people[i-1] = 1
            continue
        if i+1 <= n and not people[i+1]:
            if i+1 <= n:
                people[i+1] = 1

    answer = people.count(1) - 1
    return answer

print(solution(n, lost, reserve))