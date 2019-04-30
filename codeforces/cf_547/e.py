H, n = list(map(int, input().strip().split()))
d = list(map(int, input().strip().split()))


start = 0
max_damage = 0
time_damages = list()
for di in d:
    start -= di
    time_damages.append(start)

    if start > max_damage:
        max_damage = start
round_damage = start


# print(max_damage, round_damage)
# print(time_damages)

if round_damage <= 0 and max_damage < H:
    print(-1)
else:
    # Check if it happens in first round
    first_round = False
    if max_damage >= H:
        first_round = True

        for idx, time_damage in enumerate(time_damages):
            if time_damage >= H:
                print(idx + 1)
                break
    if first_round:
        # print("Done in first round")
        pass
    else:
        # print("Not first round")

        if H-max_damage <= round_damage:
            # print("here1")
            hg = round_damage
            num_tries = int(hg / round_damage)

            remaining = H - round_damage

            # print(hg)
            # print(num_tries)
            # print(remaining)
        else:
            # print("here2")
            hg = H - max_damage
            num_tries = int(hg / round_damage)

            prev_round_rem = (H - max_damage) % round_damage

            if prev_round_rem == 0:
                remaining = max_damage
            else:
                remaining = max_damage + prev_round_rem - round_damage
                num_tries += 1

            # print(hg)
            # print(num_tries)
            # print(remaining)

        # Calculate last round timestamp
        for idx, time_damage in enumerate(time_damages):
            if time_damage >= remaining:
                last_round_time_stamp = idx + 1
                break
        # print('last round timestamp: {}'.format(last_round_time_stamp))

        print((num_tries * n) + last_round_time_stamp)
