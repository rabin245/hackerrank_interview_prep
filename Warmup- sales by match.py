from itertools import count


def sockMerchant(n, ar):
    #
    # count = 0
    # for i in set(ar):
    #     temp = list()
    #     temp.append(i)
    #     ar.remove(i)
    #     for j in range(len(ar)):
    #         if i == ar[j]:
    #             temp.append(ar[j])

    #     count += len(temp)//2

    # using arr.count()
    # count = 0
    # for i in set(ar):
    #     i_count = ar.count(i)
    #     count += i_count//2

    # using dict
    temp = dict()
    for i in ar:
        temp[i] = 0
    for i in ar:
        temp[i] += 1

    count = 0
    for i in temp:
        count += temp[i] // 2

    print(count)
    return count


# n = 9
# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
# ar  ={10,20,30,50}
# max pair = n//2
# n = int(input())
# ar = [int(input) for i in range(n)]
sockMerchant(n, ar)
