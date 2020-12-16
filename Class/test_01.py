import sys
sys.stdin = open('./input/input_test01.txt', 'r')

# 해당 체크가 들어있는 9개 영역을 확인하는 함수이다.
def area_checking(y, x, num):
    check_area_y = 0
    check_area_x = 0
    # y와 x가 어느 영역에 소개있는지 확인한다.
    if y == 0 or y == 1 or y == 2:
        check_area_y = 0
    if y == 3 or y == 4 or y == 5:
        check_area_y = 3
    if y == 6 or y == 7 or y == 8:
        check_area_y = 6

    if x == 0 or x == 1 or x == 2:
        check_area_x = 0
    if x == 3 or x == 4 or x == 5:
        check_area_x = 3
    if x == 6 or x == 7 or x == 8:
        check_area_x = 6

    # 해당 구역을 돌면서 0이 아니고 같은 숫자가 있지 않은지 확인하며 있으면 False를 리턴한다.
    for yy in range(check_area_y, check_area_y+3):
        for xx in range(check_area_x, check_area_x+3):
            if yy == y or xx == x:
                continue
            if s_map[yy][xx] != 0 and s_map[yy][xx] == num:
                return False

    # 문제가 없으면 True를 리턴한다.
    return True

# 이 함수를 실행하여 스도쿠를 진행하는 데 문제가 없는지 판별하는 함수를 생성한다.
def is_correct(check):
    y = check[0]
    x = check[1]
    num = check[2]

    # 해당 위치에 숫자를 저장한다.
    s_map[y][x] = num

    # 행과 열을 기준으로 스토쿠가 진행되는 데 문제가 없는지 확인한다.
    for i in range(9):
        if i != x and s_map[y][i] == num:
            return False
        if i != y and s_map[i][x] == num:
            return False

    # 해당 체크 위치가 들어있는 9칸 구역을 확인한다.
    if not area_checking(y, x, num):
        return False

    # 문제가 없으면 True를 리턴한다.
    return True

TC = int(input())
for tc in range(TC):
    N = int(input())
    # 스도쿠 배열을 생성한다.
    s_map = []
    for _ in range(9):
        s_map.append(list(map(int,input().split())))
    # 체크를 해야되는 배열을 생성한다.
    checks = []
    for _ in range(N):
        checks.append(list(map(int,input().split())))
    # 체크를 해야되는 배열을 돌면서 스도쿠가 진행되는 횟수를 판별한다.
    ans = 0
    for check in checks:
        if not is_correct(check):
            break
        # 문제가 없이 진행되면 ans를 1씩 더해준다.
        ans += 1
        
    print('#{} {}'.format(tc+1, ans))
