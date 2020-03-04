import sys
sys.stdin = open('./input/input_5656.txt','r')

TC = int(input())
for tc in range(TC):
    N, H, K = map(int,input().split())
    block = []
    for _ in range(K):
        block.append(list(map(int,input().split())))

