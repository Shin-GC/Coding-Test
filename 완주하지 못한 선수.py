import collections
def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    answer_list=collections.Counter(participant)-collections.Counter(completion)
    answer=list(answer_list)[0]
    return answer
participant=["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]

print(solution(participant,completion))

