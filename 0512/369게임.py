# 369

for i in range(1, 101):
    no = 0
    if i % 10 == 3:
        print('짝', end='')
    elif i % 10 == 6:
        print('짝', end='')
    elif i % 10 == 9:
        print('짝', end='')
    else:
        no += 1

    if i // 10 == 3:
        print('짝', end='')
    elif i // 10 == 6:
        print('짝', end='')
    elif i // 10 == 9:
        print('짝', end='')
    else:
        no += 1

    if no == 2:
        print(i)
    else:
        print()
