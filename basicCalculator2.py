s = "808/9-87+35/23"

cur_num = s[0]
num_stack = []
help_stack = []
for i in range(len(s)):
    if 48 <= ord(s[i]) <= 57:
        cur_num += s[i]
    elif s[i] == '+':
        pass
    elif s[i] == '-':
        pass
    elif s[i] == '*':
        pass
    elif s[i] == '/':
        pass
    else:
        pass

#print(result)
