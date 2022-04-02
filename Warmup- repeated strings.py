def repeatedStrings(s, n):
    # using list
    # t = list(s)
    # count = 0
    # while(len(t) < n):
    #     t.extend(s)

    # for i in range(0, n):
    #     if t[i] == 'a':
    #         count += 1
    # print(t[:n])
    count, num_a, string_length = 0, 0, len(s)

    # can use string.count() method as well
    for i in range(string_length):
        if s[i] == 'a':
            num_a += 1

    # to calculate how many times the full string has to be repeated
    quotient = n//string_length
    # to calculate how many characters of the string have to be repeated
    remainder = n % string_length

    # repeated full strings have num_a*quotient A's
    count = num_a*quotient

    for i in range(remainder):
        if s[i] == 'a':
            count += 1

    print(count)
    return count


# s = 'a'
# n = 1000000000000

# s = 'abcac'
# n = 10
s = 'aba'
n = 10
repeatedStrings(s, n)
