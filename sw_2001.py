import sys
sys.stdin = open('./input/input_2001.txt','r')

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    p_map = []
    for _ in range(N):
        line = list(map(int,input().split()))
        p_map.append(line)
    catches = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            catch = 0
            for y in range(r,r+M):
                for x in range(c,c+M):
                    catch += p_map[y][x]
            catches.append(catch)
    print('#{} {}'.format(tc+1,max(catches)))