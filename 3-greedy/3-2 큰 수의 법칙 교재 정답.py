n, m, k = map(int, input().split()) 
# N, M, K를 공백으로 구분하여 입력받기/map(적용할 함수, 적용할 data)/data는 input으로 입력받음

data = list(map(int, input().split()))
#N개의 수를 공백으로 구분하여 입력받기

data.sort()
num1 = data[n-1]
num2 = data[n-2]

result = 0

while True:
    for i in range(k):
        if m==0:
            break
        result += num1
        m -= 1
    if m==0:
        break
    result += num2
    m -= 1

print(result)