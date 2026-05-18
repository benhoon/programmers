def solution(s, n): #a 97 z 122 A 65 Z 90
    answer = ""
    for c in s:
        if(c == " "):
            answer += c
            continue
        else:
            if(c.isupper()):
                answer += chr((ord(c)+n-65)%26 + 65)
            else:
                answer += chr((ord(c)+n-97)%26 + 97)
    return answer