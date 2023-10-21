import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = []
count = 0
for _ in range(n):
    array.append(input())

for _ in range(m):
    if input() in array:
        count += 1

print(count)