def solution(m, musicinfos):
    check = []
    for i in range(len(musicinfos)):
        musicinfo = musicinfos[i].split(',')

        play_time = 0
        if int(musicinfo[1][:2]) - int(musicinfo[0][:2]):
            play_time += (60*(int(musicinfo[1][:2]) - int(musicinfo[0][:2])))
        play_time += int(musicinfo[1][3:]) - int(musicinfo[0][3:])

        new_melody = []
        for k in range(len(musicinfo[3])-1):
            if musicinfo[3][k] == '#':
                continue
            if musicinfo[3][k+1] == '#':
                new_melody.append(musicinfo[3][k]+'#')
                continue
            new_melody.append(musicinfo[3][k])
        if musicinfo[3][-1] != '#':
            new_melody.append(musicinfo[3][-1])

        len_melody = len(musicinfo[3]) - musicinfo[3].count('#')
        if play_time <= len_melody:
            musicinfo[3] = new_melody[:play_time]
        else:
            cnt = play_time // len_melody
            remain = play_time % len_melody
            musicinfo[3] = (new_melody * cnt) + (new_melody[:remain])

        contain_check = ''
        f = len(m) - m.count('#')
        flag = True
        for i in range(len(musicinfo[3])-f+1):
            for j in range(i, i+f):
                contain_check += musicinfo[3][j]

            if contain_check == m:
                check.append((play_time, musicinfo[2]))
                flag = False
                break
            contain_check = ''
            if not flag:
                break
    if not check:
        return '(None)'
    check.sort(key=lambda x:-x[0])

    return check[0][1]

print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))