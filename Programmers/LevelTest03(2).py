def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        pass_people = 0
        for time in times:
            pass_people += (mid // time)
        if pass_people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


print(solution(6, [7, 10]))

