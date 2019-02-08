def get_nearby_chars(ch):
    # this function is given
    if ch == 'h':
        return set(['g', 'h', 'i'])
    else:
        return set(['n', 'o', 'p'])


def is_word(word):
    # this function is given
    return word in set(['gig', 'hii'])


def helper(word, init_set, idx):
    if idx == len(word):
        curr_word = ''.join(word)
        # print(curr_word)
        # print(is_word(curr_word))
        if is_word(curr_word):
            init_set = init_set.union([curr_word])

        return init_set

    curr_char = word[idx]
    for char in get_nearby_chars(curr_char):
        word[idx] = char
        init_set = init_set.union(helper(word, init_set, idx + 1))
    word[idx] = curr_char

    return init_set


def nearby_words(word):
    init_set = set()
    idx = 0
    init_set = helper(word, init_set, idx)
    return init_set


word = ['h', 'o', 'h']
print(nearby_words(word))
print(word)