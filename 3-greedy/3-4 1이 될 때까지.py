N, K = map(int, input().split())

count = 0

while N>1:
    if N%K==0:
        N = N//K
        count += 1

    else: 
        N -= 1 
        count += 1


print(count)

'''
point
- ctrl +f2 = 동일한 글자 동시에 변경하기
'''