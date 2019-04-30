n = int(input())
l = input()
r = input()

left_char_pos = dict()
right_char_pos = dict()

left_rem = 0
right_rem = 0

for i in range(n):
    li = l[i]
    ri = r[i]

    if li in left_char_pos:
        left_char_pos[li].append(i+1)
    else:
        left_char_pos[li] = [i+1]

    if li != '?':
        left_rem += 1

    if ri != '?':
        right_rem += 1

    if ri in right_char_pos:
        right_char_pos[ri].append(i+1)
    else:
        right_char_pos[ri] = [i+1]

all_chars = set(list(l) + list(r))
# left_rem = n
# right_rem = n
pairs_to_print = list()

# print(all_chars)
# print(left_char_pos)
# print(right_char_pos)


for char in all_chars:
    if char != '?':
        if char in left_char_pos and char in right_char_pos:
            # print('Char {} in both left and right'.format(char))
            while len(left_char_pos[char]) > 0 and len(right_char_pos[char]) > 0:
                left_pos_to_pop = left_char_pos[char].pop()
                right_pos_to_pop = right_char_pos[char].pop()

                left_rem -= 1
                right_rem -= 1

                pairs_to_print.append("{} {}".format(left_pos_to_pop, right_pos_to_pop))


# print(left_rem)
# print(right_rem)

left_pos_remaining = list()
right_pos_remaining = list()
for char in all_chars:
    if char != '?':
        if char in left_char_pos:
            left_pos_remaining.extend(left_char_pos[char])
        if char in right_char_pos:
            right_pos_remaining.extend(right_char_pos[char])


if '?' in left_char_pos:
    m1 = len(left_char_pos['?'])
else:
    m1 = 0

if '?' in right_char_pos:
    m2 = len(right_char_pos['?'])
else:
    m2 = 0


# print(m1, left_rem)
# print(m2, right_rem)

left_qm_match_pos = min(m1, right_rem)
right_qm_match_pos = min(m2, left_rem)

for _ in range(left_qm_match_pos):
    m1 -= 1
    right_match = right_pos_remaining.pop()
    left_match = left_char_pos['?'].pop()

    pairs_to_print.append("{} {}".format(left_match, right_match))

for _ in range(right_qm_match_pos):
    m2 -= 1
    right_match = right_char_pos['?'].pop()
    left_match = left_pos_remaining.pop()

    pairs_to_print.append("{} {}".format(left_match, right_match))

qm_qm_match = min(m1, m2)
# print(qm_qm_match)

for _ in range(qm_qm_match):
    left_match = left_char_pos['?'].pop()
    right_match = right_char_pos['?'].pop()

    pairs_to_print.append("{} {}".format(left_match, right_match))

print(len(pairs_to_print))
for line in pairs_to_print:
    print(line)