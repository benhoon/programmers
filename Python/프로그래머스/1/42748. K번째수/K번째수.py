def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        c_array = []
        for a in range(len(array)):
            if a+1 >= i and a+1 <= j:
                c_array.append(array[a])
        c_array.sort()
        answer.append(c_array[command[2]-1])
    return answer