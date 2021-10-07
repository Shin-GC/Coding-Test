def max_profit_memo(price_list, count, cache):
    if count < 2:  # count 가 2보다 작을 경우 값을 바로 리턴
        cache[count] = price_list[count]
        return cache[count]

    if count in cache: # 만약 cache 에 값이 있다면 바로 값 주기
        return cache[count]
    # base case -end-
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for i in range(1, (count // 2) + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))

    cache[count] = profit
    return profit


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
