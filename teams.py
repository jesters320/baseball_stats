team_file = open("./2016eve/TEAM2016",'r')
list_of_comma_separated_team_details = team_file.read().split('\n')
team_file.close()

list_of_team_details = []

for comma_separated_team_details in list_of_comma_separated_team_details:
	list_of_team_details.append(comma_separated_team_details.split(','))

for team_details in list_of_team_details:
	print(team_details)
