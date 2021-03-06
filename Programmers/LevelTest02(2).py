def solution(citations):
    k = max(citations)
    while k:
        up_check = 0
        down_check = 0
        for citation in citations:
            if citation >= k:
                up_check += 1
            elif citation < k:
                down_check += 1
        if up_check >= k and down_check <= k:
            return k
        k -= 1
    return 0



print(solution([3, 0, 6, 1, 5]))


