

def logic(s):
    contains_number = any(letter.isdigit() for letter in s)

    if contains_number is True:
        # decode
        temp = list()

        s_t = list()
        curnum = ''
        for i in range(len(s)):
            if s[i].isdigit():
                curnum = curnum + s[i]
                print(curnum)
                continue
            else:
                s_t.append(curnum)
                s_t.append(s[i])
                curnum = ''
        # print(s_t)
        i = 0
        while(i < len(s_t)):

            if s_t[i].isdigit():
                temp.append(s_t[i+1]*(int(s_t[i])-2))
                i += 2
                continue
            temp.append(s_t[i])
            i += 1

        print(''.join(temp))

    else:
        # encode
        # cur = None
        # count = 0
        # temp = list()
        # for i in range(len(s)):
        #     if cur is not None:
        #         if cur == s[i]:  # cccc
        #             count += 1
        #             continue
        #         temp.append((cur, count))

        #     cur = s[i]
        #     count = 1

        # temp.append((cur, count))
        # print(temp)

        # ans = list()
        # for x, y in temp:
        #     if y == 1:
        #         ans.append(x)
        #         continue
        #     ans.append(str(y+2))
        #     ans.append(x)
        # print(''.join(ans))

        # simpler way
        con_flag = False
        temp = list()
        count = 1
        # s = 'chheccck'
        for i in range(0, len(s)-1):
            if s[i] != s[i+1] and con_flag is True:
                temp.append(str(count+2))
                temp.append(s[i])
                con_flag = False
                count = 1
            elif s[i] != s[i+1] and con_flag is False:
                temp.append(str(count+2))

                temp.append(s[i])
                # con_flag = False
                count = 1
            elif(s[i] == s[i+1]):
                count += 1
                con_flag = True
        # print(temp)
        # print(count)
        if(not con_flag):
            # single letter at last
            temp.append(s[-1])
        else:
            temp.append(str(count+2))
            temp.append(s[-1])
        print(''.join(temp))


# s = '8A5a3x14m'
s = 'AAAAAAaaaXMMMMMMMMMMMM'
# s = 'c4he5ck'

logic(s)
