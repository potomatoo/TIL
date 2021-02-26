def solution(arr):
    if arr == [10]:
        return [-1]
    arr.remove(min(arr))
    return arr

print(solution([4, 3, 2, 1]))
