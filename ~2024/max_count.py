from collections import Counter


my_str = 'bbaa'
counter = Counter(my_str)
answer = ''
for key, val in counter.items():
    if val == max(counter.values()):
        answer += key
print(''.join(sorted(answer)))
