import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=False)

for i in array:
    print(i)