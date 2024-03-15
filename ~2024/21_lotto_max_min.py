def solution(lottos, win_nums):
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    max_rate = 7-(cnt+lottos.count(0))
    min_rate = 7-cnt
    if cnt < 2:
        min_rate = 6
        if cnt+lottos.count(0) == 0:
            max_rate = 6
    answer = [max_rate, min_rate]
    return answer
