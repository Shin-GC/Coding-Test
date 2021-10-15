def sublist_max(profits):
    # 코드를 작성하세요.
    max_profit = profits[0]

    for i in range(len(profits)):
        for j in range(i, len(profits)):
            max_profit = max(max_profit, sum(profits[i:j + 1]))
    return max_profit


# 테스트
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
