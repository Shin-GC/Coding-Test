# 입차시간과 출차시간을 가진 리스트를 잘라서 입차시간과 차량 번호를 묶은 dict 를 생성
# {차량번호 : 입차시간} 그 후 반복문을 통해 안을 조사하다가 출차 내역에 입차한 차량이 있을 시,
# dict 에서 꺼내 입차시간과 출차시간을 계산한 후 , {차량번호: 주차시간} 을 나타내는 dict 를 생성한다.
from datetime import datetime
import math

def parking_dict(records):
    start_parking = {}
    # 입차 내역 {차량 번호: 입차시간}
    time_parking = {}
    # 차량 주차시간 {차량 번호: 출차시간 - 입차시간}

    for record in records:
        data = record.split(" ")

        if data[2] == 'IN':
            start_parking[data[1]] = data[0]
        else: # 출차 내역일시
            if data[1] not in time_parking:
                time_parking[data[1]] = ((datetime.strptime(data[0], "%H:%M") -
                                          datetime.strptime(start_parking[data[1]], "%H:%M")).seconds) / 60
                del start_parking[data[1]]
            else:
                time_parking[data[1]] += ((datetime.strptime(data[0], "%H:%M") -
                                           datetime.strptime(start_parking[data[1]], "%H:%M")).seconds) / 60
                del start_parking[data[1]]

    for start in start_parking.keys(): # 만약 입차 내역만 있고 출차 내역이 없는 차량일 경우 출차 시간을 23:59분으로 강제 설정
        if start in time_parking:
            time_parking[start] += ((datetime.strptime("23:59", "%H:%M") - datetime.strptime(start_parking[start],"%H:%M")
                                     ).seconds) / 60
        else:
            time_parking[start] = ((datetime.strptime("23:59", "%H:%M") - datetime.strptime(start_parking[start],
                                                                                            "%H:%M")).seconds) / 60

    return time_parking


def billing_parking(time_parking, fees): #기본시간, 기본요금, 단위시간, 단위요금 순
    billing_car = {}
    for time in time_parking.keys():
        if time_parking[time] <= fees[0]:
            billing_car[time] = fees[1]
        else:
            billing_car[time] = fees[1] + (math.ceil((int(time_parking[time]) - fees[0]) / fees[2]) * fees[3])

    return billing_car


def sort_car_number(billing_car):
    car_number = sorted(billing_car.keys())
    answer = []
    for i in range(0, len(car_number)):
        answer.append(billing_car[car_number[i]])
    return answer


def solution(fees, records):
    answer = []
    time_parking = parking_dict(records)
    billing_car = billing_parking(time_parking, fees)
    answer = sort_car_number(billing_car)
    return answer


print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))

