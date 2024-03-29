### 📔 문제 설명

오픈채팅방
카카오톡 오픈채팅방에서는 친구가 아닌 사람들과 대화를 할 수 있는데, 본래 닉네임이 아닌 가상의 닉네임을 사용하여 채팅방에 들어갈 수 있다.

신입사원인 김크루는 카카오톡 오픈 채팅방을 개설한 사람을 위해, 다양한 사람들이 들어오고, 나가는 것을 지켜볼 수 있는 관리자창을 만들기로 했다. 채팅방에 누군가 들어오면 다음 메시지가 출력된다.

"[닉네임]님이 들어왔습니다."

채팅방에서 누군가 나가면 다음 메시지가 출력된다.

"[닉네임]님이 나갔습니다."

채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.

채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
채팅방에서 닉네임을 변경한다.
닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.

예를 들어, 채팅방에 "Muzi"와 "Prodo"라는 닉네임을 사용하는 사람이 순서대로 들어오면 채팅방에는 다음과 같이 메시지가 출력된다.

"Muzi님이 들어왔습니다."
"Prodo님이 들어왔습니다."

채팅방에 있던 사람이 나가면 채팅방에는 다음과 같이 메시지가 남는다.

"Muzi님이 들어왔습니다."
"Prodo님이 들어왔습니다."
"Muzi님이 나갔습니다."

Muzi가 나간후 다시 들어올 때, Prodo 라는 닉네임으로 들어올 경우 기존에 채팅방에 남아있던 Muzi도 Prodo로 다음과 같이 변경된다.

"Prodo님이 들어왔습니다."
"Prodo님이 들어왔습니다."
"Prodo님이 나갔습니다."
"Prodo님이 들어왔습니다."

채팅방은 중복 닉네임을 허용하기 때문에, 현재 채팅방에는 Prodo라는 닉네임을 사용하는 사람이 두 명이 있다. 

이제, 채팅방에 두 번째로 들어왔던 Prodo가 Ryan으로 닉네임을 변경하면 채팅방 메시지는 다음과 같이 변경된다.

"Prodo님이 들어왔습니다."
"Ryan님이 들어왔습니다."
"Prodo님이 나갔습니다."
"Prodo님이 들어왔습니다."

채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때, 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.

### 🧰 변수 설명

- **answer**
    - 타입 : 리스트
    - 저장 데이터 : 최종적으로 방을 개설한 사람이 보게 되는 메시지
- id_dict
  - 타입: 딕셔너리
  - 저장 데이터 : 유저 id를 key 값으로, 최종 닉네임을 value 값으로 저장한다.
- word
  - 타입 : 리스트
  - 저장 데이터 : 입력받은 record 의 문자열을 공백을 기준으로 잘라서 저장

### 🖨풀이 과정

```txt
1. record 를 for문을 통해 요소를 하나씩 뽑아 split을 통해 공백 기준으로 잘라준다 [ word ]
2. 이때 유저가 들어오거나 닉네임을 변경할 경우 값을 변경해준다. [ id_dict ]
3. 모든 값을 id_dict에 최신화 해줬으면, for문을 통해 record의 요소를 split으로 공백 기준으로
   잘라 준 후, word가 Enter의 경우에는 들어왔다는 문자열을, Leave의 경우 나갔다는 문자열을
   answer에 저장해준다.
4. return answer

```
```python
def solution(record):
    answer = []
    id_dict = {}  # 유저 id와 최종 닉네임을 저장
    # check : record 값

    for check in record:
        word = check.split(" ")
        if word[0] == 'Change' or word[0] == "Enter":
            id_dict[word[1]] = word[2]

    for check in record:
        word = check.split(" ")

        if word[0] == "Enter":
            answer.append(f"{id_dict[word[1]]}님이 들어왔습니다.")
        elif word[0] == "Leave":
            answer.append(f"{id_dict[word[1]]}님이 나갔습니다.")

    return answer

```
정확성: **100.0**

합계: **100.0 / 100.0**
