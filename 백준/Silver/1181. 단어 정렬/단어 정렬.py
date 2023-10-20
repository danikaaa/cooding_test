n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

set_arr = set(arr) #중복값제거
arr = list(set_arr) # set 사용해서 list로 변경
arr.sort()
arr.sort(key=len) #문자의 길이순으로 정렬


for i in arr:
    print(i)