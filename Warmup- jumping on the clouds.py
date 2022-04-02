def jumpingOnClouds(c):
    jumps, i = 0, 1
    while(i < len(c)):
        if i == len(c)-1:
            jumps += 1
            break
        elif c[i+1] == 0:
            jumps += 1
            i = i+1
        else:
            jumps += 1
        i += 1
    print(jumps)
    return jumps


c = [0, 0, 0, 1, 0, 0]
# c = [0, 0, 1, 0, 0, 1, 0]
# c = [0, 0, 0, 0, 1, 0]
jumpingOnClouds(c)
