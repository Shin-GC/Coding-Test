def max_profit(stock_list):
    # 현재까지의 최대 수익 [판매가를 위한 저장]
    max_profit_so_far = stock_list[1] - stock_list[0]
    # 현재까지의 최소 가격 [구입가를 위한 저장]
    min_so_far = min(stock_list[0], stock_list[1])

    for i in range(2, len(stock_list)):
        max_profit_so_far = max(max_profit_so_far, stock_list[i] - min_so_far)
        #  현재 저장된 최소 가격으로 구입 후 현재 주식 가에 판매한 금액과 저장된 최대 금액 비교
        min_so_far = min(min_so_far, stock_list[i])
        #  현재 저장된 최소금액과 현재 주식금액을 비교후 최소금액 갱신
    return max_profit_so_far


# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))