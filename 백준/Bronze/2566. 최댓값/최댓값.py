arr = [list(map(int, input().split())) for _ in range(9)]
max_num, max_row, max_col = 0, 0, 0

for i in range(9):
    for j in range(9):
        if max_num <= arr[i][j]: # 가장 큰 값 찾아서 이전 max_num 값이랑 비교
            max_num = arr[i][j]
            max_row = i+1
            max_col = j+1
print(max_num)
print(max_row, max_col)