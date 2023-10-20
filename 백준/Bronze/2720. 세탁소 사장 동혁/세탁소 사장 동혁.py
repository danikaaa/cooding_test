T = int(input())
c_types = [25, 10, 5, 1]

for _ in range(T):
    c = int(input())

    for i in c_types:
        print(c//i, end=' ')
        c = c%i
