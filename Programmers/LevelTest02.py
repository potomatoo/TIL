def solution(n):
    def trans_n(num):
        if num == 1:
            return '1'
        trans = ''
        while num // 2 >= 1:
            remain = num % 2
            num = num // 2
            trans = str(remain) + trans
            if num < 2:
                trans = str(num) + trans
        return trans
    check = trans_n(n).count('1')
    n += 1
    while True:
        if trans_n(n).count('1') == check:
            break
        n += 1
    return n

print(solution(78))
print(solution(15))


