cnt = 0
def solution(n):
    global cnt
    def backtrack(idx):
        global cnt
        if idx == n:
            # 다 찾았음, 해
            cnt += 1
            return

        # 해당 상태에서 선택 할 수 있는 후보군 생성
        # 노드가 유망한지 확인: 열, 상향대각, 하향대각

        for i in range(n):
            # if 열이 유망하고, 대각들이 유망
            if not col[i] and not dia_1[idx + i] and not dia_2[n + i - idx - 1]:
                # 모든 후보군에 대해서 다음 상태 실행
                col[i] = 1
                dia_1[idx + i] = 1
                dia_2[n + i - idx - 1] = 1
                print(idx, i, col)
                print(idx,i,  dia_1)
                print(idx,i, dia_2)
                backtrack(idx + 1)
                col[i] = 0
                dia_1[idx + i] = 0
                dia_2[n + i - idx - 1] = 0

    col = [0] * n
    dia_1 = [0] * (2*n-1)
    dia_2 = [0] * (2 * n - 1)
    backtrack(0)

    return cnt

print(solution(4))