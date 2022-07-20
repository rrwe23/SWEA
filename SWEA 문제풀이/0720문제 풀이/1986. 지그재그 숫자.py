#1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.


k = int(input())
for i in range(1,k+1):
    a = int(input())
    result = 0

    for i in range(1,a+1):
        if i % 2 == 0:
            result -= i
        else:
            result += i
    print("#%d" %i,result)






