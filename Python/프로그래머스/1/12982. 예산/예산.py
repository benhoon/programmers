def solution(d, budget):
    answer = 0
    d.sort()
    chk = 0
    for i in d:
        if(chk + i <= budget):
            chk += i
            answer+=1
        else:
            break
    
    return answer