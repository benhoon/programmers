def solution(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        curent = queue.pop(0)
        if any(curent[1] < q[1] for q in queue):
            queue.append(curent)
        else:
            answer += 1
            if curent[0] == location:
                return answer
    