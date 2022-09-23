N = int(input())
case = 0

for h in range(1, N+1):
    for m in range(60):
        for s in range(60):
            if '3' in  str(h) + str(m) + str(s):
                case += 1

print(case)

'''
point
- 시, 분, 초 정보를 문자열로 바꾸고 일렬로 합쳐주어 하나의 문자열로, 그리고 그 내에서 3이 등장하는 개수를 세면, 시분초에 따라 나누어 생각할 필요가 없다.
- in 기능 기억하기
'''