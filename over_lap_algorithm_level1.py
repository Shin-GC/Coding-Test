def find_same_number(some_list):

    """
    # 리스트를 사용한 방법
    over_lap = []

    for i in some_list:
        if i not in over_lap:
            over_lap.append(i)
        elif i in over_lap:
            return i
    """
    over_lap = {}

    for i in some_list:
        if i in over_lap:
            return i
        over_lap[i] = True


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
