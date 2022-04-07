def arrayManipulation(n, queries):
    # time limit exceeded n^2
    # res = [0]*n
    # print(res)
    # for row in queries:
    #     start, end, k = row[0]-1, row[1], row[2]
    #     for i in range(start, end):
    #         res[i] += k
    # print(res)
    # print(max(res))
    # return max(res)

    # could never think on my own
    # create array in such a way that as soon as a range ends subtract the k value
    # so that when adding in last loop, the actual sum of each coinciding ranges can be calculated
    # [3, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0]  => 3 starts at 0 and ends at 4, so subtract -3 at 5
    # [3, 0, 0, 7, 0, -3, 0, 0, -7, 0, 0] => similarly, 7 starts 3 and ends at 7, so subtract 7 at 8
    # [3, 0, 0, 7, 0, -2, 0, 0, -7, -1, 0] => 1 starts at 5 and ends at 8, here a[5] = -3 so it becomes a[5]=-2
    # this way the final sum of all the elements yields 0 as all the values k are added at the start of their range
    # and deleted at the end of the range
    array = [0 for x in range(0, n+1)]

    for a, b, k in queries:
        array[a-1] += k
        array[b] -= k
        print(array)
    tmp = 0
    maxi = 0
    for i in array:
        tmp += i
        maxi = max(maxi, tmp)

    return maxi


# n = 5
# queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
arrayManipulation(n, queries)
