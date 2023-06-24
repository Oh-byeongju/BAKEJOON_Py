import sys
input = sys.stdin.readline

number_list = list(map(int, input().split()))
team_A = []
team_B = []

team_A.append(max(number_list))
number_list.remove(max(number_list))
team_B.append(max(number_list))
number_list.remove(max(number_list))
team_B.append(max(number_list))
number_list.remove(max(number_list))
team_A.append(max(number_list))
number_list.remove(max(number_list))

print(abs(sum(team_A) - sum(team_B)))
