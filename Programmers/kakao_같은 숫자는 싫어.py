def solution(arr):
    answer = [arr[0]]
    check = arr[0]
    for i in range(1, len(arr)):
        if check != arr[i]:
            check = arr[i]
            answer.append(arr[i])

    return answer

print(solution([1,1,3,3,0,1,1]))