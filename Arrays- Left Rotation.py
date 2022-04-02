def rotLeft(a, d):
    # n = len(a)
    # rot_a = [0]*n
    # print(rot_a)
    # for i in range(n):
    #     pos = (i-d) % n
    #     print(i, pos)
    #     rot_a[pos] = a[i]

    # fucking idiot, use list slicing
    n = len(a)
    m = d % n
    rot_a = a[m:] + a[:m]

    print(rot_a)
    return rot_a


a = input().split()
d = int(input())
rotLeft(a, d)
