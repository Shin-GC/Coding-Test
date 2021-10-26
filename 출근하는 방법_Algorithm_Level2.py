def staircase(n):
    # 코드를 작성하세요.
    first_step, second_step = 1, 1

    for i in range(n):
        first_step, second_step = second_step, first_step + second_step

    return first_step


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
