def solution(citations):
    ans = 0
    citations.sort(reverse=True)
    val = citations[0]
    flag = False

    while val:
        check = 0
        for i in range(len(citations)):
            if citations[i] >= val:
                check += 1
            if check >= val:
                flag = True
                break
        if flag:
            ans = val
            break
        val -= 1

    return ans

print(solution([5, 5, 5, 5, 5]))