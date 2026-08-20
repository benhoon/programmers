def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i in range(citations[0],0,-1):
        count = 0
        for _ in citations:
            if (_ >= i+1):
                count+=1
        if(count >= i+1) and (answer <= i+1):
            answer = i+1
    return answer
            
    