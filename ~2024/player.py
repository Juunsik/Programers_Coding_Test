def solution(participant, completion):
    answer = []
    answer_dict = dict.fromkeys(participant, 0)
    for i in participant:
        answer_dict[i] += 1
    for i in completion:
        answer_dict[i] -= 1
    for key, val in answer_dict.items():
        if val != 0:
            answer.append(key)
    return ' '.join(answer)


print(solution(["mislav", "stanko", "mislav", "ana", "mislav"],
      ["stanko", "ana", "mislav"]))
