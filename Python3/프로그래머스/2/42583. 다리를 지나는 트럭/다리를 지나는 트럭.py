def solution(bridge_length, weight, truck_weights):
    bridge = []
    bw = 0
    answer = 0
    while True:
        if truck_weights and (bw + truck_weights[0] <= weight):
            truck = truck_weights.pop(0)
            bridge.append([truck,0])
            bw += truck
        for t in bridge:
            t[1] += 1
        if (bridge[0][1]==bridge_length):
            bw -= bridge[0][0]
            bridge.pop(0)
        answer += 1
        if not truck_weights and not bridge:
            break
    return answer+1
                
        