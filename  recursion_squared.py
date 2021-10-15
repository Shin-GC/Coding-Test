def power(x, y):
    """
    y가 4일경우 = 2^4 = 16
    2 ^ 0 = 0
    2 ^ 1 = 2
    2 ^ 2 = 4   2 ^ 1 * 2 ^ 1
    2 ^ 3 = 8   2 * 2 ^ 1 * 2 ^ 1
    2 ^ 4 = 16  2 ^ 2 * 2 ^ 2
    2 ^ 5 = 32  2 * 2 ^ 2 * 2 ^ 2
    2 ^ 6 = 64  2 ^ 3 * 2 ^ 3
    2 ^ 7 = 128 2 * 2 ^ 3 * 2 ^ 3
    y가 짝수 일 경우에는 x^y // 2 * x^y // 2
    y가 홀수 일 경우네는 x * x^y//2 * x^y // 2
    """
    if y == 0:
        return 1

    sub_result = power(x, y // 2)

    if y % 2 == 0:
        return sub_result * sub_result
    else:
        return x * sub_result * sub_result


"""
power(2, 4) 일때 진행 과정
sub_result = power(2, 4) 진행
sub_result = power(2, 2) 진행
sub_result = power(2, 1) 진행
sub_result = power(2, 0) 진행

y == 0 base case 가 충족되어 sub_result = power(2, 0) = 1 반환
sub_result = power(2, 1) 진행

y = 1 이므로 y % 2 == 0 을 충족 못해 else 조건문 작동
return x * sub_result * sub_result  = 2 * 1 * 1
즉 sub_result = power(2, 1) = 2 * 1 * 1 = 2 반환

y == 2 이므로 y % 2 == 0 을 충족 if 문으로 작동
return sub_result * sub_result = 2 * 2
즉 sub_result = power(2, 2) = 2 * 2 = 4 반환

y == 4 일때 y % 2 == 0 을 충족 if 문으로 작동
return sub_result * sub_result = 4 * 4
즉 sub_result = power(2, 4) = 4 * 4 = 16 반환
"""

# 테스트
print(power(2, 4))
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))

