
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