def solution(n):
    answer = 0
    arr=[]
    quo=None
    rem=None
    while quo!=0:
        rem=n%3  #3으로 나눈 나머지 저장
        quo=n//3 # 3으로 나눈 몫 저장
        arr.append(rem)  #3으로 나눴을때 나머지를 저장
        n=quo  # n값을 quo값으로 변경
       
    arr.reverse()
    count=0
    for i in arr:
        answer=answer+(i*(3**count))
        count+=1

    return answer

print(solution(125))