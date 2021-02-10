def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    newid = ''
    # 2단계
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isnumeric() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            newid += new_id[i]
    # 3단계
    while True:
        if not newid.count('..'):
            break
        newid = newid.replace('..', '.')
    # 4단계
    if len(newid) >= 1 and newid[0] == '.':
        newid = newid[1:]
    if len(newid) >= 1 and newid[-1] == '.':
        newid = newid[:-1]
    # 5단계
    if not newid:
        newid = 'a'
    # 6단계
    if len(newid) >= 16:
        newid = newid[:15]
        if newid[-1] == '.':
            newid = newid[:14]
    # 7단계
    if len(newid) <= 2:
        plus = newid[-1]
        while True:
            if len(newid) == 3:
                break
            newid += plus

    return newid

print(solution("=.="))