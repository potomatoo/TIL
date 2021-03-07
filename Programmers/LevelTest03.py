def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    N = len(A)
    idx_A = 0
    idx_B = 0
    while N:
        if A[idx_A] < B[idx_B]:
            idx_A += 1
            idx_B += 1
            answer += 1
        else:
            idx_B += 1
        N -= 1
    return answer


print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))
