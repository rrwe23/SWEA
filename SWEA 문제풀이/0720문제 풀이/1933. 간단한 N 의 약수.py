# 입력으로 1개의 정수 N 이 주어진다.

# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
 

# [제약사항]

# N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)

# N = int(input())                              # list 사용 풀이

# 1 <= N <= 1000                
# result = []

# for i in range(1,N+1):
#     if N % i == 0:
#         result.append(i)

# print(result)


n = int(input())

for i in range(1,n+1):
    if n % i == 0:
        print(i,end=' ')


