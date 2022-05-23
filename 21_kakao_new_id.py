from string import punctuation


def solution(new_id):
    lo_id = new_id.lower()  # 1
    symbols = punctuation.replace("-", "").replace("_", "").replace(".", "")

    for symbol in symbols:  # 2
        lo_id = lo_id.replace(symbol, "")

    overlap_dot = str(lo_id[0])
    for i in lo_id[1:]:  # 3
        if i == "." and overlap_dot[-1] == ".":
            pass
        else:
            overlap_dot += i

    remove_period = overlap_dot.strip(".")  # 4

    if len(remove_period) == 0:  # 5
        remove_period += "a"
    elif len(remove_period) > 15:  # 6
        remove_period = remove_period[:15]
        if remove_period[-1] == ".":
            remove_period = remove_period.strip(".")
    if len(remove_period) < 3:  # 7
        while(len(remove_period) < 3):
            remove_period += remove_period[-1]

    answer = remove_period
    return answer
