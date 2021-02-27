def solution(citations):
    answer = 0
    max_list=[]
    check=0

    if max(citations) == 0: # 만약 발표한 논문의 인용된 논문 수의 최대치가 0 일시 0을 반환
        return 0

    for count in citations:   # 만약 발표한 논문의 갯수 보다 발표한 모든 논문의 인용 수가 높을 경우 논문 수 만큼 반환
        if count > len(citations):
            check+=1
        
        if check == len(citations):
            return check


    for i in range(min(citations),max(citations)+1): # H-Index
        count=0
        for j in range(0,len(citations)):
            if i <= citations[j]:
                count+=1

            if i == count:
                max_list.append(i)
            
    answer=max(max_list)

    return answer


print(solution([0,0,0]))