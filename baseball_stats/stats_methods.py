import copy
from . import stats_constants
from .pitcher import Pitcher

###########################
# Methods
###########################

def set_new_game_item(dict_new_game, dict_info, new_game_details):
	dict_new_game.clear()
	dict_info.clear()
	dict_new_game[stats_constants.game_id] = new_game_details[stats_constants.new_game_value_position]
	return

def set_info_item(dict_info, info_details):
	dict_info[info_details[stats_constants.info_key_position]] = info_details[stats_constants.info_value_position]
	return

def set_current_pitcher(current_details):
	if current_details[stats_constants.position_position] == str(stats_constants.pitcher):
		return Pitcher(current_details[1])
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
	
	dict_at_bat = set_game_information_for_at_bat(dict_game, batting_info, current_inning)
	
	set_pitch_information_for_at_bat(current_pitcher, batting_info.get(stats_constants.current_pitch_call))
	
	outcome = set_outcome_information_for_at_bat(batting_info)
	
	dict_at_bat[stats_constants.hit] = outcome.get("hit")
	
	# deep copy all objects
	dict_at_bat[stats_constants.current_pitcher] = copy.deepcopy(current_pitcher).__dict__
	dict_at_bat[stats_constants.info_key] = copy.deepcopy(dict_info)
	list_at_bat.append(dict_at_bat)
	return	

def set_game_information_for_at_bat(dict_game, batting_info, current_inning):
	dict_at_bat = copy.deepcopy(dict_game)
	dict_at_bat[stats_constants.at_bat_id] = dict_at_bat.get(stats_constants.game_id) + "_" + batting_info.get(stats_constants.inning) + "_" + str(current_inning.at_bat_count)
	
	# add all batting info to the dictionary
	dict_at_bat.update(batting_info)
	return dict_at_bat

def set_pitch_information_for_at_bat(current_pitcher, pitch_call):
	pitches = Pitcher.get_pitch_count(pitch_call)
	
	current_pitcher.pitch_count += pitches["count_of_pitches"]
	current_pitcher.ball_count += pitches["count_of_balls"]
	current_pitcher.strike_count += pitches["count_of_strikes"]
	current_pitcher.faced_batters_count += 1
	
def set_outcome_information_for_at_bat(batting_info):
	outcome = {}
	outcome["hit"] = 0
	if any(x in batting_info.get(stats_constants.scorecard) for x in stats_constants.hit_symbols):
		outcome["hit"] = 1
	
	return outcome