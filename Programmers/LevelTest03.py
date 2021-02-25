def solution(dirs):
    answer = 0
    visit = []
    dir_dic = {
        'U': [-1, 0],
        'D': [1, 0],
        'L': [0, -1],
        'R': [0, 1]
    }
    y, x = 5, 5
    for dir in dirs:
        ty = y + dir_dic[dir][0]
        tx = x + dir_dic[dir][1]
        if ty < 0 or tx < 0 or ty > 10 or tx > 10:
            continue
        if {(ty, tx), (y, x)} not in visit:
            visit.append({(ty, tx), (y, x)})
            answer += 1
        y, x = ty, tx
    return answer


print(solution('ULURRDLLU'))
print(solution('LULLLLLLU'))