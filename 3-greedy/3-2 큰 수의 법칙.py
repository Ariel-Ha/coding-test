import random

random.seed(1)

N = random.randrange(2, 1000)
M = random.randrange(1, 10000)

if M == 10000:
    K = random.randrange(1, 10000)
else:   
    K = random.randrange(1, M+1)

print(N, M, K)

data = random.sample(range(1,10001), N)
# data = [element.replace(',', ' ') for element in data]
# print(data)

for i in data:
    num = str(data).replace(',', ' ')
    num_list = num[1:-1]
print(num_list)


# 큰 수의 법칙
data.sort(reverse = True)

num1 = data[0]
num2 = data[1]

result = num1*K + num2 + num1*K