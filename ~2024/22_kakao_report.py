def solution(id_list, report, k):
    stop_id = []
    id_dic = dict.fromkeys(id_list, 0)
    s_report = list(set(report))

    for i in s_report:
        i_list = i.split()
        id_dic[i_list[1]] += 1

    for i in id_dic:
        if id_dic[i] >= k:
            stop_id.append(i)

    id_dic = dict.fromkeys(id_list, 0)
    for i in s_report:
        i_list = i.split()
        if i_list[1] in stop_id:
            id_dic[i_list[0]] += 1
    answer = list(id_dic.values())
    return answer
