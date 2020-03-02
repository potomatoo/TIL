import sys
sys.stdin = open('./input/input_4008.txt','r')

def DFS(k, n, s, op1, op2, op3, op4):
    global MAX, MIN
    if k == n:
        if s > MAX:
            MAX = s
        if s < MIN:
            MIN = s
        return
    else:
        if op1 > 0:
            DFS(k+1, n, s+num[k], op1-1, op2, op3, op4)
        if op2 > 0:
            DFS(k+1, n, s-num[k], op1, op2-1, op3, op4)
        if op3 > 0:
            DFS(k+1, n, s*num[k], op1, op2, op3-1, op4)
        if op4 > 0:
            DFS(k+1, n, int(s/num[k]), op1, op2, op3, op4-1)

for tc in range(1, int(input())+1):
    n = int(input())
    op1, op2, op3, op4 = map(int, input().split())
    num = list(map(int, input().split()))
    MAX = -0xffffffff
    MIN = 0xffffffff
    SUM = num[0]
    DFS(1, n, SUM, op1, op2, op3, op4)
    print('#%d %d' %(tc, MAX-MIN))
