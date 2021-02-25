from itertools import combinations
def is_prime(k):
    for i in range(2, k):
        if not k % i:
            return False
    return True

def solution(nums):
    answer = 0
    for num in combinations(nums, 3):
        if is_prime(sum(num)):
            answer += 1

    return answer

print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))

