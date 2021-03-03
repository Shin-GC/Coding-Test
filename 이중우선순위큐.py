import heapq

def solution(operations):
    answer = []
    save=[]
    heapq.heapify(answer)
    while len(operations) != 0:
        
        if operations[0][0] == 'I':
            num = int(operations[0][1:].strip())
            heapq.heappush(answer,num)
            del operations[0]
        
        elif operations[0][0] == 'D':
            if len(answer) == 0 :
                del operations[0]
                pass
            else:
                if operations[0][1:].strip() == '1':
                    max=heapq.nlargest(1,answer)
                    answer.remove(max[0])
                    del operations[0]
                elif operations[0][1:].strip() == '-1':
                    heapq.heappop(answer)
                    del operations[0]
    if len(answer) == 0:
        save = [0,0]
    
    else:
        save.append(heapq.nlargest(1,answer)[0])
        save.append(answer[0]) 

    return save

print(solution(["I 2","I 4","D -1", "I 1", "D 1"]))