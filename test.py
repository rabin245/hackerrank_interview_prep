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
a = 'showman'
b = 'womanm'
x = [element for element in a if element in b]
y = [element for element in b if element in a]
print(x)
print(y)
