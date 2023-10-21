import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    data = input()
    stack = []
    result = "YES"

    for i in data:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if stack:
                stack.pop()
            else:
                result = "NO"
                break

    if stack:
        print("NO")
    else:
        print(result)
