import sys
sys.stdin = open('./input/input_2806.txt','r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]

