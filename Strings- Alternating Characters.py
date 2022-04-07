def alternatingCharacters(s):
    # Write your code here
    count = 0
    if (s.count('A') == 0) or (s.count('B') == 0):
        count = len(s)-1
        print(count)
        return count
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    print(count)
    return count


# s = 'AAABBBAABB'
# s = 'AAAA'
s = 'BBBBB'
# ABABABAB
# BABABA
# AAABBB
alternatingCharacters(s)
