import sys
sys.stdin = open('./input/input_4871.txt','r')
TC = int(input())
for tc in range(TC):
    V, E = map(int,input().split())
    G = [[] for _ in range(V+1)]  # 그래프
    visit = [0] * (V+1)  # 방문정보
    S = []  # 스택
    check = []
    for _ in range(E):
        u, v = map(int,input().split())
        G[u].append(v)

    start, end = map(int, input().split())

    # 1번 정점 출발점
    v = start
    visit[v] = 1
    check.append(v)  # 출발점을 방문하고 현재 방문하는 정점을 v에 저장
    S.append(v)  # 출발점을 스택에 저장
    while S:
        # v의 방문하지 않은 인접정점(w)을 찾는다.
        for w in G[v]:
            if visit[w]: continue
            # v를 스택에 저장하고, w를 방문하고, w를 현재 방문하는 정점으로 설정
            S.append(v)
            visit[w] = 1
            check.append(w)
            v = w
            break
        else:  # 더이상 방문할 인접 정점이 없다면 이전에 방문한 정점으로 돌아간다.
            v = S.pop()

    if end in check:
        print('#{} {}'.format(tc+1,1))

    else:
        print('#{} {}'.format(tc+1,0))

