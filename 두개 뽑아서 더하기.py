"""
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의
 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 
 return 하도록 solution 함수를 완성해주세요.
"""
def solution(numbers):
    answer = numbers
    answer.sort()
    true_answer=[]
    for i in range(len(answer)):
        for j in range(len(answer)):
            if i==j:
                continue
            else:
                true_answer.append(answer[i]+answer[j])
    true_answer=set(true_answer)
    answer=list(true_answer)
    answer.sort()
    return answer
numbers=[5,0,2,7]
print(solution(numbers))