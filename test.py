# arr = [1, 2, 1, 1, 2]

# for i in range(len(arr)):
#     for j in range(1, len(arr)):
#         print(i, j, arr)
#         print(arr[i], arr[j])
#         if arr[j] == 1:
#             arr.pop(j)
#         print(arr[i], arr[j])
#         print(i, j, arr)

# from collections import Counter
# lst = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# c = Counter(lst)
# print(c)

# s = 'a'
# a_n = 1
# n = 1000000000000
# l = 1
# # s = 'abcac'
# # a_n = 2
# # n = 10
# # l = 5
# # s = 'aba'
# # a_n = 2
# # n = 10
# # l = 3

# quot = n//l
# rem = n % l

# print(quot, rem)

# count = quot * a_n


# for i in range(0, rem):
#     if s[i] == 'a':
#         count += 1
# print(count)

# for i in range(2):
#     temp = input().split()
#     temp = list(map(int, temp))
#     print(temp)

# arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0,
#                                                                                                             1, 2, 4, 0]]
# for i in range(4):
#     for j in range(4):
#         print(arr[i][j:j+3])
#         print(arr[i+1][j+1])
#         print(arr[i+2][j:j+3])

#         print(sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3]))
#         print()


# max = None
# test = -3056
# if max is None or test > max:
#     max = test
# print(max)


# a = [1, 2, 3, 4, 5]
# for i, j in enumerate(a):
#     print(i, j)
# a = list(a)
# b = a[3:] + a[:3]
# print(b)

# b = -2
# print(abs(b))
# x = [1, 2, 3, 4, 5, 6, 7]
# s, e = 1, 4


# x, y = list(map(int, input().split()))
# test = [list(map(int, input().split())) for i in range(x)]
# print(x, y)
# test = [[2, 5, 4], [3, 7, 8, 9], [5, 5, 6, 8, 9, 10]]

# print(type(*test))
# n = 10
# # for i in range(n):
# #     if i > 3:
# #         n = n-1
# #     print(i, n)
# i = 0
# while i < n:
#     if i > 3:
#         n = n-1
#     print(i, n)
#     i += 1

# a = ['a', 'b', 'c', 'd', 'e']
# i = 0
# while i < len(a):
#     print(a[i])
#     if a[i] == 'c':
#         a.remove(a[i])
#         i -= 1
#     print(i, a[i], a)
#     i += 1
# a = 'showman'
# b = 'womanm'
# x = [element for element in a if element in b]
# y = [element for element in b if element in a]
# print(x)
# print(y)

# x = dict()
# x[1] = 2
# x[2] = 12
# if(x[3] == 1):
#     print('yes')
# else:
#     print('no')
# print(x)

# s = 'aabbccdddd'
# dic = {}
# for c in s:
#     if c in dic:
#         dic[c] += 1
#     else:
#         dic[c] = 1
# print(dic)
# l = list(set(dic.values()))
# print(l)
# if len(l) == 1:
#     print("YES")
# elif len(l) == 2:
#     l1 = []
#     l2 = []
#     for key in dic.keys():
#         val = dic[key]
#         if val == l[0]:
#             l1.append(key)
#         if val == l[1]:
#             l2.append(key)
#     if len(l1) == 1 or len(l2) == 1:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")

# a = 'cd'
# c = 'cd'

# if (a == c == 'cd'):
#     print('yes')
# else:
#     print('no')

# test = {'abc': 1}
# x = 'abc'
# if x not in test:
#     test[x] = 1
# else:
#     test[x] += 1
# print(test)
# x = dict()
# s = 'aaaa'
# n = len(s)
# for i in range(2, n+1):
#     for j in range(n):
#         if (j+i) <= n:
#             z = s[j:j+i]
#             print(z)
#             if(z not in x):
#                 x[z] = 1
#             else:
#                 x[z] += 1
#         else:
#             break
# print(x)

# s = 'aaabaa'
# n = len(s)
# l = []
# count = 0
# cur = None

# # 1st pass
# for i in range(n):
#     if s[i] == cur:
#         count += 1
#     else:
#         if cur is not None:
#             l.append((cur, count))
#         cur = s[i]
#         count = 1
# l.append((cur, count))

# print(l)

# from itertools import groupby
# s = 'aabcddeeeeaa'
# for x, y in groupby(s):
#     print(x, sum(1 for i in y))

# def func(x, y):
#     m = len(x)
#     n = len(y)
#     # m = 4
#     # n = 2

#     c = [[0 for j in range(n+1)] for i in range(0, m+1)]
#     b = [['' for j in range(n+1)] for i in range(0, m+1)]
#     # print(c)
#     for i in range(0, m):
#         for j in range(0, n):
#             if(x[i] == y[j]):
#                 c[i][j] = c[i-1][j-1]+1
#                 b[i][j] = 'upleft'

#             elif c[i-1][j] >= c[i][j-1]:
#                 c[i][j] = c[i-1][j]
#                 b[i][j] = 'up'
#             else:
#                 c[i][j] = c[i][j-1]
#                 b[i][j] = 'left'

#     print(b)
#     print(c)


# x = 'ABCD'
# y = 'ABDC'
# func(x, y)

# a = 'give'
# b = 'Give'
# c = dict()
# c[a] = 1
# # print(c)
# if b not in c:
#     print('working')

# temp = list()
# x = 'x'

# temp.append('a'*6)
# temp.append((x*(len(temp[0])-2)+'yz'))
# print(temp)

temp = [[0 for i in range(4)] for j in range(4)]
print(temp)

temp[0] = [1, 2, 3, 4]
temp[1] = [2, 3, 4, 1]
temp[2] = [3, 4, 2, 3]
temp[3] = [3, 4, 1, 2]

x = max(temp)
print(x)
