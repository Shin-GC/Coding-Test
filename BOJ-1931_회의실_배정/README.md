### 📔 문제 설명

한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

### 🧰 변수 설명

- **N**
    - 타입 : int
    - 저장 데이터 : 회의 개수를 입력 받아 저장

- **result**
    - 타입 : deque
    - 저장 데이터 : 회의 사용 시간을 저장

- **count**
    - 타입 : int
    - 저장 데이터 : 회의 수 카운트

- **end**
    - 타입 : int
    - 저장 데이터 : 회의가 끝나는 시간을 저장


### 🖨풀이 과정


1. 회의 개수를 입력받는다. \[ N ]

2. N번 만큼 반복하며 회의 시간을 입력받는다 \[ result ]
3. result를 회의가 빨리 끝나는 순으로 정렬 후, 한번 더 회의가 빨리 시작하는 순으로 정렬해준다.
4. 정렬 후 가장 첫번째 값의 끝나는 시간을 end로 두고 count를 1로 선언한다.
5. 처음 값을 뺏으므로 result에서 popleft()로 값을 하나 빼준다.
\[ pop()은 O(N)의 시간이 걸리지만 popleft()는 O(1)의 시간이 걸리므로 deque 사용]
6. result에 값이 있는 동안 반복해주며, 회의 시작 시간이 end 보다 크거나 같으면 count를 증가시키고 end를 그 회의가 끝나는 시간으로 재할당 해준 후, result에서 popleft()를 통해 값을 빼준다.

6-1. 회의가 끝나는 시간보다 시작시간이 작은 경우에는 popleft()로 값만 빼준다.


```python
import sys
from collections import deque
N = int(sys.stdin.readline())
result = []

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    result.append((start, end))

result.sort(key=lambda x: (x[1], x[0]))
result = deque(result)

count = 1
end = result[0][1]
result.popleft()

while result:
    if result[0][0] >= end:
        count += 1
        end = result[0][1]
        result.popleft()
    else:
        result.popleft()
        
print(count)
```
시간 : **332ms**
