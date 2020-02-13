TC = int(input())
for tc in range(TC):
    h1, m1, h2, m2 = map(int,input().split())
    h3, m3 = h1+h2, m1+m2
    if h3 > 12:
        h3 = h3 - 12
    if m3 >= 60:
        m3 = m3 - 60
        h3 = h3 + 1
        if h3 > 12:
            h3 = h3 - 12
    print('#{} {} {}'.format(tc+1, h3, m3))