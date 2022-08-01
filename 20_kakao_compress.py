def solution(s):
    min = 100

    for i in range(1, len(s)//2+1):
        compress = ""
        cnt = 1
        string_slice = [s[j:j+i] for j in range(0, len(s), i)]

        for i in range(1, len(string_slice)):
            if string_slice[i-1] == string_slice[i]:
                cnt += 1
            else:
                if cnt > 1:
                    compress += str(cnt)+string_slice[i-1]
                    cnt = 1
                else:
                    compress += string_slice[i-1]

        if cnt > 1:
            compress += str(cnt)+string_slice[-1]
        elif cnt == 1:
            compress += string_slice[-1]

        if min > len(compress):
            min = len(compress)

    answer = min
    return answer


a = solution("xababcdcdababcdcd")
print(a)


# 문자열 일정 길이로 자르기
# seq='f09f9989x'; length=2; [seq[i:i+length] for i in range(0, len(seq), length)]
# # ['f0', '9f', '99', '89', 'x']

# seq='f09f9989x'; length=2; [''.join(x) for x in zip(*[list(seq[z::length]) for z in range(length)])]
# #['f0', '9f', '99', '89']

# seq='f09f9989x'; length=2; map(''.join, zip(*[iter(seq)]*length))

# # ['f0', '9f', '99', '89']
