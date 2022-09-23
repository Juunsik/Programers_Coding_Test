def solution(s):
    string = list(s)
    for i in range(len(s)-1):
        print(i)
        if string[i] == string[i+1]:
            del(string[i+1:i+2])
            print(string)

    return True


print(solution("baabaa"))
