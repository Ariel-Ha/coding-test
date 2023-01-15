#N, M을 공백으로 구분하여 입력받기 
n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n): #n개의 행마다 노드 요소 저장
    graph.append(list(map(int, input())))

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드 방문
def dfs(x, y):
    #주어진 범위를 벗어나는 경우 즉시 종료
    #x가 행의 범위, y가 열의 범위를 나타낸다.
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False #종료조건1

    #현재 노드 미방문이라면
    if graph[x][y] == 0: #x행의 y열(y번째 요소)가 0이라면
        graph[x][y] == 1 #1로 변경해주어 다음 탐색 시 중복적으로 개수를 세지 않도록
        #인접한 노드가 0이다. = 상하좌우 요소이므로 연결되어 있다. = 세기 시작했던 노드 기준으로 1번 카운트할 때, 묶음에 포함된다.
        dfs(x+1, y) #상
        dfs(x-1, y) #하
        dfs(x, y-1) #좌
        dfs(x, y+1) #우
        return True
    return False #종료조건2 = 모든 노드의 탐색이 끝났을 때

#모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i, j) == True: #(1.미방문 노드를 방문 처리/2.인접 노드 탐색)을 했다면 result+1 (묶음 중 한 번만 카운트된다.)
            result += 1

print(result)
