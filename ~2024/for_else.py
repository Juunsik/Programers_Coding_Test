answer = 1
for i in range(5):
    a = int(input())
    answer *= a
    if int(answer**0.5)**2 == answer:
        print('found')
        break
else:
    print('not found')
