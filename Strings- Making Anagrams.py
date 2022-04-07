from itertools import count


def makeAnagram(a, b):
    # initial
    # count = 0
    # temp = list(a)
    # for i in a:
    #     # print(i)
    #     # print(temp, b )
    #     if(b.find(i) != -1):
    #         # print('found ', i)
    #         count += 1
    #         b = b.replace(i, '', 1)
    #         temp.remove(i)
    #     #     print(temp, b, count)
    #     # print(a, temp, b)

    # total = len(temp) + len(b)
    # # print(total)
    # return total

    # using set
    # counta, countb = 0, 0
    # total = 0
    # joined = list(set(a+b))
    # print(joined)
    # for i in joined:
    #     counta = a.count(i)
    #     countb = b.count(i)
    #     total += abs(counta-countb)
    #     print(counta, countb, total)
    # print(total)
    # return total

    # using dict
    count = dict()

    total = 0
    for i in a:
        count[i] = 0
    for i in a:
        count[i] += 1
    print(count)

    # or
    # for i in a:
    #     if i not in count:
    #         count[i] = 1
    #     else:
    #         count[i] += 1
    # print(count)

    for i in b:
        if i not in count:
            total += 1
        elif count[i] > 0:
            count[i] -= 1
            if count[i] == 0:
                del count[i]
        print(i, total, count)
    total = total+sum(count.values())
    print(total)
    return total


# a = 'cde'
# b = 'dcf'
# a = 'cde'
# b = 'abc'
# a = 'showman'
# b = 'womanzx'
a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'  # 30
makeAnagram(a, b)
