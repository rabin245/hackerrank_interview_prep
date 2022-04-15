def checkMagazine(magazine, note):
    m, n = len(magazine), len(note)
    word_dict = dict()
    for word in magazine:
        word_dict[word] = 0
    for word in magazine:
        word_dict[word] += 1

    for word in note:
        if word not in word_dict or word_dict[word] == 0:
            print('No')
            return
        word_dict[word] -= 1
    print('Yes')
    return
