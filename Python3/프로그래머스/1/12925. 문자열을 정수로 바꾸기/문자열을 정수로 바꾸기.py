def solution(s):
    answer = 0
    n = len(s)
    sign = 1
    for i in s:
        
        if i == '-':
            sign = -1
        elif i == '+':
            sign = 1
        
        else : 
            answer += (ord(i)-ord("0")) * 10**(n-1)
        n -= 1
    return answer * sign
        
         
