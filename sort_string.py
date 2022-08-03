s, n = input().strip().split(' ')
n = int(n)

if len(s) < n and (n-len(s)) % 2 == 0:
    print(s.ljust(n))
    print(s.center(n))
    print(s.rjust(n))
