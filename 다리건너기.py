def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length #다리 길이 만큼 생성
    
    while len(bridge) != 0:
        time += 1 #시간 증가
        bridge.pop(0) 
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight: #현재 다리를 건너는 차와 뒤차 무게와 한계중량 비교
                bridge.append(truck_weights.pop(0)) # 합이 한계중량 보다 낮을 시 같이 건너기
            else:
                bridge.append(0) 
        
    return time

print(solution(bridge_length=3,weight=10,truck_weights=[4,5,6,7,8,9]))