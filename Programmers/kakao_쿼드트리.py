count_one = 0
count_zero = 0

def solution(arr):
    def devide_area(i, j, n):
        global count_one, count_zero
        flag = True
        check = arr[i][j]
        for y in range(i, i + n):
            if not flag: break
            for x in range(j, j + n):
                if check != arr[y][x]:
                    flag = False
                    devide_area(i, j, n // 2)
                    devide_area(i, j + n // 2, n // 2)
                    devide_area(i + n // 2, j, n // 2)
                    devide_area(i + n // 2, j + n // 2, n // 2)
                    break

        if flag:
            if check:
                count_one += 1
            else:
                count_zero += 1

    devide_area(0, 0, len(arr))
    answer = [count_zero, count_one]

    return answer