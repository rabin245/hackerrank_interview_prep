def isValid(s):
    d = dict()
    for i in s:
        d[i] = 0
    for i in s:
        d[i] += 1
    print(d)

    # can use set to calc the counts of each char
    # temp = list()
    # for letter in set(s):
    #     temp.append(s.count(letter))
    # print(temp)
    # if len(d.keys()) == 1:
    #     print('yes')
    #     return 'yes'

    cd = dict()
    for x in d.values():
        cd[x] = 0
    for x in d.values():
        cd[x] += 1
    print(cd)
    if len(cd.keys()) == 1:
        print('yes')
        return 'yes'

    if len(cd.keys()) == 2:
        keylst = list(cd.keys())
        vallst = list(cd.values())
        # print(keylst, vallst)
        # aa-bb-cc d
        # abc ddd
        if vallst[1] == 1:
            if (keylst[1]-1 == keylst[0] or keylst[1]-1 == 0):
                print('yes')
                return 'yes'
        elif vallst[0] == 1:
            if (keylst[0]-1 == keylst[1] or keylst[0] == 0):
                print('yes')
                return 'yes'
    print('no')
    return 'no'


s = 'abcdddd'
# s = 'aaaaaaa'
# s = 'aabbc'
# s = 'aabbccc'
# s = 'abcc'
# s = 'abccc'
# s = 'aabbccddeefghi'
# s = 'abcdefghhgfedecba'
# s = 'abc'

isValid(s)
