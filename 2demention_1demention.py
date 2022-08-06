import itertools


def solution(mylist):
    answer = list(itertools.chain.from_iterable(mylist))
    # answer = sum(mylist, [])

    return answer


print(solution([['A', 'B'], ['X', 'Y'], ['1']]))
