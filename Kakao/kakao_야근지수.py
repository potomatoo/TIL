import heapq

def solution(n, works):
    answer = 0
    for i in range(len(works)):
        works[i] = -works[i]
    heapq.heapify(works)

    while n:
        max_work = heapq.heappop(works)
        if max_work == 0:
            return 0
        heapq.heappush(works, max_work+1)
        n -= 1
    for work in works:
        answer += work ** 2
    return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))