def solution(lottos, win_nums):
    
    answer = [] #최고순위, 최저순위 순으로 등록
    lose_lottos = lottos.copy() # 리스트 복사
    win_count = 0 # 최고 순위 맞는 번호 체크
    lose_count = 0 #최저 순위 번호 체크
    lose = list(range(1,46)) # 로또에서 나올 수 있는 모든 값 을 저장한 list  [ 최저순위 찾기용 ]

    win_point = list(set(win_nums) - set(lottos)) # lotto에 정답이 들어가있지 않은 값들만 남기고 삭제
    lose_point = list(set(lose) - set(win_nums)) # 나올 수 있는 모든 수에 정답이 들어있는 값 삭제
    lose_point = list(set(lose_point) - set(lottos)) # 중복값이 있으면 안된다 했으므로 lottos에 들어간 값도 삭제
    
    for win in win_nums:
        for lotto in lottos:
            if lotto == 0:
                index = lottos.index(lotto) # 값이 0인 곳의 index 찾아오기
                lottos[index] = win_point.pop() # 중복되지 않는 정답인 win_point 값을 0에 넣어주기!

                lose_index = lose_lottos.index(lotto) # 값이 0인 곳의 index 찾아오기
                lose_lottos[lose_index] = lose_point.pop()# 중복되지 않는 오답인 lose_point 값을 0에 넣어주기!

    for nums in win_nums: 
        if nums in lottos:
            win_count+=1     

    for nums in win_nums:
        if nums in lose_lottos:
            lose_count+=1

    if win_count == 6:
        answer.append(1)
    elif win_count == 5:
        answer.append(2)
    elif win_count == 4:
        answer.append(3)
    elif win_count == 3:
        answer.append(4)
    elif win_count == 2:
        answer.append(5)
    else:
        answer.append(6)

    if lose_count == 6:
        answer.append(1)
    elif lose_count == 5:
        answer.append(2)
    elif lose_count == 4:
        answer.append(3)
    elif lose_count == 3:
        answer.append(4)
    elif lose_count == 2:
        answer.append(5)
    else:
        answer.append(6)


    return answer
