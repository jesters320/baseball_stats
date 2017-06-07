import copy
from . import stats_constants

###########################
# Methods
###########################

def set_new_game_item(dict_new_game, new_game_details):
	dict_new_game.clear()
	dict_new_game[stats_constants.game_id] = new_game_details[stats_constants.new_game_value_position]
	return

def set_info_item(dict_info, info_details):
	dict_info[info_details[stats_constants.info_key_position]] = info_details[stats_constants.info_value_position]
	return

def set_starting_pitcher(starter_details):
	if starter_details[stats_constants.starter_position_position] == str(stats_constants.pitcher):
		return starter_details[1]
	else:
		return

def set_batting_info(play_details):
	# play,3,0,jay-j001,10,BX,D9/L.2-H;1-3
	dict_batting_info = {}
	
	dict_batting_info[stats_constants.inning] = play_details[stats_constants.inning_position]
	dict_batting_info[stats_constants.player_id] = play_details[stats_constants.player_id_position]
	dict_batting_info["balls_and_strikes"] = play_details[stats_constants.batting_count_position]
	dict_batting_info[stats_constants.balls] = play_details[stats_constants.batting_count_position][:1]
	dict_batting_info[stats_constants.strikes] = play_details[stats_constants.batting_count_position][1:2]
	dict_batting_info[stats_constants.current_pitch_call] = play_details[stats_constants.pitch_sequence_position]
	scorecard_list = play_details[stats_constants.scorecard_position].split("/")
	dict_batting_info[stats_constants.scorecard] = scorecard_list[0]
	if len(scorecard_list) == 2:
		dict_batting_info[stats_constants.hit_location] = scorecard_list[1]
	# TODO
	# RBI, Out, Sacrifice
	return dict_batting_info
	
def set_at_bat(list_at_bat, dict_game, dict_info, current_inning, batting_info, current_pitcher):
	# eventually break this down so pitch is the smallest atomic object. right now it's "at bat."
	dict_at_bat = copy.deepcopy(dict_game)
	dict_at_bat[stats_constants.at_bat_id] = dict_at_bat.get(stats_constants.game_id) + "_" + batting_info.get(stats_constants.inning) + "_" + str(current_inning.at_bat_count)
	dict_at_bat.update(batting_info)
	dict_at_bat[stats_constants.current_pitcher] = current_pitcher
	dict_at_bat[stats_constants.info_key] = dict_info
	list_at_bat.append(dict_at_bat)
	return	