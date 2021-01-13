def solution(n, build_frame):
    answer = []
    pillars = []
    bos = []

    def is_range(a, b, c, d):
        if a < 0 or b < 0 or c < 0 or d < 0 or a > n or b > n or c > n or d > n:
            return False
        return True

    def check_pillar(down_x, down_y, up_x, up_y):
        if down_y == 0:
            return True
        else:
            if is_range(down_x-1, down_y, down_x, down_y):
                if (down_x-1, down_y, down_x, down_y) in bos:
                    return True
            if is_range(down_x, down_y, down_x+1, down_y):
                if (down_x, down_y, down_x + 1, down_y) in bos:
                    return True
            if is_range(down_x, down_y-1, down_x, down_y):
                if (down_x, down_y-1, down_x, down_y) in pillars:
                    return True
        return False

    def check_bo(left_x, left_y, right_x, right_y):
        if is_range(left_x, left_y, left_x, left_y-1):
            if (left_x, left_y-1, left_x, left_y) in pillars:
                return True
        if is_range(right_x, right_y, right_x, right_y-1):
            if (right_x, right_y-1, right_x, right_y) in pillars:
                return True
        if is_range(left_x-1, left_y, left_x, left_y) and is_range(right_x, right_y, right_x+1, right_y):
            if (left_x-1, left_y, left_x, left_y) in bos and (right_x, right_y, right_x+1, right_y) in bos:
                return True
        return False

    def delete_pillar(x, y):
        pillars.remove((x, y, x, y+1))
        for down_x, down_y, up_x, up_y in pillars:
            if not check_pillar(down_x, down_y, up_x, up_y):
                return False
        for left_x, left_y, right_x, right_y in bos:
            if not check_bo(left_x, left_y, right_x, right_y):
                return False
        return True

    def delete_bo(x, y):
        bos.remove((x, y, x+1, y))
        for down_x, down_y, up_x, up_y in pillars:
            if not check_pillar(down_x, down_y, up_x, up_y):
                return False
        for left_x, left_y, right_x, right_y in bos:
            if not check_bo(left_x, left_y, right_x, right_y):
                return False
        return True

    for x, y, kind, do in build_frame:
        if do == 1:
            if kind == 0:
                if is_range(x, y, x, y+1):
                    if check_pillar(x, y, x, y+1):
                        pillars.append((x, y, x, y+1))
                        continue
            elif kind == 1:
                if is_range(x, y, x+1, y):
                    if check_bo(x, y, x+1, y):
                        bos.append((x, y, x+1, y))
                        continue
        elif do == 0:
            if kind == 0:
                if not delete_pillar(x, y):
                    pillars.append((x, y, x, y+1))
                    continue
            elif kind == 1:
                if not delete_bo(x, y):
                    bos.append((x, y, x+1, y))
                    continue
    for down_x, down_y, up_x, up_y in pillars:
        answer.append([down_x, down_y, 0])
    for left_x, left_y, right_x, right_y in bos:
        answer.append([left_x, left_y, 1])
    answer.sort()
    return answer

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))