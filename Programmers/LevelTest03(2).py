def solution(stones, k):
    answer = 0
    start = 0
    end = max(stones)
    while start <= end:
        mid = (start + end) // 2
        check = 0
        flag = False
        for i in range(len(stones)):
            if stones[i] <= mid:
                check += 1
                if check == k:
                    flag = True
                    break
            else:
                check = 0
        if flag:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


