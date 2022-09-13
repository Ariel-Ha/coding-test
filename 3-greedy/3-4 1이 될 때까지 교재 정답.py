## sol1) 일일이 1을 빼는 방법 ##

n, k = map(int, input().split())
result = 0

# N이 K이상이라면 K로 계속 나누기
while n>=k:
    #N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n%k != 0:
        n -= 1
        result += 1
    #K로 나누기
    n//=k
    result += 1

#마지막으로 남은 수에 대하여 1씩 빼기
while n>1:
    n -= 1
    result += 1

print(result)


## sol2) N이 K의 배수가 되도록 ##

n, k = map(int, input().split())
result = 0

while True: # 무한반복
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k) * k # n을 k로 나누었을 때, "몫" 정보만 가져와서 k와 곱해주면 n을 k로 나눌 수 있는 최대 정수가 나온다. (ex: 25 3 -> target은 8*3 = 24)
    result += (n - target) # result = result(0) + n(25)-target(24) =1 -->result(1)
    n = target # n(25)를 target(24)로 업데이트 --> n(24)

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출/ex) n=1, k=3 -> 정수 몫 존재X
    if n<k: #n을 k로 나누기 반복 2회차 결과 n(2)<k(3)이 되었으므로 반복문 탈출 후 가장 밑단의 들여쓰기 미시행 부분을 수행하게 된다.
        break
    
    # K로 나누기
    result += 1 # 아까 1씩 빼줘야 할 횟수 1이 저장된 result에 1회를 더해준다. 한 번 나누었기 때문에 더해준 것! result(2)
    n //= k # n 은 n(24)을 k(3)로 나눈 몫인 8로 다시 업데이트 so n(8)

    # (반복 2회차)
    # target = (n//k) * k --> target = n(8) 나누기 k(3)의 몫인 2 --> target(2*3 = 6) 
    # result += (n - target) --> result = result +(n(8) - target(6)) = 2+2 = 4
    # n = target --> n(4)
    # K로 나누기
    # result += 1 --> result = result(4)+1 = 5
    # n //= k --> n = n//k ==> 6/3 = 2 -->n(2)
    # ---> n(2)<k(3)이므로 반복문을 탈출하고 아래 명령문을 실행한다.


# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1) #result = result(5) + (2-1)
print(result)

'''
# point 
- result += (n - target) 과정이 아직 정확히 이해되지 않음
'''