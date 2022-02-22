import sys

N, L = map(int, sys.stdin.readline().split())

for i in range(L, 101):  # L은 2보다 크거나 같고, 100보다 작거나 같은 자연수 이기 때문에 100까지만 반복
    x = N - (i * (i + 1) / 2)
    # x = (N - L * ( L + 1) // 2) // L
    temp = ""

    if x % i == 0:
        x = int(x / i)

        if x >= -1:
            for j in range(1, i + 1):
                temp += f"{x + j} "
            print(temp)
            break
else:
    print(-1)
