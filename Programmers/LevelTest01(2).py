def solution(new_id):
    new_id = new_id.lower()
    now_id = ''
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isnumeric() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            now_id += new_id[i]
    new_id = now_id[0]
    for i in range(1, len(now_id)):
        if now_id[i] == '.' and new_id[-1] == '.':
            continue
        elif now_id[i] == '.' and new_id[-1] != '.':
            new_id += '.'
            continue
        new_id += now_id[i]
    if new_id:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if not new_id:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
