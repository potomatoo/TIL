import pandas as pd
import numpy as np

def solution(info, query):
    answer = []
    lang = []
    kind = []
    grade = []
    food = []
    score = []
    for i in range(len(info)):
        one = info[i].split()
        lang.append(one[0])
        kind.append(one[1])
        grade.append(one[2])
        food.append(one[3])
        score.append(int(one[4]))
    data = pd.DataFrame({'lang': lang, 'kind': kind, 'grade': grade, 'food': food, 'score': score})
    for i in range(len(query)):
        one = query[i].split(' and ')
        last_word = one[-1].split()
        last_word[-1] = int(last_word[-1])
        one = one[:-1] + last_word
        cal = ''
        if one[0] != '-':
            cal += 'lang == "{}"'.format(one[0])
        if one[1] != '-':
            if not cal:
                cal += 'kind == "{}"'.format(one[1])
            else:
                cal += ' & kind == "{}"'.format(one[1])
        if one[2] != '-':
            if not cal:
                cal += 'grade == "{}"'.format(one[2])
            else:
                cal += ' & grade == "{}"'.format(one[2])
        if one[3] != '-':
            if not cal:
                cal += 'food == "{}"'.format(one[3])
            else:
                cal += ' & food == "{}"'.format(one[3])

        if not cal:
            cal += 'score >= {}'.format(one[4])
        else:
            cal += ' & score >= {}'.format(one[4])

        answer.append(len(data.query(cal).index.tolist()))

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))