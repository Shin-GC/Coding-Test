import collections
import copy
def solution(progresses, speeds):
    answer = collections.deque()
    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds) #효율성을 위해 list 대신 deque 사용
    
    count=0
    check=0
    
    while len(progresses)!=0:
        if count<=len(progresses)-1: #모든 작업은 동시에 하므로 모든 작업을 진행
            progresses[count]+=speeds[count]
            count+=1
        if count == len(progresses):
            if progresses[0]>=100:  #첫번째 작업이 100이 넘는지 확인
                for progresse in copy.deepcopy(progresses):  #deque를 사용할때 내용이 변경되면 오류발생 [copy.deepcopy를 사용하여 해결]
                    #에러내용 [RuntimeError: deque mutated during iteration ]
                    if progresse>=100:
                        check+=1  #완료된 작업의 수
                        progresses.popleft()  # 작업이 완료되면 deque에서 삭제
                        speeds.popleft()
                    else:
                        break  #가장 앞의 작업이 모두 진행되지 않았다면 앞으로 돌아가 작업 재게
                answer.append(check) #완료된 작업의 수 넣기
            else:
                check=0 #완료된 작업 수 초기화
                count=0
            check=0 #완료된 작업 수 초기화
            count=0

    answer=list(answer)
    return answer
#앞에 있는 작업이 배포되기 전에는 뒤에는 배포 금지 
#모두 함께 작업이 진행되나, 배포는 앞에가 될때 같이 된다. 
#가장 첫번째 작업이 완료 될때 까지는 계속 반복이 진행되어야 한다.
#answer에는 배포 했을때 총 갯수가 append 된다.


print(solution([93, 30, 55, 60, 40, 65],[1, 30, 5 , 10, 60, 7]))