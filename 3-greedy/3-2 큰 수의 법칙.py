# import random

# random.seed(1)

# N = random.randrange(2, 1000)
# M = random.randrange(1, 10000)

# if M == 10000:
#     K = random.randrange(1, 10000)
# else:   
#     K = random.randrange(1, M+1)

# print(N, M, K)

# data = random.sample(range(1,10001), N)
# # data = [element.replace(',', ' ') for element in data]
# # print(data)

# for i in data:
#     num = str(data).replace(',', ' ')
#     num_list = num[1:-1]
# print(num_list)


# # 큰 수의 법칙
# data.sort(reverse = True)

# num1 = data[0]
# num2 = data[1]

# count = M//(K+1)
# remain = M % (K+1)
# result = num1*count + num2*count + remain*num1

# print(result)


'''
정답
- 입출력 방식 
- 접근은 좋았으나 전체 m개중 k+1개 묶음 속 큰 수 개수는 k곱해주기 생각
- 두 번째로 큰 수 개수
'''

n, m, k = map(int, input().split()) 
# N, M, K를 공백으로 구분하여 입력받기/map(적용할 함수, 적용할 data)/data는 input으로 입력받음

data = list(map(int, input().split()))
#N개의 수를 공백으로 구분하여 입력받기

data.sort()
num1 = data[n-1]
num2 = data[n-2]

count = m//(k+1)*k 
## m//(k+1)에 k를 곱해줘야 큰 수가 더해지는 횟수. m//(k+1)은 전체 m개 중 K+1개로 몇 번 묶이는지, 묶음 속에 큰 수가 k개 존재하므로...
remain = m % (k+1)
result = num1*count + num2*(m-count) + remain*num1
## 두 번째로 큰 수는 m-count번

print(result)