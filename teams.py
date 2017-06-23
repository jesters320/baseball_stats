###########################
# Imports
###########################
from pymongo import MongoClient
import json
from bson import json_util

####################################
# Variables
####################################
list_of_teams = []
team_file_name = "./data/TEAM2016"

print("opening ", team_file_name)
team_file = open(team_file_name,'r')
list_of_comma_separated_team_details = team_file.read().split('\n')
team_file.close()

for comma_separated_team_details in list_of_comma_separated_team_details:
	team = comma_separated_team_details.split(',')
	dict_team = {"code": team[0], "league": team[1], "location": team[2], "name": team[3]}
	# print(dict_team)
	list_of_teams.append(dict_team)

# print(*list_of_teams)

client = MongoClient("mongodb://localhost:27017")
db = client.baseball_stat_development
db.teams.delete_many({})
for team in list_of_teams:
	db.teams.insert_one(team)


print("total teams:", db.teams.count())
one_team = db.teams.find_one()
print("sample team:", json.dumps(one_team, indent=2, default=json_util.default))

client.close()