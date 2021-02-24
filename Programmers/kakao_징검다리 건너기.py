def solution(stones, k):
    answer = 0
    start = 1
    end = max(stones) + 1
    while start <= end:
        mid = (start + end) // 2
        now = 0
        flag = True
        for stone in stones:
            if stone <= mid:
                now += 1
            else:
                now = 0
            if now >= k:
                flag = False
                break
        if flag:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))