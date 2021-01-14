def solution(n, lost, reserve):
    answer =len(reserve)
    n-=len(set(lost+reserve))
    answer+=n
    
    for l in lost[:]:
        for r in reserve:
            if l==r:
                reserve.remove(r)
                lost.remove(l)
    for l in lost[:]:
        if l-1 in reserve:
            answer+=1
            reserve.remove(l-1)
            lost.remove(l)
        elif l+1 in reserve:
            answer+=1
            reserve.remove(l+1)
            lost.remove(l)
    
    return answer