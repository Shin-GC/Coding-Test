import collections #collections의 Counter를 사용하여 Dictionary로 바꾸기
def solution(participant, completion):
    answer=0
    participant.sort() # 오름차순 정렬
    completion.sort() # 오름차순 정렬

    answer=collections.Counter(participant)-collections.Counter(completion)
    answer=list(answer)[0]
    return answer
participant=["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]

print(solution(participant,completion))

