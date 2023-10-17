def solution(s):
    answer = True
    
    n = 0
    for i in s:
        
        if i == '(':
            n += 1
        elif i == ')':
            n -= 1
        
        if n == -1:
            answer = False
            
    if n > 0:
        answer = False
    
    return answer
 