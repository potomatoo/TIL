def solution(a, b):
    month_dic = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    days = b-1
    for month in range(1, a):
        days += month_dic[month]

    answer_dic = {
        0: 'FRI',
        1: 'SAT',
        2: 'SUN',
        3: 'MON',
        4: 'TUE',
        5: 'WED',
        6: 'THU'
    }
    print(days)
    return answer_dic[days%7]

print(solution(5, 24))