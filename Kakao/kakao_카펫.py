def solution(brown, yellow):
    def g_yellow(n):
        com_yellow = []
        for i in range(1, n+1):
            if i > n//i:
                break
            if not n % i:
                com_yellow.append([n // i, i])
        return com_yellow
    can_yellow = g_yellow(yellow)

    for height, width in can_yellow:
        check_brown = (height * 2) + (width * 2) + 4
        if check_brown == brown:
            return [height+2, width+2]

print(solution(8, 1))