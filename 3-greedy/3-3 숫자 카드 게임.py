from random import randrange


N, M = map(int, input().split())

inum = []
inum_min = []

for n in range(1,N):

    for i in range(1,M):
        inum.append(input().split())
        inum_min.append(min(inum))
        i += 1

    if len(inum)==M:
        n += 1
    

print(inum_min)



    