def solution(numbers, hand):
    answer = ''
    board = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['*', '0', '#']]
    number_dic = dict()
    number = 1
    for y in range(3):
        for x in range(3):
            number_dic[number] = (y, x)
            number += 1
    number_dic[0] = (3, 1)

    left = (3, 0)
    right = (3, 2)
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            left = number_dic[number]
            answer += 'L'
        elif number == 3 or number == 6 or number == 9:
            right = number_dic[number]
            answer += 'R'
        elif number == 2 or number == 5 or number == 8 or number == 0:
            left_d = abs(left[1] - number_dic[number][1]) + abs(left[0] - number_dic[number][0])
            right_d = abs(right[1] - number_dic[number][1]) + abs(right[0] - number_dic[number][0])
            if left_d < right_d:
                left = number_dic[number]
                answer += 'L'
            elif left_d > right_d:
                right = number_dic[number]
                answer += 'R'
            else:
                if hand == 'left':
                    left = number_dic[number]
                    answer += 'L'
                else:
                    right = number_dic[number]
                    answer += 'R'
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))