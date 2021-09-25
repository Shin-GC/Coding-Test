def consecutive_sum(start, end):

    if start == end:
        print(f"return : {start}")
        return start

    mid = (start + end) // 2
    print(f"start : {start}, mid: {mid}, end: {end}")
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)


print(consecutive_sum(1, 10))

