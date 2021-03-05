def solution(A, B):
    answer = 0
    N = len(A)
    A.sort()
    B.sort()
    a = 0
    b = 0
    while a != len(A) and b != len(B):
        if A[a] < B[b]:
            a += 1
            b += 1
            answer += 1
            continue
        else:
            b += 1
    return answer


print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))
