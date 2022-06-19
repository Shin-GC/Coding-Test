# import collections


# def solution(clothes):
#     answer = 1
#     arr = []
#     for i, j in clothes:
#         arr.append(j)

#     kind = collections.Counter(arr)
#     print(type(kind))
#     kind_list = list(kind.values())
#     for i in kind_list:
#         answer *= (i + 1)
#     return answer - 1


# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

def solution(clothes):
    answer = 1
    obj = {}
    for x, y in clothes:
        if(obj.get(y) == None):
            obj[y] = 1
        else:
            obj[y] += 1

    for key in obj:
        answer *= obj[key] + 1

    return answer - 1


test = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(test))
