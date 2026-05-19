def solution(a):
    answer = len(a)
    left = a[0]
    right = [a[-1] for _ in range(len(a)-1)]
    for i in range(len(a)-2, 1, -1):
        right[i-1] = right[i]
        if(right[i] > a[i]):
            right[i-1] = a[i]
        
        
    for i in range(1,len(a)-1):
        if(left > a[i]):
            left = a[i]
        
        if(left < a[i] and right[i] < a[i]):
            answer -= 1
    return answer