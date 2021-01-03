def solution(A, B):
    answer=0
    A.sort()
    B.sort()
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] < B[j]:
                answer += 1
                B.remove(B[j])
                break
    return answer

print(solution([5,1,3,7], [2,2,6,8]))