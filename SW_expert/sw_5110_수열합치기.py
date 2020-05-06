import sys
sys.stdin = open('./input/input_5110.txt', 'r')

class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new

    if lst.head is None:
        lst.head = first
        lst.tail = last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]:
                break
            cur = cur.next
        if cur is None:  # 뒤에 추가
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None:  # 앞에 추가
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else:  # 중간에 추가가
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last

def printList(lst):
    if lst.head is None:
        return
    cur = lst.tail
    for i in range(10):
        print(cur.data, end=' ')
        cur = cur.prev
    print()

TC = int(input())
for tc in range(TC):
    mylist = LinkedList()
    N, M = map(int, input().split())
    for _ in range(M):
        arr = list(map(int, input().split()))
        addList(mylist, arr)
    print('#%d' %(tc+1), end=' ')
    printList(mylist)