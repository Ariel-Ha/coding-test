array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #i부터 끝까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]: #j번째 원소보다 한 칸 왼쪽 원소인 j-1번째 원소가 더 크다면
            array[j], array[j-1] = array[j-1], array[j] #자리를 바꾼다. 오름차순이 되도록

        else: #왼쪽 원소가 자신보다 작다면 멈춤 -> 이미 정렬이 된 상태이므로
            break

print(array)
