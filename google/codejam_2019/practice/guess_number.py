
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    n = int(input())

    num_guesses = 0
    a += 1
    while num_guesses < n:
        num_guesses += 1
        curr_guess = int((a + b) / 2)
        # print(a, b)
        print(curr_guess, flush=True)
        response = input()

        if response == 'TOO_SMALL':
            a = curr_guess + 1
        elif response == 'TOO_BIG':
            b = curr_guess - 1
        else:
            break

