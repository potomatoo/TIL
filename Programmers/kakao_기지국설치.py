def solution(n, stations, w):
    answer = 0
    check_len = []
    start = 0

    for i in range(len(stations)):
        stations[i] -= 1
        min_check = []
        max_check = []
        for j in range(w, 0, -1):
            if min_check and max_check:
                break
            if stations[i]-j >= 0:
                min_check.append(stations[i]-j)
            if stations[i]+j <= n-1:
                max_check.append(stations[i]+j)
        if not min_check:
            min_check.append(stations[i])
        if not max_check:
            max_check.append(stations[i])
        check_len.append(min_check[0] - start)
        start = max_check[0] + 1

    if start != n:
        check_len.append(n-start)

    for i in range(len(check_len)):
        wifi = check_len[i] // ((2*w)+1)
        wifi_flag = check_len[i] % ((2 * w) + 1)
        if wifi_flag:
            answer += (wifi + 1)
        else:
            answer += wifi

    return answer

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))