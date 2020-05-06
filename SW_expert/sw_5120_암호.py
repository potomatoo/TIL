import sys
sys.stdin = open('./input/input_5120.txt', 'r')

class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d  # 정수 값
        self.prev = p
        self.next = n  # 다음 노드 주소

class LinkedList:
    def __init__(self):
        self.head = None  # 첫 번째 노드
        self.tail = None  # 마지막 노드
        self.size = 0  # 노드의 수

def addLast(lst, new):  # new: 새로 추가할 노드 객체
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new

    lst.size += 1

def printLast(lst):
    if lst.head is None: return
    cur = lst.head.prev
    if lst.size < 10:
        for i in range(lst.size):
            if i == lst.size-1:
                print(cur.data)
            else:
                print(cur.data, end=' ')
            cur = cur.prev

    elif lst.size >= 10 :
        for i in range(10):
            if i == 9:
                print(cur.data)
            else:
                print(cur.data, end=' ')
            cur = cur.prev

TC = int(input())
for tc in range(TC):
    mylist = LinkedList()
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    for val in arr:
        addLast(mylist, Node(val))

    cur = mylist.head
    for _ in range(K):  # M
        for _ in range(M):
            cur = cur.next  # k

        prev = cur.prev
        new = Node(prev.data + cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new  # 새로 추가된 위치를 시작위치로 재설정
        mylist.size += 1
    print('#%d' % (tc + 1), end=' ')
    printLast(mylist)