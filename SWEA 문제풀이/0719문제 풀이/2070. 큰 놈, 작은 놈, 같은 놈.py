#2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

t = int(input())

for i in range(1, t + 1) :
    a, b = map(int, input().split())
    if a == b :
        print('#%d %s' % (i, '='))
    elif a < b :
        print('#%d %s' % (i, '<'))
    else :
        print('#%d %s' % (i, '>'))

