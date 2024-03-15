import itertools


def solution(arr, k):
    answer = list(itertools.chain.from_iterable(arr))
    answer.sort()
    return answer[k-1]


print(solution([[5, 12, 4, 31], [24, 13, 11, 2],
      [43, 44, 19, 26], [33, 65, 20, 21]], 4))
