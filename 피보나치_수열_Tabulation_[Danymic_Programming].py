def fib_tab(n):
    # 코드를 작성하세요.
    cache = {1:1,
             2:1}
    if n <= 2:
        return cache[n]

    for i in range(3, n+1):
        cache[i] = cache[i - 2] + cache[i - 1]

    return cache[n]
# 테스트
print(fib_tab(16))
print(fib_tab(56))
print(fib_tab(132))