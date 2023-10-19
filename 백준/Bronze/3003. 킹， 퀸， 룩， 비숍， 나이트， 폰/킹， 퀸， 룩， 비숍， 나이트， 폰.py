n = list(map(int, input().split()))
dn = [1, 1, 2, 2, 2, 8]

for i in range(len(n)):
    print(dn[i]-n[i], end=' ')