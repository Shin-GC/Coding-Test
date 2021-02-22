import collections
def solution(priorities, location):
    answer = 0

    priorities=collections.deque(priorities)
    d_pri = collections.deque([ (j,i) for i,j in enumerate(priorities)]) # (중요도, 인덱스)
    while len(d_pri):
        save=d_pri.popleft()
        
        if d_pri and max(d_pri)[0] > save[0]: #d_pri 가 비었을때 max(d_pri를 하게 될 경우 max() arg is an empty sequence 오류를 막기 위해 d_pri and 사용)
            d_pri.append(save)
        else:
            answer+=1
            if save[1] == location:
                break
    
    return answer

print(solution([3,3,4,2],3))