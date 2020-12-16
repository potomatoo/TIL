import sys
sys.stdin = open('./input/input_5108.txt', 'r')

class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

def printList(lst):
    cur = lst.head
    while cur is not None:
        print(cur.data)
        cur = cur.next

TC = int(input())
for tc in range(TC):
    N, M, L = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(M):
        idx, num = map(int,input().split())
        arr.insert(idx,num)
    print('#{} {}'.format(tc+1, arr[L]))
