TC = int(input())
for tc in range(TC):
    P, A, B = map(int, input().split())
    PA = P
    PB = P
    IA = 1
    IB = 1
    CA = int((IA + PA) / 2)
    CB = int((IB + PB) / 2)
    number_a = 0
    number_b = 0
    while True:
        if CA < A:
            IA = CA
            CA = int((IA + PA) / 2)
            number_a += 1
        elif CA > A:
            PA = CA
            CA = int((IA + PA) / 2)
            number_a += 1
        elif CA == A:
            break
    while True:
        if CB < B:
            IB = CB
            CB = int((IB + PB) / 2)
            number_b += 1
        elif CB > B:
            PB = CB
            CB = int((IB + PB) / 2)
            number_b += 1
        elif CB == B:
            break
    if number_a < number_b:
        print('#{} {}'.format(tc + 1, 'A'))
    elif number_a > number_b:
        print('#{} {}'.format(tc + 1, 'B'))
    elif number_a == number_b:
        print('#{} {}'.format(tc + 1, '0'))