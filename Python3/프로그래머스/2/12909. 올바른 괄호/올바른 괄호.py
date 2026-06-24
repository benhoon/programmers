def solution(s):
    stack = 0
    for _ in s:
        if(stack < 0):
            return False
        elif(_ == '('):
            stack += 1
        elif(_ == ')'):
            stack -= 1
    if (stack != 0):
        return False
    else:
        return True