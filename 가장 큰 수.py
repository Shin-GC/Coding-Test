def solution(num):
    num = list(map(str, num)) #num 배열의 int 값을 map을 사용하여 str 형으로 변환
    #숫자의 앞자리 만을 구분하기 위해 문자열로 바꾸기
    #!문자열 비교는 ASCII 값으로 치환되어 정렬되므로 num의 첫번째 인덱스 값으로 비교한다.!
    #즉 6,10,2 일때 6=86, 1=81 , 2= 82 이므로 10 2 6 순서가 된다.
    #순서가 큰 순서로 합쳐야 하므로 reverse = True 값 [ 내림차 순 ] 을 주어 순서를 바꿔준다.
    print(num)
    num.sort(key = lambda x : x*3, reverse = True) # num의 값은 1000이하이므로 x를 3번 반복하여 세자릿 수 로 맞추어 비교
    # x*3을 안할 경우 9와 998을 비교할때 998이 앞으로 오는 경우를 막기 위해 9 또한 3번 반복시켜주어 999로 만든 후 998과 비교
    print(num)
    return str(int(''.join(num))) #list로 나눈 num을 join을 통해 하나의 int형으로 바꿔준 후 문자열로 변환
    #int 형 변환을 해주는 이유 : num이 0,0,0일때 처리하기 위해 int로 바꿔준다.
