def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n
    while start <= end:
        mid = (start+end) // 2
        pass_people = 0
        for time in times:
            one = mid // time
            pass_people += one
        if pass_people >= n:
            answer = mid
            end = mid - 1

        if pass_people < n:
            start = mid + 1

    return answer

print(solution(6, [7, 10]))