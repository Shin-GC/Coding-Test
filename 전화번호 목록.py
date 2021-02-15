def solution(phone_book):
    new_phone_book=sorted(phone_book)
    for i in range(0,len(new_phone_book)):

        if len(new_phone_book) == 1:
            break
        #startswith는 tuple 타입과 str 타입만 지원하기 때문에 join을 이용하여 str로 변환
        if ''.join(new_phone_book[1:2]).startswith(new_phone_book[0]): #startswith를 이용하여 시작문자 비교
            return False
        
        else:
            pass
        del new_phone_book[0] 
    return True

print(solution(['119', '97674223','1195524421']))
