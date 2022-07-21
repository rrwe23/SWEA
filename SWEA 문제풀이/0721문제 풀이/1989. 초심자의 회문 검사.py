# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라

T = int(input())

for t in range(1,T+1):
    A = input()         
    for i in range(len(A)//2):          
        if A[i] == A[-1-i]:      #    A의 첫 리스트와 A의 마지막 리스트를 순서대로 비교
            answer = 1
        else:
            answer = 0

    print('#{} {}'.format(t,answer))











