def base_10to3(n):
    res = ""
    while(n/3 >= 1):
        res = str(n%3) + res
        n = int(n/3)
    res = str(n) + res
    return res

def base_3to10(n):
    res = 0
    for i in range(len(n),0,-1):
        res += (3 ** (int(i)-1)) * int(n[len(n)-i])
    return res

def reverse(n):
    res = ""
    for i in n:
        res = i + res
    return res
    
def solution(n):
    return base_3to10(reverse(base_10to3(n)))
    