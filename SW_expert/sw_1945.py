TC = int(input())
for tc in range(TC):
    n = int(input())
    number_ls = [2, 3, 5, 7, 11]
    cnt_ls = [0, 0, 0, 0, 0]
    while n != 0:
        for i in range(len(number_ls)):
            if n % number_ls[i] == 0:
                cnt_ls[i] += 1
                n = n / number_ls[i]
                break
            else:
                continue

    print(cnt_ls)
