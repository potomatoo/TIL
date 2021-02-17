def solution(m, musicinfos):
    answer = []
    mm = []
    now_m = ''
    for i in range(len(m)):
        if now_m and m[i] != '#':
            mm.append(now_m)
            now_m = m[i]
            continue
        if now_m and m[i] == '#':
            now_m += '#'
            mm.append(now_m)
            now_m = ''
            continue
        now_m += m[i]
    if now_m:
        mm.append(now_m)

    cnt = 0
    for musicinfo in musicinfos:
        start, end, name, e = musicinfo.split(',')
        start_hour, start_min = int(start[:2]), int(start[3:])
        end_hour, end_min = int(end[:2]), int(end[3:])
        play_time = (end_hour - start_hour) * 60 + (end_min - start_min)
        em = []
        now_e = ''
        for i in range(len(e)):
            if now_e and e[i] != '#':
                em.append(now_e)
                now_e = e[i]
                continue
            if now_e and e[i] == '#':
                now_e += '#'
                em.append(now_e)
                now_e = ''
                continue
            now_e += e[i]
        if now_e:
            em.append(now_e)
        if play_time <= len(em):
            em = em[:play_time]
        else:
            em = em * (play_time//len(em)) + em[:play_time%len(em)]
        check_em = ''
        for i in range(len(em)-len(mm)+1):
            for j in range(i, i+len(mm)):
                check_em += em[j]
            print(check_em)
            if check_em == m:
                answer.append((cnt, play_time, name))
                break
            check_em = ''
        cnt += 1
    if not answer:
        return '(None)'
    answer.sort(key=lambda x:[-x[1], x[0]])
    print(answer)
    return answer[0][2]

print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))