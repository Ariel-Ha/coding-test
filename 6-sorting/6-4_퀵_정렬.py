array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start >= end: #퀵 정렬을 적용하는 리스트의 원소가 하나일 경우 퀵 정렬 종료
        return
    pivot = start #피벗(정렬 기준)은 첫 번째 원소
    left = start+1 #피벗 바로 오른쪽 원소는 left 원소 ex) 7
    right = end #제일 마지막 원소(제일 오른쪽 원소)가 right 원소 ex) 8
    while left <= right: #작은 데이터와 큰 데이터를 스와프하는 조건/엇갈리지 않을 때
        #피벗보다 큰 데이터를 찾을 때까지 무한 반복, 조건문 불만족 시 while 문 실행 안하고 반복 종료
        while left <= end and array[left] <= array[pivot]:
            left += 1 #큰 데이터 아니면 오른쪽으로 이동, 왼쪽에서 피벗보다 큰 데이터를 찾아야 한다.
        #피벗보다 작은 데이터를 찾을 때까지 무한 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1 #작은 데이터 아니면 왼쪽으로 이동, 오른쪽에서 피벗보다 작은 데이터를 찾아야 한다.
        #피벗기준 큰 데이터(left))와 작은 데이터(right)가 확정된 후, 둘이 엇갈렸다면, 피벗과 작은 데이터를 교체한다.
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        #피벗기준 큰 데이터(left)와 작은 데이터(right)가 확정된 후, 둘이 엇갈리지 않고 왼쪽과 오른쪽에 잘 위치했다면, 두 데이터를 교체한다.
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
                
        
