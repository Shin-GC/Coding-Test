def fib_optimized(n):
    # 코드를 작성하세요.
    current = 1
    previous = 0

    for i in range(2, n+1):
        previous, current = current, current + previous
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
