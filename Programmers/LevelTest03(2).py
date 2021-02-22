from copy import deepcopy

def solution(tickets):
    answer = []
    seconds = []
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            seconds.append((tickets[i][1], i))

    def dfs(now, k):
        if k == len(tickets):
            c_order = deepcopy(order)
            answer.append(c_order)
        for i in range(len(tickets)):
            if visit[i]: continue
            if tickets[i][0] == now:
                order.append(tickets[i][1])
                visit[i] = 1
                dfs(tickets[i][1], k+1)
                order.pop()
                visit[i] = 0

    for second, idx in seconds:
        order = ['ICN', second]
        visit = [0] * len(tickets)
        visit[idx] = 1
        dfs(second, 1)
    answer.sort()
    return answer[0]

print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))