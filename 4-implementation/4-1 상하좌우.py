
N = int(input())
paths = list(map(str, input().split()))

x_move = 1
y_move = 1

for i in range(0, len(paths)):
    if (0<x_move<5) and (0<y_move<5):
        if paths[i]=='L':
            x_move -= 1
            i+= 1
        if paths[i]=='R':
            x_move += 1
            i+= 1
        if paths[i]=='U':
            y_move -= 1
            i+= 1
        if paths[i]=='D':
            y_move += 1
            i+= 1
        else: pass
    else: i+= 1

print('(',y_move,',',x_move,')')

'''
point
- paths[i]==무언가로 더하기를 한 후에는 한 단계가 진행된 것이므로 각각의 it문 모두에 i+=1로 단계 정보를 업데이트 해야한다.
- else:pass 는 아무것도 하지 않고 넘어가는 것을 뜻한다.
- 이동 명령이 x, y 좌표를 0~5 범위가 넘게 할 경우 아무것도 하지 않지만, 단계는 진행되었기 때문에 else: i+=1 로 단계 정보를 업데이트 해야한다.
'''