class Solution:
    def partitions(self, n):
        return [[], [], []]

    def get_possible_nums(self, total_leds, on_leds):

        return

    def get_time(self, hour, minute):
        hour_str = str(hour)
        minute_str = '{:02d}'.format(minute)
        return hour_str + ':' + minute_str

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        partitions = self.partitions(num)
        final_times = list()
        for partition in partitions:
            hour_leds = partition[0]
            minute_leds = partition[1]

            possible_hours = self.get_possible_nums(4, hour_leds)
            possible_minutes = self.get_possible_nums(6, minute_leds)

            for ph, pm in zip(possible_hours, possible_minutes):
                final_times.append(self.get_time(ph, pm))

        return final_times

sol = Solution()
# print(sol.get_time(11,1))