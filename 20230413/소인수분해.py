T = int(input())

for test_case in range(1, T + 1):
    value = int(input())

    a = value
    b = value
    c = value
    d = value
    e = value

    answer = [0, 0, 0, 0, 0]

    while 1:
        if a % 2 == 0:
            a = a // 2
            answer[0] += 1
        else:
            break

    while 1:
        if b % 3 == 0:
            b = b // 3
            answer[1] += 1
        else:
            break

    while 1:
        if c % 5 == 0:
            c = c // 5
            answer[2] += 1
        else:
            break

    while 1:
        if d % 7 == 0:
            d = d // 7
            answer[3] += 1
        else:
            break

    while 1:
        if e % 11 == 0:
            e = e // 11
            answer[4] += 1
        else:
            break

    print("#", end='')
    print(test_case, end=' ')
    for i in range(0, 5):
        print(answer[i], end=' ')
    print()