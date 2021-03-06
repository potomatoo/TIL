from collections import deque
def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5
    for i in range(len(cities)):
        cities[i] = cities[i].upper()
    answer = 0
    Q = deque()
    for i in range(len(cities)):
        if len(Q) == cacheSize:
            if cities[i] in Q:
                Q.remove(cities[i])
                Q.append(cities[i])
                answer += 1
            else:
                Q.popleft()
                Q.append(cities[i])
                answer += 5
        else:
            if cities[i] in Q:
                Q.remove(cities[i])
                Q.append(cities[i])
                answer += 1
            else:
                Q.append(cities[i])
                answer += 5
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))


