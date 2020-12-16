import sys
sys.stdin = open('./input/input_1248.txt', 'r')

TC = int(input())
for tc in range(TC):
    V, E, a, b = map(int,input().split())
    G = [[(0, 0, 0)] for _ in range(V+1)]
    arr = list(map(int,input().split()))
    for i in range(0, len(arr), 2):
        G[arr[i+1]].append(arr[i])

