'''
다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.
모든 정점을 깊이 우선 탐색하여 화면에 깊이우선탐색 경로를 출력하시오.
시작 정점을 1로 시작하시오.
'''
# 무향그래프는 (i,j) (j,i) 둘 다 저장을 해야한다.
# 유향그래프는 (i,j) 하나만 저장한다.
import sys
sys.stdin = open('./input/input_DFS.txt','r')

# 재귀를 사용하여 DFS 구현
# def DFS(v):
#     visit[v] = 1; print(v, end=' ')
#     for w in G[v]:
#         if visit[w]: continue
#         DFS(w)
# 스택을 사용하여 DFS 구현 (추천)
V, E = map(int,input().split())
G = [[] for _ in range(V+1)]  # 그래프
visit = [0] * (V+1)  # 방문정보
S = []  # 스택

for _ in range(E):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

# 1번 정점 출발점
v = 1
visit[v] = 1
print(v, end=' ')# 출발점을 방문하고 현재 방문하는 정점을 v에 저장
S.append(v)  # 출발점을 스택에 저장
while S:
    # v의 방문하지 않은 인접정점(w)을 찾는다.
    for w in G[v]:
        if visit[w]: continue
        # v를 스택에 저장하고, w를 방문하고, w를 현재 방문하는 정점으로 설정
        S.append(v)
        visit[w] = 1
        print(w, end=' ')
        v = w
        break
    else:  # 더이상 방문할 인접 정점이 없다면 이전에 방문한 정점으로 돌아간다.
        v = S.pop()


