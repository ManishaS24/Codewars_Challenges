""" Example
solution("camelCasing")  ==  "camel Casing" """

def solution(s):
    new_str = ''
    for i in range(len(s)):
        cur_str = s[i]
        # print(cur_str)
        # print("**")
        if cur_str.isupper():
            new_str += ' ' + cur_str
            # print(new_str)
            # print("--")
        else:
            new_str += cur_str
            # print(new_str)
            # print("++")
    return new_str

# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)


print(solution("breakCamelCase")) 