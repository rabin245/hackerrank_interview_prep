def alternate(s):
    temp = list(set(s))
    temp.sort()
    print(temp)

    ans = [['' for i in range(len(temp))] for j in range(len(temp))]
    pos_ans = [[0 for i in range(len(temp))] for j in range(len(temp))]

    n = len(temp)
    for letter in s:
        cur_pos = temp.index(letter)
        for i in range(n):
            if ans[cur_pos][i] != letter and pos_ans[cur_pos][i] != -1:
                ans[cur_pos][i] = letter
                pos_ans[cur_pos][i] += 1
            else:
                pos_ans[cur_pos][i] = -1

            if ans[i][cur_pos] != letter and pos_ans[i][cur_pos] != -1:
                ans[i][cur_pos] = letter
                pos_ans[i][cur_pos] += 1
            else:
                pos_ans[i][cur_pos] = -1
        max_t = 0
        for row in ans:
            print(row)
        for row in pos_ans:
            x = max(row)
            if x > max_t:
                max_t = x
            print(row)

    print(max_t)


# s = 'beabeefeab'
# s = 'abaacdabd'
# s = 'abcabfacb'
s = 'acbab'
alternate(s)
