def trapping_rain(buildings):
    # 코드를 작성하세요
    rain = 0
    left_max = buildings[0]
    right_max = buildings[-1]
    for i in range(1, len(buildings) - 1):
        for j in range(len(buildings) - 1):
            if j < i and buildings[j] > left_max:
                left_max = buildings[j]
            elif j > i and buildings[j] > right_max:
                right_max = buildings[j]
        if left_max > right_max:
            rain = rain + (right_max - buildings[i])
        elif left_max < right_max:
            rain = rain + (left_max - buildings[i])
        else:
            rain = rain + (left_max - buildings[i])

    return rain


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))