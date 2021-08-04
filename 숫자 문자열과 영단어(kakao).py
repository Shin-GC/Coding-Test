'''
네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.
'''

def solution(s):
    save_dict = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9,
    }
    save_answer = []
    save_alph = ""
    for word in s:
        if word.isdigit():
            word = int(word)
            save_answer.append(word) #숫자일 경우 바로 정답 리스트에 저장
        
        else: # 만약 영단어 일 경우 영어 단어의 한글자씩 받아 낸 후, 다음이 숫자인 경우 저장해놓은 값들을 dict와 비교하여 값을 넣어주기
              # 문제점 : 영단어가 두개 이상이 이어져서 나올 경우엔? = 반복할때마다 리스트 값을 방출하여 해당하는 값이 존재하는지 확인하기
            save_alph += word
            
            if save_alph in save_dict:
                save_answer.append(save_dict[save_alph])
                save_alph = ""
            else:
                continue
    save_answer = "".join(map(str, save_answer))        
    answer = int(save_answer)
    return answer

print(solution("one4seveneight"))
