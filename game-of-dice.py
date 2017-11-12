print('Game of dice')
print()
np = input('enter your name: ')
import random
o = 'y'
while (o == 'y')or(o == 'yes'):
    print()
    print(np, ', how many times will we throw a bone?', sep='')
    k = int(input())
    res = [[],[]]
    i = 0
    while (i < k):
        print()
        print('throw №', i+1, sep='', end='')
        input()
        res[0].append(random.randint(1,6))
        print(' you have -', res[0][i], end='')
        input()
        res[1].append(random.randint(1,6))
        print(' computer dropped out -', res[1][i])
        i += 1

    input()
    res[0].append(0)
    res[1].append(0)
    print('Results of the game:')
    print('{:<10}'.format(''), end='')
    print('{:^15}'.format(np), end='')
    print('{:^15}'.format('computer'))
    for j in range(0, k):
        print('{:<3}'.format(j+1), '{:<7}'.format('throw'), sep='', end='')
        for i in range(0, 2):
            print('{:^15}'.format(res[i][j]), end='')
            res[i][k] += res[i][j]
        print()
    print('{:<10}'.format('total'), end='')
    print('{:^15}'.format(res[0][k]), end='')
    print('{:^15}'.format(res[1][k]))
    if (res[0][k]) > (res[1][k]):
        print('     ', np, 'won!')
    elif (res[0][k]) < (res[1][k]):
        print('      computer win')
    elif (res[0][k]) == (res[1][k]):
        print('      draw!')

    input()
    o = input('start the game again? (y/n) ' )