import bisect

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()
for i in m_list:
    l = bisect.bisect_left(n_list, i)
    r = bisect.bisect_right(n_list, i)
    print(r-l, end=' ')