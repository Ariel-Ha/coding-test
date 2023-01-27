time = {1:4, 3:5, 0:6, 5:7, 3:8, 5:9, 6:10, 8:11, 8:12, 2:13, 12:14}
n = 0

# for i in range(1, len(time)):
#     for j in range(i, 0, -1):
#         if list(time.values())[j-1] <= list(time.keys())[j]:
#             list(time.keys())[j], list(time.values())[j] = list(time.keys())[j-1], list(time.values())[j-1]
#             n += 1
#         else:
#             break
        
# print(n)

## 딕셔너리 특정 키 출력 방법 
# num = list(time.keys())[0]
# print(num)

j = 1
result = []

for i in range(1, len(time)):
    while j < len(time):
        
        old_start = list(time.keys())[i-1]
        old_end = list(time.values())[i-1]
        new_start = list(time.keys())[j]
        new_end = list(time.values())[j]

        if old_end <= new_start :
            new_start, new_end = old_start, old_end
            n += 1
            j += 1

        else:
            j += 1

print(n)