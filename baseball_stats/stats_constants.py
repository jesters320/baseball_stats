# http://www.retrosheet.org/eventfile.htm

###########################
# Constants
###########################

# data tags
new_game_key = "id"
info_key = "info"
starter_key = "start"
play_key = "play"
sub_key = "sub"
visiting_team_ind = "0"
home_team_ind = "1"
game_id = "game_id"
at_bat_id = "at_bat_id"

# position tags
data_position = 0
new_game_key_position = 0
new_game_value_position = 1
info_key_position = 1
info_value_position = 2
starter_team_ind_position = 3
position_position = 5
inning_position = 1
home_vis_position = 2
player_id_position = 3
batting_count_position = 4
pitch_sequence_position = 5
scorecard_position = 6

# position values
pitcher = 1
catcher = 2
first_base = 3
second_base = 4
third_base = 5
short_stop = 6
left_field = 7
center_field = 8
right_field = 9

# play tags
inning = "inning"
player_id = "player_id"
balls = "balls"
strikes = "strikes"
current_pitch_call = "current_pitch_call"
scorecard = "scorecard"
hit_location = "hit_location"
RBI = "RBI"
Out = "Out"
Sacrifice = "Sacrifice"
current_pitcher = "current_pitcher"

# scorecard
no_play = "NP"
non_pitch_symbols = "+*.123>"
strike_symbols = "SCFTXLMKOQRY"
hit_symbols = ["S", "D", "T", "HR", "H", "DGR"]
non_at_bat_symbols = ["C", "E", "FC", "FLE", "HP", "I", "W", "IW"]