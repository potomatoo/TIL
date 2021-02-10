def solution(distance, rocks, n):
    answer = 0
    start = 0
    end = distance
    rocks.append(distance)
    rocks.sort()

    while start <= end:
        mid = (start+end) // 2
        remove_rock = 0
        remove_check = 0
        for rock in rocks:
            if rock - remove_check < mid:
                remove_rock += 1
            else:
                remove_check = rock
        if remove_rock > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))