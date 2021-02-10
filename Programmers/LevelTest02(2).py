def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5
    answer = 0
    cash = []
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    for city in cities:
        if not cash:
            cash.append(city)
            answer += 5
        else:
            if city not in cash:
                if len(cash) < cacheSize:
                    cash.append(city)
                else:
                    cash.pop(0)
                    cash.append(city)
                answer += 5
            else:
                cash.pop(cash.index(city))
                cash.append(city)
                answer += 1

    return answer

print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))