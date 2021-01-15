import datetime
def solution(a, b):
    answer = ''
    day=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    day_find=datetime.date(2016,a,b).weekday()
    answer=day[day_find]
    
    
    return answer
print(solution(5,24))