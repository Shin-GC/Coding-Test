def solution(s):
    answer = True
    s=s.lower()
    count_p=s.count('p')
    count_y=s.count('y')
    
    if count_p == count_y or (count_p==0 and count_y==0):
        answer=True
    else:
        answer=False
        
    return answer