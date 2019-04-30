class Solution:
    def helper(self, price_till_now, remaining_needs, special, special_idx, num_items):
        if special_idx == len(special):
            # print("Here")
            if all([x == 0 for x in remaining_needs]):
                self.min_price = min(self.min_price, price_till_now)

            return

        done = False
        curr_special = special[special_idx]
        num_curr_special = 0
        while not done:
            for idx, need in enumerate(remaining_needs):
                if need < curr_special[idx] * num_curr_special:
                    done = True
                    break
            for idx in range(num_items):
                remaining_needs[idx] -= curr_special[idx] * num_curr_special

            # print(num_curr_special, special_idx, remaining_needs)
            self.helper(price_till_now + (curr_special[-1] * num_curr_special), remaining_needs, special,
                        special_idx + 1, num_items)

            for idx in range(num_items):
                remaining_needs[idx] += curr_special[idx] * num_curr_special
            # print('\n')
            # print(remaining_needs)

            num_curr_special += 1

        return

    def shoppingOffers(self, price , special, needs):# -> int:
        num_items = len(price)
        for i in range(num_items):
            x = [0 for _ in range(num_items)]
            x[i] = 1
            x.append(price[i])
            special.append(x)

        # print(special)

        self.min_price = 0
        for i, need in enumerate(needs):
            self.min_price += price[i] * need

        # print(self.min_price)

        self.helper(0, needs, special, 0, num_items)

        return self.min_price



sol = Solution()
price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]

print(sol.shoppingOffers(price, special, needs))