def solution(s):
    answer = ''
    if len(s)%2==0:
        num=(len(s)//2)
        answer=s[num-1:num+1]
    else:
        num=(len(s)//2)
        answer=s[num:num+1]
    return answer