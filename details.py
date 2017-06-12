###########################
# Imports
###########################
import sys
from pymongo import MongoClient
import json
from bson import json_util

#locals
import baseball_stats as bs

####################################
# Variables
####################################
list_of_at_bats = []
dict_of_game_details = {}
dict_of_info = {}
current_visiting_team_pitcher_id = ""
current_home_team_pitcher_id = ""
current_inning = bs.Inning(0)
data_file_name = "./data/2016PHI - Copy.EVN"


if len(sys.argv) > 1:
	data_file_name = sys.argv[1]

print("opening ", data_file_name)
game_file = open(data_file_name,'r')
list_of_comma_separated_game_details = game_file.read().split('\n')
game_file.close()

for comma_separated_game_details in list_of_comma_separated_game_details:
	game_details = comma_separated_game_details.split(',')
	
	if bs.stats_constants.new_game_key == game_details[bs.stats_constants.data_position]: 
		bs.set_new_game_item(dict_of_game_details, game_details)
		
	elif bs.stats_constants.info_key == game_details[bs.stats_constants.data_position]:
		bs.set_info_item(dict_of_info, game_details)
		
	elif game_details[bs.stats_constants.data_position] in (bs.stats_constants.starter_key, bs.stats_constants.sub_key): 
		print("starter/sub: ", game_details)
		if game_details[bs.stats_constants.starter_team_ind_position] == str(bs.stats_constants.visiting_team_ind):
			current_visiting_team_pitcher_id = bs.set_current_pitcher(game_details) or current_visiting_team_pitcher_id
		else:
			current_home_team_pitcher_id = bs.set_current_pitcher(game_details) or current_home_team_pitcher_id
	
	elif bs.stats_constants.play_key == game_details[bs.stats_constants.data_position] and game_details[bs.stats_constants.scorecard_position] != bs.stats_constants.no_play: 
		dict_of_batting_info = bs.set_batting_info(game_details)

		if current_inning.this_inning != int(dict_of_batting_info["inning"]):
			current_inning = bs.Inning(int(dict_of_batting_info["inning"]))

		current_inning.add_at_bat()
		
		current_pitcher = current_home_team_pitcher_id
		if game_details[bs.stats_constants.home_vis_position] == bs.stats_constants.home_team_ind:
			current_pitcher = current_visiting_team_pitcher_id
		
		bs.set_at_bat(list_of_at_bats, dict_of_game_details, dict_of_info, current_inning, dict_of_batting_info, current_pitcher)
	elif bs.stats_constants.sub_key == game_details[bs.stats_constants.data_position]: 
		print("sub: ", game_details)
	else:
		print("unhandled: ", game_details)

#print(*list_of_at_bats)

client = MongoClient("mongodb://localhost:27017")
db = client.baseball_stat_development
db.at_bats.delete_many({})
for at_bat in list_of_at_bats:
	db.at_bats.insert(at_bat)
#db.at_bats.insert_many([{'at_bat': at_bat} for at_bat in list_of_at_bats])

print("total at_bats:", db.at_bats.count())
one_at_bat = db.at_bats.find_one()
print("sample at_bat:", json.dumps(one_at_bat, indent=2, default=json_util.default))

client.close()