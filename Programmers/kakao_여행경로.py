def solution(tickets):
    dic = dict()
    for start, end in tickets:
        if start in dic:
            dic[start].append(end)
        else:
            dic[start] = [end]
    for start in dic:
        dic[start].sort(reverse=True)

    S = ['ICN']
    path = []
    while S:
        now = S[-1]
        if now in dic and dic[now]:
            S.append(dic[now].pop())
        else:
            path.append(S.pop())
    return path[::-1]

print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))