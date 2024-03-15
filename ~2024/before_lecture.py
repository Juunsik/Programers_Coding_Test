def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(len(i))
    return answer


sol = solution([[1, 2], [3, 4], [5]])
print(sol)
