def solution(strings, n):
    n_words = []
    for string in strings:
        if(string[n] not in n_words):
            n_words.append(string[n])
    l = len(n_words)
    n_words.sort()
    mid_sort = [[]for _ in range(l)]
    for i in range(l):
        for string in strings:
            if(string[n] == n_words[i]):
                mid_sort[i].append(string)
        mid_sort[i].sort()
    answer = []
    for i in mid_sort:
        for j in i:
            answer.append(j)
            
    return answer