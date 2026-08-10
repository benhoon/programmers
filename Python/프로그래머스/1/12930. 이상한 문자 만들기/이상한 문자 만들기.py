def solution(s):
    answer = ""
    s = s.split(" ")
    for j in range(len(s)):
        res = ""
        for i in range(len(s[j])):
            if ((i+1)%2 != 0):
                res += s[j][i].upper()
            else:
                res += s[j][i].lower()
        s[j] = res
    answer += s[0]
    for k in range(1,len(s)):
        answer += " " + s[k]
    return answer