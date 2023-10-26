import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
rescore =[]
for i in score:
    rescore.append(i/max(score)*100)


print(round(sum(rescore)/n, 2))