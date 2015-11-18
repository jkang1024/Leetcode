# Longest Substring Without Repeating Characters

s = "bpfbhmipx"

if len(s) == 0:
    print len(s)
elif len(s) == 1:
    print len(s)
else:
    ref = []
    max_l = 0
    for i in range(len(s)):
        if len(ref) == 0:
            ref.append(s[i])
            max_l += 1
        else:
            flag = True
            for j in range(len(ref)):
                if ref[j] == s[i]:
                    flag = False
                    break
            if flag:
                ref.append(s[i])
                if len(ref) > max_l:
                    max_l = len(ref)
            else:
                del ref[0:j+1]
                ref.append(s[i])
                print ref
print max_l
