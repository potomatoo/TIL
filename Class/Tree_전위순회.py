import sys
sys.stdin = open('./input/input_tree.txt', 'r')

V = int(input())
E = V - 1
arr = list(map(int,input().split()))
L = [0] * (V+1)  # 왼쪽 자식
R = [0] * (V+1)  # 오른쪽 자식
P = [0] * (V+1)  # 부모

for i in range(0, len(arr), 2):
    parent, child = arr[i], arr[i+1]
    if L[parent]:
        R[parent] = child
    else:
        L[parent] = child
    P[child] = parent

def inorder(v):  # 방문하는 노드 번호
    if v == 0: return
    # 여기서 방문하면 전위
    print(v, end=' ')
    inorder(L[v])
    # 여기서 방문하면 중위
    # print(v, end=' ')
    inorder(R[v])
    # 여기서 방문하면 후위

inorder(1)
