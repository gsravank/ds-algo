h1, m1 = list(map(int, input().strip().split(':')))
h2, m2 = list(map(int, input().strip().split(':')))


time_in_mins1 = (h1 * 60) + m1
time_in_mins2 = (h2 * 60) + m2

mid_time_in_mins = int((time_in_mins1 + time_in_mins2) / 2)

h_mid = int(mid_time_in_mins / 60)
m_mid = mid_time_in_mins % 60

print("{:02d}:{:02d}".format(h_mid, m_mid))
