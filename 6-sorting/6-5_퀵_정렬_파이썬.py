array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    #리스트가 하나의 원소만 담고 있다면 함수 종료
    if len(array) <= 1:
        return array

    pivot = array[0] #피벗은 첫 번째 원소
    tail = array[1:] #첫 번째 원소를 제외한 원소들의 리스트

    left_side = [x for x in tail if x <= pivot] #피벗보다 작은 원소들, 피벗 기준 정렬 시 왼쪽
    right_side = [x for x in tail if x > pivot] #피벗보다 큰 원소들, 피벗 기준 정렬 시 오른쪽

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트로 병합 후 반환한다.
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array)) #함수 실행 결과 출력

'''
key point
- [pivot] 리스트로 감싸줘야 리스트로 연결, 병합 가능
'''