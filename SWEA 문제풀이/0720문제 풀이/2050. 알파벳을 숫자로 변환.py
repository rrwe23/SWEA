#알파벳으로 이루어진 문자열을 입력 받아 각 
#알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.



A = list(input())
for i in range(len(A)):
    print(ord(A[i])-64, end=' ')