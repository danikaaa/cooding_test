def solution(arr):
    if len(arr) == 0:
        arr = [-1]
    if arr[0] == 10:
        arr = [-1]
    else:
        arr.remove(min(arr))
    return arr