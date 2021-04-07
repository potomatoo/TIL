def solution(cookie):
    answer = 0
    all = sum(cookie)
    can_max = all // 2
    flag = False
    for i in range(len(cookie)-1):
        for j in range(i+1, len(cookie)):
            before = sum(cookie[i:j])
            if before > can_max:
                break
            if before <= answer:
                continue
            for r in range(len(cookie), j, -1):
                after = sum(cookie[j:r])
                if before > after:
                    break
                if before == after:
                    if before == can_max:
                        return can_max
                    answer = max(before, answer)
                    flag = True
                    break

    if flag:
        return answer
    return 0

print(solution([1,1,2,3]))
print(solution([1,2,4,5]))