# n번째 피보나치 수를 리턴
def fib(n):
    if n <= 2:
        return 1 # base case
    return fib(n - 2) + fib(n - 1) #recursive case
# 테스트: fib(1)부터 fib(10)까지 출력


print(fib(30))