def solution(nums):
    nums_2 = int(len(nums)/2)
    nums = list(set(nums))
    if len(nums) < nums_2:
        answer = len(nums)
    else:
        answer = nums_2
    return answer


print(solution([3, 3, 3, 2, 2, 4]))
