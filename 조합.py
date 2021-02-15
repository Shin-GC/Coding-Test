#https://programmers.co.kr/learn/courses/30/lessons/42578
import collections
def solution(clothes):
    answer=1
    arr=[]
    for i,j in clothes:
        arr.append(j)
    
    kind=collections.Counter(arr)
    kind_list=list(kind.values())
    
    for i in kind_list:
        answer*=(i+1)
    
    return answer-1


print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))

# 경우의 수 : (옷 +1) * (모자 +1) * (안경+1) * (바지+1) 
# 이때 문제에서 무조건 하나의 옷은 입는다 했으므로
# 아무것도 입지 않은 경우의 수 를 빼줘야 하기 때문에 -1 을 해준다
