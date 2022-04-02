def hourglassSum(arr):
    hourglass = list()
    largest_sum = None      # if all arr elements are -ve, sum will be -ve which is less than 0
    for i in range(4):
        temp = list()
        for j in range(4):
            sums = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            temp.append(sums)
            if largest_sum is None or sums > largest_sum:
                largest_sum = sums
        hourglass.append(temp)
    print(hourglass)
    print(largest_sum)
    return largest_sum


arr = list()

for i in range(6):
    temp = list(map(int, input().split()))
    arr.append(temp)
print(arr)
hourglassSum(arr)
