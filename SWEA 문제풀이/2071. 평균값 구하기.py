#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# t = int(input())
# count = 0
# for i in range(1, t + 1) :
#     age = list(map(int, input().split()))
#     for i in age:
#         if age != '':
#             count += 1
# print('#%d %s' % (format(sum(age)/count,'.1f')))

T = int(input())
for test_case in range(1, T+1):
    numbers=list(map(int,input().split()))
    avg_value = sum(numbers)/len(numbers)
    avg_value = round(avg_value)
    print("#{} {}".format(test_case,avg_value))



   

