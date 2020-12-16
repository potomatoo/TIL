import sys
sys.stdin = open('./input/input_5174.txt', 'r')

TC = int(input())
for tc in range(TC):
    E, N = map(int,input().split())
    tree = [[] for _ in range(E+2)]
    arr = list(map(int,input().split()))
    for i in range(0, len(arr)-1, 2):
        tree[arr[i]].append(arr[i+1])
    visit = [0] * (E+2)
    v = N
    visit[v] = 1
    S = []
    cnt = 0
    S.append(v)  # 출발점을 스택에 저장
    cnt += 1
    while S:
        # v의 방문하지 않은 인접정점(w)을 찾는다.
        for w in tree[v]:
            if visit[w]: continue
            # v를 스택에 저장하고, w를 방문하고, w를 현재 방문하는 정점으로 설정
            S.append(v)
            visit[w] = 1
            cnt += 1
            v = w
            break
        else:  # 더이상 방문할 인접 정점이 없다면 이전에 방문한 정점으로 돌아간다.
            v = S.pop()
    print('#{} {}'.format(tc+1, cnt))