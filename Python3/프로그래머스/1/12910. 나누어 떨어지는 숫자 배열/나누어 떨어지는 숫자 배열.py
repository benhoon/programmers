def sort(arr):
    l = len(arr)
    if(l == 0):
        arr = [-1]
        return arr
    for i in range(l):
        for j in range(i+1, l):
            if (arr[i] > arr[j]):
                arr[i],arr[j] = arr[j],arr[i]
    return arr
def solution(arr, divisor):
    answer = []
    for i in arr:
        if(i%divisor == 0):
            answer.append(i)
    answer = sort(answer)
    return answer