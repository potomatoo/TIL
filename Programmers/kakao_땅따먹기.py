def solution(land):
    for i in range(1,len(land)):
        x0 = max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][0] += x0
        x1 = max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][1] += x1
        x2 = max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][2] += x2
        x3 = max(land[i - 1][0], land[i - 1][1], land[i - 1][2])
        land[i][3] += x3

    return max(land[len(land)-1])

print(solution([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))