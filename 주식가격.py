import collections
def solution(prices):
    answer = collections.deque([])
    prices=collections.deque(prices)
    while len(prices)!=1:
        time=1
        check=prices.popleft()
        count=0
        for price in prices:   
            if check <=price:
                if time >= len(prices):
                    break
                time+=1
                count+=1
            elif count ==0:
                break
            else:
                break
        answer.append(time)
    answer.append(0)
    answer=list(answer)
    return answer


print(solution([1, 2, 3, 2, 3, 1]))