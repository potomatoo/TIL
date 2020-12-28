def solution(genres, plays):
    genre_cnt = []
    album = dict()
    check = dict()
    for i in range(len(genres)):
        if genres[i] in album:
            album[genres[i]].append((i, plays[i]))
            check[genres[i]] += plays[i]
        else:
            album[genres[i]] = [(i, plays[i])]
            check[genres[i]] = plays[i]
    for genre in album:
        album[genre].sort(key=lambda x:[-x[1],x[0]])
    for key, value in check.items():
        genre_cnt.append((key, value))
    genre_cnt.sort(key=lambda x:-x[1])
    print(album)
    answer = []
    for genre, cnt in genre_cnt:
        istwo = 0
        for i, k in album[genre]:
            answer.append(i)
            istwo += 1
            if istwo == 2:
                break
    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 500, 800, 2500]))