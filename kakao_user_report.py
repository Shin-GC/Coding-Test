def div_reporters(report): # 신고자 리스트에서 띄어쓰기를 기준으로 신고자와 가해자를 나눈다.
    attackers_dict = {} # 가해자 이름과 신고당한 횟수
    for reporter in report:
        data = reporter.split(" ")
        if data[1] in attackers_dict:
            attackers_dict[data[1]] += 1
        else:
            attackers_dict[data[1]] = 1
    return attackers_dict


def stop_users_list(attackers_dict, k):
    stop_users = []
    for key, value in attackers_dict.items():
        if value >= k:
            stop_users.append(key)
    return stop_users


def send_mail(id_list, report, stop_users): #메일을 받을 사람을 구하는 함수

    receivers = init_receivers(id_list)

    for reporter in report:
        data = reporter.split(" ")
        if data[1] in stop_users:
            if data[0] in receivers:
                receivers[data[0]] += 1
            else:
                receivers[data[0]] = 1
        else:
            continue
    return receivers


def init_receivers(id_list):
    receivers = {}

    for id in id_list:
        receivers[id] = 0
    return receivers


def solution(id_list, report, k):
    answer = []
    init_receivers(id_list)
    report = list(set(report))
    attackers_dicts = div_reporters(report)
    stop_users = stop_users_list(attackers_dicts, k)

    receivers = send_mail(id_list, report, stop_users)

    answer = list(receivers.values())

    return answer


print(solution(	["a", "b", "c", "d", "e", "f"],["a b", "a b", "b a", "e f", "c d", "d e", "d b"], 2))