def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    print(routes)
    visit = [0] * len(routes)

    for i in range(len(routes)):
        if visit[i] == 0:
            camera = routes[i][1]
            answer += 1
        else:
            continue
        for j in range(i+1, len(routes)):
            if routes[j][0] <= camera <= routes[j][1] and not visit[j]:
                visit[j] = 1
    return answer
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))