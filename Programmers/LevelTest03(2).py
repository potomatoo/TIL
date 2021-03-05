def solution(genres, plays):
    answer = []
    time_dic = dict()
    order_dic = dict()
    for i in range(len(genres)):
        if genres[i] not in time_dic:
            time_dic[genres[i]] = plays[i]
            order_dic[genres[i]] = [(i, plays[i])]
        else:
            time_dic[genres[i]] += plays[i]
            order_dic[genres[i]].append((i, plays[i]))

    time = []
    for key, value in time_dic.items():
        time.append((key, value))
    time.sort(key=lambda x: -x[1])
    for genre, t in time:
        cnt = 0
        order_dic[genre].sort(key=lambda x: [-x[1], x[0]])
        if len(order_dic[genre]) > 2:
            while cnt != 2:
                answer.append(order_dic[genre][cnt][0])
                cnt += 1
        else:
            for kk in order_dic[genre]:
                answer.append(kk[0])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

