from email.policy import default


N, M = map(int, input().split())

nnum = []
nnum_min = []

for n in range(1,N+1):
    for m in range(0, M):
        nnum.append(input().split())
        nnum_min.append(min(nnum[m], default=0))
        m += 1
        n += 1

    # if n==N:
    #     break
    
print(nnum)
print(nnum_min)
print(max(int(nnum_min)))

'''
point
- min()함수에 리스트 여러 개를 넣으면 최소값이 속한 리스트 속 리스트를 반환
- 행, 열 개수를 N, M 주어진 값에 맞게 if문으로 제약조건을 넣는 것까지 처음부터 생각하려니 어려움
- append 함수는 [[리스트], [리스트]] 형태로 병합. extend()함수는 차원을 변경하지 않고 요소들끼리 병합
'''

    