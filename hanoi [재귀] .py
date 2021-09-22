def display(num_disk, start_page, end_page):
    print(f"{num_disk}번 원판을 {start_page}기둥에서 {end_page}으로 옮겼습니다.")

def hanoi(num_disks, start_page, end_page):
    mid_page = 6 - start_page - end_page

    if num_disks == 1:
        return display(num_disks, start_page, end_page)
    elif num_disks == 0:
        return
    
    # 가장 큰 원반만 3번으로 나머지는 2번
    hanoi(num_disks - 1, start_page, mid_page)
    display(num_disks, start_page, end_page)
    hanoi(num_disks - 1, mid_page, end_page)
    
    return

hanoi(3,1,3)    