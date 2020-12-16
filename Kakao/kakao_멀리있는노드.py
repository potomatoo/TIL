def solution(n, edge):
    graph = [[] for _ in range(20001)]

    for e, v in edge:
        graph[e].append(v)
        graph[v].append(e)

    def find_one(graph, k, count, result, g):
        if 1 in graph[k]:
            result[g] = count
            return

        for i in range(len(graph[k])):
            find_one(graph, graph[k][i], count + 1, result, g)

    result = [0 for _ in range(20001)]
    for num in range(2, 20001):
        find_one(graph, num, 1, result, num)

    big = max(result)
    answer = result.count(big)

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))