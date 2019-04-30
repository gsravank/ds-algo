from collections import defaultdict
import operator

t = int(input())

for _ in range(t):
    goal_dict = defaultdict(lambda : 0)
    point_dict = defaultdict(lambda : 0)
    all_teams = list()

    for _ in range(12):
        match_str = input()
        match_items = match_str.strip().split(' ')

        team1 = match_items[0]
        team1_goals = int(match_items[1])

        team2 = match_items[4]
        team2_goals = int(match_items[3])

        all_teams.extend([team1, team2])

        goal_dict[team1] += (team1_goals - team2_goals)
        goal_dict[team2] += (team2_goals - team1_goals)

        if team1_goals > team2_goals:
            point_dict[team1] += 3
        elif team2_goals > team1_goals:
            point_dict[team2] += 3
        else:
            point_dict[team1] += 1
            point_dict[team2] += 1
    all_teams = list(set(all_teams))

    team_details = list()
    for team in all_teams:
        team_details.append((team, point_dict[team], goal_dict[team]))

    sorted_teams = sorted(team_details, key=operator.itemgetter(1, 2), reverse=True)
    # print(sorted_teams)
    print(" ".join([sorted_teams[0][0], sorted_teams[1][0]]))

"""
2
manutd 8 vs. 2 arsenal
lyon 1 vs. 2 manutd
fcbarca 0 vs. 0 lyon
fcbarca 5 vs. 1 arsenal
manutd 3 vs. 1 fcbarca
arsenal 6 vs. 0 lyon
arsenal 0 vs. 0 manutd
manutd 4 vs. 2 lyon
arsenal 2 vs. 2 fcbarca
lyon 0 vs. 3 fcbarca
lyon 1 vs. 0 arsenal
fcbarca 0 vs. 1 manutd
a 3 vs. 0 b
a 0 vs. 0 c
a 0 vs. 0 d
b 0 vs. 0 a
b 4 vs. 0 c
b 0 vs. 0 d
c 0 vs. 0 a
c 0 vs. 0 b
c 1 vs. 0 d
d 3 vs. 0 a
d 0 vs. 0 b
d 0 vs. 0 c

"""