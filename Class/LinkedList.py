class Node:
    def __init__(self, d=0, n=None):
        self.data = d  # 정수 값
        self.next = n  # 다음 노드 주소


class LinkedList:
    def __init__(self):
        self.head = None  # 첫 번째 노드
        self.tail = None  # 마지막 노드
        self.size = 0  # 노드의 수

mylist = LinkedList()

def printList(lst):  # lst: LinkedList객체
    if lst.head is None: return  # 빈 리스트 일 경우

    cur = lst.head
    print(lst.size, '[', end=' ')

    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next

    print(']')

def insertLast(lst, new):  # new: 새로 추가할 노드 객체
    # 빈 리스트일 경우
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        # 빈 리스트가 아닐 경우에는 마지막 노드를 찾는다.
        lst.tail.next = new
        lst.tail = new

    lst.size += 1

def deletLast(lst):  # 노드가 1개밖에 없는 경우도 생각을 해야 한다.
    if lst.head is None: return

    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next

    if pre is None:
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre

    lst.size -= 1
    return cur.data

def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1

def deleteFirst(lst):
    if lst.head is None: return

    # 노드가 1개일 경우 주의한다.
    lst.head = lst.head.next
    if lst.head is None:
        lst.tail = None

    lst.size -= 1

def insertAt(lst, idx, new):  # idx: 인덱스값
    # 빈 리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)

    # 마지막에 추가하는 경우 idx >= lst.size
    elif idx >= lst.size:
        insertLast(lst, new)

    else:
        # 중간에 추가하는 경우
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next

        new.next = cur
        pre.next = new
        lst.size += 1

def deleteAt(lst, idx, new):
    pass

for i in range(5):
    insertFirst(mylist, Node(i))
    printList(mylist)

for i in range(3):
    insertAt(mylist, 5, Node(i+10))
    printList(mylist)