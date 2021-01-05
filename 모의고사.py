def solution(answer):
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    true_answer=[]

    dic={1:0,2:0,3:0}
    
    for i in range(len(answer)):
        if one[i%5]==answer[i]:
            dic[1]+=1
        if two[i%8]==answer[i]:
            dic[2]+=1
        if three[i%10]==answer[i]:
            dic[3]+=1
    for i in range(1,4):
        if dic[i]==max(dic.values()):
            true_answer.append(i)

    return true_answer

answer=[1,3,2,4,2]
print(solution(answer))