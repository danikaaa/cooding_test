import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n):
    name, action = map(str, input().split())
    if action == "enter":
        dic[name] = True
    else:
        del dic[name]

dic = sorted(dic, reverse=True)
for i in dic:
    print(i)
