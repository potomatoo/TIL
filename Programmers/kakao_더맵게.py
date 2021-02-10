import heapq


def solution(scoville, K):
    t = 0
    heapq.heapify(scoville)
    while True:
        print(scoville)
        if len(scoville) == 1:
            if scoville[0] >= K:
                break
            else:
                t = -1
                break
        a = heapq.heappop(scoville)
        if a >= K:
            break
        b = heapq.heappop(scoville)
        new = a + (b * 2)
        heapq.heappush(scoville, new)
        t += 1

    return t
print(solution([2, 1, 3, 12, 10, 9]	, 7))