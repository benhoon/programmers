def solution(x):
    answer = False
    x = str(x)
    sum = 0
    
    for n in x:
        sum += int(n)
    if(int(x) % sum == 0):
        answer = True
    
    return answer