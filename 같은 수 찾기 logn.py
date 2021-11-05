def find_number(some_list, start=1, end=None):
    if end is None:
        end = len(some_list)
    if start == end:
        return start

    mid = (start + end) // 2
    left_count = 0
    for element in some_list:
        if start <= element <= mid:
            left_count += 1

    if left_count > mid - start + 1:
        return find_number(some_list, start, mid)
    return find_number(some_list, mid + 1, end)


check_list = [1, 2, 3, 4, 5, 5, 6]
print(find_number(check_list))
