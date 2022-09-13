from email.policy import default

N, M = map(int, input().split())

nnum = []
nnum_min = []

for n in range(1,N+1):
    for m in range(0, M):
        nnum.append(input().split())
        nnum_min.append(int(min(nnum[m], default=0)))
        m += 1
        n += 1

    # if n==N:
    #     break
    
print(nnum)
print(nnum_min)
print(max(nnum_min))

'''
## point
- min()함수에 리스트 여러 개를 넣으면 최소값이 속한 리스트 속 리스트를 반환
- 행, 열 개수를 N, M 주어진 값에 맞게 if문으로 제약조건을 넣는 것까지 처음부터 생각하려니 어려움->입력과 출력창만 정답이라면 제약 조건 설정 불필요?
- append 함수는 [[리스트], [리스트]] 형태로 병합. extend()함수는 차원을 변경하지 않고 요소들끼리 병합
- N=2/M=4 입력 시, nnum[m]은 nnum 리스트의 0에서 3까지 돌게 된다. 그러나 2개 행만 입력했기 때문에 min()함수에 빈 리스트가 입력되어 out of range오류가 발생한다. 따라서, min 함수에 default 값을 주어 빈 리스트가 들어올 시 0을 반환하도록 설정하여 오류를 해결했다.

## error reff.
The Python "TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'" occurs when we pass a list to the int() class. To solve the error, access a specific item in the list and pass the item to the int() class, e.g. int(my_list[0]).
'''

    