def solution(sizes):
    for i in range(len(sizes)):
        if (sizes[i][0] < sizes[i][1]):
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    low = sizes[0][0]
    col = sizes[0][1]
    for c in sizes:
        if (low < c[0]):
            low = c[0]
        if (col < c[1]):
            col = c[1]
    return low*col
        
        