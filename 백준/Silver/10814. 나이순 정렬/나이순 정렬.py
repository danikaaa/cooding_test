n = int(input())
arr = []
for _ in range(n):
    age, name = map(str,input().split())
    arr.append([age, name])

arr.sort(key=lambda a:int(a[0])) #age 우선순위 정렬

for i in range(n):
    print(arr[i][0], arr[i][1])