def countingValleys(steps, path):
    altitude, valley = 0, 0
    for p in path:
        if p == 'D':
            altitude -= 1
        else:
            altitude += 1
        if p == 'U' and altitude == 0:
            valley += 1
    print(valley)
    return valley


# steps = int(input())
# path = input()
steps = 8
# path = 'UDDDUDUU'
path = 'DDUUUUDDDU'
countingValleys(steps, path)
