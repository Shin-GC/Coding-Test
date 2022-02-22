### 📔 문제 설명

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 

노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

* 속한 노래가 많이 재생된 장르를 먼저 수록합니다.

* 장르 내에서 많이 재생된 노래를 먼저 수록합니다.

* 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

---
>* genres[i]는 고유번호가 i인 노래의 장르입니다.
>* plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
>* genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
>* 장르 종류는 100개 미만입니다.
>* 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
>* 모든 장르는 재생된 횟수가 다릅니다.
---
### 🧰 변수 설명

- **answer**
    - 타입 : 리스트
    - 저장 데이터 : 베스트 앨범에 들어갈 노래의 고유 번호
- list_ge
  - 타입 : set
  - 저장 데이터 : 장르
- album
  - 타입 : 딕셔너리
  - 저장 데이터 : 장르를 key 값으로, 재생 횟수를 value 로 넣어준다. 
- best
  - 타입 : 리스트
  - 저장 데이터 : 딕셔너리 형태의 장르, 재생 횟수, 노래의 고유번호를 지정하여 list 에 저장해준다.
- count
  - 타입 : 정수
  - 저장 데이터 : 반복 횟수를 카운트


### 🖨풀이 과정

```txt
1. 장르를 중복을 제거하여 종류만 골라서 리스트에 저장한다. [ list_ge ]
2. 장르를 key 값으로 가지는 딕셔너리를 생성한다. [ album ]
3. 이중 for문을 통해 list_ge의 요소를 하나씩 빼서 받은 장르 값과 일치할 때마다 재생횟수를 증가시켜준다.
4. album에 저장된 값을 재생횟수를 기준으로 정렬한 후, 내림차 순 정렬을 해준다.
5. 이중 for문을 통해 앨범의 요소를 하나씩 빼며 장르의 길이 만큼 반복하여 앨범의 값과 
   best의 장르가 일치하면 그 장르의 고유번호를 answer에 넣어준 후 count를 증가시킨다.
   이때 두개 씩 모으기로 했으므로 count가 2가 되면 count를 0으로 해준 후 for문을 종료시켜
   다음 album 요소 값을 비교한다.

```
```python
import operator
def solution(genres, plays):
    answer = []
    list_ge=list(set(genres))#장르만 빼오기
    album = {gen : 0 for gen in list_ge} # 장르: 재생 횟수 의 딕셔너리 생성
   
    for i in list_ge:# album 딕셔너리에 장르[Keys]와 재생 횟수[values] 넣기
        for j in range(len(genres)):
            if genres[j] == i:
                album[i] += plays[j]
   
    album = sorted(album.items(), key=operator.itemgetter(1), reverse=True) #딕셔너리를 value 기준으로 정렬하기 itemgetter값이 0 이면 key 기준, 1이면 value 기준!
    best=[]
 
    for i in range(len(genres)):
        best.append({'genres':genres[i],'plays':plays[i],'number':i})
    
    best=sorted(best, key=operator.itemgetter('plays'),reverse=True) #많이 재생된 노래 순으로 정렬 [reverse=True로 내림차순 정렬]
  
    for i in album:  #answer list에 값 넣기 [count를 통해 2개씩 자르기]
        count=0
        for j in range(len(best)):
            if count == 2:
                count=0
                break
            if i[0] ==best[j]['genres']:
                answer.append(best[j]['number'])
                count+=1

    return answer
```
시간 : **ms**
