def solution(s):
    num_string = ["zero", "one", "two", "three",
                  "four", "five", "six", "seven", "eight", "nine"]
    for i in num_string:
        if i in s:
            s = s.replace(i, str(num_string.index(i)))

    answer = int(s)
    return answer


print(solution("123"))
