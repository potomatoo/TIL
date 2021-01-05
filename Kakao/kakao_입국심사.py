def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        pass_people = 0
        for i in range(len(times)):
            pass_people += (mid // times[i])
            if pass_people >= n:
                answer = mid
                end = mid - 1
                break
        if pass_people < n:
            start = mid + 1
    return answer

print(solution(6, [7, 10]))