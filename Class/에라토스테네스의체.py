number = 100000
num_ls = [0] * 100001
for i in range(2,len(num_ls)):
    num_ls[i] = i
for i in range(2,len(num_ls)):
    if num_ls[i] == 0:
        continue
    for j in range(i+i,len(num_ls),i):
        num_ls[j] = 0
cnt = 0
for i in range(len(num_ls)):
    if num_ls[i] != 0:
        cnt += 1
        print(num_ls[i])
print('100000까지의 수 중에서 소수는 총 {}개 입니다.'.format(cnt))