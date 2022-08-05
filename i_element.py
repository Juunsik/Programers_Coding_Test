def solution(mylist):
    mylist1 = mylist[:-1]
    mylist2 = mylist[1:]
    answer = []
    for i in range(len(mylist1)):
        answer.append(abs(mylist[i]-mylist2[i]))
    return answer

# zip 사용하기
# def solution(mylist):
#     answer = []
#     for number1, number2 in zip(mylist, mylist[1:]):
#         answer.append(abs(number1 - number2))
#     return answer


print(solution([83, 48, 13, 4, 71, 11]))
