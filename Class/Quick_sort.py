arr = [9, 5, 7, 6, 1, 2, 3, 8, 3]
N = len(arr)

def getMin(lo, hi):  # arr[]에서 최소값을 찾아서 반환

    if lo == hi: return arr[lo]

    ret = getMin(lo, hi-1)
    return min(ret, arr[hi])

# print(getMin(0, N-1))

def getMin2(lo, hi):
    print(lo,hi)
    if lo == hi: return arr[lo]

    mid = (lo+hi) >> 1
    l = getMin2(lo, mid)
    r = getMin2(mid + 1, hi)
    return min(l,r)

print(getMin2(0, N-1))

def quick_sort(arr, left, right):  # 왼쪽 시작점, 오른쪽 끝지점
    # pivot 위치 결정( 피복을 기준으로 큰값은 오른쪽, 작은 값은 왼쪽으로 구분
    # 왼쪽 부분집합 정렬
    # 오른쪽 부분집합 정렬
    if left < right:
        # 피봇 구하기
        pivot = hoare_partition(arr, left, right)
        # 왼쪽 부분집합 정렬 실행
        quick_sort(arr, left, pivot-1)
        # 오른쪽 부분집합 정렬 실행
        quick_sort(arr, pivot+1, right)

def hoare_partition(arr, left, right):
    # i, j를 설정하고, 큰값 찾고, 작은값 찾아서 위치 바꿔주기
    i = left
    j = right
    pivot = arr[left]

    # i가 j보다 작을 때까지 계속해서 반복
    while i <= j:
        # 피봇보다 큰값이 나올 때 까지 i증가
        while i <= j and arr[i] <= pivot:
            i += 1
        # 피봇보다 작은 값이 나올 때 까지 j감소
        while i <= j and arr[j] >= pivot:
            j -= 1

        # i 가 j 보다 작으면, 위치 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]

    return j
quick_sort(arr, 0, len(arr)-1)
print(arr)