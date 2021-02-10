def solution(nums):
    answer = set()
    N = len(nums) // 2
    for num in nums:
        if len(answer) == N:
            return N
        answer.add(num)
    return len(answer)

print(solution([3,3,3,2,2,4]))