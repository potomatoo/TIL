from _collections import deque
priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    Q = deque()
    for i in range(len(priorities)):
        Q.append((priorities[i], i))
    middle = []

    while Q:
        is_max = True
        check = Q.popleft()
        for num in Q:
            if check[0] < num[0]:
                is_max = False
                Q.append(check)
                break

        if is_max:
            middle.append(check)

    print(middle)
    answer = 0
    for i in range(len(middle)):
        if middle[i][1] == location:
            answer = i+1
            break
    return answer

print(solution(priorities, location))