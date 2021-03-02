from itertools import combinations
def is_prime(k):
    if k == 1:
        return False
    elif k == 2:
        return True
    for i in range(2, k):
        if not k % i:
            return False
    return True

def solution(nums):
    answer = 0
    for com in combinations(nums, 3):
        if is_prime(sum(com)):
            answer += 1
    return answer

print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))


