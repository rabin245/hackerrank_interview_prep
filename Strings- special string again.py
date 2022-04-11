# def substrCount(n, s):
#     substrings = []
#     count = 0
#     # n = 5
#     # 1,2,3,4,5
#     substrings_dict = {}
#     for i in range(2, n+1):  # no need to check single characters
#         for j in range(n):
#             if (j+i) <= n:
#                 x = s[j:j+i]
#                 if x not in substrings_dict:
#                     substrings_dict[x] = 1
#                 else:
#                     substrings_dict[x] += 1
#                 # substrings.append(x)
#                 # print(x)
#             else:
#                 # print(j)
#                 break
#         print(i)
#         substrings_dict.clear()
#     # print(substrings)

#     # for x in substrings:
#     #     substrings_dict[x] = 0
#     # for x in substrings:
#     #     substrings_dict[x] += 1
#     print(substrings_dict)

#     # test = []

#     for substring in substrings_dict:
#         is_special = True
#         # print(substring)
#         for i in range(0, len(substring)//2):
#             check = substring[0]
#             if (substring[i] == substring[-(i+1)] == check):
#                 pass
#             else:
#                 is_special = False
#                 break
#         if(is_special):
#             count += substrings_dict[substring]
#             # test.append(substring)

#     count += n
#     # print(test)
#     print(count)
#     return count


from unittest.mock import _CallList


def substrCount(n, s):
    c_list = list()
    cur = None
    count = 0
    # divide string into groups of same characters
    # aabcaa = [(a,2), (b,1), (c,1), (a,2)]
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                c_list.append((cur, count))
            cur = s[i]
            count = 1
    c_list.append((cur, count))

    strcount = 0

    # Case 1: All characters are same.
    # For a string with n characters, we can make a total of n*(n+1)/2 substrings.
    # Note substrings keep the same order and don't skip characters.
    # For instance, aaaa will make a, aa, aa, aa, aaa, aaa and aaaa This is because,
    # for a string of size n we can make n - 1 substrings of size 2 and n - 2 substrings of size 3 and so on.
    # This can be generalized as n-(k-1) where k is the length of the substring. So total number of substrings (of all lenghts) is then n-1 + n-2 + ... + n - (k-1) + ... + n - (n-1).
    # This when written in reverse is same as 1 + 2 + ... + n-2 + n-1 + n. The sum of an arithmetic sequence is = n*(first+last)/2. Therefore, the sum of above sequence is n*(1+n)/2
    for cur in c_list:
        strcount += cur[1] * (cur[1]+1)//2

    # case 2: mid character different
    for i in range(1, len(c_list)-1):
        if c_list[i-1][0] == c_list[i+1][0] and c_list[i][1] == 1:
            strcount += min(c_list[i-1][1], c_list[i+1][1])

    print(strcount)
    return strcount

    # without using the tuple list
    # case 1:
    # for x,y in groupby(s):
    #     case_a += k_sum(sum(1 for i in y))
    # case 2:
    # for i in range(1,len(s)-1):
    # skip = 1
    # if s[i-skip] == s[i] or s[i+skip] == s[i]:
    #     continue
    # match = s[i-skip]
    # while i-skip>-1 and i+skip<len(s) and s[i-skip]==match and s[i+skip]==match:
    #     case_b += 1
    #     skip += 1


# s = 'aaaa'
# s = 'abcbaba'
s = 'mnonopoo'
# s = 'asasd'

substrCount(len(s), s)
