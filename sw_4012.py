import sys
sys.stdin = open('./input/input_4012.txt','r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    f_map = []
    for _ in range(N):
        line = list(map(int,input().split()))
        f_map.append(line)

