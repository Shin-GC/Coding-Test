import heapq

def solution(scoville, K):
    count = 0
    check = 0
    
    heapq.heapify(scoville)
   
    while len(scoville) != 0:
        
        for i in scoville:
            if i < K:
                break

            if len(scoville) == 1:
                if scoville[0] > K:
                    return count
                else:
                    return -1

            else:
                return count
        if len(scoville) == 1:
            if scoville[0] > K:
                return count
            else:
                return -1
                
        first = heapq.heappop(scoville)
       
        two = heapq.heappop(scoville)

        heapq.heappush(scoville,first + (two*2))
        count+=1

    """
    while len(scoville) !=0:

        first = min(scoville)
        scoville.remove(min(scoville))        

        if len(scoville) == 0:
            return -1

        two = min(scoville)*2
        scoville.remove(min(scoville))

        scoville.append(first+two)

        for i in scoville:
            if i >= K:
                check+=1
            else:
                break
        if check == len(scoville):
            return count
        count+=1
    """
    return check


print(solution([1,2,3],11))