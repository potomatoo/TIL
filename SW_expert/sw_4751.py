TC = int(input())
for _ in range(TC):
    words = input()
    w = len(words)
    print('..#.'*w,end='')
    print('.')
    print('.#'*(w*2),end='')
    print('.')
    print('#',end='')
    for i in range(len(words)):
        if i == len(words) - 1:
            print('.{}.#'.format(words[i]))
        else:
            print('.{}.#'.format(words[i]), end='')
    print('.#' * (w * 2), end='')
    print('.')
    print('..#.' * w, end='')
    print('.')



