def solution(s):
 
    
    arr=list(s)
    check=[]
    for i in range(len(arr)):
        if arr[i] == '(':
            check.append(i)
        elif arr[i] == ')':
            if len(check) == 0:
                return False
            else:
                check.pop()
    if len(check) == 0:
        return True
    else:
        return False
    return False

print(solution('()())'))