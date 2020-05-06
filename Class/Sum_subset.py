arr = [i for i in range(1,11)]
N = len(arr)
A = []  # 포함되는 요소들의 집합
def backtrack(k, cur_sum):
    if cur_sum > 10: return
    if k == N:
        if cur_sum == 10:
            print(A)
    else:
        A.append(arr[k])
        backtrack(k+1, cur_sum+arr[k])  # k번 원소를 포함하는 경우
        A.pop()
        backtrack(k+1, cur_sum) # k번 원소를 포함하지 않는 경우

print(backtrack(0, 0))

