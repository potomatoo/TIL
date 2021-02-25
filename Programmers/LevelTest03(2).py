from copy import deepcopy

def solution(tickets):
    def dfs(now, k):
        if k == len(tickets)-1:
            c_order = deepcopy(order)
            answer.append(c_order)
        for i in range(len(tickets)):
            if visit[i]:
                continue
            if now == tickets[i][0]:
                visit[i] = 1
                order.append(tickets[i][1])
                dfs(tickets[i][1], k + 1,)
                visit[i] = 0
                order.pop()
    answer = []
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            visit = [0] * len(tickets)
            visit[i] = 1
            order = ['ICN', tickets[i][1]]
            dfs(tickets[i][1], 0)
    answer.sort()
    return answer[0]


print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
