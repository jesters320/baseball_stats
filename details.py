###########################
# Imports
###########################
from pymongo import MongoClient
import json
from bson import json_util

#locals
import stats_methods
import stats_constants
import inning

####################################
# Variables
####################################
list_of_at_bats = []
dict_of_game_details = {}
dict_of_info = {}
current_visiting_team_pitcher_id = ""
current_home_team_pitcher_id = ""
current_inning = inning.Inning(0)


game_file = open("./2016eve/2016PHI - Copy.EVN",'r')
list_of_comma_separated_game_details = game_file.read().split('\n')
game_file.close()

for comma_separated_game_details in list_of_comma_separated_game_details:
	game_details = comma_separated_game_details.split(',')
	
	if stats_constants.new_game_key == game_details[stats_constants.data_position]: 
		stats_methods.set_new_game_item(dict_of_game_details, game_details)
		
	elif stats_constants.info_key == game_details[stats_constants.data_position]:
		stats_methods.set_info_item(dict_of_info, game_details)
		
	elif stats_constants.starter_key == game_details[stats_constants.data_position]: 
		if game_details[stats_constants.starter_team_ind_position] == str(stats_constants.visiting_team_ind):
			current_visiting_team_pitcher_id = stats_methods.set_starting_pitcher(game_details) or current_visiting_team_pitcher_id
		else:
			current_home_team_pitcher_id = stats_methods.set_starting_pitcher(game_details) or current_home_team_pitcher_id
	
	elif stats_constants.play_key == game_details[stats_constants.data_position]: 
		dict_of_batting_info = stats_methods.set_batting_info(game_details)

		if current_inning.this_inning != int(dict_of_batting_info["inning"]):
			current_inning = inning.Inning(int(dict_of_batting_info["inning"]))

		current_inning.add_at_bat()
		
		current_pitcher = current_home_team_pitcher_id
		if game_details[stats_constants.home_vis_position] == stats_constants.home_team_ind:
			current_pitcher = current_visiting_team_pitcher_id
		
		stats_methods.set_at_bat(list_of_at_bats, dict_of_game_details, dict_of_info, current_inning, dict_of_batting_info, current_pitcher)



client = MongoClient("mongodb://localhost:27017")
db = client.baseball_stats
db.baseball_stats.delete_many({})
db.baseball_stats.insert_many([{'at_bat': at_bat} for at_bat in list_of_at_bats])

print("total at_bats:", db.baseball_stats.count())
one_at_bat = db.baseball_stats.find_one()
print("sample at_bat:", json.dumps(one_at_bat, indent=2, default=json_util.default))

client.close()