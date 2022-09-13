## min 함수만 사용 ##

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
for i in range(n): #행의 범위만큼 반복
    data = list(map(int, input().split())) #공백으로 구분한 입력을 리스트로 받기
    min_value = min(data) #현재 줄 즉, 행에서 '가장 작은 수'찾기
    result = max(result, min_value) #0과 min_value 중 큰 수 찾아서 result에 다시 저장
    #n번 행들을 돌면서 각 행에서 가장 작은 수를 min_value에 저장 후/행 별 작은 수 끼리 비교해 큰 수를 result에 저장&업데이트

print(result)


## 2중 반복문 구조 ##
n, m = map(int, input().split())

result = 0 
for i in range(n):
    data = list(map(int, input().split()))

    #현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

'''
point!
- min, max 함수에 인자 두 개 이상 전달 시, 비교하는 것
- 입력받은 수를 굳이 행 별로 나누어 저장할 필요X, 하나의 리스트에 요소를 저장하고, 반복 범위를 행으로 주기
'''