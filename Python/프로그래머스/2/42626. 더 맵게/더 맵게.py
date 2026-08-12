import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while (len(scoville) > 1):
        if(scoville[0] < K):
            s_1 = heapq.heappop(scoville)
            s_2 = heapq.heappop(scoville)
            s = s_1 + s_2*2
            heapq.heappush(scoville, s)
            answer += 1
        else:
            break
    if(scoville[0] < K):
        answer = -1
    return answer