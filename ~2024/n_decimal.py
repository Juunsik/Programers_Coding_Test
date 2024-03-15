num, base = map(int, input().strip().split(' '))
s_num = str(num)[::-1]
answer = 0

for i in range(len(s_num)):
    answer += int(s_num[i])*pow(base, i)

print(answer)

# 쉬운 방법
# answer = int(str(num), base)
