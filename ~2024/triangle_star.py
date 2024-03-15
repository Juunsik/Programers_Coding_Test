import itertools
n = int(input().strip())
for i in range(1, n+1):
    print('*'*i)


# 곱집합
# abcd, xy = ax ay bx by cx cy dx dy

# itertools.product 사용하기
# itertools.product
# iterable1 = 'ABCD'
# iterable2 = 'xy'
# print(list(itertools.product(iterable1, iterable2)))
