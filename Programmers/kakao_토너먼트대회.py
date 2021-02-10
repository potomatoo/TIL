def solution(n,a,b):
    def go_up(n):
        if n % 2 == 0:
            return n // 2
        else:
            return n // 2 + 1

    round = 1
    while True:
        if abs(a - b) == 1 and (a // 2 != b // 2):  # 맞붙게 되는 경우
            break
        else:
            a = go_up(a)
            b = go_up(b)
            round += 1

    return round

