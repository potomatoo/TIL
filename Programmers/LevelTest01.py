def solution(nums):
    N = len(nums) // 2
    nums = list(set(nums))
    if N < len(nums):
        return N
    else:
        return len(nums)



print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
