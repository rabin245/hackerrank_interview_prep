def minimumBribes(q):
    q = [i-1 for i in q]
    bribes = 0
    # to go forward, bribe from back
    for i in range(len(q)-1, -1, -1):
        # if someone has bribed more than twice (cur. pos - initial pos) > 2 then chaotic
        if q[i]-i > 2:
            print('Too chaotic')
            return
        # instead of checking who bribed, check who has been bribed
        # if a person has been bribed then person q value will be greater than cur person q value
        # starting from 1 pos before original pos or starting from zero [this indicates that if a person p has been bribed, then q who bribed him can be either in positions (p or p-1)]
        # to current position of q value
        #      1, 2, 3, 4, 5
        # q = [2, 1, 5, 3, 4]
        # for pos 4, cur pos = 5
        # if a person x has bribed 4 then x can be in position 4 or 3 (if x bribes again)
        # so j = q[5]-1 to 5
        #      = 4-1 to 5
        #      = 3 to 5
        # start comparing from q[3]=5 and q[4]=3
        # in this case 4 was bribed by 5 and 5 bribes 3 once again to reach 3rd (i-1)th pos
        for j in range(max(0, q[i]-1), i):
            if q[j] > q[i]:
                bribes += 1

    # print()
    print(bribes)


# 2 2 2
    # 1, 2, 3, 4, 5, 6, 7, 8
# q = [1, 2, 5, 3, 7, 8, 6, 4]
# q = [1, 2, 5, 3, 4, 7, 8, 6]
# q = [5, 1, 2, 3, 7, 8, 6, 4]
# q = [2, 5, 1, 3, 4]
# q = [2, 1, 5, 3, 4]
q = list(map(int, input().rstrip().split()))
minimumBribes(q)
