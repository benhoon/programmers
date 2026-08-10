def remain(progresses,speeds):
    remain = []
    for i in range(len(speeds)):
        if((100 - progresses[i]) % speeds[i]):
            remain.append((100 - progresses[i]) // speeds[i] +1)
        else:
            remain.append((100 - progresses[i]) // speeds[i])
    return remain
    
def solution(progresses, speeds):
    answer = []
    n=0
    r = remain(progresses,speeds)
    while(n < len(speeds)):
        count = 0
        for i in range(n,len(speeds)):
            if(r[n] >= r[i]):
                count += 1
            else: break
        n += count
        answer.append(count)
    return answer