# #민석이는 불면증에 걸렸다. 그래서 잠이 안 올 때의 민간요법 중 하나인 양 세기를 하려고 한다.

# 민석이는 1번 양부터 순서대로 세는 것이 재미없을 것 같아서 N의 배수 번호인 양을 세기로 하였다.

# 즉, 첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다.

# 이렇게 숫자를 세던 민석이에게 잠은 더 오지 않고 다음과 같은 궁금증이 생겼다.

# 이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?

# 예를 들어 N = 1295이라고 하자.

# 첫 번째로 N = 1295번 양을 센다. 현재 본 숫자는 1, 2, 5, 9이다.

# 두 번째로 2N = 2590번 양을 센다. 현재 본 숫자는 0, 2, 5, 9이다.

# 현재까지 본 숫자는 0, 1, 2, 5, 9이다.

# 세 번째로 3N = 3885번 양을 센다. 현재 본 숫자는 3, 5, 8이다.

# 현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.

# 네 번째로 4N = 5180번 양을 센다. 현재 본 숫자는 0, 1, 5, 8이다.

# 현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.

# 다섯 번째로 5N = 6475번 양을 센다. 현재 본 숫자는 4, 5, 6, 7이다.

# 현재까지 본 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9이다.

# 5N번 양을 세면 0에서 9까지 모든 숫자를 보게 되므로 민석이는 양 세기를 멈춘다.


    

#                 check[i] = 1                            
#         if sum(check) == 10:                           
#             result = n_numbers 
#             break
                    
            

#     print(f'#{tc+1} {result}')


    
# warehouse = [str(i) for i in range(0,10)]

T = int(input())
for tc in range(T):
    numbers = input()
    numbers = numbers.split()
    numbers = list(map(int,numbers))         # 띄어쓰기 기준으로 앞, 뒤로 자름 그 후 리스트에 담음   

    n_numbers = []
    cnt = 0
    result = 0
    check = [0 for _ in range(10)]

    while True:
        for number in numbers:              # ex) numbers = [1295]
            cnt += 1
            n_numbers = cnt * number        # ex) n_numbers = 1295 * 1 = 1295        
            for i in map(int, str(n_numbers)):# ex) i = 1, 2, 9, 5 // check[1] = 1 , check[2] = 1...
                check[i] = 1
        if sum(check) == 10:                 # ex) check의 모든 리스트가 1이면 sum()이 10이므로, 종료.
            result = n_numbers
            break

    print(f'#{tc+1} {result}')




  
  
   
