def backtrack(idx):
    global N
    global cnt
    if idx == N:
        # 다 찾았음, 해
        cnt += 1
        return

    # 해당 상태에서 선택 할 수 있는 후보군 생성
    # 노드가 유망한지 확인: 열, 상향대각, 하향대각

    for i in range(N):
        # if 열이 유망하고, 대각들이 유망
        if not col[i] and not dia_1[idx+i] and not dia_2[N+i-idx-1]:
            # 모든 후보군에 대해서 다음 상태 실행
            col[i] = 1
            dia_1[idx+i] = 1
            dia_2[N+i-idx-1] = 1

            backtrack(idx+1)
            col[i] = 0
            dia_1[idx + i] = 0
            dia_2[N + i - idx - 1] = 0

TC = int(input())
for tc in range(TC):
    N = int(input())
    # 각 행에는 1개의 퀸만 올 수 있음
    col = [0] * N # 열의 사용여부를 판단하는 리스트
    # 대각 유망성을 판단할 리스트
    dia_1 = [0] * (2*N - 1) # 상향대각 (r+c)
    dia_2 = [0] * (2*N - 1) # 하향대각 (N+c-r-1)
    cnt = 0
    backtrack(0)
    print(f'#{tc+1} {cnt}')