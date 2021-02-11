def solution(s):
    answer = True
    if s.isdigit()==True:
        if len(s)==4 or len(s)==6:
            answer=True
        else:
            answer=False
    else:
        answer=False
  
    return answer

print(solution('123456'))