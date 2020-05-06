# 이진힙을 구현할 때 스택처럼
H = [0] * 100  # 완전 이진 트리로 저장
h_size = 0  # 힙에 저장된 자료의 수, 마지막 노드의 인덱스

# 최소힙 = 부모 < 자식
def push(item):
    global h_size
    h_size += 1
    H[h_size] = item
    c, p = h_size, h_size // 2
    while p and H[p] < H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c //2

arr = [26, 29, 25, 22, 33, 37, 16, 15, 18]
for val in arr:
    push(val)
print(H)
print(h_size)
def pop():
    global h_size
    ret = H[1]  # 루트
    H[1] = H[h_size]
    h_size -= 1
    p, c = 1, 2
    while c <= h_size:
        if c + 1 <= h_size and H[c] > H[c+1]:
            c = c+1
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            p = c
            c = p * 2  # c는 왼쪽 자식
        else:
            break
    return ret

while h_size:
    print(pop())



